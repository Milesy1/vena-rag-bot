# Reference_ Vena Calcs - 7 - Currency Conversions – Vena Solutions

## Page 1

Reference: Vena Calcs - 7 - Currency
Conversions
About this series
This series is about how to use  Vena Calculation Scr ipts. Vena Calculations Scripts (or  Vena Calcs ), is a
scripting language designed for V ena data models. V ena Calcs provides a powerful and flexible way to run
calculations and simulations for business rules at the database level for all dimensions and members.
We've broken down V ena Calcs into nine articles, can be read consecutively or browsed as needed.
 
Part 1: Managing Scripts  
Part 2: Notation and S yntax
Part 3: Data T ypes
Part 4: Operators
Part 5: Functions
Part 6: Conditional S tatements
Part 7: Currency Conversions-  You ar e her e
Part 8: Examples
Part 9: Troubleshooting
 
Table of contents
 Best Practices
FX Conversions
One Local, One R eporting
Multiple Local, One R eporting
One Local, Multiple R eporting
Multiple Local, Multiple R eporting
How to Optimize your Calc
Vena Support T eam
Updated  1 year ago29/12/2025, 08:59 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 1/16

## Page 2

 
 
Currency Conversions
The following article contains information on currency conversions (FX conversions) in V ena calcs.
 
FX Conv ersions
There are four standard types of FX Conversions Calculations, characterized by the number of local currencies
involved and the number of reporting currencies involved. The type you select will depend on your business
needs. In this section, we will describe the recommended data model hierarchy and the necessary calculations
to do FX Conversions for those four types.
For the following examples, assume the model has the following three dimensions:
Account
Period
Year
 
Example 1
 
Dimension : Account
  ── All_Accounts
        ├── Account001
        ├── Account002
        ... <etc>
  ── No_Account
 
 
Example 2
 
Dimension : Period
  ── All_Periods
        ├── Q1
        │   ├── Jan
        │   ├── Feb29/12/2025, 08:59 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 2/16

## Page 3

        │   └── Mar
        ├── Q2
        │   ├── Apr
        │   ├── May
        │   └── Jun
        ... <etc>
  ── No_Period
 
 
Example 3
 
Dimension : Year
  ── All_Years
        ├── 2014
        ├── 2015
        └── 2016
  ── No_Year
 
 
One Local, One R epor ting
This is the most straightforward type of FX Conversion: one local currency and one reporting currency. For this
kind of conversion, your model should have a Currency dimension with members for your local and reporting
currencies, and a third member for the rate to convert between the two. In this example, our local currency is
USD and our reporting currency is EUR.
Dimension : Currency
  ── All_Currencies
        ├── USD
        └── EUR
  ── FX_Rate
  ── No_Currency
 
Then, the calculation to do the FX Conversion is very simple:29/12/2025, 08:59 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 3/16

## Page 4

 
Scope { [Account.All_Accounts].Leaves(),
        [Period.All_Periods].Leaves(),
        [Year.All_Years].Leaves(),
        [Currency.EUR]
}
    @local  = ([Currency.USD])
    @rate  = ([Currency.FX_Rate], [Account.No_Account])  // include other No_ members here
    @this = @local * @rate
End
 
This assumes that you have different FX Rates per period and per year, but within a single period and year the
rate is the same for all accounts. For other dimensions for which the rate will be constant, such as department,
product, etc. (the specifics will depend on your business case), include that dimension's "No_" member in
the @rate  variable. Note that this calculation should be put into  sparse mode . Sparse mode is an optimization
designed specifically for FX Conversions.
In this case, our sheets would look like this:
Page options:
Account: No_Account
Year: 2015
  FX_Rat e
Jan 1.5
Feb 1.6
Mar 1.7
Account: Account001
Year: 2015
  USD EUR
Jan 1000 1500
Feb 1000 160029/12/2025, 08:59 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 4/16

## Page 5

  USD EUR
Mar 1000 1700
 
 
Multiple Local, One R epor ting
This type of FX Conversion is used when you have many local currencies and a single reporting currency. The
best way to handle this scenario is, like the one-to-many case, use two dimensions: Currency and Measure. In
this example, we're converting from inputs in both USD, GBP, and EUR, and we're reporting in GBP, these
dimensions will look like:
Dimension : Currency
  ── All_Currencies
        ├── USD
        ├── GBP
        └── EUR
  ── No_Currency
 
