# python3
import sys

def build_trie(patterns):
    trie = {}
    trie[0] = {}
    index = 1

    for pattern in patterns:
        curr_node = trie[0]
        for letter in pattern:
            if letter in curr_node.keys():  
                curr_node = trie[curr_node[letter]] 
            else:
                curr_node[letter] = index 
                trie[index] = {} 
                curr_node = trie[index]  
                index = index + 1
        curr_node['$'] = {} 
    return trie

def prefix_trie_matching(text, trie,external_index):
    index = 0 
    symbol = text[index] 
    current = trie[0] 
    res = -1  

    while True:
        if (not current) or ('$' in current):
            return res
        if symbol in current:
            current = trie[current[symbol]] 
            res = external_index 
            index += 1
            if index < len(text):
                symbol = text[index]
            elif '$' in current:
                return res
            else:
                symbol = '@'
                res = -1
        else:
            return res if '$' in current else -1

def solve(text, n, patterns):
    result = set()
    trie = build_trie(patterns)
    n = len(text)
    
    for i in range(n):
        if prefix_trie_matching(text[i:], trie,i)!=-1:
            result.add(prefix_trie_matching(text[i:], trie,i))

    return sorted(list(result))

if __name__ == "__main__":
    text = sys.stdin.readline().strip()
#         text = input().strip()
    n = int(sys.stdin.readline().strip())
#     n = int(input().strip())
    patterns = []
    for i in range(n):
        patterns += [sys.stdin.readline().strip()]
#         patterns+= [ input().strip()]

    ans = solve(text, n, patterns)
#     print(' '.join(map(str,ans))+'\n')
    sys.stdout.write(' '.join(map(str, ans)) + '\n')