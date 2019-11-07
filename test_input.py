cmd = input("Input(Usage:이름,나이,성별)>> ")

error_msg="정확하게 입력해 주세요!!!"
# 1.값이 존재여부 체크
if cmd == ' ':
    print(error_msg)
    exit()

2. ','가 있는지 체크
if ',' not in cmd:
if cmd.find(',') == -1:
    print(error_msg)
    exit()

isExistsComma = False
for i in cmd:
    if i == ',':
        isExistsComma = True
        break
    pass

if isExistsComma == False:
    print(error_msg)
    exit()

cmds=cmd.split(',')
# print(cmds[0],cmds[1],cmds[2])

# 3. cmd에 3개의 값이 들어가 있는지 체크 : len()함수 이용
if len(cmds) != 3:
    print(error_msg)
    exit()

outmsg = "당신의 이름은 {}, 나이는 {}, 성별은 {} 입니다"
print(outmsg.format(cmds[0],cmds[1],cmds[2]))
