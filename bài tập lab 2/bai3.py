n=int(input("Nhập vào một số nguyên: "))
tram=n//100
chuc=(n//10)%10
dvi=n%10
if tram == 0:
    tram = ""
elif tram == 1:
    tram = "one hundred"
elif tram == 2:
    tram = "two hundred"
elif tram == 3:
    tram = "three hundred"
elif tram == 4:
    tram = "four hundred"
elif tram == 5:
    tram = "five hundred"
elif tram == 6:
    tram = "six hundred"
elif tram == 7:
    tram = "seven hundred"
elif tram == 8:
    tram = "eight hundred"
elif tram == 9:
    tram = "nine hundred"

if chuc == 0:
    chuc = ""
elif chuc == 1:
    if dvi == 0:
        chuc = "ten"
    elif dvi == 1:
        chuc = "eleven"
    elif dvi == 2:
        chuc = "twelve"
    elif dvi == 3:
        chuc = "thirteen"
    elif dvi == 4:
        chuc = "fourteen"
    elif dvi == 5:
        chuc = "fifteen"
    elif dvi == 6:
        chuc = "sixteen"
    elif dvi == 7:
        chuc = "seventeen"
    elif dvi == 8:
        chuc = "eighteen"
    elif dvi == 9:
        chuc = "nineteen"
else:
    if chuc == 2:
        chuc = "twenty"
    elif chuc == 3:
        chuc = "thirty"
    elif chuc == 4:
        chuc = "forty"
    elif chuc == 5:
        chuc = "fifty"
    elif chuc == 6:
        chuc = "sixty"
    elif chuc == 7:
        chuc = "seventy"
    elif chuc == 8:
        chuc = "eighty"
    elif chuc == 9:
        chuc = "ninety"

if dvi == 0:
    dvi = ""
elif dvi == 1:
    dvi = "one"
elif dvi == 2:
    dvir = "two"
elif dvi == 3:
    dvi = "three"
elif dvi == 4:
    dvi = "four"
elif dvi == 5:
    dvi = "five"
elif dvi == 6:
    dvi = "six"
elif dvi == 7:
    dvi = "seven"
elif dvi == 8:
    dvi = "eight"
elif dvi == 9:
    dvi = "nine"

print(tram,chuc,dvi)