// Aditya Jha 

#include <iostream>
#include <vector>
#include <queue>
#include <limits>

using std::vector;
using std::queue;
using std::numeric_limits;


class FlowGraph {
public:
    struct Edge {
        int from, to, capacity, flow, lower_bound;
    };

private:
    vector<Edge> edges;

    vector<vector<size_t> > graph;

    std::vector<int> out, in;

    size_t last_edge;

public:
    explicit FlowGraph(size_t n, size_t m, size_t last_edge)
        : graph{n}, last_edge{last_edge}
    {
        edges.reserve(m * 2);
    }

    void set_last_edge()
    {
        last_edge = edges.size();
    }

    void set_int_out_lower_bounds(std::vector<int> out_lbs, std::vector<int> in_lbs)
    {
        out = std::move(out_lbs);
        in = std::move(in_lbs);
    }

    void print_edges_feasible_flow()
    {
        for(size_t i = 0; i < last_edge; i += 2) {
            std::cout << edges[i].flow + edges[i].lower_bound << '\n';
        }
        std::cout << std::flush;
    }

    void add_edge(int from, int to, int capacity, int lower_bound)
    {
        Edge forward_edge = { from, to, capacity, 0, lower_bound };
        Edge backward_edge = { to, from, 0, 0, lower_bound };
        graph[from].push_back(edges.size());
        edges.push_back(forward_edge);
        graph[to].push_back(edges.size());
        edges.push_back(backward_edge);
    }

    size_t size() const
    {
        return graph.size();
    }

    const vector<size_t>& get_ids(int from) const
    {
        return graph[from];
    }

    const Edge& get_edge(size_t id) const
    {
        return edges[id];
    }

    void add_flow(size_t id, int flow)
    {
        edges[id].flow += flow;
        edges[id ^ 1].flow -= flow;
    }

    int lower_bounds_sum = 0;
};

FlowGraph read_data()
{
    int vertex_count, edge_count;
    std::cin >> vertex_count >> edge_count;
    int m = edge_count;

    edge_count += vertex_count * 2; // for each v, add s->v and v->t
    vertex_count += 2; // account for s and t

    FlowGraph graph(vertex_count, edge_count, m * 2);
    vector<int> out(vertex_count), in(vertex_count);

    for (int i = 0; i < m; ++i) {
        int u, v, lower_bound, capacity;
        std::cin >> u >> v >> lower_bound >> capacity;
        graph.add_edge(u, v, capacity-lower_bound, lower_bound);
        out[u] += lower_bound;
        in[v] += lower_bound;
        graph.lower_bounds_sum += lower_bound;
    }

    for(int i = 1, s = 0, t = vertex_count - 1; i < t; ++i) {
        graph.add_edge(s, i, in[i], in[i]);
        graph.add_edge(i, t, out[i], out[i]);
    }

    graph.set_int_out_lower_bounds(std::move(out), std::move(in)); 

    return graph;
}

void BFS(const FlowGraph& graph, int s, int t, vector<int>& pred)
{
    queue<int> q;
    q.push(s);

    std::fill(pred.begin(), pred.end(), -1);

    while (!q.empty()) {

        int cur = q.front();
        q.pop();

        for (auto id : graph.get_ids(cur)) {

            const FlowGraph::Edge& e = graph.get_edge(id);

            if (pred[e.to] == -1 && e.capacity > e.flow && e.to != s) {
                pred[e.to] = id;
                q.push(e.to);
            }
        }
    }
}

int max_flow(FlowGraph& graph, int s, int t)
{
    int flow = 0;

    vector<int> pred(graph.size());

    do {

        BFS(graph, s, t, pred);

        if (pred[t] != -1) {
            int min_flow = numeric_limits<int>::max();

            /* Find minimal flow on the path from BFS. */
            for (int u = pred[t]; u != -1; u = pred[graph.get_edge(u).from]) {
                min_flow = std::min(min_flow, graph.get_edge(u).capacity - graph.get_edge(u).flow);
            }

            /* Update flow in original and residual graphs along the path from BFS*/
            for (int u = pred[t]; u != -1; u = pred[graph.get_edge(u).from]) {
                graph.add_flow(u, min_flow);
            }

            flow += min_flow;
        }

    } while (pred[t] != -1);

    return flow;
}

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);

    FlowGraph graph = read_data();
    const auto flow = max_flow(graph, 0, graph.size() - 1);

    if(flow == graph.lower_bounds_sum) 
    {
        std::cout << "YES" << '\n';
        graph.print_edges_feasible_flow();
        return 0;
    }
    std::cout << "NO" << std::endl;
    return 0;
}
