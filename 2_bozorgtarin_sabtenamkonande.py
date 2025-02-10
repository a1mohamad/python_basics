vorodi_1 = int (input())
vorodi_2 = int (input())
if vorodi_1 > vorodi_2 :
    bozorgtarin = vorodi_1
    naeb_bozorg = vorodi_2
else :
    bozorgtarin = vorodi_2
    naeb_bozorg = vorodi_1
vorodi_3 = int (input())
while vorodi_3 != -1 :
    vorodi_3 = int(input())
    if vorodi_3 > bozorgtarin :
        bozorgtarin = vorodi_3
    elif naeb_bozorg < vorodi_3 < bozorgtarin :
        naeb_bozorg = vorodi_3

print(bozorgtarin ,'', naeb_bozorg)                