# 최대 심박수 계산
# 공식: 최대 심박수 = 220 - 나이
# 계산식 작성 후 30세인 경우 최대 심박수 값 출력하기

age = 30
mhr = 220 - age
print("mhr:", mhr)

# 권장 일일 수분 섭취량 계산
# 수분 섭취량 = 체중 * 30
# code: 임의 값에 대해 몇 ml의 수분 섭취가 필요한지 계산하여 출력

weight = 78.8
water = weight * 30
print("권장 일일 수분 섭취량(ml):", water)

# 복리 저축 시 수령금액 계산
# 총 수령액 = 저축원금(1+복리이자율)
# 목표: 다양한 변수를 정의하고 값을 할당
# 1. 3,000만원을 연 3% 복리 이자로 5년 저축한 경우 얻게되는 총 금액은?
# 2. 1억원 연 3.5%의 복리 이자로 10년 저축한 경우 얻게 되는 총 금액은?

money1 = 30000000 * (1 + 0.03) ** 5  # (참고로 **은 거듭제곱이랜다)
print(money1)

money2 = 100000000 * (1 + 0.035) ** 10
print(money2)

# 온도 변환
# 섭씨온도를 화씨 온도로 변환하는 식은 아래와 같다.
# F = (9/5) X C + 32
# 위 식을 활용하여 섭씨 온도가 50도까지 10단위로 증가할 때, 이를 출력하는 코드를 작성하시오

cel1 = 0
cel2 = 10
cel3 = 20
cel4 = 30
cel5 = 40
cel6 = 50

fah1 = (9 / 5) * cel1 + 32
fah2 = (9 / 5) * cel2 + 32
fah3 = (9 / 5) * cel3 + 32
fah4 = (9 / 5) * cel4 + 32
fah5 = (9 / 5) * cel5 + 32
fah6 = (9 / 5) * cel6 + 32

print("섭씨, 화씨")
print(cel1, fah1)
print(cel2, fah2)
print(cel3, fah3)
print(cel4, fah4)
print(cel5, fah5)
print(cel6, fah6)

# 문자열을 변수에 저장하는 방법
# len은 문자열의 길이를 나타냄.

str_1 = "Hello"
str_2 = "World!"

print(str_1 + str_2)
print("str_1_len", len(str_1))
print("str_2_len", len(str_2))

# 따옴표 (인용 부호) 사용법
# 백슬래시 뒤에 '랑 "를 붙여야 제대로 나온댄다.

msg_1 = '우리는 "Python"을 활용해 배웁니다!'
msg_2 = "우리는 'Python'을 활용해 배웁니다!"
print("msg_1", msg_1)
print("msg_2", msg_2)

msg_3 = "Python' popularity is getting high."
msg_4 = '"Python\' is easy".'
print("msg_3", msg_3)
print("msg_4", msg_4)

# 여러 줄로 구성된 문장\
# """여기 사이에 글을 넣으면 편하게 줄바꿈 가능^^"""

multi_str1 = "Life is too short. \n You need Python!"
multi_str2 = """
Life is too short.
You need Python!
"""

print(multi_str1)
print(multi_str2)

# 사실 이 뒤에는 거의 다 알고 있는 거라서, 모르는 것만 정리

# 문자열 포맷 코드의 활용
print("%10s" % "hi")
print("%-10s" % "hi")  # 띄어쓰기 정도로 보면 될 듯하다.

print("%0.4f" % 3.12345678)  # 실수의 소수점 4자리까지만 표현
print("%10.4f" % 3.12345678)  # 띄어쓰기+실수의 소수점 4자리까지만 표현

# 다듬어진 규격으로 출력하기
# {0}: 1st variable
# {1}: 2nd variable
# 쉽게 말하면, 문자가 들어갈 순서를 숫자로 표현하는 것임.

print("I ate {0} orange in one day and got sick for {1} days".format(10, "three"))

# 내장함수 count, find, index, join (count는 숫자 세는 거고요, i랑 find는 처음나온 위치 찾기, join은 문자열에 뭐 끼어넣기입니다)

stringA = "appreciate"
print(stringA.count("p"))  # p가 몇 개나 있쇼
print(stringA.find("b"))  # 문자열에서 b가 처음 나온 위치. 읎으면 -1
print(stringA.find("i"))  # 문자열에서 i가 처음 나온 위치. 읎으면 -1

stringB = "Life is good"
print(stringB.index("i"))

stringC = ","
stringC.join("adbcdefghijk")  # a,d,b,c,d,e,f,g,h,i,j,k

# replace, split
print(stringA.replace("Life", "Your measuring tapge"))  # 위치 교체 되시겠습니다

# 사용자로부터 문자열을 입력받아 출력
msg_str = input("문자열을 입력하세요")
print(msg_str)


# 슬라이싱 할 때는 뒤에 오는 것 앞까지만 잘라냄. 즉, 0번부터 1번까지만 보여주는 것임.
# 리스트 슬라이싱
a = [1, 2, 3, 4, 5]
a[0:2]

# 문자열 슬라이싱
str = "12345"
str[0:2]


# 반복문 변형
my_list = ["james", "moon", "castle", "Virtual", 2, 100, 1]

# 기본
for x in my_list:
    print(x)

# 함축(실행문 for x(실행변수) in 배열)
print([x**2 for x in [1, 2, 3, 4, 5]])

# 길이가 10인 배열을 만들고 그 안에서 나머지가 0인 걸 찾아라?
[x for x in range(10) if x % 2 == 0]


# 리스트 실습 4 - 한 번에 정수를 여러개 입력 받고, 각 정수를 하나의 리스트에 저장
# 만약 정수가 아닌 값이 들어오면 리스트에 저장하지 않는다.

[x for x in input('여러 개의 정수를 입력해주세요').split() if x.isdigit() ]