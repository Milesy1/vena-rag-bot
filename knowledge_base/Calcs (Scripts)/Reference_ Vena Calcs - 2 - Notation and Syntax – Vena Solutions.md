# Reference_ Vena Calcs - 2 - Notation and Syntax – Vena Solutions

## Page 1

Reference: Vena Calcs - 2 - Notation
and Syntax
About this series
This series is about  how t o wr ite and use V ena Calculation Scr ipts. You are on  Part 1, which
provides an overview of Calc Scripts and how to manage them.
Vena Calculations Scripts (or V ena Calcs) is a scripting language designed for V ena data models.
Vena Calcs provides a powerful and flexible way to run calculations and simulations for business
rules at the database level for all dimensions and members.
You can apply Calcs for a variety of uses, including:
Calculating financial ratios and percentages
Departmental/employee allocations
FX currency conversions
We've broken down V ena Calcs into nine articles. They can be read consecutively or browsed as
needed.
 
Part 1: Managing Scripts  
Part 2: Notation and S yntax - Y ou are here
Part 3: Data T ypes
Part 4: Operators
Part 5: Functions
Part 6: Conditional S tatements
Part 7: Currency Conversions
Part 8: Examples
Part 9: Troubleshooting
Vena Support T eam
Updated  6 months ago29/12/2025, 08:12 Reference: Vena Calcs - 2 - Notation and Syntax – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027591072-Reference-Vena-Calcs-2-Notation-and-Syntax 1/18

## Page 2

 
 Table of contents
Basic Notation and S yntax
Scope S tatements
Member Names and Tuples
Dot Notation for Identifying Dimensions
Variables
Value Assignment
Advanced Notation and S yntax
Process V ariables
Cycles
Sparse Calcs
Allocation Calcs
Read Calcs
Best Practices
 
Basic Notation and Syntax 
Vena Calcs identifies a slice of the data model (or a set of intersections) and assigns values to each
intersection within that slice. The values can be a result of an arithmetic equation, function or
expression, or the value of another intersection.
At a bare minimum, a calc is composed of a single Scope statement and a single computation
within that Scope.29/12/2025, 08:12 Reference: Vena Calcs - 2 - Notation and Syntax – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027591072-Reference-Vena-Calcs-2-Notation-and-Syntax 2/18

## Page 3

A) Scope S tatements  
B) Member Names and Tuples  
C) Dot Notation  
D) Variables  
E) Value Assignment  
A) Scope Statements
All calculations start with a Scope statement, which defines the slice of the data model that the
enclosing calculation applies to using a “Set”:
Scope 
{ 
[Department.All Departments] .Leaves(), 
[Year. All Year] .Leaves(), 
[Period.Full Year] .Leaves(), 
[Placeholder 1. Not Placeholder 1 Specific], 
[Placeholder 2. Not Placeholder 2 Specific], 
[Placeholder 3. Not Placeholder 3 Specific], 
[Placeholder 4. Not Placeholder 4 Specific], 
[Scenario.Actual],[Scenario.Forecast],[Scenario.Budget], 
[Currency.All Reporting Currencies] .Leaves(), 
} 
     // body of calculation 
End 
 29/12/2025, 08:12 Reference: Vena Calcs - 2 - Notation and Syntax – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027591072-Reference-Vena-Calcs-2-Notation-and-Syntax 3/18

## Page 4

