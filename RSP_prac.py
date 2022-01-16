
a = input()
b = input()

def RSP(x, y):
    if x == '바위':
        if y == '가위':
            print(x,'가 이겼습니다')
        elif y == '보':
            print(y,'가 이겼습니다')
    if x == '가위':
        if y == '보':
            print(x,'가 이겼습니다')
        elif y == '바위':
            print(y,'가 이겼습니다')
    if x == '보':
        if y == '바위':
            print(x,'가 이겼습니다')
        elif y == '가위':
            print(y,'가 이겼습니다')

print(RSP(a, b))