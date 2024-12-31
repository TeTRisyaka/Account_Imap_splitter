from config import deleteImapPsw, readFromFile, writeResult, printResult

# КОЛИЧЕСТВО КОПИЙ
count = 10

out = 0
fileR = open("accounts.txt", "r")
content = fileR.read()
fileW = open("accounts.txt", "w+")
print(content)
while out < count:
    fileW.write(content)
    out += 1
    print(content)
fileR.close()
fileW.close()
