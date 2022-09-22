def solution(n):
    M = [int(i) for i in str(n)]

    return sum(M)

N = int(input())

number = 0
answer = 0

list = []

while(number <= N):
    number2 = solution(number)
    answer = number + number2
    list.append(answer)
    if(answer == N):
        print(number)
        break
    number += 1

if N not in list:
    print(0)