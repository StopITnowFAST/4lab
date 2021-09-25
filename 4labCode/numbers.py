a = int(input("Введите 4 числа\n"))
b = int(input())
c = int(input())
d = int(input())

secondF = a + b
secondS = c + d
final = secondF / secondS
final = float('{:.2f}'.format(final))
print("result: ", final)
