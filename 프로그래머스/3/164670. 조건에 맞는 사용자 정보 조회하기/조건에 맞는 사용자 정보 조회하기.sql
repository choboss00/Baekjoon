/*
1. used_goods_board : 중고 거래 게시판 정보를 담은 테이블
2. used_goods_user : 중고 거래 게시판 첨부파일 정보를 담은 테이블
3. 중고 거래 게시물을 3건 이상 등록한 사용자의 사용자 id, 닉네임, 전체주소, 전화번호를 조회하는 sql문 작성하기
4. 전체 주소는 시, 도로명 주소, 상세 주소가 함께 출력되어야 함
5. 전화번호의 경우 xxx-xxxx-xxxx 의 형태로 하이픈 문자열 삽입
6. 회원 id 를 기준으로 내림차순 정렬
7. 외래 키 : user_id 와 writer_id
*/
select ugu.user_id, ugu.nickname, concat(ugu.city, ' ', ugu.street_address1, ' ', ugu.street_address2) 전체주소, concat(left(tlno, 3), '-', mid(tlno, 4, 4), '-', right(tlno, 4)) 전화번호
from used_goods_board ugb
join used_goods_user ugu on (ugb.writer_id = ugu.user_id)
group by ugb.writer_id
having count(ugb.writer_id) >= 3
order by 1 desc