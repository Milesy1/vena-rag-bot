# Reference_ Vena Calcs - 8 - Examples – Vena Solutions

## Page 1

Reference: Vena Calcs - 8 - Examples
About this series
This series is about how to use  Vena Calculation Scr ipts. Vena Calculations Scripts (or  Vena Calcs ), is a scripting language
designed for V ena data models. V ena Calcs provides a powerful and flexible way to run calculations and simulations for
business rules at the database level for all dimensions and members.
We've broken down V ena Calcs into nine articles, can be read consecutively or browsed as needed.
 
Part 1: Managing Scripts  
Part 2: Notation and S yntax
Part 3: Data T ypes
Part 4: Operators
Part 5: Functions
Part 6: Conditional S tatements
Part 7: Currency Conversions
Part 8: Examples -  You ar e her e
Part 9: Troubleshooting
 
 
Table of contents
Examples
Writing to Bottom Level Members
Scoping P arent Members
Including P arent Members
Division with Members in Calcs
Comparison Operators
Read Calc: Common R oll-Up R eplacement 
Driver Calcs
TTM - T railing T welve Months
Calendar to Fiscal Y ear
 
Vena Support T eam
Updated  6 months ago29/12/2025, 09:00 Reference: Vena Calcs - 8 - Examples – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695412-Reference-Vena-Calcs-8-Examples 1/12

## Page 2

Examples
Writing t o Bott om Lev el Member s
Scope {[Bottom Level Member], [Jan]}
    @This = [Bottom Level1] * [Bottom Level2]
End
Running this calc will store the value of Bottom Level 1* Bottom Level 2 in the given context of 2015, Q1 and Jan into the
scoped Bottom Level Member. This Calc would also write to the database to update Bottom Level Member when either
Bottom Level 1 or Bottom Level 2 is changed.
 
Scoping P arent Member s
Scope {[Parent Member], [Jan]}
     @This = [Bottom Level1] * [Bottom Level2]
End
A Calc like this would function similarly to the Calc above and would show the Calc result on excel sheets. However, as it is not
possible to write values to P arent Members, the value in the database would remain unchanged, and on removal of the Calc
would return to the rollup value.
 
Including P arent Member s
Scope {[Bottom Level], [Jan]}
    @This = [Parent Member]
End
A Calc like this would store the value of P arent Member into [Bottom Level], and would write values to the database whenever
a child of P arent Member is updated (changing the rollup value). When writing a Calc like this, one has to be extremely careful
as if Bottom Level is a child of P arent Member it can create a loop that crashes the process.
 
Division with Member s in Calcs
When dividing using Members (and their intersections) in Calcs, it is important to make sure that dividing by 0 does not occur.
Scope {[Bottom Level], [Jan]}
    @This = [Parent Member]/[Local Earnings]
End
Division by 0 will result in no change in the current value at the intersection.
In this Calc, if there is a situation where [Local Earnings] equals zero, the Calc will fail to run, as dividing by zero is not a valid
operation. In order to avoid situations like this, the following code can be used.
Scope {[Bottom Level], [Jan]}
    If ([Local Earnings] != 0)
        @This  = [Parent Member]/[ Local Earnings]29/12/2025, 09:00 Reference: Vena Calcs - 8 - Examples – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695412-Reference-Vena-Calcs-8-Examples 2/12

## Page 3

    End
End
This code will only perform the division if you are not dividing by zero.
 
Comp arison Operat ors
The comparison operators are  > (greater than),  < (less than),  >= (greater than or equal to),  <= (less than or equal
to), == (equal to) and  != (not equal to). They must be used within an “if” statement to compare two different values, and in the
future will be able to compare the names of members. These can be used in conjunction with the logical operators  && (and),  ||
 (or) and  | (exclusive or).
Scope {[Measure.Reporting] ,[Accounts.All Accounts].Leaves(),[Period.All Periods].Leaves()}
    If ([Measure.Rate] > 0 || [Measure.Rate] < - 20 }
        // if rate > 0 OR rate < - 20
        @this = [Measure. Local] * [Measure.Rate]
    Else
        // otherwise
        @this = [Measure. Local]
    End
