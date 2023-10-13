import sys
maxNum = -1e10
minNum = 1e10

def back(depth, ans):
    global maxNum, minNum

    if depth == n:
        maxNum = max(maxNum, ans)
        minNum = min(minNum, ans)
    else:
        for i in range(4):
            if m_list[i] > 0:
                if i == 0:
                    m_list[i] -= 1
                    back(depth + 1, ans + n_list[depth])
                    m_list[i] += 1
                elif i == 1:
                    m_list[i] -= 1
                    back(depth + 1, ans - n_list[depth])
                    m_list[i] += 1
                elif i == 2:
                    m_list[i] -= 1
                    back(depth + 1, ans * n_list[depth])
                    m_list[i] += 1
                elif i == 3:
                    m_list[i] -= 1
                    back(depth + 1, int(ans / n_list[depth]))
                    m_list[i] += 1



input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

# 연산자 리스트 입력받기
m_list = list(map(int, input().split()))

back(1, n_list[0])

print(maxNum)
print(minNum)