# 문제5.
# 선택정렬(제자리 정렬 알고리즘)을 적용하는 코드를 완성하세요.
# 문제에 주어진 배열 [ 5, 9, 3, 8, 60, 20, 1 ] 를 크기 순서대로 정렬하여 다음과 같은 출력이 되도록 완성하는 문제입니다.

# 작은 수 뒤로 보내는게 아니라, 큰 수 앞으로 땡겨 오는 방식
def selectionsort(l):
    swap_cnt = 0;
    for i in range(0, len(l)-1):
        check_max = i
        for j in range(i+1, len(l)):
            if l[j] > l[check_max]:
                check_max = j
        if i != check_max:
            l[i], l[check_max] = l[check_max], l[i]
            swap_cnt += 1
            print (l)
    return l, swap_cnt


l = [5, 9, 3, 8, 60, 20, 1]
print('Before Sort.')
for i in l: print(i, end=' ')
else: print()
l, cnt = selectionsort(l)
print('After Sort.')
for i in l: print(i, end=' ')
else: print()
print('swap이 일어난 횟수: ', cnt)


