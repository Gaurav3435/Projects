#Gaurav Patil A-33
# # importing required libraries
import numpy
 
# creating the 2D Array
TwoDList = [[1, 2, 3], 
            [4, 5, 6],
            [7, 8, 9], 
            [10, 11, 12]]
TwoDArray = numpy.array(TwoDList)
 
# displaying the 2D Array
print("2D Array:")
print(TwoDArray)
 
# printing the sum of each column
print("\nColumn-wise Sum:")
print(numpy.sum(TwoDArray, axis = 0))