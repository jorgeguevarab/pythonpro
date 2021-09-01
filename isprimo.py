
def isprimo(num: int) -> int:
    if num % 2 == 0:
        return True
    else:
        return False

def run():
    eval = int(input('Escribe un n�mero para evaluar'))

    print(isprimo(eval))


if __name__ == "__main__":
    run()