Scope S tatement Not es & Limitations
Two for ward slash charact ers (//) signif y a comment.  Nothing on the line following these
slashes is evaluated. 
Scope stat ements may be nest ed inside each other . A nested Scope inherits the context and
unspecified dimension members from its parent Scope. 
Scope {[Divisions.Division A], [Year.2025], [Measure.Sales]} 
   Scope {[Department.Dept 101]} 
       // body
   End 
End 
 
In the above example, the innermost Scope statement is bound to the slice {[Divisions.Division
A], [Department.Dept 101], [Y ear.2015], [Measure.Sales]}.
Scope stat ements may r eference each other .  
Scope {[Year.2025]} 
     Scope {[Period.Feb]} 
          @this = [Period.Jan] 
     End 
     Scope {[Period.Mar]} 
          @this = [Period.Feb] * 2 
     End 
End  
It is possible for an inner Scope to “exit” the boundaries of the outer Scope. This can be
accomplished by defining a different member in the inner Scope statement which would replace
an initially inherited member from the outer Scope. 
Scope {[Measure.Sales], [Year.2025]} 
     Scope {[Measure.Sales], [Year.2024]} 
          // body
     End
End
Scopes may NO T create a cy cle. The following example will not compile:29/12/2025, 08:12 Reference: Vena Calcs - 2 - Notation and Syntax – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027591072-Reference-Vena-Calcs-2-Notation-and-Syntax 4/18

## Page 5

Scope {[Year.2025]} 
     Scope {[Period.Jan]} 
          @this = [Period.Feb] * 500 
     End 
     Scope {[Period.Feb]} 
          @this = [Period.Jan] * 2 // WON'T WORK
     End 
End
Two calcs or scopes may NO T be wr itten to the same section o f the cube.  In the following
example, the first calc writes to the intersections at [Y ear.2015] and the second calc also
attempts to write to the intersections at [Y ear.2015]. In this scenario, you will be unable to save
the second calc.  
Scope {[Year.2025]} 
     @this = [Account.No_Account] * 1.5 
End 
Scope {[Year.2025]} 
     @this = [Account.No_Account] / 3 // WON'T WORK 
End 
 
B) Members and Tuples
Member s
In Vena Calcs, member names:
May only start with a letter, number or asterisk (*).
May only contain letters, numbers, spaces or any of the following special characters: @ \ , - = <
> . + ' _ | *
 
Tuples
A tuple (in this context) is an ordered collection of members that defines specific intersections
within a data model.
Inside a tuple, square brackets [ ] are optional if the member name does not contain special
characters. Anything that is not a space, letter or number is considered a special character.
For example, if we have the members  Sales  and 2025,  and we want to put them in a tuple, the
following expressions are valid:
([Measure.Sales], [Year.2025]) 
([Sales], [2025]) 29/12/2025, 08:12 Reference: Vena Calcs - 2 - Notation and Syntax – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027591072-Reference-Vena-Calcs-2-Notation-and-Syntax 5/18

## Page 6

(Sales, 2025) 
 
However, if we have a member  Sales, Pr oduct_A  (i.e., the member name contains a comma), it must
be enclosed in square brackets to ensure it’s not read as two separate members:
Correct: ([Sales, Product_A], 2025) 
 
C) Dot Notation for Identifying Dimensions
If a member name is used in more than one dimension, you must identify your target dimension in
the calc. The syntax is [Dimension.Member].
For example: 
[Year.2025] 
[Scenario.Actual]
To reference a member in both dimensions:
([Products.Product_A], [Departments.Product_A])
Important notes to remember:
Member names are not case sensitive, meaning [product_A] in one dimension is equal to
[Product_A] in another. 
Vena Calc commands ARE case sensitive.  
D) Variables
Create variables with the @ character before a word. V ariables can be assigned a number, an
intersection point value or a member set.
@CostOfLiving = 1.05 
@Accounts = [Accounts.All Accounts].Leaves()
Variable names are case sensitive; @Accounts and @accounts are two different variables.
 
E) Value Assignment 
The special variable @this is used to assign values to the intersections specified by the Scope
statement. It represents the current intersection being processed within the defined Scope.29/12/2025, 08:12 Reference: Vena Calcs - 2 - Notation and Syntax – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027591072-Reference-Vena-Calcs-2-Notation-and-Syntax 6/18

## Page 7

This variable is case sensitive. For example,  @This  would be considered a new and different variable
to @this .
Scope {[Measure.Sales]}
@this = [Measure.Quantity] * [Measure.Price] 
End
This calc finds the value in the member Quantity from the dimension Measure and multiplies it to
the value in the member Price (also in the dimension Measure). It stores the result in the member
Sales, also in the dimension Measure. 
 
Advanced Notations and Syntax Rules of
Vena Calcs
 
Process Variables
Vena Calcs can access metadata variables that are global to any process linked to the data model.
These variables are denoted with an ampersand (&) in front of the metadata variable name. For
example,
Scope { &CurrentYear, [Accounts.01] } 
@this = (&PreviousYear) + 1 
End 
This calc examines all processes linked to the model to identify the metadata variables named
CurrentY ear and PreviousY ear. It retrieves the value of Account01 at the member defined by
PreviousY ear, adds 1 to this value, and stores the result in Account01 at the member defined by
CurrentY ear.
 