Dimension : Measure
  ── All_Measures
        ├── FX_Rate
        ├── Local
        └── Reporting
  ── No_Measure
And the calc will be as follows:
Scope { [Account.All_Accounts].Leaves(),
        [Period.All_Periods].Leaves(),
        [Year.All_Years].Leaves(),
        [Currency.All_Currencies].Leaves(),
        [Measure.Reporting]
}
 
    @local  = ([Measure.Local])29/12/2025, 08:59 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 5/16

## Page 6

    @rate  = ([Measure.FX_Rate], [Account.No_Account])
      @this = @local * @rate
 
End
Notice that this operates on all currencies; the  @local  and  @rate  variables will both have the same member in
the currency dimension. This calc tells V ena to take the value at a given currency and account and at
the Local  measure, and multiply by the value at the same currency but at the special  No_Account member and
the FX_Rate  measure, and to store the product in the intersection at the given currency and account at
the R eporting measure. If we have multiple values in the same account from different local currencies, we will
find the aggregate of all of the converted values in the  All_Currencies  parent member.
Again, like the one-to-one case, the assumption is made that the rates vary across period and year but remain
constant across account, and again, this calculation should be in  sparse mode .
On the sheets, our data would look like:
Page options:
Account: No_Account
Year: 2015
Measure: FX_Rate
  USD EUR GBP
Jan 1.5 2.0 1.0
Feb 1.6 2.1 1.0
Mar 1.7 1.9 1.0
Account: Account001
Year: 2015
Measure: Local
  USD EUR GBP
Jan 1000 1000 1000
Feb 1000 1000 1000
Mar 1000 1000 1000
Account: Account001
Year: 201529/12/2025, 08:59 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 6/16

## Page 7

Measure: R eporting
  USD EUR GBP All_Curr encies
Jan 1500 2000 1000 4500
Feb 1600 2100 1000 4700
Mar 1700 1900 1000 4600
So, in this case, the reporting value for a given account in a given year and period is at
the ([ Measure.R eporting ], [Currency.All_Currencies ])intersection. Also, notice that since we have inputs in GBP
and are reporting in GBP, the values at ([ Measure.FX_Rate ], [Currency.GBP ]) are always  1.0.
 
One Local, Multiple R epor ting  
This kind of FX Conversion should be used if you have a single local currency and multiple reporting
currencies. In this case, your model would need two dimensions: a Currency dimension and a Measure
dimension. In this example, we are inputting in GBP and reporting in GBP and USD.
Dimension : Currency
  ── All_Currencies
        ├── GBP
        └── Reporting
            ├── GBP_rpt
            └── USD_rpt
  ── No_Currency
 
Dimension : Measure
  ── All_Measures
        ├── FX_Rate
        └── Value
  ── No_Measure
In this case, we want to convert the values stored under the two local currencies into the single reporting
currency. Our calc would be:
Scope { [Account.All_Accounts].Leaves(),
        [Period.All_Periods].Leaves(),29/12/2025, 08:59 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 7/16

## Page 8

        [Year.All_Years].Leaves(),
        [Currency.Reporting].Leaves(),
 
        [Measure.Value]
}
 
    Scope { [Currency.GBP_rpt] }
        @local = ([Currency.GBP], [Measure.Value])
        @rate  = ([Measure.FX_Rate], [Account.No_Account], [Currency.GBP_rpt])
 
        @this = @local * @rate
    End
 
    Scope { [Currency.USD_rpt] }
         @local = ([Currency.GBP], [Measure.Value])
         @rate  = ([Measure.FX_Rate], [Account.No_Account], [Currency.USB_rpt])
        @this = @local * @rate
    End
End
The obvious difference is that we now need multiple subscopes for each reporting currency. This is because,
like the previous calcs, our calc is in  sparse mode , so we need the local value to have a one-to-one relationship
with the reporting value. If we used one scope for all of the reporting currencies, both the local value and the
rate would have a one-to-many relationship with the reporting value.
If we set the calc in non-sparse mode, we could use the one scope for all of the reporting currencies, but this
runs the risk of flooding the entire cube with 0 values and will make saves, calculation deploys, and rollups far
slower. Running FX Conversions from a non-sparse calc is not recommended.
In this case, our sheets would look like
Page options:
Account: No_Account
Year: 2015
Measure: FX_Rate
  GBP GBP_rpt USD_rpt