End
 
 
 
Read Calc: Common R oll-Up R eplacement
Replace Gross Profit [R evenue-C OGS]  in a data model’s account dimension with Gross Profit.
Margin percentage [(R evenue-C OGS) / R evenue].
Replace a roll-up sum with an average.
 
 
Driver-Based Calcs
Use Case Summar y
Using driver-based calcs allows finance managers to use assumptions as a base for planning. Drivers can be set in an input
template at the beginning of a cycle and retrieved on any report. This allows an audit trail for assumptions and saves Manager
time by applying general assumptions reliant on factors such as headcount and previous year actuals.
Example:
An account value is driven by a % of another account or a number in another account. Ie. A x B% or A x B#.
Solution:
This solution can be expanded by creating additional override members and columns for custom end-user input.
 
Limitations/Benefits
 29/12/2025, 09:00 Reference: Vena Calcs - 8 - Examples – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695412-Reference-Vena-Calcs-8-Examples 3/12

## Page 4

Limitations
Only ideal for simple logic, not suitable for complicated logic. X
If using percentages, ensure the input template saves the appropriate decimal representation. X
 
Benefits
Time saver on calculations that do not need granular, manual detail.
✓
Ability to centralize tracking of year over year assumption changes.
✓
Driver changes are instantly applied.
✓
 
Prerequisit es
If you require a headcount driven calculation, you may need to reference a member that captures the qualifying headcount
total for that calculation.
Vena Calc Scr ipt Method
Example 1: T ravel and Mis cellaneous expens es as a % o f Revenue
Scope { [Account.Travel and Miscellaneous Expense],
        [Entity.All Entities].Leaves(),
        [Period.Full Year].Leaves(),
        [Year.All Years].Leaves(),
        [Scenario.Budget],[Scenario.Forecast],
        [Measure.Value]}
      
        // % Assumption
        @OfficePercentage = [Account.Office Expense Driver]
        
        // Revenue
        @Revenue = [Account.Revenue]
        @This = @OfficePercentage * @Revenue
    
End29/12/2025, 09:00 Reference: Vena Calcs - 8 - Examples – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695412-Reference-Vena-Calcs-8-Examples 4/12

## Page 5

 
Example 2: C ell phone expens e as a $ per headc ount
Scope { [Account.Cell Phone Expense],
        [Entity.All Entities].Leaves(),
        [Department.All Departments].Leaves()
        [Employee.Not Employee Specific],
        [Period.Full Year].Leaves(),
        [Year.All Years].Leaves(),
        [Scenario.Budget],[Scenario.Forecast],
        [Measure.Value]}
        // Full Time EmployeeHeadcount per department
        @Headcount = ([Account.Headcount],[Employee.Active Employees])
    
        // Cell phone cost per head
        @Cellcost = ([Account.Driver_CellPhone],[Employee.Not Employee Specific])
        //Cell Phone expense calculation = @Headcount * @Cell phone cost
        @This = @Headcount * @CellCost
  
End
 
 
TTM - T railing T welve Months
Use Case Summar y
A trailing twelve months calculation is a type of analysis that looks at the previous 12 months’ financial data in your business.
Trailing twelve months - often abbreviated as T TM - allows you to analyze a full year’s worth of financial data at any point in
the year.
For example, let’s say it’s July, and you want to run a T TM analysis on your income. Y ou would compile information from the
profit and loss statements for your business beginning July 1 of the previous year and ending June 30 of the current year.
How to calculate T TM
1. Formula: T TM = Q (latest) + Q (1 quarter ago) + Q (2 quarters ago) + Q (3 quarters ago)
2. Formula: T TM figure = Most recent quarter(s) + Last full year – Corresponding quarter(s) last year.
3. Formula: T TM = M (latest) + M (11 months ago)
Limitations/Benefits
 
Limitations  29/12/2025, 09:00 Reference: Vena Calcs - 8 - Examples – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695412-Reference-Vena-Calcs-8-Examples 5/12

## Page 6

 Using T TM may be laborsome since you need to work back using monthly, quarterly, or semi-annual company
