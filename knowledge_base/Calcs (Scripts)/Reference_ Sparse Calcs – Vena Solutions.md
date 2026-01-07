# Reference_ Sparse Calcs – Vena Solutions

## Page 1

Reference: Sparse Calcs
Sparse mode  optimizes Calcs to compute to targets when there is existing data. 
 
Overview
Adding .sparse to a calc name enables sparse mode. In this mode, V ena updates only the existing
target intersections when a source intersection value changes (and if that source intersection has a
one-to-many relationship with the targets), avoiding new computations for other intersections.
 
 
Reference Guide
Cardinality
One-to-one
A source has a one-to-one relationship when a change in the source will only affect one
intersection in the target slice. Consider the following example of currency conversion:
Scope {[Accounts].Leaves(), [USD]}
    @this = [Local] * ([No_Account], [Rate])
End
 
This calculation iterates through all leaves of the [Accounts] member, finding the data at each
account in the local value and multiplying it by the rate stored at ([No_Account], [Rate]). For
example, a change in ([Account 1], [Local]) affects only ([Account 1], [USD]).
One-to-many
Jun Barrozo
Updated  6 months ago29/12/2025, 08:08 Reference: Sparse Calcs – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206313036-Reference-Sparse-Calcs 1/5

## Page 2

In the example above, the value at  ([No_Account], [Rate])  has a one-to-many relationship. Changes
to this value will result in changes to all of the leaf accounts in the currency USD.
 
Sparse Execution
If the calculation above was set in sparse mode, a change in the value at  ([No_Account],
[Rate])  would only recalculate any existing values in the slice  ([Accounts].Leaves(), [USD]) . For
example, suppose we had the following data before writing the calc:
  Local USD
Account 1 100  
Account 2 150  
Account 3 120  
Account 4    
Account 5    
 
  USD
No_Account 1.5
Then, after we write the calc and deploy, we see the following data:
  Local USD
Account 1 100 150
Account 2 150 225
Account 3 120 18029/12/2025, 08:08 Reference: Sparse Calcs – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206313036-Reference-Sparse-Calcs 2/5

## Page 3

Account 4    
Account 5    
Then we disable the calc and then save some more data on the sheet.
  Local USD
Account 1 100 150
Account 2 150 225
Account 3 120 180
Account 4 100  
Account 5 200  
Finally, we enable the calc and then change the rate. W e would then see the following data:
  USD
No_Account 2.0
 
  Local USD
Account 1 100 200
Account 2 150 300
Account 3 120 24029/12/2025, 08:08 Reference: Sparse Calcs – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206313036-Reference-Sparse-Calcs 3/5

## Page 4

Account 4 100  
Account 5 200  
Notice that the values at  ([Account 4], [USD])  and ([Account 5], [USD])  have not been calculated.
This is because the source that changed (the rate) has a one-to-many relationship, so V ena only
computes updates to existing values in the USD column. The solution, in this case, is to not disable
the calc when adding data -- if the calc was not disabled, the values would appear when we add the
new data:
  Local USD
Account 1 100 150
Account 2 150 225
Account 3 120 180
Account 4 100 150
Account 5 200 300
And then when we changed the rate, we'd see the correct new values get calculated:
  Local USD
Account 1 100 200
Account 2 150 300
Account 3 120 240
Account 4 100 200
Account 5 200 40029/12/2025, 08:08 Reference: Sparse Calcs – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206313036-Reference-Sparse-Calcs 4/5

## Page 5

Alternatively, if data had been saved when the calculation was disabled, you could simply  deploy
the calculation, which would detect the new sources and calculate new targets for them.
 
 
 
 
Was this ar ticle help ful?
 
2 out of 3 found this helpfulNote
Autosparse is triggered when more than 50,000 intersections are updated. When this
occurs, the source intersection doesn’t change. T o turn off Autosparse, enter   no
aut osp ar s e at the top of the calc.29/12/2025, 08:08 Reference: Sparse Calcs – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206313036-Reference-Sparse-Calcs 5/5
