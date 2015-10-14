from util import *

T0 = 273.16

T = T0 + 20
rh = 1.0
q = 0.001
p = 100000

c = HumidityConverter(p, T, q)

print c.t_rh_to_q()
c.set_relhum(rh)

print c.t_rh_to_q()
