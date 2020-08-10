import redis

client = redis.Redis(host='192.168.1.2', port=6379)


def Nav():
    print("+" + "-" * 8 + "+" + "-" * 35 + "+" + "-" * 16 + "+")
    print("|  ITEM  |" + " " * 12 + "DESCRIPTION" + " " * 12 + "|" + "     STATUS     |")
    print("+" + "-" * 8 + "+" + "-" * 35 + "+" + "-" * 16 + "+")
    print("|   1    |" + " " * 1 + "Showing 1-100 that contains Fizz" + " " * 2 + "|" + "   Not started  |")
    print("|        |" + " " * 1 + "Buzz ,FizzBuzz mixed" + " " * 14 + "|" + " " * 16 + "|")
    print("+" + "-" * 8 + "+" + "-" * 35 + "+" + "-" * 16 + "+")
    print("|   2    |" + " " * 1 + "Consider it's a leap year or not " + " " * 1 + "|" + "   Not started  |")
    print("+" + "-" * 8 + "+" + "-" * 35 + "+" + "-" * 16 + "+")
    print("|   3    |" + " " * 1 + "Show * in many ways" + " " * 15 + "|" + "   Not started  |")
    print("|  3.1   |" + " " * 4 + "Format 1 " + " " * 22 + "|" + "   Not started  |")
    print("|  3.2   |" + " " * 4 + "Format 2 " + " " * 22 + "|" + "   Not started  |")
    print("|  3.3   |" + " " * 4 + "Format 3 " + " " * 22 + "|" + "   Not started  |")
    print("|  3.4   |" + " " * 4 + "Format 4 " + " " * 22 + "|" + "   Not started  |")
    print("|  3.5   |" + " " * 4 + "Format 5 " + " " * 22 + "|" + "   Not started  |")
    print("|  3.6   |" + " " * 4 + "Format 6 " + " " * 22 + "|" + "   Not started  |")
    print("+" + "-" * 8 + "+" + "-" * 35 + "+" + "-" * 16 + "+")
    print("|   4    |" + " " * 1 + "Difference  else and finally " + " " * 5 + "|" + "   Not started  |")
    print("+" + "-" * 8 + "+" + "-" * 35 + "+" + "-" * 16 + "+")
    print("|   5    |" + " " * 1 + "Medium 1. finds all prime numbers " + "|" + "   Not started  |")
    print("+" + "-" * 8 + "+" + "-" * 35 + "+" + "-" * 16 + "+")
    print()
    print("***Enter number to select item or entering a blank to end program***")


Nav()


def item1():
    ListOfNumber = list(range(1, 101))
    for i in range(1, 101):
        if i % 3 == 0 and not i % 5 == 0:
            ListOfNumber[i - 1] = "Fizz"
        elif i % 5 == 0 and not i % 3 == 0:
            ListOfNumber[i - 1] = "Buzz"
        elif i % 3 == 0 and i % 5 == 0:
            ListOfNumber[i - 1] = "FizzBuzz"
    print(*ListOfNumber)


def item2(year):
    status = []
    if year % 400 == 0:
        status = True
    elif year % 400 != 0 and year % 100 != 0 and year % 4 == 0:
        status = True
    else:
        status = False
    print(str(year) + " is leap year -> " + str(status))


def item3_1(Number):
    for i in range(1, Number + 1):
        print('*' * i)


def item3_2(Number):
    for i in range(1, Number + 1):
        print(' ' * (Number - i) + '*' * i)


def item3_3(Number):
    print(" " * Number + "*")
    for i in range(1, Number):
        print(" " * (Number - i), end="")
        print("*", end="")
        for j in range(1, i * 2):
            print(" ", end="")
        print("*")


def item3_4(Number):
    tag = 0
    if (Number + 1) % 2 != 0:
        Number = Number - 1
        tag = 1
    algo = int(((Number + 1) / 2) - 1)
    for i in range(1, (Number - algo)):
        print(" " * (i - (algo - (algo - 1))), end="")
        print("*", end="")
        for j in range(1, (((Number - algo - i) * 2) + tag)):
            print(" ", end="")
        print("*")
    if tag == 1:
        print(" " * algo + "**")
        print(" " * algo + "**")
    else:
        print(" " * algo + "*")
    for i in range(1, (Number - algo)):
        print(" " * (algo - i), end="")
        print("*", end="")
        for j in range(1, (i * 2) + tag):
            print(" ", end="")
        print("*")


