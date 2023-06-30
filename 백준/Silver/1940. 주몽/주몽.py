"""
1940번. 주몽 ( 실버 4 )

갑옵을 만드는 재료들은 각각 고유한 번호를 가지고 있음
- 2개의 재료 필요, 2 재료의 교유한 번호를 하쳐서 m이 되면 갑옷 생성
- 갑옷을 몇개나 만들 수 있을지?


1. 정렬
2. 투포인터 이용 ( 하나는 뒤에서부터, 하나는 앞에서부터 )
- 뒤에서부터 비교해서, 만약 크기가 더 클 경우, 한칸씩 이동
- 크기가 더 작으면, 이제 앞에꺼 이동해서 값 맞추기
- 만약 두개를 더한 값이 더 크면, 앞에꺼 한칸 이동

"""
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

n_list = list(map(int, input().split()))
# 정렬
n_list.sort()

# 정답
answer = 0

# 예시 : 1 2 3 4 5 7

left = 0
right = len(n_list)-1
# 왼쪽이 오른쪽을 따라잡을 때 까지 반복
while left < right:
    # 값이 더 크면 한칸 감소
    if n_list[left]+n_list[right] > m:
        right -= 1
    elif n_list[left] + n_list[right] == m:
        answer += 1
        right -= 1
        left += 1
    elif n_list[left] + n_list[right] < m:
        left += 1

print(answer)


