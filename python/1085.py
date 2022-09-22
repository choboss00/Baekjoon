x, y, w, h = map(int, input().split())

y_1 = abs(h - y)
y_2 = abs(y)
x_1 = abs(w - x)
x_2 = abs(x)

list = [x_1, x_2, y_1, y_2]

print(min(list))