# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n

      ## Run time is O(2^n) - this is because it multiplies by itself numerous times
```

```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1

  #Runtime is 0(n) because it is increases linar to what the input is

```

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
      # This is 0(1) as it no matter the input size, it will only ever return one thing, as it only accepts 0 anyways
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

STRATEGY:
n = 20
f = ?
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
