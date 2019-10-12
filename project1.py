WorldWater=35000000 #Воды пресной всего в км^3
GrandLakesWater=WorldWater*1000000000 #Всего пресной воды в мире в м^3
GrandLakesWatercorr=GrandLakesWater*0.21 #Всего пресной воды в Великих озерах в м^3
Square=7664000 #Площадь 48 штатов США в км^2
Squarecorr=Square*1000000 #Площадь 48 штатов США в м^2
print(format(GrandLakesWatercorr/Squarecorr,'.2f'),'метров')
