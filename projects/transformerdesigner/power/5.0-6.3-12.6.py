#!/usr/bin/env python
import math
import Winding, Transformer, Machine

primary      = Winding.Winding('p',120.0,0.0,None)

secondary5   = Winding.Winding('s',4.95 ,5.0,[50],fill=False)
secondary6   = Winding.Winding('s',6.2 ,5.0,[50],fill=False)
secondary12  = Winding.Winding('s',12.4,5.0,[50],fill=False)

t = Transformer.Transformer([primary,secondary5,secondary6,secondary12],650)
t.circularMilsPerAmp = 600.0
t.coreLoss           = 0.80 # watts/lbs
t.isolationThickness = 0.003
t.wrappingThickness  = 0.015
t.insulationLayers   = 2

t.fluxDensity = t.fluxFind(bmax=103000,inc=100,fillmax=95)
#t.fluxDensity = 90000
t.compute()
t.report()



#t.fluxTable(sort='error')

#t.gcode()

#m = Machine.Machine(windings=t.windings)
# m.run()
