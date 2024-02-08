def solution(enroll, referral, seller, amount):
    answer = []
    
    enroll_dict = {}
    result_dict = {}
    
    for i in range(len(enroll)):
        if enroll[i] not in enroll_dict:
            enroll_dict[enroll[i]] = referral[i]
            result_dict[enroll[i]] = 0
    # key : 자신, value : 부모
    
    for j in range(len(seller)):
        # seller, amount 가져오기
        s = seller[j]
        a = amount[j] * 100
        
        while s != '-': # 마지막까지 올라갈 경우
            # 10퍼센트 나누기
            per_a = a // 10
            
            if per_a == 0: # 더이상 위로 보낼 돈이 없는 경우
                result_dict[s] += a
                break
            else:
                result_dict[s] += (a - per_a)
                a = per_a
                s = enroll_dict[s]
    
    for key, value in result_dict.items():
        answer.append(value)
    
    return answer

"""
## 다단계 칫솔 판매

## 문제
1. 다단계 조직을 이용하여 칫솔을 판매하고 있음

2. 판매원이 칫솔을 판매하면 그 이익이 피라미드 조직을 타고 조금씩 분배되는 형태

3. 어느정도 판매가 이루어진 후, 조직 내 누가 얼마만큼의 이득을 가져갔는지 궁금해짐

4. 조직의 이익 분배 규칙
- 민호 : center, 파란색 네모 : 8명의 판매원을 표시한 것

- 모든 판매원은 칫솔의 판매에 의하여 발생하는 이익에서 10% 를 계산하여 자신을 조직에 참여시킨 추천인에게 배분하고 나머지는 자신이 가짐 ( 위에다가 준다는 뜻 )

- 모든 판매원은 자신이 칫솔 판매에서 발생한 이익뿐만 아니라, 자신이 조직에 추천하여 가입시킨 판매원에게서 발생하는 이익의 10% 까지 자신의 이익이 됨 ( 위의 말과 동일함 )

- 자신에게 발생하는 이익 또한 마찬가지의 규칙으로 자신의 추천인에게 분배됨

- 10% 를 계산할 때는 원 단위에서 절사 ( 소수점 X )

- 10% 를 계산한 금액이 1 원 미만인 경우에는 이득을 분배하지 않고 자신이 모두 가짐

5. 예시
- young : 1200 원을 벌었을 때, 이 중 10% 에 해당하는 120원을 자신을 조직에 참여시킨 추천인인 edward 에게 배분하고 나머지를 가짐
- edward 는 young 에게서 받은 120원 중 10% 인 12 원을 mary 에게 배분하고 자신은 나머지인 108원을 가짐
- mary 는 10% 인 1 원을 민호에게 배분하고 나머지 11원을 가짐.. 반복

6. 각 판매원의 이름을 담은 배열 enroll

7. 각 판매원을 다단계 조직에 참여시킨 다른 판매원의 이름을 담은 배열 referral

8. 판매량 집계 데이터의 판매원 이름을 나열한 배열 seller

9. 판매량 집계 데이터의 판매 수량을 나열한 배열 amount

10. 각 판매원이 득한 이익금을 나열한 배열 return 하기
- 입력으로 주어진 enroll 에 이름이 포함된 순서에 따라 나열하기

## 제한사항
1. enroll 의 길이 : 1 이상 10000 이하
- enroll 에 민호의 이름은 없음
- 민호는 항상 root, enroll 의 길이는 민호를 제외한 조직 구성원의 총 수

2. referral 의 길이는 enroll 의 길이와 같음
- referral 내에서 i 번째에 있는 이름은 배열 enroll 내에서 i 번째에 있는 판매원을 조직에 참여시킨 사람의 이름
- 어느 누구의 추천도 없이 조직에 참여한 사람에 대해서는 "-" 이 기입됨 ( 위의 예시에선 john, mary 이고, 루트 노드에 이어줘야 함 )
- seller 의 길이는 1 이상 10만 이하 ( seller 내의 i번째에 있는 이름은 i번째 판매 집계 데이터가 어느 판매원에 의한 것인지를 나타냄. 즉 돈번 사람 이름, 중복이 있을 수 있음. 딕셔너리 쓸 때 조심 )

3. amount 의 길이는 seller 와 같음 ( 딕셔너리로 seller 와 amount 를 묶기 )

4. 칫솔 한개를 판매하여 얻어지는 이익 : 100원

5. 모든 조직 구성원들의 이름은 10글자 이내의 영문 알파벳 소문자들로만 이루어져 있음

## 풀이
1. enroll, referral 데이터를 활용해서 트리 구성하기
- 딕셔너리 활용
2. seller, amount 묶기

3. 반복문을 돌면서, 부모 노드를 찾으면서 위로 올라가기

"""