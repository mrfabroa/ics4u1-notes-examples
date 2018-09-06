# Python Warm Up

### Instructions
Complete the required number of problems for each section.  All solutions must be written as a function with proper parameter inputs and return values as indicated in each problem.

All solutions are to be completed in your **"Python Warm-Up"** project in **repl.it**


##SECTION 1
Complete **4** problems from this section.


### 1.1 madlib()
Write a function `madlib()` that prompts the user for a noun, verb (past tense), adjective, and noun and prints out a sentence using these values. 

##### Example Run:
```
Enter a noun: dog
Enter a verb (past tense): ate
Enter an adjective: blue
Enter a noun: lobster

The dog ate the blue lobster.
```

### 1.2 howfar()
Write a function `howfar()` that prompts the user for vehicle fuel efficiency(km/L) and an amount in litres and then outputs the range (how far they can drive with that amount of gas).  Round your answer to a whole number.

#### Example Run:
```
Enter the fuel efficiency of your vehicle(L/100km): 4.4
Enter the amount of fuel in your vehicle(L): 60
Your range is 1364km.
```

### 1.3 otherSide(a,b,c)
Write a `otherSide(a,b)` where parameters `a` and `b` represent the length of two sides of a triangle and `c` represents the contained angle. Use the cosine law to calculate the length of the  third side.  Hint: use the Math library.


### 1.4 wordCount()
Write a function `wordCount()` that prompts the user for a sentence and outputs the number of words in the sentence.  Hint: use .split()

### 1.5 round3(n)
Write a function `round3(n)` that returns the value n rounded to 3 decimal places.

### 1.6 miles2km(miles)
Write a function `miles2km(miles)` that returns the miles parameter in kilometers. Round your answer to 2 decimal places.

##### Example:
`miles2km(500)` would return `804.67`


### 1.7 diceRolls()
Write a function `diceRolls()` that simulates the rolling of a pair of die by randomly generating two numbers between 1 and 6.  Use the string formatting `.format()`
to output the results of 5 rolls in a formatted table like the one below.  Hint: you will need to import and use the `random()` function from the `random` library

```
Roll      Die 1     Die 2
-------------------------
1           3           5
2           2           6
3           1           4
4           4           3
5           3           5
```


