a3 = 5
a2 = 7
a1 = 3

b2 = 6
b1 = 4

numA = a3 * 100 + a2 * 10 + a1
numB = b2 * 10 + b1

answer = numA + numB
print("Число состоит из чисел: ", answer // 100, answer // 10 % 10, answer % 100 % 10)