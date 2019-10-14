#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)

## Run time is O(n) - 0n^3 / 0^n2 == 0(n)

b)
# Runtime is 0(n^2) because it is running a while inside a for -- Also, you always want to look for the highest possible input, in this case it is n^2

c) # Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.


# This is 0(n) since it is using recursion and will continue to call depending on the input size, but the call will be repeated linear.

## Exercise II

STRATEGY:
n = 50
f = 0
e = 0
Start e at zero
Start n at the number of floors
Start f at the floor where eggs get broken
Loop through the length of n floors and increase e+1 through each iteration until e = f

def binary_search(n, floor):
   
  ## set the start to the beginning and the end to the number of floors
    start = 0
    end = len(n) -1 

  ## while the start is not the end (list is longer than one)
    while start <= end:
  ## Cut our list in half, examine the midpoint item
  ## length of array // 2   <-- set as the midpoint
        mid = start + (end - 1) // 2 

  ## set "egg" as the midpoint to be dropped from
        egg = n[mid]

  ## If the egg is == floor, it breaks on this floor:
        if egg == floor:
            return n.index(item)

  ## Otherwise, if egg is greater than floor value
  # Repeat binary search on first half of the list
        elif egg > floor:

            end = mid - 1
    
   # Otherwise repeat binary search on second half of list
        elif egg < floor:
            start = mid + 1

   # return -1 (false value) if egg does not break on any of the floors
    return -1



```
def eggDropTest(n,f):
    e = 0
    for e in n:
      if e = f:
        return e
```
