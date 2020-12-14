# CEUY-3013-End-of-Semester-Project-
## **Summary**
This code models a simple pump system. The type of system that this code works for includes one pipe, one suction pipe and one discharge pipe that connects two reservoirs. The program does five different things:
1. Calculates the amount of head the pump needs to add in order for the system to work at a specified flowrate
2. Develops the system curve to model the head required vs. demand through the system
3. Compares the system curve to Bell & Gossett Series 80-SC pump curves and suggests the impeller size to choose if the point falls within the pump curves’ bounds
4. Identifies whether the flow most be throttled when using the suggested impeller size
5. Validates that the location of the pump inlet does not cause cavitation

This program works for any combination of pipe characteristics, pump location and reservoir elevation. If the required head or flowrate is out of the boundaries of the pump curves, the program will return an “Out of Range” message and will state the reason. Other pumps are required to meet the demands of this type of system. Due to the limits of the data frames used for analysis, the flowrate tested must be in multiples of 10 between 0-140 gpm to complete tasks 3 and 4 above. The system curve for any flowrate (not multiple of 10) will be presented visually in task 2. In this case, the user can use the visualization to determine the impeller size to use, but the program will not suggest an impeller size. In the same way, the program will not validate the pump location if the flowrate is not a multiple of 5.
## **Data Frames**
The data frames were made on a CSV file from the Bell & Gossett Series 80-SC pump curves. Pump curves are made from empirical data with no equation to model the relationship. Data was extracted visually from the graph below for the purposes of this project.
Here is the link to the homework assignment from Water Resources Engineering taught by Prof Ronan that included this graph: (https://drive.google.com/file/d/1cu46UzSR8Pyf7BUtbyjVtWvUDvTcBXX-/view?usp=sharing)
## **Example Outputs**
To allow the program to work create three vectors:
1. suctionpipe = (diameter in ft, length in ft, CH friction factor, sum of minor loss coefficients)
2. dischargepipe = (diameter in ft, length in ft, CH friction factor, sum of minor loss coefficients)
3. reservoirs = (elevation of R1 in ft, elevation of R2 in ft)
 
Next define object:
x = System(suctionpipe, dischargepipe, reservoirs, pumplocation in ft)
 
Finally, perform any function defined with your design flowrate inputted:
1. x.system_curve(flowrate)
2. x.impeller_size(flowrate)
3. x.valid_loc(flowrate)
