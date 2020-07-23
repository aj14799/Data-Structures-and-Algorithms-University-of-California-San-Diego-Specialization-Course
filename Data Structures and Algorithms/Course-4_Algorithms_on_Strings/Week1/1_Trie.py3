# Aditya Jha
import sys

def build_trie(patterns):
    trie = {}
    trie[0] = {}
    index = 1

    for pattern in patterns:
        curr_node = trie[0]
        for letter in pattern:
            if letter in curr_node.keys():  
#                 print('\n',letter,' is there \n')
                curr_node = trie[curr_node[letter]] #move to the next root node
#                 print('\n trie {} : \n'.format(trie), 'Current', curr_node)
            else:
                curr_node[letter] = index 
                trie[index] = {} 
                curr_node = trie[index]  
#                 print('\n else loop trie{} \n'.format(trie))
                index = index + 1
    return trie

if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))

