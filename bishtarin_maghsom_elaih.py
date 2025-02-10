
        #define fuunction start

def tedad_maghsom_elaih(vorodi) :
    c= 0
    for i in range(1 , vorodi) :
        if (vorodi % i == 0) :
         c += 1
    tedad = c + 1
    return tedad

        #define function end

        #insert two simple input start
vorodi_1 = int (input())
vorodi_2 = int (input())
        #insert two simple function end

        #compring inputs for perpuse start
if tedad_maghsom_elaih(vorodi_1) > tedad_maghsom_elaih(vorodi_2) :
    bishtarin_maghsom_elaih = vorodi_1
elif tedad_maghsom_elaih(vorodi_2) > tedad_maghsom_elaih(vorodi_1) :
    bishtarin_maghsom_elaih = vorodi_2
elif tedad_maghsom_elaih(vorodi_1) == tedad_maghsom_elaih(vorodi_2) and vorodi_1 > vorodi_2 :
    bishtarin_maghsom_elaih = vorodi_1
elif tedad_maghsom_elaih(vorodi_1) == tedad_maghsom_elaih(vorodi_2) and vorodi_2 > vorodi_1 :
    bishtarin_maghsom_elaih = vorodi_2
        #comparing inputs for perpuse end


        #loop to continue comparing start
for vorodi_3 in range(1 , 18) :
    vorodi_3 = int (input())
    if tedad_maghsom_elaih(vorodi_3) > tedad_maghsom_elaih(bishtarin_maghsom_elaih) :
        bishtarin_maghsom_elaih = vorodi_3
    elif tedad_maghsom_elaih(vorodi_3) == tedad_maghsom_elaih(bishtarin_maghsom_elaih) and vorodi_3 > bishtarin_maghsom_elaih :
        bishtarin_maghsom_elaih = vorodi_3
        #loop to continue comparing start

                        #result

print(bishtarin_maghsom_elaih,tedad_maghsom_elaih(bishtarin_maghsom_elaih))

