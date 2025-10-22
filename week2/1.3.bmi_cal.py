"""
신체 질량 지수 계산
공식: 신체 질량 지수 = 체중(kg) x 신장(m)^2
"""
weight = 78.8 # kg
height = 183  # cm
bmi =  weight / ((height / 100) ** 2)
print("BMI: ", bmi)