def power(a,b,c):
    if b == 1:
        return a % c
    elif b == 2:
        return (a ** 2) % c
    else:
        # 홀수일 때
        if b % 2:
            return ((power(a, b//2, c) ** 2) * a) % c
        # 짝수일 때
        else:
            return ((power(a,b//2,c)**2)) % c

a,b,c = map(int, input().split())

print(power(a,b,c))