#Small Calculator Programm
def somma(x: int|float, y: int|float) -> int|float:
    return x+y

def differenza(x: int|float, y: int|float) -> int|float:
    return x-y

def prodotto(x: int|float, y: int|float) -> int|float:
    return x*y

def divisione(x: int|float, y: int|float) -> int|float:
    return x/y

def main():
    x = (int or float)(input("Insert first number: "))
    y = (int or float)(input("Insert second number: "))
    print("\nSomma:",x,"+",y,"=",somma(x,y))
    print("Differenza:",x,"-",y,"=",differenza(x,y))
    print("Prodotto:",x,"x",y,"=",prodotto(x,y))
    print("Divisione:",x,"/",y,"=",divisione(x,y))

if __name__ == "__main__":
    main()