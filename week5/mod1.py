# module 1 - 함수로만 구성된 모듈

def add(a, b): 
    return a+b

def sub(a, b): 
    return a-b

'''
mod1.py을 직접 실행한 경우(True)에만 아래 조건문 이하 루틴이 실행됨
아래 if 문이 없으면, 주피터 노트북에서 from mod1 하면 print 문이 수행됨
'''
if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))