Caution
When a model is linked to multiple processes with variables sharing the same name, a
calc cannot determine which process to read from. For instance, if a data model is
connected to "Budgeting" and "Forecasting," and both processes contain a metadata
variable called CurrentY ear—set to Y2015 in Budgeting and Y2016 in Forecasting—the
calc won't know whether to use Y2015 or Y2016 until execution. 29/12/2025, 08:12 Reference: Vena Calcs - 2 - Notation and Syntax – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027591072-Reference-Vena-Calcs-2-Notation-and-Syntax 7/18

## Page 8

 
Cycles
Multiple separate calculation files may not reference each other to create a cycle. For example, only
one of the following two calculations will compile:
// Calculation for Jan
     Scope {[Period.Jan], [Year.2015]} 
          @this = [Period.Feb] + 2 
     End 
// Calculation for Feb 
     Scope {[Period.Feb], [Year.2015]} 
          @this = [Period.Jan] + 2 
     End 
 
In addition, a single calculation may not target a slice that it uses as a source (i.e., create a cycle
with itself). For example, the following is not allowed:
Scope {[Period.Jan], [Year.2015]} 
@this = [Period.Jan] + 1 
End 
 
Sparse Calcs
Add “.sparse”  to the end of the calc name to run in sparse mode. 
Running a calc in sparse mode modifies its behavior for source intersections (inputs) that have a
one-to-many relationship with the target intersections. In sparse mode, the calc triggers only if the
target intersections already contain values.
 The only solution is to avoid reusing metadata names across processes. A better
approach is naming variables uniquely, such as CurrentY ear_Budgeting and
CurrentY ear_Forecasting, to clearly specify the intended variable in calculations.
Note
Sparse mode is only activated via Data Save and ETL Saves.29/12/2025, 08:12 Reference: Vena Calcs - 2 - Notation and Syntax – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027591072-Reference-Vena-Calcs-2-Notation-and-Syntax 8/18

## Page 9

Sparse mode does not affect the triggering behavior for source intersections with one-to-one or
many-to-one relationships. Changes to these intersections trigger the calc as usual, regardless of
sparse mode.
 
Cardinality
One-t o-one
In a one-to-one relationship, a change in the source affects only one point in the target
slice.  Consider the following currency conversion example:
Scope {[Accounts.All Accounts].Leaves(), [Currency.USD]} 
     @this = [Currency.Local] * ([Accounts.No_Account], [Measure.Rate]) 
End 
This calculation iterates through all [Accounts] leaves multiplying the local value for each account
by the rate at ([No_Account], [Rate]). For instance, a change at ([Account 1], [Local]) impacts only
([Account 1], [USD]) due to their one-to-one relationship.
 
One-t o-many
In this example, the value at ([No_Account], [Rate]) has a one-to-many relationship, meaning
changes to it affect all leaf accounts under USD.
 
Sparse Ex ecution
In sparse mode, a change to ([No_Account], [Rate]) recalculates only existing values in the slice
([Accounts].Leaves(), [USD]). For example, consider the following data before the calculation:
  Local USD
Account 1 100  
Account 2 150  
Account 3 120  
Account 4    
Account 5    29/12/2025, 08:12 Reference: Vena Calcs - 2 - Notation and Syntax – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027591072-Reference-Vena-Calcs-2-Notation-and-Syntax 9/18

## Page 10

 
  USD
No_Account 1.5
 
Then, after we write the calc and deploy, we see the following data:
  Local USD
Account 1 100 150
Account 2 150 225
Account 3 120 180
Account 4    
Account 5    
 
We then disable the calc and save some more data on the sheet.
  Local USD
Account 1 100 150
Account 2 150 225
Account 3 120 180
Account 4 100  
Account 5 200  
 
Finally, we re-enable the calc and change the rate. W e see the following data:
  USD
No_Account 2.029/12/2025, 08:12 Reference: Vena Calcs - 2 - Notation and Syntax – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027591072-Reference-Vena-Calcs-2-Notation-and-Syntax 10/18

## Page 11

 
  Local USD
Account 1 100 200
Account 2 150 300
Account 3 120 240
Account 4 100  
Account 5 200  
 
Notice that the values at ([Account 4], [USD]) and ([Account 5], [USD]) have not been
calculated.  When calculating updates for the USD column, V ena only processes existing data due to
the one-to-many relationship of the rate source. T o resolve missing values for Accounts 4 and 5 in
USD, ensure the calculation remains enabled when adding new data to automatically generate
updated values:
Before rate change:
  Local USD
