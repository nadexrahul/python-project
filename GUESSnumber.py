n1 = 0
# print("you have 5 chance to enter the correct number"
while n1 < 2:
    print("you enter the number", end=" ")
    num1 = int(input())

    if num1 == 20:
        print("winner")
        break
    elif num1 < 15:
        print("smaller \ntry again")
    elif num1 > 25:
        print("greater \ntry again")
    elif num1 >= 15 & num1 <= 25:
        print("close \ntry again")

    else:
        continue

    n1 = n1 + 1

    if n1 > 2:
        break

print("\nGame over")