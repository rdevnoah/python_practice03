# range() 함수와 유사한 frange() 함수를 작성해 보세요. frange() 함수는 실수 리스트를 반환합니다.


def frange(stop, start=0.0, step=0.1):
    if stop < start:
        stop, start = start, stop
    i = start
    l = []
    while i < stop:
        l.append(round(i, 2))
        i += step
    return l


print(frange(2))
print(frange(2.0))
print(frange(2))
print(frange(1.0, 2.0))
print(frange(1.0, 3.0, 0.5))


