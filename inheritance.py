class A:
    name = ''
    age = 0


class B(A):
    height = ''


class C(B):
    def Read(self):
        print('Please Enter the Following Values')
        self.name = input('Enter Name:')
        self.age = (int(input('Enter Age:')))
        self.height = (input('Enter Height:'))
        self.weight = (int(input('Enter Weight:')))

    def Display(self):
        print('Entered Values are as follows')
        print(' Name = ', self.name)
        print(' Age = ', self.age)
        print(' Height = ', self.height)
        print(' Weight = ', self.weight)


B1 = C()
B1.Read()
B1.Display()
