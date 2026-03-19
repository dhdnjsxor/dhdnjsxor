number = int(input("입력 진수 결정(16/10/8/2):"))
input = (input("값 입력:"))
if number == 16:
    input = int(input,16)
if number == 10:
    input = int(input,10)
if number == 8:
    input = int(input,8)
if number == 2:
    input = int(input,2)

print("16진수:",hex(input))
print("10진수:",int(input))
print("8진수:",oct(input))
print("2진수:",bin(input))

