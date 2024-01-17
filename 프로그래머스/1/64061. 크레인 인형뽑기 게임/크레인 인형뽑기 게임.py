def solution(board, moves):
    answer = 0
    
    stack = []
    
    for move in moves:
        move -= 1 # 인덱스 번호에 맞게 수정하기
        # 인덱스 번호 체크
        idx = 0
        
        while board[idx][move] == 0:
            idx += 1
            # 만약 비어있을 경우
            if idx == len(board):
                break
        
        # 비어있는 경우
        if idx == len(board):
            continue
        
        if len(stack) == 0:
            stack.append(board[idx][move])
            board[idx][move] = 0
            continue
        
        if stack[-1] == board[idx][move]:
            stack.pop()
            answer += 2
            board[idx][move] = 0
        else:
            stack.append(board[idx][move])
            board[idx][move] = 0
    
    
    return answer


"""
## 크레인 인형뽑기 게임

## 문제
1. 화면 구성
- 1 * 1 크기의 칸들로 이루어진 N * N 크기의 정사각 격자
- 위쪽에는 크레인이 있고 오른쪽에는 바구니가 있음
- 각 격자 칸에는 다양한 인형이 들어있으며, 인형이 없는 칸은 빈칸임
- 모든 인형은 1 * 1 크기의 격자 한 칸을 차지하며 격자의 가장 아래 칸 부터 차곡차곡 쌓여있음

2. 게임 사용자는 크레인을 좌우로 움직여서 멈춘 위치에서 가장 위에 있는 인형을 집어올릴 수 있음
- 집어 올린 인형은 바구니에 쌓이게 됨
- 바구니의 가장 아래 칸 부터 인형이 순서대로 쌓이게 됨

3. 같은 모양의 인형 2개가 바구니에 연속해서 쌓이게 되면 두 인형은 사라짐

4. 인형이 없는 곳에서 크레인을 작동시키는 경우, 아무런 일도 일어나지 않음
- 바구니는 모든 인형이 들어갈 수 있을 만큼 충분히 크다고 가정

5. 격자의 상태가 담긴 2차원 배열 board
- 인형을 집기 위해 크레인을 작동시킨 위치가 담긴 배열 moves

6. 크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수 return 하기

## 제한사항
1. board 배열의 크기 : 5 * 5 이상, 30 * 30 이하

2. board 의 각 칸에는 0 이상 100 이하인 정수가 담겨있음
- 0 : 빈 칸
- 나머지 : 각기 다른 인형의 모양을 의미

3. moves 배열의 크기 : 1 이상 1000 이하
- 각 원소들의 값은 1 이상이며, board 배열의 가로 크기 이하인 자연수

## 풀이
1. 바구니 : 가장 아래부터 쌓이고, 꺼낼 때는 가장 위부터 꺼냄 -> 스택 활용

2. 크레인의 위치에 따라 인형 가져오기

"""