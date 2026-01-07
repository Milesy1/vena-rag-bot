# How-To: Data Model Series (Part 2): Hierarchies and Roll-Ups – Vena Solutions

How-To: Data Model Series (Part 2):
Hierarchies and Roll-Ups
About this series
This series is all about  how t o build and use Data Models . You are in  Part 2, which provides step-by-step
instructions on how to build and manage a Dimension.
This series was designed to be read in order. If you don't have any previous experience with the Data Model
tool, we recommend that you follow this approach, starting with P art 1. But if you are already familiar with V ena
Data Models and are just looking for a refresher, you can also feel free to dip in anywhere within this series.
Part 1: Building a Data Model
Part 2:   Hierarchies and R oll-ups -  you ar e her e
Part 3:   Attributes and V ersioning
Part 4:  ETL T ool
 
Before you begin
To follow the instructions in this article, you will need at least  Modeler  access. If Data P ermissions are set up in
your environment, you will also need the appropriate permissions for the data that you are working with.
 
Table of contents
Overview
Hierarchies and roll-ups
Dimension/Dimension Member tools
How to 
Add a Dimension
Edit a Dimension Name
Delete a Dimension
Create a Dimension Member
Vena Support T eam
Updated  6 months ago26/12/2025, 15:43 How-To: Data Model Series (Part 2): Hierarchies and Roll-Ups – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039163832-How-To-Data-Model-Series-Part-2-Hierarchies-and-Roll-Ups 1/11

Rename a Dimension Member
Add a Dimension Member Alias
Cut/P aste a Dimension Member
Share a Dimension Member
Delete a Dimension Member
 
 
Overview
Hierarchies and Roll-Ups
The dimensions of an OL AP cube are structured into hierarchies. For example, in a database that tracks
information for periods, hierarchies may be broken down into: 
All Period (Complete year)
Halves
Quarters
Months
An example of a hierarchy. (Displaying dimensions and dimension members.) 
A Dimensions Display all dimensions created within a data model.
B Dimension Members Dimension member hierarchy.
C Roll-up Lower-level members (child members) will "roll-up" under this umbrella.26/12/2025, 15:43 How-To: Data Model Series (Part 2): Hierarchies and Roll-Ups – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039163832-How-To-Data-Model-Series-Part-2-Hierarchies-and-Roll-Ups 2/11

D Bottom Level Member Lower-level dimension member which fits under the parent umbrella
dimension members.
 
 
Dimension/Dimension Member tools
Leverage the available tools on the  Member s page to build your hierarchy. 
A Choose Data Model Select the drop-down menu, and then select from the available data models.
B Dimensions A list of dimensions of the selected data model.
C Dimension Member Selected dimension member.
D Operator Aggregation method used for roll-up dimension member:
 (~) No Aggregation
 (+) Add
 (-) Subtract
E Edit Allows you to rename the member, add/edit an alias, add/edit attributes and
add/edit an operator.
F Sibling Member Create a new sibling of the selected member.26/12/2025, 15:43 How-To: Data Model Series (Part 2): Hierarchies and Roll-Ups – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039163832-How-To-Data-Model-Series-Part-2-Hierarchies-and-Roll-Ups 3/11

G Child Member Create a new child (subordinate) member of the selected member.
H Preview Intersections Preview all data intersections for selected member with the option to export
to a CSV file.
I Expand All Display all levels of the hierarchy.
J Cut  Cut the selected member.
K Add Calculated Member Add a calculated member to this dimension member.
Learn more about Calculated Members.
L Sort Children by Name Option to sort children alphabetically by name.
M Sort Children by Alias Option to sort children alphabetically by alias.
N Pin as Default Member Allows you to manually select a specific member as the Default
Member.  Learn more about Default Members.
O Delete Allows you to delete a dimension member.
 
 
How to 
Add a Dimension
1. Navigate to the  Modeler  tab. The  Data Modeler  window should open automatically.26/12/2025, 15:43 How-To: Data Model Series (Part 2): Hierarchies and Roll-Ups – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039163832-How-To-Data-Model-Series-Part-2-Hierarchies-and-Roll-Ups 4/11

2. Select the  data model  that you want to add the dimension to ( Reporting,  in this example).
Or, if you are in the  Member s section, choose your  data model  from the  drop-down menu:
3. Select the  pencil icon  (
 ) at the end of the Dimensions list.
4. Select  + Add Dimension .
5. Enter a name for the new Dimension in the textbox.
6. Select  + Add Dimension  to save the dimension.26/12/2025, 15:43 How-To: Data Model Series (Part 2): Hierarchies and Roll-Ups – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039163832-How-To-Data-Model-Series-Part-2-Hierarchies-and-Roll-Ups 5/11

 
 
Edit a Dimension name
Editing a dimension name after it has been created will impact existing data records but will not impact (break)
reports that display the data from a specific data model.
1. Navigate to the  Modeler  tab.
2. Select the  Data Modeler  sidebar.
3. Select the  
  (pencil ) icon at the end of all the dimension names. This opens the drawer showing existing
dimensions in the model.
4. Hover over the dimension you want to rename and select the  
   (pencil ) icon.
5. Type in the new dimension name and select  + Updat e to save the change.
 
Delet e a Dimension
It is rare that you would need to delete a dimension after setting up a data model. However, in the event that
you have made an error or need to re-order members, then you can delete a dimension by following these
steps.
1. Navigate to the  Modeler  tab.
2. Select the  Data Modeler  sidebar.
3. Select the  
  (pencil ) icon at the end of all the dimension names. This opens the drawer showing existing
dimensions in the model.
4. Hover over the dimension you want to delete and select the  
  (trash ) icon.
