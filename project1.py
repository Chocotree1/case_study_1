world_water = 35_000_000                                               #Воды пресной всего в км^3
Grand_Lakes_Water = World_Water * 1_000_000_000                        #Всего пресной воды в мире в м^3
Grand_Lakes_Water_corr = Grand_Lakes_Water * 0.21                      #Всего пресной воды в Великих озерах в м^3
Square = 7_664_000                                                     #Площадь 48 штатов США в км^2
Square_corr = Square * 1_000_000                                       #Площадь 48 штатов США в м^2
print(format(Grand_Lakes_Water_corr / Square_corr,'.2f'),'метров')
