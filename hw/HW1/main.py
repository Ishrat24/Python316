 #Name : Ishrat Amin


# Make definitions here
  # 1.First, we'll utilize the input() function for radius to take user input and save it in a variable.
  # 2. The value of "pi" can be stored using a constant.
  # 3.The formula area = Radius** 2 * math.pi will now be used to 
  # determine the area of a circle.

   # 4.Finally, print a circle's area to get the output.

import math  
  
def compute_area_circle (Radius):  
  
   # processing using a function
  
    area = Radius** 2 * math.pi  
    return area  
 # get the radius using a function  
  
Radius = float (input ("Please enter the radius of circle: "))  

# output the area here by calling a function

print (" The area of the circle is: ", compute_area_circle (Radius))  
