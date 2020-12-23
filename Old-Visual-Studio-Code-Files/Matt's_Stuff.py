def load() -> (str,int,int,int):
    '''Allows user to input data'''
    name = input("Enter name: ")
    num1 = int(input("Ender value 1: "))
    num2 = int(input("Ender value 2: "))
    num3 = int(input("Ender value 3: "))
    return name, num1, num2, num3           # tuple - allowed to return more than one thing unlike other languages


def calc_sum(num1: int, num2:int, num3:int) -> (int):
    '''Calculate sum'''
    sum = num1 + num2 + num3
    return sum


def calc_avg(sum:int) -> (float):
    '''calculate avg'''
    avg = sum / 3
    return avg


def output(name:str, num1:int, num2:int, num3:int, sum:int, avg:float):
    '''Prints a report of the data provided'''
    print()
    print("Your name is", name)
    print("The 3 numbers are:", num1, num2, num3)
    print("The sum is", sum)
    print("The average is", avg)


def main():
    # Varible names must be consistant in main, but nowhere else (except within function)
    name, num1, num2, num3 = load()
    sum = calc_sum(num1, num2, num3)
    avg = calc_avg(sum)
    output(name, num1, num2, num3, sum, avg)


if __name__ == "__main__":
    main()