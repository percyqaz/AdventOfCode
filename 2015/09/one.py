data = open("input.txt").read().split("\n")
nodes = {}
for line in data:
    s = line.split()
    distance = int(s[-1])
    a = s[0]
    b = s[2]
    if a not in nodes: nodes[a] = {}
    nodes[a][b] = distance
    if b not in nodes: nodes[b] = {}
    nodes[b][a] = distance

def hamiltonian_path_dfs(current_node, visited, accum_dist):
    if len(visited) == len(nodes):
        yield accum_dist
        return

    for path in nodes[current_node]:
        if path in visited:
            continue
        for result in hamiltonian_path_dfs(path, visited + [path], accum_dist + nodes[current_node][path]):
            yield result

def hamiltonian_paths(nodes):
    for node in nodes:
        for path in hamiltonian_path_dfs(node, [node], 0):
            yield path

print(min(hamiltonian_paths(nodes)))
