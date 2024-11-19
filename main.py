


# True, если вы используете текстовый файл, False, если хотите вставить скопированный текст
readFile = False


if readFile == True:
    fileR = open("accounts.txt", "r")
    fileW = open("accounts_imap.txt", "w+")
    content = fileR.read()
    psw = content.split()
    for item in psw:
        spl = item.split(":")
        fileW.write(spl[0] + ':' + spl[1] + ':' + spl[1] + '\n')
    fileR.close()
    fileW.close()
else:
    fileR = ""
    print("Введите данные в консоль в формате почта:пароль (без разрывов строк)")
    while True:
        text = input()
        if text:
            fileR += text + " "
        else:
            break
    fileW = open("accounts_imap_test.txt", "w+")
    psw = fileR.split()
    for item in psw:
        spl = item.split(":")
        fileW.write(spl[0] + ':' + spl[1] + ':' + spl[1] + '\n')
    fileW.close()