reports.X
For companies with a volatile business, the values of their financial data may quickly change and T TM analysis
might not be reliable.X
 
Benefits
Trailing twelve months shows the most current 12-month financial performance of a business.
✓
 TTM helps investors and creditors accurately evaluate and value a company.
✓
The use of T TM can help business owners make strategic decisions that drive company performance.
✓
 
Pre-requisit es
In the ‘P eriod’ dimension, you will require the following members:
1. Calendar P eriods
1. Full Y ear
1. Q1
1. 01
2. 02
3. 03
2. Q2
1. 04
2. 05
3. etc.
2. TTM P eriods
1. 01 TTM
2. 02 TTM
3. 03 TTM
4. etc.29/12/2025, 09:00 Reference: Vena Calcs - 8 - Examples – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695412-Reference-Vena-Calcs-8-Examples 6/12

## Page 7

Vena Calc Scr ipt Method
Scope{
    [Account.All Accounts].Leaves(),
    [Entity.All Entities].Leaves(),
    [Department.All Departments].Leaves(),
    //add any other placeholder dimensions
    [Year.All Years].Leaves(),
    // Period as a filter
    [Scenario.All Scenarios].Leaves(),
    [Currency.All Currencies].Leaves(),
    [Measure.All Measures].Leaves()
}
TimeScale([Year.2017], [Period.H1], [Period.01]) //<<--- regular set up for timescale (review documentation)
    Scope { [Period.01 TTM]}
     @this = [Period.01].PrevPeriods(11).Sum() + [Period.01]
    End
    
    Scope { [Period.02 TTM]}
     @this = [Period.02].PrevPeriods(11).Sum() + [Period.02]
    End
    
    Scope { [Period.03 TTM]}
     @this = [Period.03].PrevPeriods(11).Sum() + [Period.03]
    End
    
    Scope { [Period.04 TTM]}
     @this = [Period.04].PrevPeriods(11).Sum() + [Period.04]
    End
    
    Scope { [Period.05 TTM]}
     @this = [Period.05].PrevPeriods(11).Sum() + [Period.05]
    End
    
    Scope { [Period.06 TTM]}
     @this = [Period.06].PrevPeriods(11).Sum() + [Period.06]
    End
    
    Scope { [Period.07 TTM]}29/12/2025, 09:00 Reference: Vena Calcs - 8 - Examples – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695412-Reference-Vena-Calcs-8-Examples 7/12

## Page 8

     @this = [Period.07].PrevPeriods(11).Sum() + [Period.07]
    End
    
    Scope { [Period.08 TTM]}
     @this = [Period.08].PrevPeriods(11).Sum() + [Period.08]
    End
    
    Scope { [Period.09 TTM]}
     @this = [Period.09].PrevPeriods(11).Sum() + [Period.09]
    End
    
    Scope { [Period.10 TTM]}
        @this = [Period.10].PrevPeriods(11).Sum() + [Period.10]
    End
    
    Scope { [Period.11 TTM]}
     @this = [Period.11].PrevPeriods(11).Sum() + [Period.11]
    End
    
    Scope { [Period.12 TTM]}
     @this = [Period.12].PrevPeriods(11).Sum() + [Period.12]
    End
End
 
