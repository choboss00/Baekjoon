-- 코드를 입력하세요
SELECT b.title, b.board_id, r.reply_id, r.writer_id, r.contents, date_format(r.created_date, '%Y-%m-%d') created_date
from used_goods_board b join used_goods_reply r on (b.board_id = r.board_id)
where b.created_date like '2022-10%'
order by r.created_date, b.title

-- 풀이
-- 1. 중고거래 게시판 정보를 담은 used_goods_board
-- 2. 중고거래 게시판 첨부파일 정보를 담은 used_goods_reply
-- 3. 2022년 10월에 작성된 게시글 제목
-- 4. 제목, 게시글 id, 댓글 id, 댓글 작성자 id, 댓글 내용, 댓글 작성일을 조회하는 sql문
-- 5. 댓글 작성일을 기준으로 오름차순 정렬, 댓글 작성일이 같다면 게시글 제목을 기준으로 오름차순 정렬하기