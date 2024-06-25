def themmoihs():
    student = []
    id = int(input('Enter id: '))
    name = input('Enter name:  ')
    gpa = float(input('Enter gpa: '))
    student.append(id)
    student.append(name)
    student.append(gpa)
    return student
def main():
    listStudent = []
    menu = -1
    print('0.exit')
    print('1.them moi hoc sinh')
    print('2.xem danh sach hoc sinh')
    while menu !=0:
        menu = int(input('Enter menu: '))
        if menu == 1:
            listStudent.append(themmoihs())
        if menu == 2:
            for student in listStudent:
                print(student)
if __name__ == '__main__':
    main()

