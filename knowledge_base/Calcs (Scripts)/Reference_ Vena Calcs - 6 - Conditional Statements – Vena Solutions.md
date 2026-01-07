# Reference_ Vena Calcs - 6 - Conditional Statements – Vena Solutions

## Page 1

Reference: Vena Calcs - 6 -
Conditional Statements
About this series
This series is about  how t o wr ite and use V ena Calculation Scr ipts. You are on  Part 6, which
provides an overview of conditional statements.
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
Part 4: Operators
Part 5: Functions
Part 6: Conditional S tatements -  You ar e her e
Part 7: Currency Conversions
Part 8: Examples
Part 9: Troubleshooting
Vena Support T eam
Updated  1 year ago29/12/2025, 08:58 Reference: Vena Calcs - 6 - Conditional Statements – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027974231-Reference-Vena-Calcs-6-Conditional-Statements 1/3

## Page 2

 
 
 
Conditional Statements
A statement that starts with “ If” (If statements) s is the primary conditional statement.
 
An If statement:
Requires a boolean expression as its conditional test and may optionally be followed by one or
more  ElseIf  statements.
Is terminated by an  End statement.
Performs conditional tests within a formula. Using the IF statement, you can define a boolean
test, as well as formulas to be calculated if the test returns either a TRUE or F ALSE value.
 
An ELSEIF  statement:
Defines a conditional test and conditions that are performed if the preceding IF test generates a
value of F ALSE. For this reason, multiple ELSEIF commands are allowed following a single IF.
 
Example 1:
If ( [Measure.Sales] > 100 )
    // do something
ElseIf ( [Measure.Sales] > 10 )
    // do something else
Else
    // do some third thing
End
 
Example 2:
If (( [Measure.Sales] > 100 ) && ( [Measure.Sales] < 200 ))
    // do something29/12/2025, 08:58 Reference: Vena Calcs - 6 - Conditional Statements – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027974231-Reference-Vena-Calcs-6-Conditional-Statements 2/3

## Page 3

ElseIf (( [Measure.Sales] > 201 ) && ( [Measure.Sales] < 300 ))
    // do something else
Else
    // do some third thing
End
The parenthesis around boolean expressions for  If and  ElseIf  statements are always required.
 
Was this ar ticle help ful?
 
5 out of 12 found this helpful
Related articles
Reference: V ena Calcs - 8 - Examples
Reference: V ena Calcs - 5 - Functions
Reference: V ena Calcs - 7 - Currency Conversions
Reference: V ena Calcs - 2 - Notation and S yntax
Reference: V ena Calcs - 4 - Operators
Recently viewed articles
Reference: V ena Calcs - 5 - Functions
Reference: V ena Calcs - 4 - Operators
Reference: V ena Calcs - 3 - Data T ypes
Reference: V ena Calcs - 2 - Notation and S yntax
Reference: V ena Calcs - 1 - Managing Scripts29/12/2025, 08:58 Reference: Vena Calcs - 6 - Conditional Statements – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027974231-Reference-Vena-Calcs-6-Conditional-Statements 3/3
