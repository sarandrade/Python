# Versão do curso

def mdc(numeros):
    def calc_divisor(divisor):
        return divisor if sum(map(lambda x: x % divisor, numeros)) == 0 else calc_divisor(divisor - 1)
    
    return calc_divisor(min(numeros))


if __name__ == "__main__":
    print(mdc([21, 7])) # 7
    print(mdc([125, 40])) # 5
    print(mdc([9, 564, 66, 3])) # 3
    print(mdc([55, 22])) # 11
    print(mdc([15, 150])) # 15
    print(mdc([7, 9])) # 1
