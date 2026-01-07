# Reference_ Vena Calcs - 9 - Troubleshooting – Vena Solutions

## Page 1

Reference: Vena Calcs - 9 -
Troubleshooting
About this series
This series is about how to use  Vena Calculation Scr ipts. Vena Calculations Scripts (or  Vena Calcs ),
is a scripting language designed for V ena data models. V ena Calcs provides a powerful and flexible
way to run calculations and simulations for business rules at the database level for all dimensions
and members.
We've broken down V ena Calcs into nine articles, can be read consecutively or browsed as needed.
Part 1: Managing Scripts  
Part 2: Notation and S yntax
Part 3: Data T ypes
Part 4: Operators
Part 5: Functions
Part 6: Conditional S tatements
Part 7: Currency Conversions 
Part 8: Examples
Part 9: Troubleshooting -  you ar e her e.
 
Table of contents
 Calcs T roubleshooting F AQ
Why is my calc not calculating?
Why is my calc slower than usual?
Why is the total number of intersections incorrect?
Vena Support T eam
Updated  6 months ago29/12/2025, 09:01 Reference: Vena Calcs - 9 - Troubleshooting – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360047724411-Reference-Vena-Calcs-9-Troubleshooting 1/4

## Page 2

 
Calcs Troubleshooting FAQ
 
1.) Why is my calc not calculating?
Are the member s new?
Although in scope, any newly added members require a deploy.
 
Is ther e source dat a?
Export the data in the source intersections to see if the cube is actually populated or if the
data has not been saved due to a mapping issue on the template.
Use the drill calc feature.
 
Is it an Allocation calc?
If the first source of the calc is not populated, the calc will not recalculate even if the second
source has changed.
                 Eg. A x B = T arget, 
                 5 x 10 = 50
                 If A or B change, then target will be recalculated.
 
               If Blank x 10 = 0
               Any change to 10 (B) will not trigger recalculation (T arget).
               Any change to Blank (A) will trigger a recalculation (T arget).
 
              If 5 x Blank = 0
              Any change to 5 (A) will trigger a recalculation (T arget).
             Any change to Blank(B) will trigger a recalculation (T arget).
Is it a R ead calc?
A Read Calc will not show results if the server property below has not been set to
True: EnableR eadCalcsSSSEmptyT argets
Have you overwritten calc t arget dat a?29/12/2025, 09:01 Reference: Vena Calcs - 9 - Troubleshooting – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360047724411-Reference-Vena-Calcs-9-Troubleshooting 2/4

## Page 3

Drill saves on the answer that you are expecting. Do past saves include a non-calc template or
ETL saves?
If the answer is yes to either, consider excluding the members from the calc’s target scope. If
logic requires an override: 
Templat e save - use an over-ride member instead to separate the two data paths.
ETL - Use an over-ride member to load data into a separate member and map this
member in the template as an override.
 
 2.) Why is my calc slow er than usual?
Have you added a signi ficant amount o f member s? 
Adding members adds to the sparsity of the cube and adds to the number of intersections
that require scanning. The higher the number of dimensions, the larger the stress on the calc.
Refer to this article for how to optimize your calc.
 
Are you having t o deplo y a calc o ften? 
Please reach out to our support or services team for more calc optimization tips.
 
3.) Why is the t otal number o f intersections incorr ect?
Have you ac cident ally wr itten to the calc p arent?
Check the calc revisions to see if there are parent members in the target scope. This could
happen for a couple of reasons: 
 1. The calc may have been a read calc to the parent that has accidentally been saved
without the .R ead appended to the calc. 
 2. The calc was saved and deployed with an iDescendents,  iChildren or without
.Leaves() notation.
To remedy, you may undeploy the calc. Please note if there are any intersections overwriting
calc targets, undeploying will remove those values.  If you ar e unsur e, please r each out t o
suppor t befor e undeploying.
To verify whether it's safe to undeploy:
Drill into the calculated intersection.
Review the save history.
Confirm that all writes are labeled as calc or calc deploy.
If any save is labeled differently (e.g., a manual data entry), undeploying will remove that
value.
 29/12/2025, 09:01 Reference: Vena Calcs - 9 - Troubleshooting – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360047724411-Reference-Vena-Calcs-9-Troubleshooting 3/4

## Page 4

Was this ar ticle help ful?
 
1 out of 1 found this helpful
Related articles
Reference: V ena Calcs - 2 - Notation and S yntax
Reference: V ena Calcs - 1 - Managing Scripts
Reference: V ena Calcs - 8 - Examples
Troubleshoot: Calc T arget Contains Data Even Though It Shouldn’t
Reference: Writing Expressions (MQL & HQL)
Recently viewed articles
Reference: V ena Calcs - 8 - Examples
Reference: V ena Calcs - 7 - Currency Conversions
Reference: V ena Calcs - 6 - Conditional S tatements
Reference: V ena Calcs - 5 - Functions
Reference: V ena Calcs - 4 - Operators29/12/2025, 09:01 Reference: Vena Calcs - 9 - Troubleshooting – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360047724411-Reference-Vena-Calcs-9-Troubleshooting 4/4
