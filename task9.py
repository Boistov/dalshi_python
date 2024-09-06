def messages(tree, k):
    count = 1
    for child in tree.get(k, []):
        count += messages(tree, child)
    return count

def main():
    N = int(input())
    tree = {}

    for _ in range(N):
        msg, parent = map(int, input().split())
        if parent not in tree:
            tree[parent] = []
        tree[parent].append(msg)

    k = int(input())
    result = messages(tree, k)
    print(result)

main()
