import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Bell & Gossett Pump Curves.csv')
df2 = pd.read_csv('Bell & Gossett NPSHR.csv')

class System:
    def __init__(self, suctionpipe, dischargepipe, reservoirs, pumplocation):
        """
        suctionpipe, dischargepipe and reservoirs are vectors, pumploc and flowrate are scalar:
        pipes = (diameter, length, CH value, sum of minor loss coefficients); diameter and length in feet
        reservoirs = (elevation of R1, elevation of R2); in feet
        pumploc = elevation of pump inlet in feet
        flowrate = design flowrate in gpm
        """
        self.suctionpipe = suctionpipe
        self.dischargepipe = dischargepipe
        self.reservoirs = reservoirs
        self.pumplocation = pumplocation

    def calc_velocity(self, flowrate):
        """
        calculates the velocities in each pipe
        """
        Qx = flowrate*(1/60)*(1/7.48) ##conversion to cfs
        Ds, Dd = self.suctionpipe[0], self.dischargepipe[0] ##assigning diameters
        ##calculating velocities in each pipe using Q = AV
        Vs, Vd = (4*Qx)/(math.pi*Ds**2), (4*Qx)/(math.pi*Dd**2)
        return Vs, Vd

    def head_loss(self, flowrate):
        """
        function calculates the total headloss in each pipe, suction and discharge,
        using the Hazen-Williams equation and minor loss equation
        """
        ##assigning velocities, diameters, lengths, CH values and minor losses
        Vs, Vd = self.calc_velocity(flowrate)
        Ds, Dd = self.suctionpipe[0], self.dischargepipe[0]
        Ls, Ld = self.suctionpipe[1], self.dischargepipe[1]
        CHs, CHd = self.suctionpipe[2], self.dischargepipe[2]
        Ks, Kd = self.suctionpipe[3], self.dischargepipe[3]
        ##Calculating headloss in each pipe using Hazen-Williams
        hLs, hLd = (Ls*Vs**1.85)/(((1.318*CHs)**1.85)*(Ds/4)**1.17), (Ld*Vd**1.85)/(((1.318*CHd)**1.85)*(Dd/4)**1.17)
        ##calculating minor losses in each pipe
        hMs, hMd = Ks*((Vs**2)/(2*32.2)), Kd*((Vd**2)/(2*32.2))
        return (hLs + hMs), (hLd + hMd)

    def head_req(self, flowrate):
        """
        Function calculates required head needed by pump using simplified energy equation
        in two reservoirs gage pressures are zero and water surface velocities are neglible
        """
        return self.reservoirs[1] - self.reservoirs[0] + sum(self.head_loss(flowrate))

    def system_curve(self, flowrate):
        """
        function for graphing system curve, including marker that represents the head required at the specified design flowrate
        also graphs Bell & Gossett Series 80-SC curves for pump sizes 5.0-7.0 inches for comparison
        """
        Q = flowrate
        hp = self.head_req(Q)
        xval = df['Capacity']
        yval = []
        for i in xval:
            yval.append(self.head_req(i))
        pump1, pump2, pump3, pump4, pump5 = df['5.0-inch'], df['5.5-inch'], df['6.0-inch'], df['6.5-inch'], df['7.0-inch']
        plt.plot(xval, yval, color='red', label = "System Curve")
        plt.plot(Q, hp, marker="X", linewidth=5, markersize=12)
        plt.plot(xval, pump5, color='black', label = '7.0 in')
        plt.plot(xval, pump4, color='black', label = '6.5 in')
        plt.plot(xval, pump3, color='black', label = '6.0 in')
        plt.plot(xval, pump2, color='black', label = '5.5 in')
        plt.plot(xval, pump1, color='black', label = '5.0 in')
        plt.title('System Curve and Pump Curves', fontweight='bold')
        plt.xlabel('Flowrate (GPM)')
        plt.ylabel('Head (ft)')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
        plt.show()
        print('Design Flowrate =', Q, 'gpm')
        print('Total Head Required =', round(hp, 1), 'ft')
        return None

    def impeller_size(self, flowrate):
        """
        function that determines what impeller size to choose, uses "same input" as head_req and "system_curve" functions
        note #1: can only work for flowrates 0-140 at intervals of 10 due to dataframe restrictions
            for all other flowrates solve for impeller size visually using "system_curve" function
        note #2: results may also be out of range of pump curves, which can be seen visually in out put of "system_curve" function
            in this case, this function will return an "Out of Range" message
        """
        Q = flowrate
        h = self.head_req(Q)
        ##assigning list of column names for later use ['Capacity', '7.0-inch',	'6.5-inch',	'6.0-inch',	'5.5-inch', '5.0-inch']
        xval = list(df.columns)
        count1 = 0
        count2 = 0
        countNaN = 0
        ##for loop below inspects all pump head values at specificed flowrate for 4 cases
        ##1) where pump values is greater than the head required
        ##2) where pump values are less than the head required
        ##3) where a pump value is exactly equal to head required
        ##4) where the design flowrate is out of the domain of the pump curve
        for index, i in enumerate(df.loc[Q/10][1:]):
            if i > h:
                count1 = count1 +1
            elif i < h:
                count2 = count2 +1
            elif i == h:
                ##in this case function is ended because pump size meets demand perfectly
                print('Impeller size that meets demand is', list(df.columns)[index+1])
                print('Throttling flow is not required')
            return None
        else:
            ##keeps track of NaN values (where flowrate is out of domain)
            countNaN = countNaN+1
        ##if-statement below identifies cases where pump size cannot be determined because of pump curve limitations
        ##this happens when all four cases in the first statement are untrue (else statement)
        ##(i.e. when pump head in pump curve right below point of head required is NaN)
        ##and when the head-required is above maximum head of all 5 pumps (elif statement)
        if (count1 == 1 and countNaN < 4) or (count1 == 2 and countNaN < 3) or (count1 == 3 and countNaN < 2) or (count1 == 4 and countNaN < 1):
            count3 = countNaN + count2
            ##print function below indexes list of column names using counts accumulated in for loop
            print('Point is between', xval[6-count3], 'and', xval[count1])
            print('Choose impeller size:', xval[count1])
            print('Throttle flow to limit flowrate to', Q, 'gpm')
        elif count1 == 0:
            print("Out of Range: The head required is above all pump capabilities")
        else:
            print("Out of Range: Outside pump curve domain")
        return None

    def NPSH_available(self, flowrate):
        """
        function for calculating Net Positive Suction Head Available
        """
        Pvap = 0.26*144 ##vapor pressure of water at 60 degreess fahrenheight in psf
        Patm = 14.7*144 ##atmospheric pressure in psf
        y = 62.4 ##specific weight of water at 60 degrees fahrenheight in pcf
        return self.reservoirs[0] - self.pumplocation - self.head_loss(flowrate)[0] + (Patm - Pvap)/y

    def NPSH_required(self, flowrate):
        """
        function that returns indexed NPSHR from dataframe for specified flowrate
        """
        return  df2[df2['Capacity'] == flowrate]['NPSHR']

    def valid_loc(self, flowrate):
        """
        function that validates position of pump inlet to prevent cavitation in suction pipe
        note #1: can only work for flowrates 0-140 at intervals of 5 due to dataframe restrictions
        """
        ##NPSHA is compared with Net Pump Section Head Required at the design flowrate based on data
        if 1 == sum((df2['NPSHR'] < self.NPSH_available(flowrate)) & (df2['Capacity'] == flowrate)):
            print("Proposed elevation of pump,", self.pumplocation, "ft, will work")
        else:
            print("Proposed elevation of pump,", self.pumplocation, "ft, may cause cavitation")
        return None
