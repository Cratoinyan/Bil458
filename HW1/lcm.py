def find_lcm(num1, num2):

    #find the bigger number
    if num1 > num2:
        greater = num1
    else:
        greater = num2

    #start from the greater number and go until lcm is found
    while True:
        if greater % num1 == 0 and greater % num2 == 0:
            lcm = greater
            break
        greater += 1

    return lcm


if __name__ == "__main__":

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    lcm = find_lcm(num1, num2)

    print("The LCM of", num1, "and", num2, "is", lcm)