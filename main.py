# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def printxtimes(loopNum, firstName, middleName, lastName):
    for y in range(loopNum):
        label = "Hi {} {} {} number {}."
        print(label.format(firstName, middleName, lastName, y))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    loopNum = 50
    firstName = '1'
    middleName = '2'
    lastName = '3'
    printxtimes(loopNum, firstName, middleName, lastName)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
