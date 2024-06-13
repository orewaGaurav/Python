class complexnumbers():
    def __init__(self,imaginary,real):
        self.real = real
        self.imaginary = imaginary
    def __str__(self):
        #string representationnof the complex numbers
        return f"{self.real} + {self.imaginary}i"
def add_complex_numbers(num1,num2):
    real_sum = num1.real + num2.real
    imaginary_sum = num1.imaginary + num2.imaginary
    return complexnumbers(real_sum,imaginary_sum)


s1 = complexnumbers(3,4)
s2 = complexnumbers(4,6)
result = add_complex_numbers(s1,s2)
print("sum:",result)