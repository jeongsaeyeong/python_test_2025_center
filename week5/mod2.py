# module 2 - 클래스와 함수로 구성된 모듈

PI = 3.141592

class Circle:
    
    def getArea(self, r):
        return PI * (r ** 2)
    
def sum(a, b):
    return a + b
    

if __name__ == "__main__":
    print(PI)
    a = Circle()
    print(a.getArea(3))
    print(sum(10,100))