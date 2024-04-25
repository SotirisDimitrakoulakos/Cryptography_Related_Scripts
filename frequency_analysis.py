
def char_freq(text):
    dct = {}
    for char in text:
        if char not in dct:
            dct[char] = 1
        else:
            dct[char] += 1
    dct_sorted = dict(sorted(dct.items(), key=lambda item: item[1], reverse=True))
    return dct_sorted

ciphertext = "LIQE0NQIXQE,0M0CMXF0HD0XFQEI0NEMHMNQA0MSBDEJQHMDS0EIYQELMSY0DGIEQHMDS0JMLSMYFH0XIEGISH.0HFI0XIEGISH0FQX0QCQUISIL0QSL0XIIUX0MHX0GEIW.0QAGFQ0KZAZ0HFEII0FQX0MLISHMBMIL0Q0REIQUHFEDZYF0MS0ISIJW0ADYMXHMNX.0NDTIEH0QXXIHX0MS0XINHDE0REQTD0SMSI0FQTI0NDSBMEJIL0HFQH0HFI0XFMGJISH0DB0IOGISXMTI0QEJDE0CMAA0GQXX0HFEDZYF0EDZHI0INFD0BMTI0HDJDEEDC0SMYFH0QX0GIE0HFI0AQHIXH0HIAIJIHEW0LQHQ.0NDJJZSMNQHMDS0CMAA0RI0ISNEWGHIL0CMHF0NQIXQE0NMGFIE0LZEMSY0HFI0DGIEQHMDS.0LINEWGH0ZXMSY0HFI0XQJI0UIW0ZGDS0EINIMGH.0M0ZEYI0WDZ0HD0HQUI0HFI0ZHJDXH0GEINQZHMDSX0MS0FQSLAMSY0HFMX0JIXXQYI0QSL0HD0ISXZEI0HFQH0HFI0MSBDEJQHMDS0EIJQMSX0USDCS0DSAW0HD0HEZXHIL0GIEXDSSIA.0EIJIJRIE0CI0QEI0HFI0YZQELMQSX0DB0DZE0SQHMDSX0XINZEMHW0QSL0DZE0XZNNIXX0FMSYIX0DS0XINEINW0QSL0GEINMXMDS.0WDZEX0MS0EIXDATI,0REQTI."

print("\nFrequency of each character: \n"+ str(char_freq(ciphertext)) + "\n\n")


cipherList = []
for i in ciphertext:
    temp = [i, "0"]
    cipherList.append(temp)

while True:
    choice1 = str(input("Replace character: "))
    choice2 = str(input("With character: "))
    if choice1 == "exit" or choice2 == "exit":
        break
    l1 = []
    for i in cipherList:
        if (i[0] == choice1) and (i[1] == '0'):
            temp = [choice2, '1']
            l1.append(temp)
        else:
            l1.append(i)
    cipherList = l1
    pr = [''.join(j) for j in zip(*cipherList)]
    print("\n"+str(pr[0])+"\n\n")