Advanced method consideration
If you are using the Advanced method, you need to update this source:
FIN_DataLoad_Advanced_Src_Cube_Data to include the following in the query:
Dimension('Period':not(bottomlevel(TTM Periods'))). 
You will receive an error when updating GL  data if this is not included.
 
 
 
 
 
 29/12/2025, 09:00 Reference: Vena Calcs - 8 - Examples – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695412-Reference-Vena-Calcs-8-Examples 8/12

## Page 9

 
 
 
 
 
 
 
 
 
 
 
Calendar t o Fiscal Y ear
Use Case
This method uses V ena calc scripts for
getting Fiscal Y ear data from a
Calendar year view.
In this particular use case:
Calendar 2020 = Jan 2020 to Dec 2020
Fiscal 20 21 = Apr 2020 to Mar 20 21
 
Limitations/Benefits
 
Limitations 
DATA SIZE; you essentially doubled the size of data held in the actual member.  While this is not a concern for smaller
implementations, this can impact performance in big implementationsX
 
Benefits 
You can reverse this method to do Fiscal to Calendar.
✓
You can use this method for both Calendar > Fiscal and Fiscal > Calendar, as soon as you define the right slice of data that
needs to use one or the other method.
✓
29/12/2025, 09:00 Reference: Vena Calcs - 8 - Examples – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695412-Reference-Vena-Calcs-8-Examples 9/12

## Page 10

Pre-requisit es
Review the following article on Time Series calcs [Insert Link here]
In the ‘P eriod’ dimension, you will require the following members:
1. Calendar P eriods
1. Full Y ear
1. Q1
1. 01
2. 02
3. 03
2. Q2
1. 04
2. 05
3. etc.
2. Fiscal P eriods
1. Fiscal - Full Y ear
1. Fiscal-Q1
1. P01
2. P02
3. P03
2. Fiscal-Q2
1. P04
2. P05
3. etc.
Vena Calc Scr ipt Method
1. To build the following calc script, you need to understand the lag period. This is the number of month between
Period P01 - Fiscal XXXX and P eriod 01 - Calendar XXXX. In this case, this is 9 months.
2. The maths are as follow:
3. [Period P01 - Fiscal 2021] = [P eriod 01 - Calendar 2021] -  9 months
4. Apr 2020 = Jan 2021 - 9 months
5. [Period P01 - Fiscal 2021] = [P eriod 01 - Calendar 2020] +  3 months )
6. Apr 2020 = Jan 2020 + 3 months
7. The calc script has two sections:
 
Example Calc:
Scope{
    [Account.All Accounts].Leaves(),
    [Entity.All Entities].Leaves(),
    [Department.All Departments].Leaves(),
    //add any other placeholder dimensions
    [Year.All Years].Leaves(),
    // Period as a filter
    [Scenario.All Scenarios].Leaves(),
    [Currency.All Currencies].Leaves(),
    [Measure.All Measures].Leaves()
}29/12/2025, 09:00 Reference: Vena Calcs - 8 - Examples – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695412-Reference-Vena-Calcs-8-Examples 10/12

## Page 11

TimeScale([Year.2017], [Period.Q1], [Period.01])    //<-- regular set up for timescale 
   //Periods in year - 1 logic
    Scope {[Period.P01]}
     @this = [Period.01].PrevPeriods(1, Lag=9).Sum()
    End
    
    Scope {[Period.P02]}
     @this = [Period.02].PrevPeriods(1, Lag=9).Sum()
    End
    
    Scope {[Period.P03]}
     @this = [Period.03].PrevPeriods(1, Lag=9).Sum()
    End
    
    Scope {[Period.P04]}
     @this = [Period.04].PrevPeriods(1, Lag=9).Sum()
    End
    
    Scope {[Period.P05]}
     @this = [Period.05].PrevPeriods(1, Lag=9).Sum()
    End
    
    Scope {[Period.P06]}
     @this = [Period.06].PrevPeriods(1, Lag=9).Sum()
    End
 
    Scope {[Period.P07]}
     @this = [Period.07].PrevPeriods(1, Lag=9).Sum()
    End
    
    Scope {[Period.P08]}
     @this = [Period.08].PrevPeriods(1, Lag=9).Sum()
    End
    
    Scope {[Period.P09]}
     @this = [Period.09].PrevPeriods(1, Lag=9).Sum()29/12/2025, 09:00 Reference: Vena Calcs - 8 - Examples – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695412-Reference-Vena-Calcs-8-Examples 11/12

## Page 12

    End
   //Periods in same year
        
    Scope{[Period.P10]}
        @this = [Period.01]
    End
        
    Scope{[Period.P11]}
        @this = [Period.02]
    End
   
    Scope{[Period.P12]}
        @this = [Period.03]
    End
End29/12/2025, 09:00 Reference: Vena Calcs - 8 - Examples – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695412-Reference-Vena-Calcs-8-Examples 12/12
