#  두 값을 구하는 법은 같다. 4줄 사용이냐? 아님 2줄 사용이냐?

# arr = [i**2 for i in range(0, 20, 2)]
# print(arr)

# lst=[]
# for i in range(0,20,2):
#     i = i**2
#     lst.append(i)
# print(lst)


# # 최대값(max) 최소값(min) 구하는 함수

# print('최대값은:',max(arr))
# print('최소값은:',min(arr))


lst = ['사과', '바나나']
outs = [f for f in lst if f != '사과']
print(outs)