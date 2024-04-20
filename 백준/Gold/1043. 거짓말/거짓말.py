N, M = map(int, input().split())

n_list = list(map(int, input().split()))

# 파티 그래프
party_graph = []

for _ in range(M):
    sub_list = list(map(int, input().split()))
    party_graph.append(sub_list[1:])

#print("파티 그래프 : ", party_graph)

true_set = set()
false_set = set()

if n_list[0] == 0:
    print(len(party_graph))
else:
    ans = 0
    # 정답을 알고 있는 사람들
    for i in n_list[1:]:
        true_set.add(i)

    for _ in range(M):
        for party in party_graph:
            party_set = set(party)
            if true_set & party_set:
                true_set.update(party_set)

    #print("true set : ", true_set)

    for party in party_graph:
        party_set = set(party)

        if true_set & party_set:
            continue
        ans += 1

    print(ans)



