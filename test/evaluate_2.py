import re



op = []
num = []
operators = ['+', '-', '*', '/']


def apply_arithematic(opr, a, b):
    if opr == '+':
        return a + b
    if opr == '-':
        return a - b

    if opr == '*':
        return a * b

    if opr == '/':
        return a / b




s = '23*4+2/2+53'
res = re.split(r'(\D)', s)

for i in range(len(res)):
    if res[i] in operators:
        op.append(res[i])

    if res[i].isdigit():
        num.append(res[i])


while len(op) != 0:
    opr = op.pop(0)
    num1 = num.pop(0)
    a = int(num1)
    num2 = num.pop(0)
    b = int(num2)
    num.insert(0,apply_arithematic(opr, a, b))
answer = num[0]
print(answer)