Note_Icon_Small.png   Note
Be aware that if you add a new Dimension, any previously mapped templates will have to be
updated to map the new Dimension.26/12/2025, 15:43 How-To: Data Model Series (Part 2): Hierarchies and Roll-Ups – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039163832-How-To-Data-Model-Series-Part-2-Hierarchies-and-Roll-Ups 6/11

5. Select  Yes, Delet e Dimension  in the confirmation pop-up to delete the dimension.
 
 
Create a Member
1. Navigate to the  Modeler  tab.
2. Navigate to the  Data Modeler  page.
3. Navigate to the  Member s sidebar tab.
4. Select the  data model  from the drop-down menu.
5. Select the targeted  dimension .
6. Right-click a  dimension member .
7. Select either  Add Sibling  or Add Child  as your new member.
 
 
Caution_Icon_Small.png   Caution
Be aware that if you delete a dimension, all dependent mappings will lose access to related
members and data.26/12/2025, 15:43 How-To: Data Model Series (Part 2): Hierarchies and Roll-Ups – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039163832-How-To-Data-Model-Series-Part-2-Hierarchies-and-Roll-Ups 7/11

A
 
 
 Available  Dimension
Member s
 
 
 Sibling -   Sibling  members are members on the same hierarchical
level under the same parent member.
Child - A  Child  member is a sub-member (descendant) of a
Parent/Sibling member. 
B  
Alias
 An alternative description used to reference a Dimension Member.
C
 
 Operat or
 
 
 Aggregation method used for Dimension Members.
 (~) No Aggregation
 (+) Add
 (-) Subtract
 
 
Rename a Member
Like dimensions, editing a member name after it has been created will impact existing data records but will not
impact (break) reports that display the data from a specific data model.
1. Locate the member you want to rename from the member list.
2. Hover over the member and select the  
 (pencil ) icon.
3. Rename your member.
4. Select  + Updat e to save the change.
 
Add a Dimension Member Alias
An Alias  is an alternative descriptive handle used to reference the dimension member. An alias can be
referenced when applying data mappings. It is useful as dimension members can have long or complex names,
and aliases provide the ability to use alternate names.
1. Locate the member you want to add an alias for.26/12/2025, 15:43 How-To: Data Model Series (Part 2): Hierarchies and Roll-Ups – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039163832-How-To-Data-Model-Series-Part-2-Hierarchies-and-Roll-Ups 8/11

2. Hover over the member and select the  
 (pencil ) icon.
3. Add a name under the  Alias  textbox.
4. Select  + Updat e to save the change.
 
Cut/Paste a Dimension Member
Re-ordering dimension members often occurs as a result of organizational changes, such as the reduction or
reallocation or cost centers. In this event, easily move a dimension member to a different location by following
these steps.
1. Select the appropriate  data model .
2. Right-click anywhere in line with the  dimension member  you wish to modify.
3. Select  cut.
4. Navigate to the dimension member location you wish to paste.
5. Right-click the dimension and select  Paste.
6. This will deposit the member in the new position in the hierarchy. Select  Cancel  if you no longer wish to
move the member.
 
Shar e a Dimension Member26/12/2025, 15:43 How-To: Data Model Series (Part 2): Hierarchies and Roll-Ups – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039163832-How-To-Data-Model-Series-Part-2-Hierarchies-and-Roll-Ups 9/11

The Shar ed Member s functionality allows Modelers to create alternate hierarchies within a dimension. Shared
members make aggregated reporting of collected data  in a number of ways possible. For example, within the
Period dimension, Month members can be shared to allow for the aggregation of quarter-to-date and year-to-
date values. T o share a dimension, follow these steps:
1. Select the  data model .
2. Select the  dimension  from the  Member Name  list you wish to share.
3. Right-click the dimension member from the  Member Name  list.
4. Select the  Shar e button. A pop-up window notifies you that the member can now be shared.
5. Navigate to, then right-click on the destination umbrella dimension member you wish to share with. Right-
click on the member and select  Complet e Shar e button. Select  Cancel  if you no longer wish to share the
member.
6. The shared member will appear in the hierarchy with a Share symbol next to it.
 
Delete a Dimension Member
In order to preserve historical reporting, any member with data attached to it should not be deleted. Deleting a
member will also delete all associated data. It should be noted that unused members may be excluded from a
report without being deleted.
1. Navigate to the desired data model.
2. Right-click the dimension member from the  Member Name  list that you want to delete.26/12/2025, 15:43 How-To: Data Model Series (Part 2): Hierarchies and Roll-Ups – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039163832-How-To-Data-Model-Series-Part-2-Hierarchies-and-Roll-Ups 10/11

3. Select  Delet e.
4. If you are sure you want to delete the member, select  Delet e in the confirmation pop-up window.
 
Related Topics
To learn how to  clone and view a data model:  How-T o: Creating a T esting Environment by Cloning a Data
Model (Clone & R emap).
To learn about how to  expor t a subset o f a data model:  How-T o: Exporting Subset of Data From Y our Data
Model or Cube.
To learn how to  create and manage a data model hierar chy using E TL Impor t: How-T o: Create and
Manage a Data Model Hierarchy Using ETL Import.
To learn how to map from  multiple data models t o a single t emplat e: How-T o: Mapping Data From
Multiple Data Models on a Single T emplate.
To learn about how to  link dimensions:   Explainer: What Are Linked Dimensions?
To learn about how to create a  custom r oll-up without cr eating alt ernate hierar chies:  How-T o: Building a
Custom R oll-up Using Calculated Members.26/12/2025, 15:43 How-To: Data Model Series (Part 2): Hierarchies and Roll-Ups – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039163832-How-To-Data-Model-Series-Part-2-Hierarchies-and-Roll-Ups 11/11

