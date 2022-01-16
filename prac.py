a = input()

r = list(a)
r.reverse()

rr = ''.join(r)
print(rr)

if a == rr:
    print("입력하신 단어는 회문(Palindrome)입니다.")