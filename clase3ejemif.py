num = int(input("ingrese un numero:"))

if num % 3 == 0 and num % 5 == 0:
    print("frizzbuzz")
elif num % 3 == 0 :
    print("frizz")
elif num % 5 == 0:
    print("buzz")
else :
    print(num)