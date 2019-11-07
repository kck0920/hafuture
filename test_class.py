class Dog:
    def __init__(self, name):  # __init__ 생성자 함수
        self.name = name   # name : 상태(property)
        print(self.name, "was Born")

    def speak(self):  # speak : 메서드(method)
        print("YELP",self.name)
        pass

    def wag(self):
        print("Dog's wag tail")
        pass

    def __del__(self):
        print("destroy!!")

# puddle = Dog("Bori")
# sheperd = Dog("Ssal")

# puddle.speak()
# sheperd.speak()

class Puppy(Dog):  # Dog를 상속 받는다. 부모를 () 안에 넣어주면 상속된다
    def __init__(self):
        self.name = "Puppy"
        self.color = "Red"
        print("QQQ> Puppy was Born")

    def __read_diary(self):  # 숨길 때 _를 두번 (__) >> Encapsulation(은닉화)
        print("Diary content!!!!!")

    def speak(self):  # speak : 메서드(method)
        print("Bow wow!",self.name)
        pass

    def wag(self):
        self.__read_diary()
        print("Puppy's wag tail")
        pass

    # def tto():  # 정적(static) class // self가 없다
    #     print("Ttoooooooooooooo00000000000")

d = Dog("puddle")
p = Puppy()
d.speak()
p.speak()
d.wag()
p.wag()

# Puppy.tto()  

# p.__read_diary()

# print('aaaaa', d.name, p.name, p.color) 