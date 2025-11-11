#Small Calculator Programm
def Operations(x: int|float, y: int|float) -> int|float:
    return x+y, x-y, x*y, x/y

x = input("Insert first number: ")
y = input("Insert second number: ")
for z in range(4):
    print(Operations(int(x),int(y))[z])