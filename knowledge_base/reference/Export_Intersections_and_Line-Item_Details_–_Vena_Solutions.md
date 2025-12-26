# Reference: Export Intersections and Line-Item Details – Vena Solutions

Reference: Export Intersections and
Line-Item Details
 
Overview
When applying a filter against an extract of intersections or line items details, you must use Model
Slice Expression Language syntax.
 
On the ETL Command Line T ool, you can leverage the Intersections and Line-Item Detail export by
choosing to use different filter query options.
Vena Support T eam
Updated  4 months ago26/12/2025, 14:26 Reference: Export Intersections and Line-Item Details – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/204264029-Reference-Export-Intersections-and-Line-Item-Details 1/3

 
Reference Guide
Model Slice Quer y Language
Below is an overview of how to create a Model Slice Query.  For more information about MQL,  visit
this article .
Here is an example expression from that language:
dimension('Time': children('Q1'))  
dimension('Department': children('Software Development'))
Syntax for matting
The query consists of a list of 'dimension(...) expressions separated by whitespace.  There should be
one for each dimension in the model.  This example would apply to a model having two
dimensions: 'Time' and 'Department'.
The right-hand part of the dimension expression describes what members to include for that
dimension. Thus, the example expression we looked at previously, selects all children of 'Q1' for the
'Time' dimension and all children of 'Software development' for the 'Department' dimension:
Children
IChildren
Descendants
IDescendants
BottomLevel
Ancestors
IAncestors
Parents
Ascendants
These can be combined with the following set operators:26/12/2025, 14:26 Reference: Export Intersections and Line-Item Details – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/204264029-Reference-Export-Intersections-and-Line-Item-Details 2/3

Union
Intersection
Subtract
Not
Building on our earlier example, we could use the following expressions:
dimension('Time': union( children('Q1') children(Q2)) )
dimension('Department': not( children('Software Development')) )
You can also list members one by one like this:
 dimension('Time': union('Q1' 'Q2') )
Line-It em Details
For Line-Item Detail, you can filter on the Label and/or ID:
label(name('My Label'))
label(ETLId(#1234567))26/12/2025, 14:26 Reference: Export Intersections and Line-Item Details – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/204264029-Reference-Export-Intersections-and-Line-Item-Details 3/3

