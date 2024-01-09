def solution(dirs):
    answer = 0
    
    # 초기 좌표
    x, y = 0, 0
    
    ans_set = set()
    
    for d in dirs:
        if d == 'U':
            y += 1
        elif d == 'D':
            y -= 1
        elif d == 'R':
            x += 1
        else:
            x -= 1
        
        # 예외처리
        if x < -5 or x > 5 or y < -5 or y > 5:
            if d == 'U':
                y -= 1
            elif d == 'D':
                y += 1
            elif d == 'R':
                x -= 1
            else:
                x += 1
            continue
        
        if d == 'U' and (x,y-1,'D') in ans_set:
            continue
        elif d == 'D' and (x,y+1,'U') in ans_set:
            continue
        elif d == 'R' and (x-1,y,'L') in ans_set:
            continue
        elif d == 'L' and (x+1,y,'R') in ans_set:
            continue
        
        ans_set.add((x, y, d))
    
    return len(ans_set)


"""
## 방문 길이

## 문제
1. (0, 0) 위치에서 시작

2. 경계 : (-5, 5), (-5, -5), (5, 5), (5, -5)

3. 명령어에 따라 움직임
- U : 위로 한칸
- D : 아래로 한칸
- R : 오른쪽으로 한칸
- L : 왼쪽으로 한칸

4. 게임 캐릭터가 지나간 길 중 캐릭터가 처음 걸어본 길의 길이를 구하려고 함

## 풀이
1. 방향을 저장하는 리스트
"""