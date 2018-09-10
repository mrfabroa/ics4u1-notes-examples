# Python Warm Up

### Instructions
Complete the required number of problems for each section.  All solutions must be written as a function with proper parameter inputs and return values as indicated in each problem.

All solutions are to be completed in your **"Python Warm-Up"** project in **repl.it**


## SECTION 1 - Simple Programs

Complete **5** problems from this section.

#### Notes
* [1.3 Printing and Comments](https://docs.google.com/document/d/1sjBpR6uY6Ql_1WsHPlO7bNg9fcVrcBwgXCBbapNlLqk/edit?usp=sharing)
* [1.4 Variables and Assignments](https://docs.google.com/document/d/1shqagy8wsR92B273K0uhtGXtroicG-1ZBqHFqb7z8Xc/edit?usp=sharing)
* [1.5 Data Conversions and User Input](https://docs.google.com/document/d/1cM1GOW8rl7YLr1NSzpxw7vUxxz1TGcq6VqdZXK6DhAU/edit?usp=sharing)
* [1.7 Built-In Functions and Libraries](https://docs.google.com/document/d/1N37lqdZqxQ8_0BLbhmZij2o82PZ2pM7lA9vnlsB_uFs/edit?usp=sharing)
* [String Formatting](https://docs.google.com/document/d/1uME8sZ-GXVJZgvQYHIAIeTO0QPHEV5KiGm68FinDyYE/edit?usp=sharing)
* [Processing Strings](https://docs.google.com/document/d/1w3or5c0l7iF9AstbHE2gwshSiLrwnBH4o6XOmw84NjI/edit?usp=sharing)

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
  
  
## SECTION 2 - Repetition
Complete **5** problems from this section.

#### Notes
* [1.7 Built-In Functions and Libraries](https://docs.google.com/document/d/1N37lqdZqxQ8_0BLbhmZij2o82PZ2pM7lA9vnlsB_uFs/edit?usp=sharing)
* [Processing Strings](https://docs.google.com/document/d/1w3or5c0l7iF9AstbHE2gwshSiLrwnBH4o6XOmw84NjI/edit?usp=sharing)
* [2.1 Boolean Values and Expressions](https://docs.google.com/document/d/1JEM_Xokqqrf3PmunijHi_e5aMqXRboDOM8DbuOE4gkk/edit?usp=sharing)
* [2.2 If Statements](https://docs.google.com/document/d/1vDTfwkYf7QKFeGoljO2YzlThSTbMxE-Ud9kl4OX6rX4/edit?usp=sharing)
* [2.3 Logical Operators](https://docs.google.com/document/d/1Jq6AX44c8bIE0C6ySmAkMzTi_PbOxrMlafpHEWhdqEM/edit?usp=sharing)
* [2.5 For Loops](https://docs.google.com/document/d/15_f7xW41qNPyQEA7C3sI67g1i7NNbaZejS1G2N5hxgI/edit?usp=sharing)
* [2.6 Conditional Loops](https://docs.google.com/document/d/1u9JC0TzQvlmGD3HAnxRl82LcBuEVn5NzPjJ1HqdUmKQ/edit?usp=sharing)

### 2.1 string_times(str, num)
Write a function string_times(str, num) where given a string `str`, return a larger string that is `num` copies of the original string. 

##### Example:

`string_times('Hi', 2)` returns `'HiHi'`  
`string_times('Hi', 3)` returns `'HiHiHi'`  
`string_times('Hi', 1)` returns `'Hi'`


### 2.2 sortaPi(n)
Write a function `sortaPi(n)` that approximates the value of  by summing the terms of this series:  4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 … where `n` represents the number of terms to sum, and then return the sum of the first `n` terms of this series. You can subtract the approximation from the value of math.pi to see how accurate it is. 

### 2.3 wordPlay(word)
Write a function `wordplay(word)` program that outputs the parameter string `word` prints it out in various ways like in the example below.

##### Example
`wordPlay("Canada")` would output:  
```
Canada    Canada      Canada    C-a-n-a-d-a
Canad      anada      anada      C-a-n-a-d
Cana        nada      nada        C-a-n-a
Can          ada      ada          C-a-n
Ca            da      da            C-a
C              a      a              C
```


### 2.4 sumChart(n)
Write a function sumChart(n) that simulates the rolling of a pair of die by randomly generating two numbers between 1 and 6 and then calculates the sum of each roll.  Use string formatting to output the results of `n` rolls in a formatted table like the one below:   
```
Roll		Die 1		Die 2		Sum
---------------------------------------
1		    3		    5         8
2		    2		    6         8
3		    1		    4         5
4		    4		    3         7
5		    3		    5         8
```

### 2.5 strExplosion(word)
Write a function `strExplosion(word)`, given a non-empty string `word` like "Code",  return a string like `"CCoCodCode"`.

##### Examples:
`strExplosion('Code')` returns `'CCoCodCode'`  
`strExplosion('abc')` returns `'aababc'`  
`strExplosion('ab')` returns `'aab'` 

### 2.6 ratRace(r1, r2) 
Write a function `ratRace(rw, rt)` where parameters rw1 is the weight of a rat at the beginning of an experiment. The parameter rt is the rate that the rat's weight is expected to increase each week (for example, 4 percent per week). Return how many weeks it would take for the weight of the rat to become 25 percent heavier than it was originally.

### 2.7 tripleCount(s)
A "triple" in a string parameter `s` is a character appearing three times in a row. Write a function `tripleCount(s)` that returns the number of triples in the given string `s`. 

##### Examples
`tripleCount("abcXXXabc")` return `1`  
`tripleCount("xxxabyyyycd")` → `3`  
`tripleCount("a")` returns `0`


## Section 3 - Selection & Repetition
Complete **5** problems from this section.

##### Notes:
* [2.1 Boolean Values and Expressions](https://docs.google.com/document/d/1JEM_Xokqqrf3PmunijHi_e5aMqXRboDOM8DbuOE4gkk/edit?usp=sharing)
* [2.2 If Statements](https://docs.google.com/document/d/1vDTfwkYf7QKFeGoljO2YzlThSTbMxE-Ud9kl4OX6rX4/edit?usp=sharing)
* [2.3 Logical Operators](https://docs.google.com/document/d/1Jq6AX44c8bIE0C6ySmAkMzTi_PbOxrMlafpHEWhdqEM/edit?usp=sharing)
* [2.5 For Loops](https://docs.google.com/document/d/15_f7xW41qNPyQEA7C3sI67g1i7NNbaZejS1G2N5hxgI/edit?usp=sharing)
* [2.6 Conditional Loops](https://docs.google.com/document/d/1u9JC0TzQvlmGD3HAnxRl82LcBuEVn5NzPjJ1HqdUmKQ/edit?usp=sharing)


### 3.1 babysitter_pay(startHour, startMin, endHour, endMin)
A babysitter charges $2.50 an hour until 9:00 PM when the rate drops to $1.75 an hour (the children are in bed). Write a function `babysitter_pay(startHour, startMin, endHour, endMin)` that takes parameters starting time and ending time in hours and minutes and calculates the total babysitting bill. You may assume that the starting and ending times are in a single 24 hour period. Partial hours should be appropriately prorated. 


