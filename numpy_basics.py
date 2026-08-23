import numpy as np
#Import NumPy and give it the short name np.
temperatures = np.array([32.5,31.2,33.1])

#Python list vs NumPy array 
'''
Python list vs NumPy array
python_list = [32.5,31.2,33.1]
numpy_array = np.array([32.5,31.2,33.1])
print(type(python_list))
print(type(numpy_array))

So here Python list -> list  Numpy array -> numpy.ndarray
and here ndarray means : N-dimensional array.
'''

print(temperatures)
temperatures = np.array([32.5,31.2,33.1])
updated = temperatures + 1
print(updated)
'''
this is the important idea of NumPy and this is called
vectorized operations which is here we have done 
temperatures + 1,where we dont explicitly write the loop.
we can do multiplication,subtraction,division,array+array here for this 
array + array,both array sizes should be same(number of elements)
and here this size of the array is called as Shape
here if we do as -> temperatures = np.array([32.5,31.3,33.1])
print(temperatures.shape)
Output -> (3,) which means 3 elements and here this comma(,)represents that this is a one-dimensional shape tuple.
Which means - (3,)->1D array containing 3 elements.
---> .ndim->Now print(temperatures.ndim) , output is 1 so shape(3,) dimensions->1
---> .size here print(temperature.size) returns 3 
So:  shape->structure 
     ndim -> number of dimensions 
     size -> total number of elements
These three properties are extremely important.
->.dtype ,Now print(temperatures.dtype) ->tells us the data type NumPy is using to store the array elements.
'''
temperatures = np.array([32.5,31.2,33.1,30.8,34.2])
humidity = np.array([61,58,64,55,67])
pm25 = np.array([82,71,91,65,105])
print("Temperatures:",temperatures)
print("Humidity:",humidity)
print("PM2.5:",pm25)

print("Temperature shape:",temperatures.shape)
print("Temperature dimensions:",temperatures.ndim)
print("Temperature size:",temperatures.size)
print("Temperature dtype:",temperatures.dtype)

'''
NumPy aggregrate functions 
like we have temperatures = np.array([32.5,31.2,33.1,30.8,34.2])
We can calculate:
Mean->print(np.mean(temperatures))
Minimum->print(np.min(temperatures))
Maximum->print(np.max(temperatures))
Sum->print(np.sum(temperatures))

Now Standard deviation->Important for data science
it provides -> np.std(deviation)
for example-> std = temperatures.std()
              print(f"Temperature standard deviation:{std:.2f}")
So,Conceptually standard deviation tells us how spread out the values are around thier mean.
If temperatures are: 32,32.1,32.2,32.3->These are tightly clustered.
If they are : 20 , 28 , 35 , 42 -> they are much more spread out.
Important -> data analysis,anomaly detection,feature scaling,machine learning.

Now we have NumPy indexing -> temperatures = np.array([32.5,31.2,33.1,30.8,34.2])
now print(temperatures[0]) -> gives 32.5
and print(temperatures[1]) -> gives 31.2
Also it supports negative indexing.
And supports Slicing same [start : stop]
Here we have the most important Boolean Filtering
Returns the output as [True  True  False False]
So we basically use the condition to filter data.
------------------------------------------------
Now we can have the 2D NumPy arrays as till now i have used the 1D arrays only.
'''
pm25 = np.array([82,91,105,76,42])
print(pm25>80)
#Representing the 2D NumPy array 
environment = np.array([
    [32.5,31.4,65],
    [31.8,30.9,46],
    [43.8,37.1,29],
    [87.6,40.1,97],
    [94.3,89.2,64]
])
print(environment)
#Now understanding the shape : 
print(environment.shape)
#Which generates in the form of as shape=(rows,columns)
'''
We have 2D indexing , to access the matrix element
To access the first row- > print(environment[0])
To access the first row and column ->print(environment[0,0])
To get the entire row of the first column so we will do as 
temperatures = environment[:,0] here : means all rows.
and it means get me every row from column zero.
----------------
Another thing is the axis which by using returns the 
average of the column as:
print(environment.mean(axis=0))
Here axis=0 means produce operation down the rows,
producing one result for each column.So all the columns 
average will be return here.
'''
