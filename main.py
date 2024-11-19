

fileR = open("accounts.txt", "r")
fileW = open("accounts_imap.txt", "w+")
content = fileR.read()
psw = content.split()
for item in psw:
    spl = item.split(":")
    fileW.write(spl[0] + ':' + spl[1] + ':' + spl[1] + '\n')
fileR.close()
fileW.close()
