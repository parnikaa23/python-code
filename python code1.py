Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #lambda fuction
... root_1=lambda a,b,c: (-b +((b*2-4*a*c)**0.5))/(2*a)
... root_2=lambda a,b,c: (-b -((b*2-4*a*c)**0.5))/(2*a)
... a=int(input("a: "))
... b=int(input("b: "))
... c=int(input("c: "))
... ptint(root_1(a,b,c))
