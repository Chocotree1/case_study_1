world_water = 35_000_000                                               #Fresh water in km^3
grand_lakes_water = world_water * 1_000_000_000                        #Fresh water in the world in m^3
grand_lakes_water_corr = grand_lakes_water * 0.21                      #ВFresh water in Grand Lakes in m^3
square = 7_664_000                                                     #Square of 48 states of USA in km^2
square_corr = square * 1_000_000                                       #Square of 48 states of USA in m^2
print(format(grand_lakes_water_corr / square_corr,'.2f'),'meters')
