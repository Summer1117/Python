import re


def CheckString(Text):
    number = 0
    m = re.search(r'[0-9]{4}', Text)
    if m is not None:
        print("there is 4 Sequence digits in the string")
    result = re.sub(r"[a-zA-Z]", "*", Text)
    print(result)

    for i in Text:
        if i.isdigit():
            number += 1
            print(i)
    if number >= 4:
        print("there is 4 Sequence digits in the string")



if __name__ == '__main__':
    CheckString('abc1122a')