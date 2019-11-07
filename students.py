from functools import reduce
from mysys import clear

clear()

g_grades = ['A','B','C','D','F']
g_grades.reverse()

class Student:
    grade = ''
    def __init__(self, line):
        name, gender, age, score, address = line.strip().split(',')
        self.name = name
        self.gender = gender
        self.age = age
        self.score = int(score)
        self.address = address
            
    def __str__(self):
        return "{}**\t{}\t{}\t{}\t{}".format(self.name[0], self.gender, self.age, self.score, self.grade)

    
    def make_grade(self):
        if self.score == 100:
            self.grade = 'A+'
            pass
        else:
            self.grade = g_grades[ self.score // 10 - 5 ]


students = []
with open('students.csv', 'r') as file:
    for i, line in enumerate(file):   # enumerate() 함수 사용
        if i ==0: continue
        students.append(Student(line))

students.sort(key = lambda stu: stu.score, reverse = True)  # lambda() 함수 사용
m = map(lambda stu: stu.make_grade(), students)  # map() 함수 사용
list(m)  #--------------------------- map()함수는 주소값만 받기 때문에 실행하기 위해서는 list() 함수를 같이 사용

print()
print("-----------------------------------")
print("이름\t성별\t나이\t점수\t학점")
print("----\t----\t----\t----\t----")
for stu in students:
    print(stu)

def sumfn(x, y):
    if type(x) == int:
        return x + y.score
    else:
        return x.score + y.score

# total = reduce(lambda x, y: (x if type(x) == int else x.score) + y.score, students) : lambda()를 사용하면 5줄이 한줄로...

total = reduce(sumfn, students)
avg = total / len(students)
print("-----------------------------------")
print("총계>>>", total, "// 평균>>>", avg)
print("-----------------------------------")
print()
print("------------------------")
print("평균이상인 학생과 점수")
print("------------------------")
for stu in students:
    if stu.score >= avg:
        print(stu.name, stu.score)
print("------------------------")