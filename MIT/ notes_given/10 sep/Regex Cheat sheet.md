# Regex Cheat sheet  
  
Regular Expressions (Regex) are patterns used in Python for searching, matching, validating, and replacing text. This cheat sheet offers a quick reference to common regex patterns and symbols.  
Basic Characters  

| Expression | Explanations |
| ---------- | -------------------------------------------------------------------- |
| ^ | Matches the start of a string (or start of line in MULTILINE mode). |
| $ | Matches the end of a string (or end of line in MULTILINE mode). |
| . | Matches any character except newline. |
| a | Matches the character a. |
| xy | Matches the string xy |
| a\|b | Matches expression a or b. If a is matched first, b is left untried. |
  
  
  
  
  
  
  
  
   
  
  
```
import re
​
```
```


```
```
print(re.search(r"^x","xenon"))
print
```
```
(re.search(r"s$","geeks"))

```
  
  
Output  
```
<re.Match object; span=(0, 1), match='x'>
<re.Match object; span=(4, 5), match='s'>

```
Explanation:  
* ^x matches x at the start of the string  
* s$ matches s at the end of the string  
Quantifiers  
Quantifiers define how many times a pattern should occur  

| Expressions | Explanations |
| ----------- | -------------------------------------------------------------- |
| + | Matches 1 or more occurrences of the preceding expression. |
| * | Matches 0 or more occurrences. |
| ? | Matches 0 or 1 occurrence. |
| {p} | Matches the expression to its left p times, and not less. |
| {p, q} | Matches the expression to its left p to q times, and not less. |
| {p, } | Matches the expression to its left p or more times. |
| {0, q} | Matches the expression to its left up to q times |
  
  
  
  
  
  
  
  
   
  
  
```
import re
​
print
```
```
(re.search(r"9+","289908"))

```
```
print
```
```
(re.search(r"\d{3}","hello1234"))

```
  
  
Output  
```
<re.Match object; span=(2, 4), match='99'>
<re.Match object; span=(5, 8), match='123'>

```
Explanation:  
* 9+ matches consecutive 9s -> 99  
* \d{3} matches exactly three digits -> 123  
Character Classes  
Character Classes define a set of characters to match any single character from that set in a string.  

| Expressions | Explanations |
| ----------- | ----------------------------------------------------------------------------------------------------------- |
| \\w | Matches alphanumeric characters, that is a-z, A-Z, 0-9, and underscore(_) |
| \\W | Matches non-alphanumeric characters, that is except a-z, A-Z, 0-9 and _ |
| \\d | Matches digits, from 0-9. |
| \\D | Matches any non-digits. |
| \\s | Matches whitespace characters, which also include the \\t, \\n, \\r, and space characters. |
| \\S | Matches non-whitespace characters. |
| \\A | Matches the expression to its right at the absolute start of a string whether in single or multi-line mode. |
| \\Z | Matches the expression to its left at the absolute end of a string whether in single or multi-line mode. |
| \\n | Matches a newline character |
| \\t | Matches tab character |
| \\b | Matches the word boundary (or empty string) at the start and end of a word. |
| \\B | Matches where \\b does not, that is, non-word boundary |
  
  
  
  
  
  
  
  
   
  
  
```
import re
​
print
```
```
(re.search(r"\s","xenon is a gas"))

```
```
print
```
```
(re.search(r"\D+\d*","123geeks123"))

```
  
  
Output  
```
<re.Match object; span=(5, 6), match=' '>
<re.Match object; span=(3, 11), match='geeks123'>

```
Explanation:  
* \s matches the first space  
* \D+\d* matches non-digits followed by digits -> geeks123  
Sets  
Sets match one character from a group.  

| Expressions | Explanations |
| ----------- | ------------------------------------------------------------------------------------------------ |
| [abc] | Matches either a, b, or c. It does not match abc. |
| [a-z] | Matches any alphabet from a to z. |
| [A-Z] | Matches any alphabets in capital from A to Z |
| [a\\-p] | Matches a, -, or p. It matches - because \\ escapes it. |
| [-z] | Matches - or z |
| [a-z0-9] | Matches characters from a to z or from 0 to 9. |
| [(+*)] | Special characters become literal inside a set, so this matches (, +, *, or ) |
| [^ab5] | Adding ^ excludes any character in the set. Here, it matches characters that are not a, b, or 5. |
| \\[a\\] | Matches [a] because both square brackets [ ] are escaped |
  
  
  
  
  
  
  
  
   
  
  
