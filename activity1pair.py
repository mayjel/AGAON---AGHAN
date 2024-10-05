number = init(input(" how many number would you like"))
number = []

for x in range(number):
    ask = input("numbers?:")
    number .append(ask)

    print(numbers)

    for number in numbers:
        if number > "0" :
            print(number + "positive")
        elif number < "0":
            print(number + "negative")
        else:
            print("ERRRNGK")