# How-To: Data Model Series (Part 1): Creating a Data Model – Vena Solutions

How-To: Data Model Series (Part 1):
Creating a Data Model
  
About this series
This series is all about  how t o create and use Data Models . You are in  Part 1, which provides
step-by-step instructions on how to create and manage a data model.
This series was designed to be read in order. If you don't have any previous experience with the
data model tool, we recommend that you follow this approach, starting with P art 1. But if you are
already familiar with V ena data models and are just looking for a refresher, you can also feel free to
dip in anywhere within this series.
Part 1: Creating a Data Model -  you ar e her e
Part 2: Hierarchies and R oll-ups
Part 3:   Attributes and V ersioning
Part 4:  ETL T ool
 
What is a Data Model?
A data model is a multidimensional database that stores both numeric and narrative data. It can be
built using multiple dimensions, each with many members. An intersection of members from each
dimension comprises an individual data point.
OLAP cube example:
Laura Harris
Updated  7 months ago26/12/2025, 15:43 How-To: Data Model Series (Part 1): Creating a Data Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039508511-How-To-Data-Model-Series-Part-1-Creating-a-Data-Model 1/11

 
The dat a point in the t op-right c ell can be def ined as the v alue for the t otal inc ome, in Quar ter 4, for
the Litigation Dep artment. Each piec e of data is found at the int ersection point o f all Dimensions.
 
Before you begin
 
To follow the instructions in this article, you will need at least  Modeler  access. If Data P ermissions
are set up in your environment, you will also need the appropriate permissions for the data that
you are working with.
 User Permission Requirements
Users are required to possess the following permissions to perform data model-related
tasks such as creating, updating, or deleting dimensional hierarchies and members. The
same permissions functionality can also be applied to processes and specific data sets.
For more information, check out the  Application P ermissions Guide  and the  Data
Permissions Guide .26/12/2025, 15:43 How-To: Data Model Series (Part 1): Creating a Data Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039508511-How-To-Data-Model-Series-Part-1-Creating-a-Data-Model 2/11

 
Table of contents
How to
Create a Data Model
Rename a Data Model 
Attach a Data Model to a Process
Export a Data Model
Clone a Data Model
Delete a Data Model
Notes & Limitations
Best Practices
Related T opics
 
The V ena Admin  is responsible for creating/assigning all of the above permissions.
Contents within a model include:
Dimensions of a model
Members of a dimension
Contents within a process include:
Tasks
Activities
Review T asks
Task Details
Approve/R eject capabilities, etc.26/12/2025, 15:43 How-To: Data Model Series (Part 1): Creating a Data Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039508511-How-To-Data-Model-Series-Part-1-Creating-a-Data-Model 3/11

 
 
How to 
 
Create a Data Model
1. 
Navigate to the  Modeler  tab. 
2. 
Select the Data Modeler  sidebar.  
3. 
Select + Add New Model . 
4. 
The Add Data Model drawer opens on the right side of the screen. Name the new data model,  
then select Next: Configure Model Dimensions.  
 
5. 
Configure the dimensions for the new model. Select +Add Dimension to add Standard  
Dimensions or include custom dimensions. When you’re  finished, select Save Model.  
26/12/2025, 15:43 How-To: Data Model Series (Part 1): Creating a Data Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039508511-How-To-Data-Model-Series-Part-1-Creating-a-Data-Model 4/11

 
 
Rename a Data Model
Name changes will impact existing data records but will not impact (break) reports that display the
data from a specific data model. 
1. Navigate to the  Modeler  tab.
2. Select the  Data Modeler  sidebar.
3. Hover over the data model that you want to rename. Select the  Edit (pencil ). 
4. Enter a new name in the text box. 
26/12/2025, 15:43 How-To: Data Model Series (Part 1): Creating a Data Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039508511-How-To-Data-Model-Series-Part-1-Creating-a-Data-Model 5/11

5. Select  + Updat e to save your changes.  
 
Attach a Data Model to a Process
Attaching one or more data models to a process will:
Allow users with different data permissions to access different templates.
Pull data from multiple data models for a specific process.
Users in the Manager role can create templates/reports to write/read from different data models.
 
 
To attach a data model t o a pr ocess:
1. Navigate to the  Manager  tab.
2. Select the  process  you want to attach a data model to from the  Processes table. This opens the
process workflow.
 Note
If you run into an "invalid data model" error message when working with Ad Hoc
reporting, follow the steps below to ensure that your process is attached to the
correct data model.26/12/2025, 15:43 How-To: Data Model Series (Part 1): Creating a Data Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039508511-How-To-Data-Model-Series-Part-1-Creating-a-Data-Model 6/11

3. On the  Designer  page, select the  
  (gear ) icon in the upper right-hand corner.