Account 1 100 150
Account 2 150 225
Account 3 120 180
Account 4 100 150
Account 5 200 300
 
After rate change:
  Local USD
Account 1 100 200
Account 2 150 30029/12/2025, 08:12 Reference: Vena Calcs - 2 - Notation and Syntax – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027591072-Reference-Vena-Calcs-2-Notation-and-Syntax 11/18

## Page 12

Account 3 120 240
Account 4 100 200
Account 5 200 400
Alternatively, if data was saved when the calculation was disabled, activating the calculation would
automatically identify new sources and compute targets.
 
 
Allocation Calcs
Add ".allocation" to the end of a calc name to enable allocation mode. In this mode, V ena Calcs
identifies the first source intersection in the calc text and uses its values in the V ena Cube as a
reference during execution. Allocation calcs are ideal for operations like multiplication, division,
foreign exchange, allocations, driver-based calculations and certain KPIs.
 
Allocation Ex ecution
Suppose we had the following calc in Allocation mode:
Scope {[Product.Electronics], [Measure.Sales]} 
@this = [Product.Laptops] + [Product.Tablets] + [Product.Cell Phones] 
End 
The calculation engine would select [Product.Laptops] as the Allocation Source, using its values as a
reference during execution.
Consider this example dataset:
Sales Laptops Tablets Cell Phones Electr onics
Store 1 100 20 60  
Store 2 20   35  
Store 3   10 20  
Store 4 200   40  
 
After we deploy the calc, we would see the following data:29/12/2025, 08:12 Reference: Vena Calcs - 2 - Notation and Syntax – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027591072-Reference-Vena-Calcs-2-Notation-and-Syntax 12/18

## Page 13

 Sales Laptops Tablets Cell Phones Electr onics
Store 1 100 20 60 180
Store 2 20   35 55
Store 3   10 20  
Store 4 200   40 240
The calculation does not compute the value for ([S tore 3], [Electronics], [Sales]) due to the empty
intersection at ([S tore 3], [Laptops], [Sales]). Whenever triggered by a Deploy or Save, the
calculation engine identifies target intersections linked to existing special allocation source
intersections in the Cube.
 
Selecting the Allocation Sour ce
Vena Calcs selects the first source intersection as the Allocation Source. If the desired Allocation
Source cannot be positioned at the start of an expression, it can be assigned to a variable at the
beginning of the calculation.
For efficiency, ensure the variable with the most intersections appears first in the value statement
(@this = A * B). This minimizes the fan-out ratio, achieving a 1:1 relationship for better
performance.
Allocation mode for an FX calculation:
 //CONVERSION FOR ENTITIES WHERE LOCAL CURRENCY IS USD 
Scope { 
[Entity.All Entities in Local USD].Leaves() 
[Department.All Departments].Leaves(), 
[Year.All Years].Leaves(), 
[Period.Full Year].Leaves(), 
[Scenario.Actual],[Scenario.Forecast],[Scenario.Budget], 
[Currency.All Reporting Currencies].Leaves() 
     } 
