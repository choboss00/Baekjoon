/*
1. used_goods_board : 중고거래 게시판 정보를 담은 테이블
2. used_goods_file : 중고거래 게시판 첨부파일 정보를 담은 테이블
3. board_id : 외래 키
4. 조회수가 가장 높은 중고거래 게시물에 대한
5. 첨부파일 경로를 조회하는 sql문 작성하기
6. 첨부파일 경로는 file id 를 기준으로 내림차순 정렬
7. 기본적인 파일 경로 : /home/grep/src/
8. 게시글 id 를 기준으로 디렉토리가 구분됨
9. 파일이름은 파일 id, 파일 이름, 파일 확장자로 구성되도록 출력
10. 조회수가 가장 높은 게시물은 하나만 존재함
*/
select concat('/home/grep/src/', ugf.board_id, '/', ugf.file_id, ugf.file_name, ugf.file_ext) as file_path
from used_goods_file ugf
join used_goods_board ugb using (board_id)
where ugb.views = (
    select max(views)
    from used_goods_board
)
order by ugf.file_id desc
