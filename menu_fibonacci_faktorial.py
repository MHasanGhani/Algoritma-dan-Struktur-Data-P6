def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


def faktorial(n):
    hasil = 1
    for i in range(1, n+1):
        hasil *= i
    return hasil

while True:
    print("\nMenu Pilihan")
    print("1. Barisan Fibonacci")
    print("2. Faktorial")
    print("0. Keluar")

    pilih = int(input("Pilih Menu: "))

    if pilih == 1:
        n = int(input("Masukkan jumlah suku: "))
        print("Fibonacci:")
        fibonacci(n)

    elif pilih == 2:
        n = int(input("Masukkan bilangan: "))
        print("Hasil faktorial:", faktorial(n))

    elif pilih == 0:
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid")