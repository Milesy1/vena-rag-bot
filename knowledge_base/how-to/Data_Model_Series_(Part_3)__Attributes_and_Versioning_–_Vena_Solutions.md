# How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions

How-To: Data Model Series (Part 3):
Attributes and Versioning
 
About this series
This series is all about  how t o build and use Data Models . You are in  Part 3, which provides step-by-step
instructions on how to add and manage attributes and V ersioning in a Data Model.
This series was designed to be read in order. If you don't have any previous experience with the Data Model
tool, we recommend that you follow this approach, starting with P art 1. But if you are already familiar with
Vena Data Models and are just looking for a refresher, you can also feel free to dip in anywhere within this
series.
Part 1:  Building a Data Model
Part 2: Hierarchies and R oll-ups
Part 3:  Attributes and V ersioning -  you ar e her e
Part 4:  ETL T ool
 
Before you begin
To follow the instructions in this article, you will need at least  Modeler  access. If Data P ermissions are set up
in your environment, you will also need the appropriate permissions for the data that you are working with.
 
Table of contents
Attributes overview
Attributes
Attribute tools
Vena Support T eam
Updated  5 months ago26/12/2025, 15:44 How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039572432-How-To-Data-Model-Series-Part-3-Attributes-and-Versioning 1/13

How T o 
Create an attribute
Delete an attribute
Edit an attribute name
Attach a dimension member to  an attribute
Remove a dimension member from an attribute
Versioning overview
How to
Version data
Background processing
Related topics 
Attributes overview
Attributes
Data model members, including bottom-level and parent members, can be labeled with Attributes.
Attributes group members with shared properties, even if they are in different parts of the hierarchy. For
example, office supplies like pens and markers may share a color attribute, such as blue.
Using attributes allows for the easy retrieval of members with specific characteristics, regardless of their
location within the hierarchy.
In Vena templates, attributes can be used with the Expression Editor to dynamically map members based on
selected page options. For instance, choosing a page option can filter table rows to show only members with
the corresponding attribute.
The following is an example of tagging members with attributes:
As an example, V ena can produce a Dynamic Range based on any of the attributes.26/12/2025, 15:44 How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039572432-How-To-Data-Model-Series-Part-3-Attributes-and-Versioning 2/13

‘silver’ will produce the list of Members: Y aris, Corolla, and Odyssey
'silver’ UNION ‘CD’ will produce a list of Members: Y aris, Accent, Corolla, Odyssey
Attribute tools
A Modeler can leverage the Attributes functionality to tag Dimension Members with specific attribute names.
For example, a department Dimension Member can be tagged with a location attribute, such as London.
A Modeler tab The area of the application where elements such as data models,
integrations and the ETL tool reside.
B Data Modeler page This page used to create and manage data models, attributes and
versioning.
C Members page The Members page is how you access, create and manage your
dimensions and members.
D Choose Data Model Select a data model from the available list.
E Dimensions View, edit or delete dimensions.
F Manage Lists existing attributes, as well as the options to create or delete
attributes.  Note: In Standard Models, you will see a Manage drop-down
menu. Under the drop-down menu, you can manage your attributes
and range rules.  Visit this article for more information on range rules. 
G Attached Members Displays current attributes assigned to members.
 
How to 
Create an attribute26/12/2025, 15:44 How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039572432-How-To-Data-Model-Series-Part-3-Attributes-and-Versioning 3/13

1. Navigate to the  Modeler  tab.
2. Navigate to the appropriate  data model .
3. Locate the dimension member you want to add an attribute to.
4. Right-click on the dimension member and select  Edit from the menu.
5. Select  + Add A ttribute. A drawer opens with a list of existing attributes.
6. Select  + Add A ttribute.
7. Enter an attribute name.
8. Select  + Add A ttribute to save the new attribute.
9. Select  Done  to close the drawer.
 
Delet e an attr ibute26/12/2025, 15:44 How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039572432-How-To-Data-Model-Series-Part-3-Attributes-and-Versioning 4/13

1. Navigate to the  Modeler  tab.
2. Navigate to the appropriate  data model .
3. Select  Manage A ttributes. This opens the attributes drawer.
4. Hover over the attribute you want to delete and select the  
  (delet e) icon.
5. Select  Yes, Delet e Attribute in the pop-up confirmation.
 
Edit an attr ibute name
1. Navigate to the  Modeler  tab.
2. Navigate to the appropriate  data model .
3. Select  Manage A ttributes. This opens the attributes drawer.
Note
If you are using a S tandard Model, select  Manage > A ttributes. 26/12/2025, 15:44 How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039572432-How-To-Data-Model-Series-Part-3-Attributes-and-Versioning 5/13

4. Hover over the attribute you want to edit and select the  
  (pencil ) icon.
5. Rename your attribute.
6. Select  Updat e to finalize the changes. 
7. Select  Done  to close the drawer.
 
Attach a dimension member t o an attr ibute
1. Navigate to the  Modeler  tab.
2. Navigate to the appropriate  data model .26/12/2025, 15:44 How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039572432-How-To-Data-Model-Series-Part-3-Attributes-and-Versioning 6/13

3. Locate the dimension member you want to add an attribute to.
4. Right-click on the dimension member and select  Edit from the menu.
5. Select the check-box next to each attribute in the drop-down menu that you want to attach to the
dimension member.
6. Select  + Updat e to save your changes.
 
Remov e a dimension member fr om an attr ibute
1. Navigate to the  Modeler  tab.
2. Navigate to the appropriate  data model .26/12/2025, 15:44 How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039572432-How-To-Data-Model-Series-Part-3-Attributes-and-Versioning 7/13

3. Locate the dimension member you want to add an attribute to.
4. Right-click on the dimension member and select  Edit from the menu.
5. Uncheck the check-box next to each attribute in the drop-down menu that you want to remove from the
dimension member.
6. Select  + Updat e to save your changes.
 
 Versioning overview
Versioning allows Modelers to bulk copy data from one group of intersections and write them to another
group of intersections within the same data model. The desired data set can be isolated by adding
Dimension Members in the P age(s) box. The P age(s) box acts as a list of filters for identifying the data set to
copy. For example, a Modeler may want all collected "Plan" data to become the pre-populated "Forecast"
data for a particular year.26/12/2025, 15:44 How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039572432-How-To-Data-Model-Series-Part-3-Attributes-and-Versioning 8/13

 
A Versioning Displays utilities used to bulk copy data between dimension members.
B Dimension Members Navigate and select dimension member.
C Saved Configurations Existing versioning configurations that you can run and edit.
D Configuration Name Choose a name for your versioning configuration.
E Filter Dimensions by
MembersUse the  Filter section to narrow down what data you want to copy, i.e.,
limit copying to data involving your selected members.
F Copy From Copy from dimension member.
G Copy T o Copy to dimension member.
H Copy Line Items Choose whether line items are copied; and if so, in which format.
I Version P arent Members Choose whether parent members will be included or not when defining
what to copy.
J Clear Destination
Intersections Before CopyIf selected, V ena will clear out all values in the destination (“Copy T o”)
intersections, then copy over the values from the source (“Copy From”).26/12/2025, 15:44 How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039572432-How-To-Data-Model-Series-Part-3-Attributes-and-Versioning 9/13

K Run Calcs If you have any V ena Calcs set up that include the destination intersections
in their scope, this option allows you to specify whether or not those calcs
are executed when the data copy is performed.
L Save Save your versioning configuration.
M Run Execute copy based on chosen parameters.
 
Learn more about V ersioning in Modeler.
 
How to
Version data
1. Log in to V ena and navigate to the  Modeler  tab. 
2. Select  Data Modeler .
3. Select  Versioning  from the sidebar tab.
4. Select the appropriate data model from the data model drop-down list at the top of the page.
5. Input a name for your V ersioning Configuration.
26/12/2025, 15:44 How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039572432-How-To-Data-Model-Series-Part-3-Attributes-and-Versioning 10/13

6. Select the dimension that you want to copy.
7. Choose a member that describes the type of intersections you would like to bulk copy, then hover over
that member row. Three icons should appear:
Filter Dimension by Members
Copy From
Copy T o
Select the  
  (Filter Dimension by Member s) button to add your member to the  Filter Dimension b y
Member s section under  Versioning C onfiguration .
8. Use the  Filter section to narrow down what data you want to copy, i.e., limit copying to data involving
your selected members. For example, if you were copying your budget, you would choose the Budget
member (or similar).
Note
If you choose to run your V ersioning configuration immediately, you do not have to input a
name. However, if you intend to save the configuration for a later date, you must include a
name.
Note
You can add more than one member from unique dimensions. For example, during a cycle
rollover, if you want to version last year's December Actuals to January Budget, Copy from:26/12/2025, 15:44 How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039572432-How-To-Data-Model-Series-Part-3-Attributes-and-Versioning 11/13

9. Next, choose the member that you would like to copy from and select  
  (Copy Fr om) in
the Member  row to add it to the  Copy From section. This is where you select the source of the data to be
copied.
For example, if it were currently 2020 and you wanted to copy your 2020 budget to 2021, you would
choose the Y2020 (or similar) member here. If you leave this section blank, V ena will copy all data for all
dimensions in the data model.
10. Now, choose the member that you would like to copy to and select the  
  (Copy T o) button to add it
to the  Copy To section. This is where you select the destination of the copied data. For example, if you
wanted to copy your 2020 budget to 2021, you would choose the Y2021 (or similar) member here.
11. For basic V ersioning, do not change the options from their default settings (see a screenshot of default
settings, below):
By leaving the default settings unchanged, this means you answer "No" to the following questions:
- Do you want t o clear all destination int ersection v alues befor e copying? No
- Do y ou want t o copy line it ems? No
- Do y ou want t o run calls? No
- Do y ou want t o version p arent member s? No
See Advanced V ersioning Options  below for more information on these functions.2020 (Y ear), Actuals (Scenario), December (Month). Copy to: 2021 (Y ear), Budget (Scenario),
January (Month).
Note
The member you choose for  Copy To and Copy From must be the same dimensions .26/12/2025, 15:44 How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039572432-How-To-Data-Model-Series-Part-3-Attributes-and-Versioning 12/13

12. Select  Run to start the V ersioning job, which will copy the specified values. Y ou can also select  Save to
save your configuration without running it.
13. If you select the  Run button, V ena will create and process a new V ersioning job, and display a message
confirming that your V ersioning job has started.
14. Versioning jobs appear with ETL jobs in the  History section of the Modeler interface, where you can see
their status.
For information on V ersioning in the  Modele r, please refer to  this ar ticle. 
 
Back ground pr ocessing
The V ersioning process may take longer depending on the volume of intersections being copied. During this
time, the data model remains unlocked, allowing users to use V ena regularly while the data copy processes
in the background.
 To view the status of your job:
1. Select  Data Modeler . 
2. Select  History from the sidebar.
3. Your job should be visible on the ETL Jobs page. 
4. In the table, you'll see V ersioning jobs with V ersioning in the  Job Name  column, along with an outline of
the configured job.
5. You can check the job status using the indicators on the right side.
 
Related topics
Check out this article to learn how to dynamically map tables based on attributes.
Check out this article to learn how to  copy data in bulk with V ersioning . 
 
Questions? Comments? R each out to us directly at  support@venasolutions.com .
(Please include the link to the article for reference.)26/12/2025, 15:44 How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039572432-How-To-Data-Model-Series-Part-3-Attributes-and-Versioning 13/13

