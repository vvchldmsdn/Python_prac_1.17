word = 'ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC'

a = list(map(lambda x,y:x*y, [word.count('A'),word.count('B'),word.count('C'),word.count('D')],[4,3,2,1]))
sum = sum(a)
print(sum)

