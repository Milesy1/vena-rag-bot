# Reference_ Vena Calcs - 1 - Managing Scripts – Vena Solutions

## Page 1

Reference: Vena Calcs - 1 - Managing
Scripts
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
 
Part 1: Managing Scripts -  You ar e her e
Part 2: Notation and S yntax
Part 3: Data T ypes
Part 4: Operators
Part 5: Functions
Part 6: Conditional S tatements
Part 7: Currency Conversions
Part 8: Examples
Vena Support T eam
Updated  1 month ago29/12/2025, 08:10 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 1/17

## Page 2

Part 9: Troubleshooting
 
Video
Check out a video of this article's content. 
 
 
Table of contents
Calc Scr ipts Ov erview
Calc Script Editor
How T o
Create a Calc Script P age
Managing a Calc Scr ipt P age
Script Writing
Revisions (Script History)
Deploy and Undeploy
Calculation Graph
Calculation Profiler
Script Details
 
Calc Scripts Overview
Vena Calc Scripts are data-model-specific and only work within the model they are written in. Calc
Scripts can be created by adding script pages under the desired data model.
 
Calc Scr ipt Edit or
Vena Calc Scripts are input and managed on the front-end Script Editor. T o use the editor effectively,
it is important to familiarize yourself with the functionality.  
 29/12/2025, 08:10 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 2/17

## Page 3

  Featur e Descr iption
A Search Locate specific Calc Scripts using the  Search bar.
B Rename Choose a name for your calc.
C Delete Delete your calc.
Caution:  Deleting a calc erases all values associated with it, impacting
all templates and reports linked to that script.
D Revisions Calculation Hist ory View er: Compares the script’s current version
with a past one.  Learn mor e about calc r evisions.
E  Save Select  Save any time you make changes to a Calc Script.
F
  "Disable/ "Enable
 Enabling a Calc Script allows it to run whenever its source intersection
data changes.
Disabling a Calc Script  effectively turns it “off” and it will not run.29/12/2025, 08:10 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 3/17

## Page 4

G
 Deploy/  
Undeploy 
 Deploying a calc means running the script with all existing data
currently saved in the data model.
Undeploying a calc means erasing all values saved by this calc . Learn
more about Deploy/Undeploy and how it imp acts calc scr ipts.
H  View Calc Profiler Provides an in-depth overview of the execution of a calculation or set
of calculations.  Learn mor e about the Calc Pr ofiler.
I
 Calculation
Graph
 Shows a view of the dependencies between different calculations,
allowing you to see which calculations depend on which other
calculations.  Learn mor e about the Calc Graph.
J 
 Add Calc Script
Page
 Creates a new Calc Script page for the data model. Each page is
managed through the buttons at the top of the list of data models.
Depending on the current state of the script, the exact list of options
available may vary (e.g., Deploy/Undeploy, Enable/Disable).
K Script Detail Shows the number of total potential intersections in the sources stated
by each scope and the potential resulting number of target
intersections.
 
How To
Create a Calc Scr ipt P age
1. Navigate to the  Modeler  tab.
2. Select  Scripts in the sidebar to access your scripts.
3. Select the  folder  for the data model you want to create a calc for. Each folder represents a data
model and can be expanded to show all calcs associated with it. 29/12/2025, 08:10 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 4/17

## Page 5

4. Select  + to create a new Calcs Script P age.  
5. Enter a name for your new Calcs Script and select  Save. 
 
6. Once you have created your page you can start on your Calcs Script.29/12/2025, 08:10 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 5/17

## Page 6

 
Managing a Calc Script Page
Script Wr iting
Select your V ena Calc Script to view its contents. By default, the script is enabled and comes into
effect as soon as you can save it successfully. V ena does not save the script if there are errors.
Verification is applied to the syntax whenever a script is saved. If there are errors upon saving, a
debug window appears below the script window.
An asterisk (*) after the name of the script signifies it has unsaved changes. A green icon means that
the script is currently enabled. Greyed out names means it is  not enabled. 
 
 
Revisions (Scr ipt Hist ory)
Select  Revisions  to access a script’s Calculation History and compare the current version of a script
with a past version of the same script.29/12/2025, 08:10 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 6/17

## Page 7

In the view (below), the current version of the script is shown in the right pane, and an older version
is shown to the left. Above each pane is the name of that version of the script and its
enabled/disabled state. 
Select the drop-down menu in the left pane to choose from all previous versions of the calc. These
versions are listed by date and time and provide a short summary of the differences between that
version and the previous version.
 
Deploy and Undeploy
Deploying a calc means to run the script with all existing data currently saved in the data model.29/12/2025, 08:10 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 7/17

## Page 8

1. Select  Deploy . A confirmation message appears, prompting you to select  Deploy  to continue.
2. In cases with large amounts of data, this process could take several hours to complete. Monitor
the status of the deploy in the  History tab of the sidebar menu.  
 
Undeploying a calc means erasing all values that were saved by this calc. This is particularly helpful
for debugging. For example, if a user inputs data in USD, the calc would produce the following data
for CAD: 
Jan Feb Mar
USD 100 120 11029/12/2025, 08:10 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 8/17

## Page 9

CAD 105 127 116
 
If a user then saved the value  140 to the intersection at Feb>CAD, then selected  Undeploy , the
sheet would display:
 
 Jan Feb Mar
USD 100 120 110
CAD 140
 
