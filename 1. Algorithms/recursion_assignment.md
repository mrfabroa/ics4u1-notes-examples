# Recursion Problems

### subCount(fullString, sub)
Given a string `fullString` and a non-empty substring `sub`, compute recursively the 
number of times that sub appears in the string, without the `sub` strings overlapping.


```markdown
subCount("aaabbbaaa", "aaa") → 2
subCount("aabbbaaa", "bbb") → 1
subCount("aabbbaaa", "ccc") → 0

```

### noDupes(sString)
Given a string `sString`, return recursively a "cleaned" string where adjacent characters that are the same have been 
reduced to a single character. So "yyzzza" yields "yza".

```markdown
noDupes("yyzzza") → "yza"
noDupes("abbbcdd") → "abcd"
noDupes("Hello") → "Helo"
```

### eight_count(nInt)
eight_count() Given a non-negative int `nInt`, compute recursively (no loops) the count of the occurrences of 8 as a digit, 
except that an 8 with another 8 immediately to its left counts double, so 8818 yields 4. 
Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (//) by 10 removes the rightmost digit (126 / 10 is 12).

```markdown
eight_count(8) → 1
eight_count(818) → 2
eight_count(8818) → 4
```



### sub_sandwich(fullString, sub)
sub_sandwich() Given a string and a non-empty substring sub, compute recursively the largest substring which starts and 
ends with sub and return its length.

```markdown
  sub_sandwich("catcowcat", "cat") → 9
  sub_sandwich("catcowcat", "cow") → 3
  sub_sandwich("cccatcowcatxx", "cat") → 9
```