Jan 1 1.5 2.029/12/2025, 08:59 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 8/16

## Page 9

  GBP GBP_rpt USD_rpt
Feb 1 1.6 2.1
Mar 1 1.7 1.9
Account: Account001
Year: 2015
Measure: V alue
  GBP GBP_rpt USD_rpt
Jan 1000 1500 2000
Feb 1000 1600 2100
Mar 1000 1700 1900
 
 
 
Multiple Local, Multiple R epor ting
This is the most complex of FX Conversion types: multiple local currencies, and multiple reporting currencies.
In cases like this, you will need to have two dimensions: Local Currency and Measure. In the example below, we
have USD and GBP as locals, and are reporting in GBP and EUR.
Dimension : Local Currency
  ── All_Local_Currencies
        ├── USD_loc
        └── GBP_loc
  ── No_Currency
 
Dimension : Measure
  ── All_Measures
        ├── Value
        └── Reporting29/12/2025, 08:59 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 9/16

## Page 10

            ├── GBP_rpt
            └── EUR_rpt
  ── No_Measure
One obvious difference is that we now do not have any reporting currencies in the "Local Currency"
dimension. Instead, we use the combination of the two dimensions to describe the intersections.
  Value GBP_rpt EUR_rpt
USD_loc Literal value in
USDUSD value converted into GBP USD value converted
into EUR
GBP_loc Literal value in
GBPGBP value converted into GBP (should be
identical to previous column)GBP value converted
into EUR
All_local_currencies (meaningless) Total in GBP Total in EUR
This way, when looking at a converted value, we always know where that value came from. Essentially, the
"Measures" department is a "R eporting Currencies" department and the "V alue" member could be renamed
"Local value".
In this scenario, the calc should look like the following:
Scope {
        [Account.All_Accounts].Leaves(),
        [Period.All_Periods].Leaves(),
        [Year.All_Years].Leaves(),
        [Currency.All_Local_Currencies].Leaves(),
        [Measure.Reporting].Leaves()
}
 
    Scope { [Measure.GBP_rpt]}
        @local = ([Measure.Value])
        @rate = ([Account.No_Account], [Measure.GBP_rpt])
        @this = @local * @rate
    End
 
    Scope { [Measure.EUR_rpt]}
        @local = ([Measure.Value])29/12/2025, 08:59 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 10/16

## Page 11

        @rate  = ([Account.No_Account], [Measure.EUR_rpt])
 
        @this  = @local * @rate
    End
 
End
Again, this calc should be in  sparse mod e and, just like the case with multiple local currencies and one
reporting currency, has separate scopes for each reporting currency.
On the sheet, our data will look like so:
Page options:
Account: No_Account
Year: 2015
Period: Jan
  USD_Loc GBP_Loc
GBP_rpt 1.5 1.0
EUR_rpt 1.6 1.0
Account: Account001
Year: 2015
Measure: V alue
  USD_Loc GBP_Loc
Jan 1000 1000
Account: Account001
Year: 2015
Measure: GBP_rpt
  USD_Loc GBP_Loc All_Local_Curr encies
Jan 1500 1000 2500
Account: Account001
Year: 2015
Measure: EUR_rpt29/12/2025, 08:59 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 11/16

## Page 12

  USD_Loc GBP_Loc All_Local_Curr encies
Jan 3000 2000 5000
Notice that in this design, like in the many-to-one, the end result is the aggregation of all of the values from
the local currencies, after they have each been converted appropriately.
 
 
 
How t o Optimize y our Calc
 
1.) For m
1. Comment: Add commentary using the double slash (//) to provide context to others reading your calc.
Rule of thumb: Add a comment for each scope.
2. Proper indentation via T ab key and align each nested scope.
 
2.) Define ev ery dimension
Defining all dimensions in your target scope will help our support team and other users at your company
follow the scope. This includes both stating the dimension and applicable members. Excluding a dimension
increases the calc scope drastically as it will ask the calc to calculate based on all the members in that
dimension.
 
3.) Manage Scope Size
Make sure to check your .Leaves() notation and e nsure bottom level members under .Leaves() parents are
relevant. If they are not consider .Exclude sources members that are not likely to be populated.
 
