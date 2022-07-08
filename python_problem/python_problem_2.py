# 함수 이름은 변경 가능합니다.

# menu 1


def Menu1(name, mid_score, final_score):
    students.append(Student(name, mid_score, final_score, 0))

# menu 2


def Menu2():
    for i in students:
        if not i.grade:
            average = (i.mid_score + i.final_score) / 2
            if average >= 90:
                i.grade = "A"
            elif average >= 80:
                i.grade = "B"
            elif average >= 70:
                i.grade = "C"
            else:
                i.grade = "D"

# menu 3


def Menu3():
    print("-------------------------------")
    print(" name    mid    final    grade")
    print("-------------------------------")
    for i in students:
        print(i.name, "\t", i.mid_score, "\t", i.final_score, "\t", i.grade)

# menu 4


def Menu4(name):
    for i in students:
        if i.name == name:
            idx = names.index(name)
            del students[idx]
            del names[idx]
    print(name, "student information is deleted.")


class Student:
    def __init__(self, name, mid_score, final_score, grade):
        self.name = name
        self.mid_score = mid_score
        self.final_score = final_score
        self.grade = grade


# 학생 정보를 저장할 변수 초기화
names = []
students = []

print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")

while True:
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        try:
            x = input("Enter name mid-score final-score : ").split()
            if len(x) != 3:
                raise Exception("Num of data is not 3!")
            name, mid_score, final_score = x
            if name in names:
                raise Exception("Already exist name!")
            else:
                if (mid_score.isnumeric()) and (final_score.isnumeric()):
                    mid_score = int(mid_score)
                    final_score = int(final_score)
                    if mid_score <= 0 or final_score <= 0:
                        raise Exception("Score is not positive integer")
                    else:
                        names.append(name)
                        Menu1(name, mid_score, final_score)
                        continue
                else:
                    raise Exception("Score is not positive integer")

        except Exception as e:
            print(e)

    elif choice == "2":
        # 예외사항 처리(저장된 학생 정보의 유무)
        # 예외사항이 아닌 경우 2번 함수 호출
        # "Grading to all students." 출력
        if len(students) == 0:
            print("No student data!")
            continue
        print("Grading to all students.")
        Menu2()

    elif choice == "3":
        if len(students) == 0:
            print("No student data!")
            continue
        flag = 0
        for i in students:
            if not i.grade:
                flag = 1
                break
        if flag == 1:
            print("There is a student who didn't get grade.")
            continue
        else:
            Menu3()

    elif choice == "4":
        if len(students) == 0:
            print("No student data!")
            continue
        name = input("Enter the name to delete : ")
        if name not in names:
            print("Not exist name!")
        else:
            Menu4(name)

    elif choice == "5":
        # 프로그램 종료 메세지 출력
        # 반복문 종료
        print("Exit Program!")
        break

    else:
        # "Wrong number. Choose again." 출력
        print("Wrong number. Choose again.")
