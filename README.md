# COSC310HW2
Blank Repository for COSC 310 Homework

You should add the following to this repository. 
* Array.py
  - This file should contain a working array class with the following methods:
      * __init__(self, size)
      * __len__(self)
      * get(self,n)
      * set(self,n, value)
      * swap(self, i,k)
      * insert(self,item)        
      * find(self, item)
      * search(self,item)               
      * delete(self,item)                
      * traverse(self,function = print)
      * __str__(self) 
      * bubbleSort(self)
      * selectionSort(self)
      * insertionSort(self)
   
* Homework2.ipynb
  - Use markdown to neatly describe what each portion of this document is doing. 
  - This file should contain a timing test of the three sort algorithms: bubbleSort(), selectionSort(), and insertionSort().
    * You should import your Array.py module so that you have access to the above stated methods for a simple array.
    * Write a function that creates a random array of a specified size. 
    * You should then use the random module, and the matplotlib.pyplot module in conjunction with the timeit module to create a plot for the time it takes to sort random arrays of sizes 10 to 10000.
    * You should include this plot nicely in the .ipynb file with proper labels on all the axis.

## Note this repository includes a main.py file for testing. 