Calculation Graph
The Calculation Graph shows a view of the dependencies between different calculations (which
calculations depend on which other calculations).
 
Viewing the Graph  
View the Calculation Graph by selecting the  eye icon  (
 ) in the Data Model row.
When the graph is built, V ena reads each calculation and generates a node for every bottom-level
scope. Each node is labeled with the calculation name and a number for the scope it came from. 
The first bottom-level scope in a calculation begins with the number 0 and each successive scope
receives the next number. If a node’s name is too long, it’s shortened with an ellipsis (...). T o view the
full name, move your mouse over that node. 
To view the full names of all nodes at the same time, select  Show full names o f all calculations  on
the bottom left of the window.29/12/2025, 08:10 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 9/17

## Page 10

Arrows in the graph point from sources to targets. In the example below, the node  FX Convers... uses
a value produced by the node  Forecast [....] : 
 
Hovering over a node highlights its connecting arrow and provides more information. 
Incoming arrows are green and outgoing arrows are blue. The counters in the bottom left list the
number of nodes acting as sources (incoming) and as targets (outgoing) of the current node. 29/12/2025, 08:10 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 10/17

## Page 11

Example 1 below highlights a node with four outgoing targets:  
Example 2 below highlights a node with four incoming sources:
 
Manipulating the Graph
Selecting a node hides all other nodes not connected to it. Select  Back T o Previous View  to bring
back the other nodes. 29/12/2025, 08:10 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 11/17

## Page 12

Select and drag a node allows to reposition it in the view.
Use the mouse scroll wheel to zoom in and out.
 
Calculation Pr ofiler
The Calculation Profiler provides an in-depth overview of the execution of a calculation or set of
calculations.
To open the profiler, select the  clock icon (
 ) next to a data model.
 29/12/2025, 08:10 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 12/17

## Page 13

A Date &
TimeDay and time of the current data set. Select this drop-down for data from
the 10 most recent deploys or ETL data loads in real time.  
B Node List A list of all the nodes being calculated. Each can be expanded to view a
listing of all steps involved in the calculation.
C Calculation
GraphA view of how the Calculation Graph looked at the time of the deploy. If the
deploy is currently in progress, the completed nodes will be colored green.
Nodes currently being calculated will be colored blue and nodes to be
calculated will be colored grey. If the deploy has been completed, all nodes
will be colored green.  
 29/12/2025, 08:10 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 13/17

## Page 14

Below is a sample calculation expanded in Profiler, from a data model containing almost 37,000
intersections to be sources for this calculation. For large amounts like this, V ena creates batches of
up to 1000 source intersections, resulting in 37 batches in this case. 
 
This calculation took the following steps:
1. Fetched the intersections to be used for this batch.
2. Built the graph specific to those intersections.
3. Found the groups of interdependent intersections in the graph.
4. Loaded any dependencies.
1. Cached dependencies are values either supplied in the source intersections or calculated by a
previous step.
2. Missing dependencies are new values that need to be fetched from the Cube, if, for example,
the calculation has other sources from the cube which were not part of the current batch of
1000.
5. Calculated each group
1. In this case, for 1000 source intersections, there were 1000 independent groups, meaning that
there were no interdependent intersections in the batch.29/12/2025, 08:10 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 14/17

## Page 15

6. Stored the results in the Cube.
1. In this case, from 1000 source intersections, V ena produced 1000 results, meaning that each
of those source intersections directly produced a result. If, for example, one of the source
intersections was an FX rate, we might see many more than 1000 results produced.
 
In the right column, the profiler lists the time, in milliseconds, that each step took. In this example,
calculation A took just over 44 seconds, with Batch #1 taking 2.333 seconds and Batch #2 taking
1.488 seconds.
 
Note
If a calculation has multiple sources from the cube and only one of them is supplied in a batch, then
in Step #4, the rest of the intersections will be fetched for that specific calculation.
Later in the deploy, those intersections will be part of some other batch. In that case, V ena knows
that they have already been used to produce a value and won’t recalculate it. In this case, less than
1000 results may be produced. 
 
Script Details
Script Details show the number of total potential intersections in the sources stated by each scope
and the potential resulting number of target intersections. They can also be used to calculate the
potential fan-in/out ratio (the number of potential sources to the number of potential targets).
Select the  green graph icon (
 ) next to the script to open Script Details. 29/12/2025, 08:10 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 15/17

## Page 16

 
Calculation name The first scope of the calc that is highlighted.
# of sour ce int ersections The number of potential source intersections in scope or subscope.
# of target int ersections The number of potential target intersections in scope or subscope.29/12/2025, 08:10 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 16/17

## Page 17

 
 
Was this ar ticle help ful?
 
4 out of 4 found this helpful
Related articles
Reference: V ena Calcs - 2 - Notation and S yntax
Reference: V ena Calcs - 5 - Functions
Reference: V ena Calcs - 4 - Operators
Reference: V ena Calcs - 6 - Conditional S tatements
Explainer: T arget Member Attribute Calc T rigger
Recently viewed articles
Reference: Sparse Calcs
How-T o: Using V ena’s Foreign Exchange (FX) Conversion Function
Explainer: T arget Member Attribute Calc T rigger
Reference: V ena’s Foreign Exchange (FX) Conversion Function F AQs
Troubleshooting: Encountered More Than the Limit of 1000 Unmapped Members29/12/2025, 08:10 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 17/17
