T01 = (1,2,3,4,5)

try:
    T01[0] = 100
except TypeError as error:
    print(error)

# 5종의 재고를 받아서 입력

D01 = dict()

items = 5

for x in range(0, items):
    item = input("물품명과 수량을 입력해주세요:").split()
    key = item[0]
    val = int(item[1])
    D01[key] = int(val)

print(D01)

D01["일품도시락"] = 3
print(D01.popitem())

print("전체 물품 종류 개수:", len(D01))
print("전체 수량:", sum(D01.values))
print("평균 수량:", sum(D01.values)/len(D01))