# Troubleshooting_ Calc Conversion Not Working or Zero Values Appearing – Vena Solutions

## Page 1

Troubleshooting: Calc Conversion Not
Working or Zero Values Appearing
Issue summary
Values from a Calc are incorrectly showing as zero or the conversion is not working even though the
rate and local value has been loaded into V ena.
 
Suggested solution
1. Check and confirm the rate and local values have been saved or loaded into the cube or data
model. 
2. Select an  intersection . 
3. Select  Drill Sav e on one of the bottom-level intersections where the converted (e.g., USD) value
is expected. 
4. If this intersection is a Calc target, select  Drill Calc .
5. A web browser window will open with details about the calculation. The details will include the
source intersection, target intersection and part of the script that calculates the value for that
intersection.
6. Ensure that all the sources required for the formula or calculation have values and that these
values do not contain commas or double quotes.
7. If it is a currency conversion Calc that uses the formula   r at e*local , ensure that the rate is saved
before any local values are saved in the cube by looking at the  Save Dat e column.
8. If the local value was saved before the rate, then you will have to file-to-cube ETL to load 0 into
the intersections or save 0 from a template and then save the local values again.
Olalekan Adebayo
Updated  2 years ago29/12/2025, 09:01 Troubleshooting: Calc Conversion Not Working or Zero Values Appearing – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14037013905293-Troubleshooting-Calc-Conversion-Not-Working-or-Zero-Values-Appearing 1/3

## Page 2

9. Check if the intersection is blank or if the value being shown is incorrect.
10. If the intersection value is correct but it’s still not working, manually deploy the Calc by opening
the Modeler  tab in vena.io.
11. Select  Scripts. 
12. Select your  calculation.  
13. Select  Deploy .
 
Cause
This issue could occur for a few reasons. Some of the values needed for the calculation are not
present, a new member was recently added, the values are present but are being treated as texts or
local values are saved into the cube before the rate.
 Info
This is especially useful when a dimension member of the intersection was recently
added to the data model. 29/12/2025, 09:01 Troubleshooting: Calc Conversion Not Working or Zero Values Appearing – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14037013905293-Troubleshooting-Calc-Conversion-Not-Working-or-Zero-Values-Appearing 2/3

## Page 3

Keywords
calc, conversion, USD, EUR, script, zero, blank, template, not showing
Was this ar ticle help ful?
 
0 out of 1 found this helpful
Related articles
How-T o: Building a Custom R oll-up Using Calculated Members
Troubleshoot: Calc T arget Contains Data Even Though It Shouldn’t
Recently viewed articles
Troubleshoot: Calc T arget Contains Data Even Though It Shouldn’t
Reference: V ena Calcs - 9 - T roubleshooting
Reference: V ena Calcs - 8 - Examples
Reference: V ena Calcs - 7 - Currency Conversions
Reference: V ena Calcs - 6 - Conditional S tatements29/12/2025, 09:01 Troubleshooting: Calc Conversion Not Working or Zero Values Appearing – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14037013905293-Troubleshooting-Calc-Conversion-Not-Working-or-Zero-Values-Appearing 3/3
