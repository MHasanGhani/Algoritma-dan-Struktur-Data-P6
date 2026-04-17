def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


def perkalian(m, n):
    return m * n


while True:
    print("\nMenu Pilihan")
    print("1. Barisan Fibonacci")
    print("2. M Kali N")
    print("0. Keluar")

    pilih = int(input("Pilih Menu: "))

    if pilih == 1:
        n = int(input("Masukkan jumlah suku: "))
        print("Fibonacci:")
        fibonacci(n)

    elif pilih == 2:
        m = int(input("Masukkan suatu bilangan bulat: "))
        n = int(input("Masukkan suatu bilangan pengali: "))
        print("Hasil:", perkalian(m, n))

    elif pilih == 0:
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid")
