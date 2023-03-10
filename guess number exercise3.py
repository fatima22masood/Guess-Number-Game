n= 23
i=10
while(i>0):
    print("guess number")
    num= int(input())
    i = i - 1
    print("no of guesses left", i)

    if num== 23:
        print("your number is correct")
        break

    elif num<23:
        print("increase your number")
    else:
        print("decrease your number")
print("game over!")