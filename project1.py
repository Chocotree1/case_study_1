world_water = 35_000_000                                               #Воды пресной всего в км^3
grand_lakes_water = world_water * 1_000_000_000                        #Всего пресной воды в мире в м^3
grand_lakes_water_corr = grand_lakes_water * 0.21                      #Всего пресной воды в Великих озерах в м^3
square = 7_664_000                                                     #Площадь 48 штатов США в км^2
square_corr = square * 1_000_000                                       #Площадь 48 штатов США в м^2
print(format(grand_lakes_water_corr / square_corr,'.2f'),'метров')