```
import re
​
print
```
```
(re.search(r"[^abc]","abcde"))

```
```
print
```
```
(re.search(r"[a-p]","xenon"))

```
  
  
Output  
```
<re.Match object; span=(3, 4), match='d'>
<re.Match object; span=(1, 2), match='e'>

```
Explanation:  
* [^abc] matches d  
* [a-p] matches e  
Groups  
Groups allow you to capture parts of a match.  

| Expressions | Explanations |
| ----------------- | -------------------------------------------------------------------------------------------- |
| ( ) | Matches the expression inside the parentheses and groups it which we can capture as required |
| (?#...) | Read a comment |
| (?P<name>pattern) | Matches the expression AB, which can be retrieved with the group name. |
| (?:A) | Matches the expression as represented by A, but cannot be retrieved afterwards |
| (?P=group) | Matches the expression matched by an earlier group named “group” |
  
  
  
  
  
  
  
  
   
  
  
```
import re
​
```
```


```
```
example = (re.search(r"(?:AB)","ACABC"))
print
```
```
(example)

```
```
print(example.groups())
​
result = re.search(
```
```
r"(\w*), (\w*)","geeks, best")

```
```
print(result.groups())

```
  
  
Output  
```
<re.Match object; span=(2, 4), match='AB'>
()
('geeks', 'best')

```
Explanation:  
* re.search(r"(?:AB)", "ACABC"): Finds AB using a non-capturing group, so nothing is stored.  
* example.groups(): Returns () because non-capturing groups don’t save matches.  
* re.search(r"(\w*), (\w*)", "geeks, best"): Uses capturing groups to extract words before and after the comma.  
* result.groups(): Returns ('geeks', 'best').  
Assertions  
Assertions are regex patterns that match a position in a string without consuming any characters.  

| Expression | Explanation |
| ---------- | -------------------------------------------------------------------------------------------------------- |
| A(?=B) | This matches the expression A only if it is followed by B. (Positive look ahead assertion) |
| A(?!B) | This matches the expression A only if it is not followed by B. (Negative look ahead assertion) |
| (?<=B)A | This matches the expression A only if B is immediate to its left.  (Positive look behind assertion) |
| (?<!B)A | This matches the expression A only if B is not immediately to its left. (Negative look behind assertion) |
| (?()\|) | If else conditional |
  
  
  
  
  
  
  
  
   
  
  
```
import re
​
```
```


```
```
print(re.search(r"z(?=a)", "pizza"))
print(re.search(r"z(?!a)", "pizza"))

```
  
Output:  
```
<re.Match object; span=(3, 4), match='z'>
<re.Match object; span=(2, 3), match='z'>

```
Explanation:  
* re.search(r"z(?=a)", "pizza"): Positive lookahead; matches z only if followed by a.  
* re.search(r"z(?!a)", "pizza"): Negative lookahead; matches z only if not followed by a.  
Flags  
Flags modify regex behavior, such as ignoring case or allowing multiline matching.  

| Expression | Explanation                                          |
| ---------- | ---------------------------------------------------- |
| a          | Matches ASCII only                                   |
| i          | Ignore case                                          |
| L          | Locale character classes                             |
| m          | ^ and $ match start and end of the line (Multi-line) |
| s          | Matches everything including newline as well         |
| u          | Matches Unicode character classes                    |
| x          | Allow spaces and comments (Verbose)                  |
  
  
  
  
  
  
  
  
   
  
  
```
import re
​
exp = 
```
```
"""hello there

```
```
I am from
Geeks for Geeks"""
```
```


```
```
​
print(re.search(r"and", "Sun And Moon", flags=re.IGNORECASE))
print
```
```
(re.findall(r"^\w", exp, flags = re.MULTILINE))

```
  
  
Output  
```
<re.Match object; span=(4, 7), match='And'>
['h', 'I', 'G']

```
Explanation:  
* re.search(r"and", "Sun And Moon", flags=re.IGNORECASE): IGNORECASE matches "and" ignoring case.  
* re.findall(r"^\w", exp, flags=re.MULTILINE): MULTILINE matches start of each line; returns ['h', 'I', 'G'].  
