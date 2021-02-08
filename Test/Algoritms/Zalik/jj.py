class multiplication:
    def f_1(self,a, b):
        return a + b

    def f_2(self,a, b):
        return a * self.f_1(self.a1, self.b1) + b

    def f_3(self,a, b):
        return a * self.f_2(self.a2, self.b2) + b
    def __init__(self):
        self.a1 = 1234
        self.b1 = 54321

        self.a2 = 123
        self.b2 = 4321

        self.a3 = 12
        self.b3 = 12

        self.result = 5 * self.f_3(self.a3, self.b3) * 5
        myFile = open("output.txt", "w")
        myFile.write(str(self.result))
        myFile.close()

if __name__=='__main__':
    multiplication = multiplication()