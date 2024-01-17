def solution(n, k, cmd):
    
    deleted = []
    
    up = [i-1 for i in range(n+2)]
    down = [i+1 for i in range(n+1)]
    
    # 현재 위치
    k += 1
    
    for cmd_i in cmd:
        if cmd_i.startswith("C"):
            deleted.append(k)
            # 상대적 위치 변경
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            k = up[k] if n < down[k] else down[k]
        # 가장 최근에 삭제된 행을 복원
        elif cmd_i.startswith("Z"):
          restore = deleted.pop( ) 
          down[up[restore]] = restore
          up[down[restore]] = restore
        
        else:
          action, num = cmd_i.split() 
          if action == "U":
            for _ in range(int(num)):
              k = up[k]
          else:
            for _ in range(int(num)):
              k = down[k]

    answer = ["O"] * n
    
    for i in deleted:
        answer[i - 1] = "X"
    return "".join(answer)

"""
## 표 편집

## 문제
1. 명령어 기반 표의 행을 선택, 삭제, 복구하는 프로그램 작성

2. 세부 요구 사항
- 파란색으로 칠해진 칸 : 현재 선택된 행
- 한 번에 한 행만 선택할 수 있음
- 다음과 같은 명령어를 이용해 표 편집 가능
"U X" : 현재 선택된 행에서 X 칸 위에 있는 행 선택
"D X" : 현재 선택된 행에서 X 칸 아래에 있는 행 선택
"C" : 현재 선택된 행 삭제 후 바로 아래 행 선택
-- 만약 삭제된 행이 가장 마지막 행 인 경우, 바로 윗 행 선택 ( 체크 )
"Z" : 가장 최근에 삭제된 행을 원래대로 복구 ( 캐시, 스택 활용 )
-- 현재 선택된 행은 바뀌지 않음

3. 처음 표의 행 개수를 나타내는 정수 n, 처음에 선택된 행의 위치를 나타내는 정수 k
- 수행한 명령어들이 담긴 문자열 배열 cmd

4. 모든 명령어를 수행한 후 표의 상태와 처음 주어진 표의 상태를 비교하여 삭제되지 않은 행은 O, 삭제된 행은 X 로 표시하여 문자열 형태로 return 하는 함수 만들기

## 제한사항
1. 5 <= n <= 100만

2. 0 <= k < n ( k 는 행의 개수를 벗어나지 않음 )

3. 1 <= cmd 의 원소 개수 <= 20만
- cmd 에 따라 위치가 바뀜

4. 원래대로 복구할 행이 없을 때, Z 명령어로 주어지는 경우는 없음
- 스택의 길이가 0 일 경우 신경쓰지 않아도 됨

5. O, X 를 순서대로 이어붙인 문자열 형태 return 하기

## 풀이
1. 명령어 집합에 맞게 동작하기

2. 캐시 -> 스택 활용


"""