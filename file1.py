def write_file():

    with open("students.csv", "w") as file:
        file.write("이름,성별,나이,성적\n")
        file.write("김일수,남,24,80\n")
        file.write("홍길순,여,23,75\n")
        file.write("박길동,남,45,55\n")
        file.write("최순식,남,34,90\n")
        file.write("강감찬,남,49,100\n")
        file.write("갑돌이,남,38,65\n")
        file.write("박삼순,여,31,70\n")
        file.write("김갑순,여,28,85\n")
        file.write("이갑순,여,28,85\n")
        file.write("이순신,남,58,89\n")

#  def read_file():
#     with open("a.csv", "r") as file:
#         for line in file:
#             print("line >>", line)

write_file()