import pyotp

wrd1 = ""
wrd2 = ""
wrd3 = ""
wrd4 = ""
wrd5 = ""
wrd6 = ""
wrd7 = ""
wrd8 = ""


def check_number():  # Убрать -1 после успешного запуска
    global word_num
    if word_num == "00":
        word_num = 1
    elif word_num == "01":
        word_num = 1
    elif word_num == "02":
        word_num = 2 - 1
    elif word_num == "03":
        word_num = 3 - 1
    elif word_num == "04":
        word_num = 4 - 1
    elif word_num == "05":
        word_num = 5 - 1
    elif word_num == "06":
        word_num = 6 - 1
    elif word_num == "07":
        word_num = 7 - 1
    elif word_num == "08":
        word_num = 8 - 1
    elif word_num == "09":
        word_num = 9 - 1
    elif str(word_num)[:1] == "-":
        word_num = int(str(word_num).replace("-", ""))
    elif int(word_num) == 0:
        word_num += 1
    else:
        word_num = int(word_num) - 1


def read_line(file, linenumber):
    with open(file) as fp:
        for i, line in enumerate(fp):
            if i == linenumber:
                return line


def word_generate():
    global word_num
    global wrd1, wrd2, wrd3, wrd4, wrd5, wrd6, wrd7, wrd8
    key = "CFLVB44VY6TM7CAM"  # pyotp.random_base32()
    # print(key)
    totp = pyotp.TOTP(key)
    #print(totp.now())

    # word 1

    word_num = totp.now()[:2]
    check_number()
    word_num1 = word_num
    word1 = read_line("words.txt", int(word_num1))
    wrd1 = word1
    #print(word1)

    # word 2

    word_num = totp.now()[2] + totp.now()[3]
    check_number()
    word_num2 = word_num
    word2 = read_line("words.txt", int(word_num2))
    wrd2 = word2
    #print(word2)

    # word 3

    word_num = totp.now()[4] + totp.now()[5]
    check_number()
    word_num3 = word_num
    word3 = read_line("words.txt", int(word_num3))
    wrd3 = word3
    #print(word3)

    # word 4

    word_num4 = int(word_num1) * int(word_num2) - int(word_num3)
    word_num = word_num4 - 1
    check_number()
    word_num4 = word_num
    # print(word_num4)
    word4 = read_line("words.txt", int(word_num4))
    wrd4 = word4
    #print(word4)

    # word 5

    word_num5 = int(word_num4) - int(word_num2) + int(word_num3)
    word_num = word_num5 - 1
    check_number()
    word_num5 = word_num
    # print(word_num5)
    word5 = read_line("words.txt", int(word_num5))
    wrd5 = word5
    #print(word5)

    # word 6

    word_num6 = int(word_num5) - int(word_num1) + int(word_num2)
    word_num = word_num6 - 1
    check_number()
    word_num6 = word_num
    # print(word_num6)
    word6 = read_line("words.txt", int(word_num6))
    wrd6 = word6
    #print(word6)

    # word 7

    word_num7 = int(word_num6) + int(word_num1) - int(word_num3)
    word_num = word_num7 - 1
    check_number()
    word_num7 = word_num
    # print(word_num7)
    word7 = read_line("words.txt", int(word_num7))
    wrd7 = word7
    #print(word7)

    # word 8

    word_num8 = int(word_num2) + int(word_num1) - int(word_num3)
    word_num = word_num8 - 1
    check_number()
    word_num8 = word_num
    # print(word_num8)
    word8 = read_line("words.txt", int(word_num8))
    wrd8 = word8
    #print(word8)
