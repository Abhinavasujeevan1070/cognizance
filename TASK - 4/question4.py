pal=input("enter the number")
j=int(len(pal))
cal=pal[j-1::-1]
if (pal==cal):
    print("it is a palindrome")

else:
    print("it is not a palinndrome")

