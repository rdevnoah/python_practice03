# 문제4.
# 구구단 중에 특정 곱셈을 만들고 그 답을 선택하는 프로그램을 작성하는 문제입니다.
# 답을 포함하여 9개의 정수가 아래와 같은 형태로 출력되고 사용자는 답을 골라 입력하게 됩니다.
# 프로그램은 정답 여부를 다시 출력합니다.
import random


def f(x=1, y=10):
    l = []
    for i in range(x, y):
        for j in range (x, y):
            l.append(i*j)
    return l


l = f();

n1 = random.randrange(9) + 1
n2 = random.randrange(9) + 1
answer = n1 * n2
print(n1, 'x', n2, '=', '?')
print()
l2 = [answer]

while True:
    if len(l2) == 9:
        break;
    num = l[random.randrange(len(l))]
    if num not in l2:
        l2.append(num)


random.shuffle(l2)
index = 0
while index < 9 :
    for i in range (0, 3):
        print(l2[index], end='\t')
        index += 1
    else: print()


print('answer : ', end='')
choice = int(input())
print()

if choice not in l2:
    print('표를 잘 보세요 표에 없는 수입니다.')
else:
    if choice == answer:
        print('정답')
    else:
        print('땡!!')