def item3_5(Number):
    Number = Number + 2
    tag = 0  # 0:odd ,1 :even
    if (Number + 1) % 2 != 0:
        tag = 1
    for i in range(1, Number - tag):
        if (float(i) % 2) != 0:
            print(" " * (int((Number - i) / 2) - 1), end="")
            print("*" * i, end="")
            print(" ")
    for i in range(3, Number):
        if (float(i + tag) % 2) == 0:
            print(" " * (int(i / 2) - 1), end="")
            print("*" * (Number - i), end="")
            print(" ")


def item3_6(Number):
    for i in range(0, Number):
        for j in range(1, Number - i):
            print("A", end="")
        print("+", end="")
        if i > 0:
            for j in range(0, (i * 2) - 1):
                print("E", end="")
            print("+", end="")
        for j in range(1, Number - i):
            print("B", end="")
        print(" ")

    for i in range(0, Number - 1):
        for j in range(1, i + 2):
            print("C", end="")
        print("+", end="")
        for j in range(0, ((Number - i - 2) * 2) - 1):
            print("E", end="")
        if i < Number - 2:
            print("+", end="")
        for j in range(1, i + 2):
            print("D", end="")
        print(" ")


def item5(Number):
    NumberList = list(range(2, Number + 1))
    i = 0
    j = 1
    while i < len(NumberList):
        while j < len(NumberList) - i:
            if (NumberList[j + i] % NumberList[i]) == 0:
                NumberList.remove(NumberList[j + i])
                j -= 1
            j += 1
        j = 1
        i += 1
    print(NumberList)


def printitem2():
    x = client.llen('item2')
    for i in range(0, int(x)):
        x = client.lindex('item2', i)
        print(str(i + 1) + "). ", end="")
        item2(int(x))


def printitem3_1():
    x = client.llen('item3_1')
    for i in range(0, int(x)):
        x = client.lindex('item3_1', i)
        print(str(i + 1) + "). ")
        item3_1(int(x))


def printitem3_2():
    x = client.llen('item3_2')
    for i in range(0, int(x)):
        x = client.lindex('item3_2', i)
        print(str(i + 1) + "). ")
        item3_2(int(x))


def printitem3_3():
    x = client.llen('item3_3')
    for i in range(0, int(x)):
        x = client.lindex('item3_3', i)
        print(str(i + 1) + "). ")
        item3_3(int(x))


def printitem3_4():
    x = client.llen('item3_4')
    for i in range(0, int(x)):
        x = client.lindex('item3_4', i)
        print(str(i + 1) + "). ")
        item3_4(int(x))


def printitem3_5():
    x = client.llen('item3_5')
    for i in range(0, int(x)):
        x = client.lindex('item3_5', i)
        print(str(i + 1) + "). ")
        item3_5(int(x))


def printitem3_6():
    x = client.llen('item3_6')
    for i in range(0, int(x)):
        x = client.lindex('item3_6', i)
        print(str(i + 1) + "). ")
        item3_6(int(x))


def printitem5():
    x = client.llen('item5')
    for i in range(0, int(x)):
        x = client.lindex('item5', i)
        print(str(i + 1) + "). ")
        item5(int(x))


