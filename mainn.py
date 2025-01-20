"""16"""
# x1=float(input("X1="))
# x2=float(input("X2="))

# distance=abs(x2-x1)
# print(distance)

"""17"""
# A=float(input("A: "))
# B=float(input("B: "))
# C=float(input("C: "))

# AC=abs(C-A)  
# BC=abs(C-B)
# gathered=AC+BC
# print(AC)
# print(BC)
# print(gathered)

"""18"""
# A=float(input("A: "))
# B=float(input("B: "))
# C=float(input("C: "))

# AC=abs(C-A)
# BC=abs(C-B)
# multiplication=AC*BC
# print(AC)
# print(BC)
# print(multiplication)

"""19"""
# x1 = float(input("Birinchi uchning x1 koordinatasi: "))
# y1 = float(input("Birinchi uchning y1 koordinatasi: "))
# x2 = float(input("Ikkinchi uchning x2 koordinatasi: "))
# y2 = float(input("Ikkinchi uchning y2 koordinatasi: "))

# uzunlik = abs(x2 - x1) 
# kenglik = abs(y2 - y1)  

# perimetr = 2 * (uzunlik + kenglik)
# yuza = uzunlik * kenglik

# print(f"To'g'ri to'rtburchakning perimetri: {perimetr}")
# print(f"To'g'ri to'rtburchakning yuzasi: {yuza}")


"""20"""
# import math

# x1 = float(input("Birinchi nuqtaning x1 koordinatasi: "))
# y1 = float(input("Birinchi nuqtaning y1 koordinatasi: "))
# x2 = float(input("Ikkinchi nuqtaning x2 koordinatasi: "))
# y2 = float(input("Ikkinchi nuqtaning y2 koordinatasi: "))

# masofa = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# print(f"Nuqtalar orasidagi masofa: {masofa}")


"""21"""
# import math

# x1=float(input("X1="))
# y1=float(input("Y1="))
# x2=float(input("X2="))
# y2=float(input("Y2="))
# x3=float(input("X3="))
# y3=float(input("Y3="))

# a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
# b = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)  
# c = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)  

# p = (a + b + c) / 2 
# perimetr = a + b + c

# yuza = math.sqrt(p * (p - a) * (p - b) * (p - c))

# print(f"AB tomon uzunligi: {a}")
# print(f"BC tomon uzunligi: {b}")
# print(f"AC tomon uzunligi: {c}")
# print(f"Uchburchakning perimetri: {perimetr}")
# print(f"Uchburchakning yuzasi: {yuza}")

"""22"""
A = int(input("A sonini kiriting: "))
B = int(input("B sonini kiriting: "))

A, B = B, A

print("A ning yangi qiymati:", A)
print("B ning yangi qiymati:", B)

"""23"""
A = int(input("A sonini kiriting: "))
B = int(input("B sonini kiriting: "))
C = int(input("C sonini kiriting: "))

A, B, C = B, C, A

print("A ning yangi qiymati:", A)
print("B ning yangi qiymati:", B)
print("C ning yangi qiymati:", C)

"""24"""
A = int(input("A sonini kiriting: "))
B = int(input("B sonini kiriting: "))
C = int(input("C sonini kiriting: "))

A, B, C = C, A, B

print("A ning yangi qiymati:", A)
print("B ning yangi qiymati:", B)
print("C ning yangi qiymati:", C)

"""25"""
A = 3
B = 6
C = 7
x = int(input(""))

Y = A*x**5-B*x**2-C
print(Y)

