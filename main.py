def triang_pascal():
    n = i = 0
    linhas = 1

    n = int(input("Digite o valor de 'n': "))

    def fatorial(f):
        if (f == 0):
            return 1

        return (f * fatorial(f - 1))

    print("n \t| \t     Coeficientes de (a+b)^n \t\t| \tnº de subconjuntos\n", end='')

    while linhas <= n:
        print("{} \t|   ".format(linhas), end='')
        for i in range(linhas):
            print("{}".format((fatorial(linhas) / (fatorial(linhas - i) * fatorial(i)))), end='')
            if i <= linhas - 1:
                print(", ", end='')

        print("  -> {} = ".format(pow(2, linhas)), end='')
        print(" 2^{}".format(linhas))
        linhas = linhas + 1


triang_pascal()