4.) Manage y our Number o f Scopes
Scopes can be reduced by checking if the same members are applicable across scopes.  For example, in the
following calc, there is only one Entity P arent. This can be moved to the T arget Scope:29/12/2025, 08:59 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 12/16

## Page 13

 Scope   { 
     [Department.All Departments].Leaves(),
     [Year.All Years].Leaves(),
     [Period.Full Year].Leaves(),
     [Placeholder 1.Not Placeholder 1 Specific],
     [Placeholder 2.Not Placeholder 2 Specific],
     [Placeholder 3.Not Placeholder 3 Specific],
     [Placeholder 4.Not Placeholder 4 Specific],
     [Scenario.Actual],[Scenario.Forecast],[Scenario.Budget],
     [Currency.All Reporting Currencies].Leaves()
    }
    //CONVERSION FOR ENTITIES WHERE LOCAL CURRENCY IS USD
    Scope {[Entity.All Entities in Local USD].Leaves()} //<<--- list of entities which have USD as l
          //Define FX Rates. Include Placeholders if they are in use. 
          @rate  = ([Account.Average Rate], [Measure.Local Rate USD], [Entity.Not Entity Specific], 
          [Department.Not Department Specific])
    
        Scope {[Account.Net Income]}.Leaves()
          //Define local values
          @local = ([Currency.Local])
          
          //Reporting value = FX Rates * local value
          @this =  @Local * @rate
          
        End
End
End
 
Your new calc should look like the following:
Scope   { 
[Entity.All Entities in Local USD].Leaves()     29/12/2025, 08:59 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 13/16

## Page 14

[Department.All Departments].Leaves(),
[Year.All Years].Leaves(),
[Period.Full Year].Leaves(),
[Placeholder 1.Not Placeholder 1 Specific],
[Placeholder 2.Not Placeholder 2 Specific],
[Placeholder 3.Not Placeholder 3 Specific],
[Placeholder 4.Not Placeholder 4 Specific],
[Scenario.Actual],[Scenario.Forecast],[Scenario.Budget],
 [Currency.All Reporting Currencies].Leaves()
    }
           //Define FX Rates. 
  @rate  = ([Account.Average Rate], [Measure.Local Rate USD], [Entity.Not Entity Specific], 
          [Department.Not Department Specific])
    
        Scope {[Account.Net Income]}.Leaves()
          
 //Define local values
          @local = ([Currency.Local])
         
          //Reporting value = FX Rates * local value
          @this = @Local * @rate 
          
        End
End
 
5.) Consider y our Allocation Mode
Allocation mode is useful for calcs with a multiplication (eg. T arget = A x B) or divide calculation (eg. T arget = A
/ B) . During deploy, the allocation mode detects all populated source intersections and only calculates those
intersections. If the source intersection is not populated, data will not recalculate.
 
Signs that your calc should be in Allocation mode:
1 Multiplication or division calculation. This is most
common in Driver based planning, allocations,
KPI calculations, and Foreign Exchange. 29/12/2025, 08:59 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 14/16

## Page 15

2
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 View script details for potential fan-out ratio.
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  
Example: Bad pot ential fan-out ratio
Example: Efficient pot ential fan-out ratio:
3 Move the larger variable to the front of the value
statement. 29/12/2025, 08:59 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 15/16

## Page 16

4 Append  .Allocation  to the name of the calc
 
6.) User V ariables
Define @rate = slice instead of only stating the slice in the value statement.
For example:
Correct:
@Localvalues = [Currency.Local]
@rate = [Account.Average Rate],[Measure.Local Rate USD]
@This = @Localvalues * @rate 
 
Incorr ect:
@localvalues = slice
@This = @localvalues *  [Account.Average Rate],[Measure.Local Rate USD]
 
7.) Consider using an A ttribute
Using an attribute for Y ear and/or P eriod allows the calc to only recalculate values from that year. If the calc
wrote to previous years when you change the members attached to the attribute the values will remain. Note,
when attribute changes (eg. if a new cycle is beginning) then the calc will have to be redeployed.
 
8.) Consider splitting y our calc int o multiple calcs
Smaller scopes in multiple calcs will increase performance. Note, this may differ if there are dependent calcs.
Common logic is splitting calcs up by:
Financial S tatement type (ie. Income statement/Balance Sheet). This is common in FX rates as the two
statements reference different rates.
Subsidiary
Scenario29/12/2025, 08:59 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 16/16