def algoform(printitem, strtopic, strdata, strtopic2):
    printitem()
    select = input("Enter a number (1 to Add,2 to Delete) ,entering a blank to main program): ")
    backNav = 0
    while backNav == 0:
        if select == "1":
            cont = 1
            while cont == 1:
                Number = input(
                    "Enter a number to " + strtopic + "or entering a blank to main program : ")
                if Number.isdigit():
                    client.rpush(strdata, Number)
                    printitem()
                    print(strtopic2 + " Completed")
                elif Number.isalpha():
                    print(Number, "is Wrong input !")
                else:
                    Nav()
                    cont = 2
                    backNav = 1
        elif select == "2":
            cont = 2
            while cont == 2:
                selectsubitem = input(" +" + "-" * 13 + "Enter option to delete" + "-" * 13 + "+\n"
                                                                                              " |1:delete last one    | 2:select index to delete |\n "
                                                                                              "|3:delete all         | 4:show data              |\n"
                                                                                              " or entering a blank to main program :")
                if selectsubitem == "1":
                    client.rpop(strdata)
                    printitem()
                    print("delete complete")
                elif selectsubitem == "2":
                    x = client.llen(strdata)
                    selectlredis = input("Enter number of item :")
                    if selectlredis.isdigit() and x >= int(selectlredis):
                        value = client.lindex(strdata, str(int(selectlredis) - 1))
                        client.lrem(strdata, str(int(selectlredis) - 1), value)
                        printitem()
                        print("delete complete")
                    else:
                        print("index " + selectlredis + " don't have data")
                elif selectsubitem == "3":
                    x = client.llen(strdata)
                    for i in range(0, int(x)):
                        client.rpop(strdata)
                    printitem()
                    print("delete complete")
                elif selectsubitem == "4":
                    printitem()
                elif selectsubitem.isdigit() or selectsubitem.isalpha():
                    print(selectsubitem, "is Wrong input !")
                else:
                    Nav()
                    cont = 1
                    backNav = 1
        elif select.isdigit() or select.isalpha():
            print(select, "is Wrong input !")
            select = input("Enter a number (1 to Add,2 to Delete ,entering a blank to main program): ")
        else:
            Nav()
            break


def SelectItem(item):
    while True:

        if item == "1":
            backNav = 0
            while backNav == 0:
                item1()
                input("Press Enter to main program:")
                backNav = 1
                Nav()
        elif item == "2":
            algoform(printitem2, "check leap yeap", "item2", "cal leap year")
        elif item == "3.1":
            algoform(printitem3_1, "Show * Format 1 ", "item3_1", "Add * Format 1 ")
        elif item == "3.2":
            algoform(printitem3_2, "Show * Format 2 ", "item3_2", "Add * Format 2 ")
        elif item == "3.3":
            algoform(printitem3_3, "Show * Format 3 ", "item3_3", "Add * Format 3 ")
        elif item == "3.4":
            algoform(printitem3_4, "Show * Format 4 ", "item3_4", "Add * Format 4 ")
        elif item == "3.5":
            algoform(printitem3_5, "Show * Format 5 ", "item3_5", "Add * Format 5 ")
        elif item == "3.6":
            algoform(printitem3_6, "Show * Format 6 ", "item3_6", "Add * Format 6 ")
        if item == "4":
            backNav = 0
            while backNav == 0:
                print("\nข้อแตกต่างของ 'else' กับ 'finally' คือ \n"
                      "else จะถูกทำงานเมื่อคำสั่งใน try block ไม่มีข้อยกเว้น \n"
                      "finally ทำงานโดยไม่สนว่าข้อความใน try block ล้มเหลวหรือประสบความสำเร็จ\n"
                      "try , except  หากมีการ error ใน try จะข้ามไปทำคำสั่งใน except ต่อ\n"
                      "เช่น \n"
                      "try    : x = x+3 \n"
                      "except : x = 4+4  \n"
                      "else   : print('else'+x)   \n"
                      "finally: print('finally'+x) \n"
                      "จะเห็นว่า ใน try error ทำให้ใน else ไม่ทำงาน แต่ใน finally ทำงาน\n"
                      "ผลลับจึงออกมาเป็น finally8\n")
                input("Press Enter to main program:")
                backNav = 1
                Nav()
        elif item == "5":
            algoform(printitem5, "finds all prime number ", "item5", "finds prime number")
        elif item.isdigit() or item.isalpha():
            print()
        elif item == " ":
            print("thank you for use program.")
            break

        item = input("Please Enter Item number (1,2,4,5 or 3.1-3.6): ")


SelectItem(input("Please Enter Item number (1,2,4,5 or 3.1-3.6): "))
