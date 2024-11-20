from config import deleteImapPsw, readFromFile, writeResult, printResult

if deleteImapPsw:
    if readFromFile:
        fileR = open("accounts.txt", "r")
        if writeResult:
            fileW = open("accounts.txt", "w+")
        content = fileR.read()
        psw = content.split()
        for item in psw:
            spl = item.split(":")
            if writeResult:
                fileW.write(spl[0] + ':' + spl[1] + '\n')
            if printResult:
                print(spl[0] + ':' + spl[1] + '\n')
        fileR.close()
        if writeResult:
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
        if writeResult:
            fileW = open("accounts.txt", "w+")
        psw = fileR.split()
        for item in psw:
            spl = item.split(":")
            if writeResult:
                fileW.write(spl[0] + ':' + spl[1] + '\n')
            if printResult:
                print(spl[0] + ':' + spl[1] + '\n')
        if writeResult:
            fileW.close()
else:
    if readFromFile:
        fileR = open("accounts.txt", "r")
        if writeResult:
            fileW = open("accounts_imap.txt", "w+")
        content = fileR.read()
        psw = content.split()
        for item in psw:
            spl = item.split(":")
            if writeResult:
                fileW.write(spl[0] + ':' + spl[1] + ':' + spl[1] + '\n')
            if printResult:
                print(spl[0] + ':' + spl[1] + ':' + spl[1] + '\n')
        fileR.close()
        if writeResult:
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
        if writeResult:
            fileW = open("accounts_imap_test.txt", "w+")
        psw = fileR.split()
        for item in psw:
            spl = item.split(":")
            if writeResult:
                fileW.write(spl[0] + ':' + spl[1] + ':' + spl[1] + '\n')
            if printResult:
                print(spl[0] + ':' + spl[1] + ':' + spl[1])
        if writeResult:
            fileW.close()
