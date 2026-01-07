# Reference_ Vena Calcs - 4 - Operators – Vena Solutions

## Page 1

Reference: Vena Calcs - 4 - Operators
About this series
This series is about  how t o wr ite and use V ena Calculation Scr ipts. You are on  Part 4, which
provides a description of various Calc Scripts operators.
Vena Calculations Scripts (or V ena Calcs) is a scripting language designed for V ena data models.
Vena Calcs provides a powerful and flexible way to run calculations and simulations for business
rules at the database level for all dimensions and members.
You can apply calcs for a variety of uses, including calculating financial ratios and percentages,
departmental/employee allocations or FX currency conversions.
We've broken down V ena Calcs into nine articles. They can be read consecutively or browsed as
needed.
 
Part 1: Managing Scripts  
Part 2: Notation and S yntax
Part 3: Data T ypes
Part 4: Operators -  You ar e her e
Part 5: Functions
Part 6: Conditional S tatements
Part 7: Currency Conversions
Part 8: Examples
Part 9: Troubleshooting
 
Vena Support T eam
Updated  1 year ago29/12/2025, 08:12 Reference: Vena Calcs - 4 - Operators – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027593692-Reference-Vena-Calcs-4-Operators 1/4

## Page 2

Table of contents
Operators
Arithmetic Operators
Comparison Operators
Member Comparison Operators
Logical Operators
 
Operat ors
Below is the list of operators available in V ena Calcs.
 
Arithmetic Operat ors
Operators used for creating arithmetic expressions.
Operat or Example Descr iption
+ [Sales] + 2 Addition
- [Sales] - 2 Subtraction
* [Sales] * 2 Multiplication
/ [Sales] / 2 Division (note: evaluates to 0 when the
denominator is 0)
^ [Sales] ^ 2 Exponentiation
 
Comp arison Operat ors
Operators used for comparing two numeric operands. Operands can be an intersection value or a
hardcoded number.29/12/2025, 08:12 Reference: Vena Calcs - 4 - Operators – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027593692-Reference-Vena-Calcs-4-Operators 2/4

## Page 3

Operat or Example Descr iption
>  [Sales] > [Budget] Greater than
<  [Sales] < 2 Less than
>= 2 >= [Sales] Greater than or equal
<= [Sales] <= 2 Less than or equal
== [Sales] == 2 Exactly equal
!= [Sales] != 0 Is not equal
 
Member Comp arison Operat ors
Operators used for comparing two text values. Operands can be an intersection value or a
hardcoded text.
Operat or Example Descr iption
>  'Dec' > 'Jan' Greater than
<  'Dec' < 'Jan' Less than
>= [Period._] >= &CurrentP eriod Greater than or equal
<= [Period._] <= &CurrentP eriod Less than or equal
== [Measure._] == 'Budget' Exactly equal
!= [Measure._] != 'Budget' Is not equal29/12/2025, 08:12 Reference: Vena Calcs - 4 - Operators – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027593692-Reference-Vena-Calcs-4-Operators 3/4

## Page 4

 
Logical Operat ors
Operators used to connect more than one Boolean statement.
Operat or Example Descr iption
&& ([Budget] > [Sales]) && ([Budget] < 5000) Logical AND
|| ([Budget] > [Sales]) || ([Budget] < 5000) Logical OR
| ([Budget] > [Sales]) | ([Budget] < 5000) Exclusive OR29/12/2025, 08:12 Reference: Vena Calcs - 4 - Operators – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027593692-Reference-Vena-Calcs-4-Operators 4/4
