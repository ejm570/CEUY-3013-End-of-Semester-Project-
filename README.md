# CEUY-3013-End-of-Semester-Project-
## **Summary**
This code models a simple pump system. The type of system that this code works for includes one pump, one suction pipe and one discharge pipe that connects two reservoirs. The program does five different things:
1. Calculates the amount of head the pump needs to add in order for the system to work at a specified flowrate
2. Develops the system curve to model the head required vs. demand through the system
3. Compares the system curve to Bell & Gossett Series 80-SC pump curves and suggests the impeller size to choose if the point falls within the pump curves’ bounds
4. Identifies whether the flow most be throttled when using the suggested impeller size
5. Validates that the location of the pump inlet does not cause cavitation

This program works for any combination of pipe characteristics, pump location and reservoir elevation. If the required head or flowrate is out of the boundaries of the pump curves, the program will return an “Out of Range” message and will state the reason. Other pumps are required to meet the demands of this type of system. Due to the limits of the data frames used for analysis, the flowrate tested must be in multiples of 10 between 0-140 gpm to complete tasks 3 and 4 above. The system curve for any flowrate (not multiple of 10) will be presented visually in task 2. In this case, the user can use the visualization to determine the impeller size to use, but the program will not suggest an impeller size. In the same way, the program will not validate the pump location if the flowrate is not a multiple of 5.
## **Data Frames**
The data frames were made on a CSV file from the Bell & Gossett Series 80-SC pump curves. Pump curves are made from empirical data with no equation to model the relationship. Data was extracted visually from the graph below for the purposes of this project.
![Pump Curves](https://user-images.githubusercontent.com/73856285/102037691-82455200-3d93-11eb-8811-99317776246d.PNG)

Here is the link to the homework assignment from Water Resources Engineering taught by Prof Ronan that included this graph: (https://drive.google.com/file/d/1cu46UzSR8Pyf7BUtbyjVtWvUDvTcBXX-/view?usp=sharing)
## **Example Outputs**
To allow the program to work first import the class and matplotlib.pyplot:
1. from source import System
2. import matplotlib.pyplot as plt

Create three vectors:
1. suctionpipe = (diameter in ft, length in ft, CH friction factor, sum of minor loss coefficients)
2. dischargepipe = (diameter in ft, length in ft, CH friction factor, sum of minor loss coefficients)
3. reservoirs = (elevation of R1 in ft, elevation of R2 in ft)
 
Next define object:
1. x = System(suctionpipe, dischargepipe, reservoirs, pump inlet elevation in ft)
 
Perform any function defined with your design flowrate inputted:
1. x.system_curve(flowrate)
2. x.impeller_size(flowrate)
3. x.valid_loc(flowrate)

Lastly, show system curve and pump curves:
1. plt.show()

Example 1:
Case where all functions give intended output  
![Example 1](https://user-images.githubusercontent.com/73856285/102038390-1bc13380-3d95-11eb-9eae-95ea76825213.PNG)

Example 2:
Case where marker is out of pump curve bounds
![Example 2](https://user-images.githubusercontent.com/73856285/102037939-0c8db600-3d94-11eb-8279-668c729fb857.PNG)
 
Example 3:
Case where the head required exceeds pump capabilities

![Example3](https://user-images.githubusercontent.com/73856285/102037946-11526a00-3d94-11eb-84de-a8fd81db50a8.PNG)
 
Example 4:
Case where flowrate is not divisible by 10 or 5 and tasks 3-5 cannot be performed
![Example4](https://user-images.githubusercontent.com/73856285/102037969-20d1b300-3d94-11eb-8475-1af5bf3f3025.PNG)

