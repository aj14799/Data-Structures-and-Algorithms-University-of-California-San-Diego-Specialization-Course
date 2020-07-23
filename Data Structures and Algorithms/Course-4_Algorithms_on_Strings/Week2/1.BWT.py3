# Aditya Jha
import sys

def BWT(text):
    M = [text]*(len(text))
    for i in range(len(text)):
        M[i] = (text[i:] + text[:i])
    M.sort()
    result = [x[-1] for x in M]
    return ''.join(result)

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))