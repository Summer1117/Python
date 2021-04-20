import re


def CheckString(Text):
    m = re.search(r'[0-9]{4}', Text)
    if len(m.group()) == 4 :
        print("there is 4 Sequence digits in the string")
    result = re.sub(r"[a-zA-Z]", "*", Text)
    print(result)


if __name__ == '__main__':
    CheckString('abc1122a')