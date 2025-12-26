# Reference: Creating a Calculated Number That Excludes a Member – Vena Solutions

Reference: Creating a Calculated
Number That Excludes a Member
Use a  Calculated Number  to intentionally exclude a member
from a roll-up or calculation.
Overview
In certain instances, you may want to intentionally exclude a member from a rollup. Y ou can do this
using Calculated Numbers. This reference article explains how to write an expression for
a Calculat ed Number  depending on the member you want excluded from the calculation.
Reference Guide
In the example above, let's say you want to create a rollup of Operation Divisions excluding Division
D. To go about this, the expression will be:
SUBTRACT(CHILDREN(' Oper ating Divisions '),'Division D' )
If you want to exclude Dept 401, which is a bottom level child of Division D, then the expression will
be:
SUBTRACT(BO TTOMLEVEL(' Oper ating Divisions '),'Dept 401' )
Vena Support T eam
Updated  1 year ago26/12/2025, 14:23 Reference: Creating a Calculated Number That Excludes a Member – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115003655403-Reference-Creating-a-Calculated-Number-That-Excludes-a-Member 1/2

 
Summary:
If the excluded member is an immediate child:
SUBTRACT(CHILDREN(' Target rollup member '),'Child member t o be ex cluded ')
If the excluded member is not an immediate child:
SUBTRACT(BO TTOMLEVEL(' Target rollup member '),'Bottom lev el child member t o be ex cluded ')
Was this ar ticle help ful?
 
6 out of 10 found this helpful
Related articles
Reference: Writing Expressions (MQL & HQL)
How-T o: Building a Custom R oll-up Using Calculated Members
How-T o: Using Drill Functions (Drill Down, Drill Save and Drill T ransactions)
How-T o: Enable & Add a MDR Insert R ow to a T emplate
How-T o: Importing Data to V ena with Microsoft P ower Automate Connector
Recently viewed articles
Explainer: What Are Unmapped Dimensions and Default Members?
Explainer: What Are Linked Dimensions?
How-T o: Copy Data in Bulk and Save V ersioning Configurations in Modeler
Explainer: What’s the Difference Between an Alternate Hierarchy and Calculated Members?
How-T o: Search for Members, Attributes, Aliases and GL Codes With the Modeler Search26/12/2025, 14:23 Reference: Creating a Calculated Number That Excludes a Member – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115003655403-Reference-Creating-a-Calculated-Number-That-Excludes-a-Member 2/2

