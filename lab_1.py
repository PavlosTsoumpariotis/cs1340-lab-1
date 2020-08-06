#print() is for a line break
message = """
At the prompt please enter the following:

Customer's classification code
Number of days vehicle was rented
Vehicle's odometer reading at the beginning of the period
Vehicle's odometer reading at the end of the period"""
print(message)
print()
while True:
    clasfcode = input("Customer's Classification Code:")
    if clasfcode == "b" or clasfcode == "B":
        days = input("number of day vehicles was rented:")
        start = input("Vehicle's odometer reading at the beginning of the period:")
        end = input("Vehicle's odometer reading at the end of the period:")
        miles = (float(end) - float(start))
        avgmiles = (float(end) - float(start)) // float(days)
        amtdue = 40.00 * float(days) + (float(end) - float(start))*0.25
        print()
        print("customer's classification code:", str(clasfcode))
        print("number of days vehicle was rented: ", str(days))
        print("Vehicle's odometer reading at the beginning of the period:", str(start))
        print("Vehicles' odometer reading at the end of the period:", str(end))
        print("Number of miles driven:", str(miles))
        print("Amount Due: $", str(amtdue))
        print()

    elif clasfcode == "d" or clasfcode == "D":
        days = input("number of day vehicles was rented:")
        start = input("Vehicle's odometer reading at the beginning of the period:")
        end = input("Vehicle's odometer reading at the end of the period:")
        miles = (float(end) - float(start))
        avgmiles = (float(end) - float(start)) / float(days)
        if float(avgmiles) >= float(100.00):
            amtdue = (60.00 * float(days)) + (float(avgmiles) - 100.00)*0.25*float(days)
            print()
            print("number of days vehicle was rented: ", str(days))
            print("Vehicle's odometer reading at the beginning of the period:", str(start))
            print("Vehicles' odometer reading at the end of the period:", str(end))
            print("Number of miles driven:", str(miles))
            print("Amount due: $", str(amtdue))
            print()

        else:
            amtdue = 60.00 * float(days)
            print()
            print("number of days vehicle was rented:", str(days))
            print("Vehicle's odometer reading at the beginning of the period:", str(start))
            print("Vehicles' odometer reading at the end of the period:", str(end))
            print("Number of miles driven:", str(miles))
            print("Amount Due: $", str(amtdue))
            print()

    elif clasfcode == "Q" or clasfcode == "q":
        break

    else:
        print("Please put valid classification code b or d")