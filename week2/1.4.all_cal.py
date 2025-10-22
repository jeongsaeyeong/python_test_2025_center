""""
변수 정의
"""
age = 30
weight = 78.8   # kg
height = 183  # cm

"""
최대 심박수
"""
mhr = 220 - age
print("최대 심박수:", mhr)

"""
수분 섭취량
"""
water = weight * 30
print("권장 일일 수분 섭취량(ml): ", water)

"""
BMI
"""
bmi =  weight / ((height / 100) ** 2)
print("BMI: ", bmi)