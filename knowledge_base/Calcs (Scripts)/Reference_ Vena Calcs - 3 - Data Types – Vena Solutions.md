# Reference_ Vena Calcs - 3 - Data Types – Vena Solutions

## Page 1

Reference: Vena Calcs - 3 - Data Types
 
About this series
This series is about  how t o wr ite and use V ena Calculation Scr ipts. You are on  Part 3, which
provides a description of various Calc Scripts data types.
Vena Calculations Scripts (or V ena Calcs) is a scripting language designed for V ena data models.
Vena Calcs provides a powerful and flexible way to run calculations and simulations for business
rules at the database level for all dimensions and members.
You can apply calcs for a variety of uses, including calculating financial ratios and percentages,
departmental/employee allocations or FX currency conversions.
We've broken down V ena Calcs into nine articles. They can be read consecutively or browsed as
needed.
 
Part 1: Managing Scripts 
Part 2: Notation and S yntax
Part 3: Data T ypes -  You ar e her e
Part 4: Operators
Part 5: Functions
Part 6: Conditional S tatements
Part 7: Currency Conversions
Part 8: Examples
Part 9:Troubleshooting
Vena Support T eam
Updated  6 months ago29/12/2025, 08:12 Reference: Vena Calcs - 3 - Data Types – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027593532-Reference-Vena-Calcs-3-Data-Types 1/4

## Page 2

 
 
Table of contents
Data T ypes
Dedicated T ype T able
 
Data T ypes
Various data types are used in V ena Calcs for intersection value assignment, function/expression
return values and conditional statements.
 
 Dedicat ed Type T able
Type Example Descr iption
Bool true, false Boolean value
Current
Member[Year._] A special notation of a member, returning
the current Member S tring for that
dimension
Glob al Variable &CurrentY ear, [&CurrentY ear] A variable returning the Member string or
Member in the corresponding metadata
variable
Member S tring '2010' A sequence of characters representing a
member name, wrapped in single quotes
Member [Sales], [Jan], [USD, Rate] A name of a data model member
Member Set {Sales, Jan, Feb, Mar,
[Rates].Leaves()}A set of members representing their cross
product29/12/2025, 08:12 Reference: Vena Calcs - 3 - Data Types – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027593532-Reference-Vena-Calcs-3-Data-Types 2/4

## Page 3

Type Example Descr iption
Number 1234 An arbitrary size number precise to 16
decimal places
String "abcd" A sequence of characters wrapped in
double quotes
Tuple (Sales, Jan, [USD, Rate]) An intersection of a sequence of members
Tuple Set [Sales].Y TD() A set of tuples returned from the cube
Was this ar ticle help ful?
 
2 out of 2 found this helpful
Related articles
Reference: V ena Calcs - 4 - Operators
Reference: V ena Calcs - 5 - Functions
Reference: V ena Calcs - 2 - Notation and S yntax
Reference: V ena Calcs - 1 - Managing Scripts
Reference: V ena Calcs - 8 - Examples
Recently viewed articles
Reference: V ena Calcs - 2 - Notation and S yntax
Reference: V ena Calcs - 1 - Managing Scripts
Reference: Sparse Calcs29/12/2025, 08:12 Reference: Vena Calcs - 3 - Data Types – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027593532-Reference-Vena-Calcs-3-Data-Types 3/4

## Page 4

How-T o: Using V ena’s Foreign Exchange (FX) Conversion Function
Explainer: T arget Member Attribute Calc T rigger29/12/2025, 08:12 Reference: Vena Calcs - 3 - Data Types – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027593532-Reference-Vena-Calcs-3-Data-Types 4/4
