def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent,a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    parent = [0] * (n + 1) # 부모 테이블 초기화
    edges = [] # 모든 간선을 담을 리스트
    result = 0 # 최종 비용을 담을 변수
    for i in range(1, n+1):
        parent[i] = i
    
    for _ in costs:
        a,b,cost = _
        edges.append((cost,a,b))
        
    edges.sort()
    for edge in edges:
        cost,a , b = edge
        # 사이클이 발생하지 않는 경우에만
        if find_parent(parent,a) != find_parent(parent, b):
            union_parent(parent,a,b)
            result += cost
    return result