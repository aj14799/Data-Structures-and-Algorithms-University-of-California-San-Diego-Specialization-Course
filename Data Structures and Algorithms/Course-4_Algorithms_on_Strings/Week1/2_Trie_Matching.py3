#Aditya Jha

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
    return trie

def prefix_trie_matching(text, trie):
    index = 0 
    symbol = text[index] 
    current = trie[0] 

    while True:
        if not current:  
            return True
        elif symbol in current.keys(): 
            current = trie[current[symbol]] 
            index = index + 1 
            if index < len(text):
                symbol = text[index]
            else: 
                symbol = '$'
        else:
            return False

def solve(text, n, patterns):
    result = []
    trie = build_trie(patterns) 

    n = len(text)
    for i in range(n):
        if prefix_trie_matching(text[i:], trie):
            result.append(i)

    return result

if __name__ == "__main__":
    text = sys.stdin.readline().strip()
#     text = input().strip()
    n = int(sys.stdin.readline().strip())
#     n = int(input().strip())
    patterns = []
    for i in range(n):
        patterns += [sys.stdin.readline().strip()]
#         patterns+= [ input().strip()]

    ans = solve(text, n, patterns)
#     print(' '.join(map(str,ans))+'\n')
    sys.stdout.write(' '.join(map(str, ans)) + '\n')