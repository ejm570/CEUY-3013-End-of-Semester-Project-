from source import System
import matplotlib.pyplot as plt
##spipe = suction pipe
##dpipe = discharge pipe
##to test code create vectors spipe, dpipe
##spipe, dpipe = (diameter(ft), length(ft), CH value, sum of minor loss coefficients)
##reservoirs = (elevation of R1(ft), elevation of R2(ft))
##x = System(spipe, dpipe, reservoirs, pump inlet elevation in ft)
##all functions required the input of the design flowrate (i.e. x.function(flowrate))
spipe = (4/12, 50, 100, 13.5)
dpipe = (3/12, 250, 100, 2.8)
reservoirs = (-13, 75)
x = System(spipe, dpipe, reservoirs, 4)
##functions that generate primary output
x.system_curve(92)
x.impeller_size(92)
x.valid_loc(92)
##intermediate functions
print(x.calc_velocity(92))
print(x.head_loss(92))
print(x.head_req(92))
print(x.NPSH_available(92))
print(x.NPSH_required(92))
##following line shows plot generated in system_curve function
plt.show()