Scope {[Account.Net Income]}.Leaves() 
//Define local values 
@local = ([Currency.Local]) 
//Define FX Rates. Include Placeholders if they are in use. 
@rate = ([Account.Average Rate], [Measure.Local Rate USD], [Entity.Not Entity Specific], [
//Reporting value = FX Rates * local value 
@this = @local * @rate 
End 
End 
 29/12/2025, 08:12 Reference: Vena Calcs - 2 - Notation and Syntax – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027591072-Reference-Vena-Calcs-2-Notation-and-Syntax 13/18

## Page 14

Using the order “@this = @local * @rate” ensures better scalability by prioritizing intersections in
@local, which are more numerous, over @rate. This allows the calculation engine to check if @local
is populated before proceeding. If @local is empty, the engine skips to the next set of intersections,
optimizing efficiency.
 
To check if you are using the calc in the most effective order, select the  View Scr ipt Details icon  (
) to the right of the calc.
This will show you a breakdown of the calculation fan-out. 
The following is an example of an inefficient calc.  In this example, fewer intersections are positioned
first (@rate) and more intersections second (@local) for both FX Calc [1] and FX Calc [2], leading to
a high fan-out ratio (@Rate / @Local). R eordering these variables can improve efficiency.29/12/2025, 08:12 Reference: Vena Calcs - 2 - Notation and Syntax – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027591072-Reference-Vena-Calcs-2-Notation-and-Syntax 14/18

## Page 15

 
 
Let’s correct this calc.  
 
Allocation mode for an FX calculation:
//CONVERSION FOR ENTITIES WHERE LOCAL CURRENCY IS USD 
Scope { 
[Entity.All Entities in Local USD].Leaves() 
[Department.All Departments].Leaves(), 
[Year.All Years].Leaves(), 
[Period.Full Year].Leaves(), 
[Scenario.Actual],[Scenario.Forecast],[Scenario.Budget], 
[Currency.All Reporting Currencies].Leaves() 
     } 
Scope {[Account.Net Income]}.Leaves() 
//Define local values 
@local = ([Currency.Local]) 
//Define FX Rates. Include Placeholders if they are in use. 
@rate = ([Account.Average Rate], [Measure.Local Rate USD], [Entity.Not Entity Specific], [
//Reporting value = FX Rates * local value 
@this = @local * @rate 
End 
End 
To optimize efficiency, the calc engine skips intersection calculations if the first variable is empty. 29/12/2025, 08:12 Reference: Vena Calcs - 2 - Notation and Syntax – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027591072-Reference-Vena-Calcs-2-Notation-and-Syntax 15/18

## Page 16

Let's view the new script details.
Note the fan-out is now greater than 1:1.
 
 
Read Calcs 
Adding “.read” to a calc's name switches it to read mode. Unlike write mode, which triggers
calculations when source intersections are updated, read mode activates calculations only when
target intersections are  read, not simply when the value is retrieved.
 
Read calcs are used for:
Replacing roll-ups
Associated calculations with parent intersections29/12/2025, 08:12 Reference: Vena Calcs - 2 - Notation and Syntax – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027591072-Reference-Vena-Calcs-2-Notation-and-Syntax 16/18

## Page 17

Calculating values on demand
Overriding normal cube aggregations
Calculating ratios
Instances where calculating across the entire model isn't practical due to its size.
 
Read mode is ideal for calcs with large scopes, such as parent calcs. Since target values are
calculated only when queried, it reduces unnecessary processing for intersections unlikely to be
retrieved. This approach optimizes performance by calculating values on demand instead of pre-
calculating entire scopes.
 
Limitations
.read calcs values are not supported in V ena Insights and P ower BI.
Read calcs compute target intersections on-demand when queried, resulting in potential delays
based on their complexity. 
Read calcs can only be queried through ETL exports or Integration channels using Cube sources
and the V alues (Advanced) export type.
 
A key limitation of read calcs is their interaction with rollups. R ead calc results are not stored in the
database, impacting rollup computations. Here’s an example to illustrate this:
Scope { [Period.All Periods].Leaves(), [Measure.Avg Sell Price Per Unit] } 
@this = [Measure.Revenue] / [Measure.Units Sold] 
End 
If we have the following data, where Q1 is a parent of Jan, Feb and Mar:
Period Revenue Units Sold
Q1 4200 60
Jan 1200 20
Feb 1500 20
Mar 1500 20
Then, when mapping a template to view the A vg Sell Price P er Unit, we'll see that the read calc
results in the correct values for the bottom level intersections, at Jan, Feb and Mar. But the
intersection for Q1 is empty.
Period Avg Sell Pr ice P er Unit29/12/2025, 08:12 Reference: Vena Calcs - 2 - Notation and Syntax – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027591072-Reference-Vena-Calcs-2-Notation-and-Syntax 17/18

## Page 18

Q1  
Jan 60
Feb 75
Mar 75
 
In these cases, typically the solution is to change the scope of the read calc to operate on all
descendants, instead of just bottom-level members. This may look like:
Scope { [Period.All Periods].IDescendants(), [Measure.Avg Sell Price Per Unit] } 
@this = [Measure.Revenue] / [Measure.Units Sold] 
End 
 
Now if we look at the data at a parent level, we should see the calculation work correctly:
Period Avg Sell Pr ice P er Unit
Q1 70
Jan 60
Feb 75
Mar 75
 
 
Best Practices 
All calcs containing a dimension should include the dimension name in the script.
Add commentary using the double slash ( // ) to provide context to others reading your calc.
Always maintain proper indentation (use the T ab button on your keyboard).
 29/12/2025, 08:12 Reference: Vena Calcs - 2 - Notation and Syntax – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027591072-Reference-Vena-Calcs-2-Notation-and-Syntax 18/18
