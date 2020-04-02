import xlrd


shdata = []
txtDst = 0

mnObj = []
fdstIP = []
fhostIP = []

pss = []


def getWB(PATHWB, PATHDST, shNAME):
    global txtDst

    wb = xlrd.open_workbook(PATHWB)                     #opens workbook by path
    p = wb.sheet_names()

    txtDst = open(PATHDST, "w")                         #specifies destination file, writable

    for y in p:                                         #appends wb to new string array
        sh = wb.sheet_by_name(shNAME)                   #name of the sheet to work with
        for rownum in range(sh.nrows):
            shdata.append((sh.row_values(rownum)))



def prArr():
    global mnObj
    global fdstIP
    global fhostIP

    mnObj = [str(i).split("object")[1:] for i in shdata]
    mnObj = [str(i).split('"')[1:] for i in mnObj]
    mnObj = [str(i).split('"')[0] for i in mnObj]
    mnObj = [str(i).split("'")[1:] for i in mnObj]      #final managed object array, splitted

    fdstIP = [str(i).split("dst")[1:] for i in shdata]
    fdstIP = [str(i).split(' "')[0] for i in fdstIP]
    fdstIP = [str(i).split(' ')[1:] for i in fdstIP]    #final dst ip array, splitted

    fhostIP = [str(i).split("host")[1:] for i in shdata]
    fhostIP = [str(i).split(',')[0] for i in fhostIP]
    fhostIP = [str(i).split(' ')[1:] for i in fhostIP]  #final host ip array, splitted



def getDict(x):                                         #getting rid of repeated objects, going from a-z and 0-9
    x.sort()
    return list(dict.fromkeys(x))



def appArr():
    global mnObj
    global fdstIP
    global fhostIP

    x = 0
    for i in mnObj:                                     #appends to pss list
        if not (fdstIP[x]) and not (fhostIP[x]):
            1
        else:
            pss.append(''.join(map(str, i)) + ''.join(map(str, fdstIP[x])) + ''.join(map(str, fhostIP[x])))

        x += 1

    fPass = getDict(pss)

    return fPass



def writeTo(passedArr):
    global txtDst

    for i in passedArr:
        txtDst.write(str(i) + ('\n' * 2))               #passing onto the txt file

    txtDst.close()



getWB("path-to-wb", "path-to-txt", "working-sheet")
prArr()
writeTo(appArr())
