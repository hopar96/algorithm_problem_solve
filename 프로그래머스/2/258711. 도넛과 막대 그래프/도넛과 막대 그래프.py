from collections import deque
def solution(edges):
    answer = [0,0,0,0]

    not_first_vertexes = set()
    first_vertexes = []
    edge_dict = {}
    for edge in edges:
        not_first_vertexes.add(edge[1])
        if edge[0] in edge_dict:
            edge_dict[edge[0]].append(edge[1])
        else:
            edge_dict[edge[0]] = [edge[1]]

    for key in edge_dict.keys():
        if len(edge_dict[key]) > 1 and not key in not_first_vertexes:
            first_vertexes.append(key)

    answer[0] = first_vertexes[0]
    first_vertex = first_vertexes[0]
    start_vertexes = edge_dict[first_vertex]
    del edge_dict[first_vertex]

    for start_vertex in start_vertexes:
        vertex_set = set()
        vertex_set.add(start_vertex)
        edge_cnt = 0
        que = deque()
        que.append(start_vertex)

        while que:
            _vertex = que.popleft()
            vertex_set.add(_vertex)
            if _vertex in edge_dict and len(edge_dict[_vertex]) > 0:
                for _v in edge_dict[_vertex]:
                    que.append(_v)
                    edge_cnt += 1
                del edge_dict[_vertex]

        if len(vertex_set) == edge_cnt:
            answer[1] += 1
        elif len(vertex_set) > edge_cnt:
            answer[2] += 1
        else:
            answer[3] += 1


    return answer

