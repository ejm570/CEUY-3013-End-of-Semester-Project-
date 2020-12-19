from source import System
import matplotlib.pyplot as plt
##spipe = suction pipe
##dpipe = discharge pipe
##to test code create vectors spipe, dpipe
##spipe, dpipe = (diameter(ft), length(ft), CH value, sum of minor loss coefficients)
##reservoirs = (elevation of R1(ft), elevation of R2(ft))
##x = System(spipe, dpipe, reservoirs, pump inlet elevation in ft)
##all functions required the input of the design flowrate (i.e. x.function(flowrate))
spipe = (4/12, 2000, 100, 13.5)
dpipe = (3/12, 2000, 100, 2.8)
reservoirs = (-13, 75)
x = System(spipe, dpipe, reservoirs, 4)
##functions that generate primary output
x.system_curve(100)
x.impeller_size(100)
x.valid_loc(100)
##intermediate functions
print(x.calc_velocity(100))
print(x.head_loss(100))
print(x.head_req(100))
print(x.NPSH_available(100))
print(x.NPSH_required(100))
##following line shows plot generated in system_curve function
plt.show()