4. Select  Manage Models  from the drop-down list.
5. Use the  Attach New Model  drop-down to select the data model that you want to attach to the
process.
6. Select  Attach  to complete the action once you've selected the model.
26/12/2025, 15:43 How-To: Data Model Series (Part 1): Creating a Data Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039508511-How-To-Data-Model-Series-Part-1-Creating-a-Data-Model 7/11

 
Export a Data Model
In order to export/migrate data from one environment (tenant) to another in V ena, you have two
options. Y ou can either use the  ETL Expor t functionality or  Tenant Migration . Identifying what you
are trying to accomplish will help you to decide which option to use.
1. Expor t Data Model via E TL Tool
The ETL tool  is Vena's traditional tool for importing and exporting data. With the ETL tool, you
can export data model hierarchies, selected dimensions and intersection data without requiring
the use of a template.  More information about the ETL Export tool, including step-by-step
instructions, can be found here.
Data models:  Model hierarchies and attributes.
✔
Select ed Dimensions:  Isolate specific
dimensions for export. 
✔
Intersection Data
✔
Processes : Process workflows and their
metadata (e.g., task assignments, due dates,
task form assignments, process variables, etc.). 
✘
Integration Components:  Integration setups,
including sources, channels, and destinations.
✘
2. Expor t a data model via T enant Migration
The Tenant Migration  feature allows you to easily maintain a multi-environment system by
duplicating work done in one environment in any of your other environments. This means you
can fully build out a complex process in a development (Sandbox) environment away from live
users,  then move it over to a testing environment where you can safely validate it without
touching production data, and finally deploy it on your production environment when it's
ready.  Read the T enant Migration article for more information and step-by-step instructions. 26/12/2025, 15:43 How-To: Data Model Series (Part 1): Creating a Data Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039508511-How-To-Data-Model-Series-Part-1-Creating-a-Data-Model 8/11

Data models:  Model hierarchies and attributes.
✔
Select ed Dimensions:  Isolate specific
dimensions for export. 
✘
Intersection Data
✘
Processes : Process workflows and their
metadata (e.g., task assignments, due dates,
task form assignments, process variables, etc.). ✔
Integration Components:  Integration setups,
including sources, channels, and destinations.
✔
 
Clone a Data Model
Read this article for full instructions on how to clone a data model. 
 
 
Delete a Data Model
 Note
After you duplicate a cube, the associated processes should also be duplicated. This
allows the user to re-map any existing templates to the new cube without disturbing
existing templates connected to the source cube.
After the processes have been duplicated, the user should disconnect the new cube
from the source processes to prevent any association with the original data model.
The source cube should only be connected to the source processes and the new
cube should only be connected to the new duplicated processes.26/12/2025, 15:43 How-To: Data Model Series (Part 1): Creating a Data Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039508511-How-To-Data-Model-Series-Part-1-Creating-a-Data-Model 9/11

1. Navigate to the  Modeler  tab.
2. Navigate to the  Data Modeler  sidebar.
3. Hover over the data model you want to delete and select the  
  (delet e) icon.
4. A confirmation modal will ask you to confirm the deletion. Select  Yes, Delet e Model  to remove
the data model.
5. The data model will be deleted and removed from the list. Y ou have completed the deletion of
the testing environment from your V ena tenant.
 
Warning
Delete data models with care, as this may cause errors in PivotT ables or formulas that  
reference these tables. PivotT able results can change in unexpected ways after a  
relationship is deleted  or deactivated.
  Caution
Ensure there are no processes attached to the data model. Once a data model is
deleted, it will no longer be accessible and can adversely impact any workflow
processes previously attached to it. Processes can be detached by deselecting
the Attach Pr ocess  button in the Manage Model drawer, accessible via the Manager
tab. Read this article for step-by-step instructions on how to detach a process. 26/12/2025, 15:43 How-To: Data Model Series (Part 1): Creating a Data Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039508511-How-To-Data-Model-Series-Part-1-Creating-a-Data-Model 10/11

 
Notes & Limitations
You can build multiple data models in any V ena application.
Each process may connect to multiple data models.
 
Best Practices
Ensure that each user has the proper access to relevant data models. For example, if a user
doesn't have to provide changes (manual input) to a model, then ensure their Data P ermissions
are set to  Read. 
Make sure that only those individuals who need to make changes (edit, add, remove) are
given  Write permissions. The best practice is to only give  Write access to users who modify data.
This reduces the risk of data corruption and accidental errors.
 
Related Topics
Read about how to clone and view a data model. 
Read about how to export a data model. 
Read about how to create and manage a data model hierarchy using ETL Import. 
Read about how to map from multiple data models to a single template. 
Was this ar ticle help ful?
 26/12/2025, 15:43 How-To: Data Model Series (Part 1): Creating a Data Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039508511-How-To-Data-Model-Series-Part-1-Creating-a-Data-Model 11/11

