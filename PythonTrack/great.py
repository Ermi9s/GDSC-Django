def great(name):
    print(f"Hello {name}")
def add_numbers(num1,num2):
    return num1 + num2
def print_args(*args):
    print(args)
def calculate_average(*nums):
    return sum(nums)/len(nums)

addition = lambda x,y: x + y
square = lambda x: x*x
is_even = lambda num: True if num%2==0 else False
numbers = list(map(int,input().split()))
evens = filter(is_even,numbers)
doubles = map(lambda x:2*x ,numbers)

try:
    a = int(input())
    b = int(input())
    print(a/b)
except b == 0:
    print("Cant divide by zero")

great("ermi")
print(add_numbers(100,500))
print_args("abebe","kebede","melaku","yitna","alemu")
print(calculate_average(1,3,4,5,6,7,8,8,3,2,4,5,23,54))






