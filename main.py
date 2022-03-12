import mat as m
from Student import Student

class main:
    def __init__(self):
        mat = m.mat()
        print(mat.cember_alani(5))
        print(mat._mat__pi)

        student1 = Student("osman", "mutlu", "male", "2", "2018510050")
        student2 = Student("beyza", "gur", "female", "1", "2018510035")
        student1.display()
        print("----------")
        student2.display()

if __name__ == "__main__":
    main()
