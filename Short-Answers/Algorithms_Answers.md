#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)

## Run time is O(n) - 0n^3 / 0^n2 == 0(n)

b)
#Runtime is 0(n^2) because it is running a while inside a for -- Also, you always want to look for the highest possible input, in this case it is n^2

c)

# This is 0(n) since it is using recursion and will continue to call depending on the input size, but the call will be repeated linear.

## Exercise II

STRATEGY:
n = 50
f = 20
e = 0
Start e at zero
Start n at the number of floors
Start f at the floor where eggs get broken
Loop through the length of n floors and increase e+1 through each iteration until e = f

```
def eggDropTest(n,f):
    e = 0
    for e in n:
      if e = f:
        return e
```
