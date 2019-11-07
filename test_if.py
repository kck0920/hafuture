# if문을 이용해서 합격 가능영부

score=int(input('점수를 입력하세요: '))

if score > 70:
    print('합격')
    print('축하합니다!')
elif score == 70:
    print('합격도 아니고 불합격도 아님')
else:
    print('불합격')
    print('다음 기회에 응시해주세요')
