# 함수 - 실습 1

def getMaxAvgMin(mylist, mode = 'max'):
    if mode == 'max':
        return max(mylist)
    elif mode == 'min':
        return min(mylist)
    elif mode == 'avg':
        return sum(mylist) / len(mylist)
    else:
        print('Wrong Mode!')

mylist = [20, 100, 37, 77, 69, 24, 46]
while(True):
    print("\n주어진 데이터: ", mylist)
    mymode = input("다음과 같이 명령어를 입력하세요: \n"
              "1) 최대 값을 원하면: max\n"
              "2) 평균 값을 원하면: avg\n"
              "3) 최소 값을 원하면: min\n"
              "mode 입력: ")
    print(getMaxAvgMin(mylist, mymode))