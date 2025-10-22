"""
변수를 사용하는 예시
변수명 = 변수에 저장할 값
"""
a = 1
b = 'python'
c = [1,2,3]

"""
변수 a는 정수형 객체 3을 가리킴
"""
a = 3

"""
확인해 보자!
"""
print(type(a))
print(type(3))

"""
동일한 정수형 객체를 참조
"""
a = 3
b = 3
print(a is b)

"""
동일한 정수형 객체를 참조하는 두 변수의 메모리 주소
"""
print(id(a))
print(id(b))

"""
b 변수가 참조하는 객체를 변경
"""
a = 3
b = 10
print(a is b)

"""
동일한 객체를 참조하는 변수 카운팅
"""
import sys

a = 1000
print("Refcount for 1000:", sys.getrefcount(a))

b = [1, 2, 3]
print("Refcount for list:", sys.getrefcount(b))

"""
변수를 메모리에서 지우기
"""
a = 100
b = 200
del(a)
del(b)

"""
변수 체크?!
"""
#print(a)

"""
동적형 결정 오류 예시
"""
num = 10       # 정수형 변수
text = "20"    # 문자열 변수
result = num + text
print(result)

"""
# 두 값의 자료형이 맞지 않아서 오류가 발생하는 코드
num = 10       # 정수형 변수
text = "20"    # 문자열 변수

# 문자열과 숫자를 더하려고 할 때 TypeError가 발생합니다
result = num + text
print(result)
"""

"""
see 
 - mhr_cal.py
 - water_cal.py
 - bmi_cal.py
 - all_cal.py
 - money_cal.py
 - cel_2_fah.py
"""