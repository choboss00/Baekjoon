def solution(record):
    answer = []
    
    record_dict = {}
    
    for re in record:
        r = re.split()
        if r[0] == 'Enter' or r[0] == 'Change': # 채팅방 입장, 닉네임 변경
            record_dict[r[1]] = r[2]
    
    for re2 in record:
        r2 = re2.split()
        if r2[0] == 'Enter':
            answer.append(record_dict[r2[1]] + "님이 들어왔습니다.")
        elif r2[0] == 'Leave':
            if r2[1] not in record_dict:
                continue
            answer.append(record_dict[r2[1]] + "님이 나갔습니다.")
    
    
    return answer

"""
## 오픈채팅방

## 문제
1. 관리자창 : 다양한 사람들이 들어오고, 나가는 것을 지켜볼 수 있음

2. 채팅방에 누군가 들어오거나 나가면 다음 메시지가 출력됨
- [닉네임] 님이 들어왔습니다. / 나갔습니다.

3. 채팅방에서 닉네임을 변경하는 방법
- 채팅방을 나간 후, 새로운 닉네임으로 다시 들어가기
- 채팅방에서 닉네임을 변경하기

4. 닉네임 변경 시, 기존에 채팅방에 출력되어 있떤 메시지의 닉네임도 모두 변경됨

5. 예시
- Muzi, Prodo 입장
- Muzi 나감
- Prodo 라고 이름 변경 후 들어옴 ( Muzi -> Prodo, 중복 닉네임 허용, Prodo2 라고 생각 )
- 채팅방에 두번째로 들어온 Prodo 가 닉네임 변경 ( Prodo -> Ryan )

6. 채팅방에 들어오고 나가거나, 닉네임을 변경한 기록이 담긴 문자열 배열 record

7. 모든 기록이 처리된 후, 최종적으로 방을 개설한 사람이 보게 되는 메시지를 문자열 배열 형태로 return 하는 프로그램 작성

## 입력
1. record : 채팅방에 들어오고 나가거나, 닉네임을 변경한 기록이 담긴 문자열 배열
- 길이 : 1 이상 100000 이하

2. record 에 담긴 문자열
- 채팅방 입장 : Enter [유저 아이디] [닉네임]
- 채팅방 퇴장 : Leave [유저 아이디]
- 닉네임 변경 : Change [유저 아이디] [닉네임]

3. 유저 아이디와 닉네임은 알파벳 대문자, 소문자를 구별함

4. 유저 아이디와 닉네임의 길이는 1 이상 10 이하

## 출력
1. 모든 기록이 처리된 후, 최종적으로 방을 개설한 사람이 보게 되는 메시지를 문자열 배열 형태로 return 하는 프로그램 작성

## 풀이
1. 유저 아이디 : key, 닉네임 : value 로 생각해서 딕셔너리로 접근

"""