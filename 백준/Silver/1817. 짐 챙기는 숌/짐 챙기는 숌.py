from collections import deque

N, M = map(int, input().split())

ans = 0

# 예외처리
if N == 0:
    print(ans)
    exit(0)

# 차례대로 책을 넣어야 함
books = deque(map(int, input().split()))

book_list = []

while books:
    book = books.popleft()

    if book + sum(book_list) <= M:
        book_list.append(book)
    else:
        book_list = []
        books.appendleft(book)
        ans += 1
    #print(f" 현재 담고 있는 책 : {book_list}")

if len(book_list):
    ans += 1

print(ans)