# How-To: Creating a Testing Environment by Cloning a Data Model (Clone & Remap) – Vena Solutions

How-To: Creating a Testing
Environment by Cloning a Data
Model (Clone & Remap)
Why use this featur e?
When your V ena environment is set up and in production, performing testing on your templates
can be risky. If you make a mistake, it can have a major impact on your V ena processes and
everyone who is involved with them.
This is where creating a testing environment can be very helpful. Y ou can experiment however you
like within the testing environment, without the risk of affecting your live processes. A testing
environment is most useful when it closely mimics your production environment, so using
the Clone  and Remap  features is the most efficient way of creating a testing environment that is
functionally identical to the live environment.
In this article, you will learn how to set up an environment to safely perform testing and additional
data modeling by cloning your data model and processes and remapping associated templates.
 
 
Befor e you begin
To follow the instructions in this article, you will need  Admin , Manager  and Modeler  access. If
Data P ermissions are set up in your environment, you will also need the appropriate permissions for
the data that you are working with.
 
 
Table o f cont ents
Overview
How to
Vena Support T eam
Updated  4 months ago26/12/2025, 15:46 How-To: Creating a Testing Environment by Cloning a Data Model (Clone & Remap) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206143166-How-To-Creating-a-Testing-Environment-by-Cloning-a-Data-Model-Clone-Remap 1/10

Clone the data model
Copy the process
Detach the process
Remap the templates
Set up data permissions
Finishing up
Notes & limitations
 
 
Overview
The entire process consists of five steps:
1. Clone the data model:  This creates a duplicate of the production database and member
hierarchy, which will form the basis of your testing environment.
2. Copy the pr ocess:  The data model you cloned in the first step will typically have a process
associated with it. This creates a duplicate of that process.
3. Detach the pr ocesses:  When the original data model and process have been copied, both the
original and copied processes will be attached to each of the original and cloned data models.
Since you want only the copied process to be should be separate, this step ensures that only the
appropriate process is attached to each data model.
4. Remap the t emplat es in the copied pr ocess:  The templates belonging to the copied process
will still be mapped to the original data model. This remaps them to the cloned data model.
5. Set up Data P ermissions:  Any permissions set up on the original data model will not be
inherited by the cloned data model. This recreates the same permissions in the testing
environment.
After completing these steps, you will have an exact duplicate of your production environment (as
of the time of duplication) to use for testing purposes.
 
 
How to
1. Clone the data model
To create a copy o f a data model:
1. Select the  Modeler  tab.
2. On the  Data Modeler  page, navigate to the data model you want to clone and hover over it;
select the  
  (Clone Model ) icon.26/12/2025, 15:46 How-To: Creating a Testing Environment by Cloning a Data Model (Clone & Remap) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206143166-How-To-Creating-a-Testing-Environment-by-Cloning-a-Data-Model-Clone-Remap 2/10

3. In the drawer that opens, enter a name in the textbox for your newly cloned model and a
description (optional).
Remember to identify the processes you want to include (Hierarchy, Attributes, V alues, Line-Item
Details).
4. Select the  Save Item button.
5. A message will confirm that an ETL job for the data model cloning was created. T o check on the
status of this job, go to  Modeler > E TL > Hist ory.
6. When the cloning job has finished, refresh your browser. The cloned model will appear in
the Data Modeler  table .
 
Note26/12/2025, 15:46 How-To: Creating a Testing Environment by Cloning a Data Model (Clone & Remap) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206143166-How-To-Creating-a-Testing-Environment-by-Cloning-a-Data-Model-Clone-Remap 3/10

 
2. Copy the pr ocess
 
To duplicat e a pr ocess:
1. Navigate to the  Manager  tab to view the list of available processes.
2. Right-click on the row containing the process that was attached to the data model you cloned.
Select  Copy  from the menu .
3. In the drawer, indicate which folder you want to paste the selected process.Any processes attached to a data model will also be automatically attached to any
clones of that data model. The original process should be detached from the cloned
data model and replaced with a copy (see below).26/12/2025, 15:46 How-To: Creating a Testing Environment by Cloning a Data Model (Clone & Remap) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206143166-How-To-Creating-a-Testing-Environment-by-Cloning-a-Data-Model-Clone-Remap 4/10

4. Select  Copy Under Select ed to complete the action.
5. This creates a new process that appears in the list with the same name as the process it was
copied from. 
6. To change the name of the copied process, right-click on the row of the new copied process and
select  Rename . Enter a new name for the process then select  Rename  to complete the action.
26/12/2025, 15:46 How-To: Creating a Testing Environment by Cloning a Data Model (Clone & Remap) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206143166-How-To-Creating-a-Testing-Environment-by-Cloning-a-Data-Model-Clone-Remap 5/10

3. Detach the pr ocesses
To modif y process attachments:
Attaching a data model to a specific process must be done through the  Manager  tab. See below
for instructions:
1. Navigate to the  Manager  tab.
2. Locate the  Processes table.
3. Select the  process  to which you want to attach a data model. This opens the process workflow.
4. On the  Designer  page, select the  
  (gear ) icon in the upper right-hand corner.
5. Select  Manage Models  from the drop-down list.
6. Select the  X button next to the data model that you want to remove from your process.26/12/2025, 15:46 How-To: Creating a Testing Environment by Cloning a Data Model (Clone & Remap) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206143166-How-To-Creating-a-Testing-Environment-by-Cloning-a-Data-Model-Clone-Remap 6/10

 
4. Remap the t emplat es
To remap t emplat es:
1. Navigate to the  Manager  tab.
2. Select the  process  you want to attach a data model to from the  Processes table. This opens the
process workflow.
3. On the  Designer  page, select the  
  (gear ) icon in the upper right-hand corner.
4. Select  Manage Models  from the drop-down list.
5. Use the  Attach New Model  drop-down to select the data model that you want to attach to the
process.26/12/2025, 15:46 How-To: Creating a Testing Environment by Cloning a Data Model (Clone & Remap) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206143166-How-To-Creating-a-Testing-Environment-by-Cloning-a-Data-Model-Clone-Remap 7/10

6. Once you've selected the cloned model, select  Attach  to complete the action.
7. Repeat steps 1-6, above, for any other templates that you want to use in your testing
environment.
 
5. Set up data per missions
By default, the cloned data model and the copied process will not be accounted for in your existing
permissions structure. As a final step, you will need to set up additional permissions for them.
To set up data per missions:
1. Navigate to the  Admin  tab.
2. Navigate to the  Permissions  page.
3. Find the User Group containing the users that you want to grant access to the testing
environment. Alternatively, you can create a new user group by selecting  +Add Gr oup.
4. Select  View/Edit  under both  Data Permission  and Application P ermissions  to set up the
appropriate permission for both the cloned data model and copied process.
5. Repeat steps 3 and 4 as necessary.
 
 
6. Finishing up
After you have completed the instructions in each of the five preceding sections, your testing
environment will be set up and ready to use. Y ou can begin using it right away and can try out new
features, modeling or template modifications without any risk to your production environment.26/12/2025, 15:46 How-To: Creating a Testing Environment by Cloning a Data Model (Clone & Remap) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206143166-How-To-Creating-a-Testing-Environment-by-Cloning-a-Data-Model-Clone-Remap 8/10

If desired, you can also delete the testing environment at any time by deleting the cloned data
model and the copied process.
To delet e a testing envir onment:
1. Navigate to the  Manager  tab.
2. Right-click on the process belonging to the testing environment.
3. Select  Delet e.
4. Select  Delet e in the confirmation window to confirm that you want to delete the process. Make
sure to double-check that you selected the correct process to be deleted.
5. The process will be deleted and removed from the list.
6. Navigate to the  Modeler  tab.
7. Hover over the data model you want delete and select the  
  (delet e) icon.
8. A confirmation modal will ask you to confirm the delete. Select  Yes, Delet e Model  to remove
the data model.
9. The data model will be deleted and removed from the list. Y ou have completed the deletion of
the testing environment from your V ena tenant.
 
Notes & limitations
The testing environment you create will be an exact duplicate of your production environment
at the time it is created. This means that any changes to the production environment after this
date will not be reflected in the testing environment (and vice-versa).
You do not have to copy V alues, Line-Item Details and Attributes when you clone the data
model. Depending on your preference, leave the relevant box(es) unchecked if you do not want
these to be included in the cloned data model.  The only it em that is mandat ory when
cloning a data model is the Hierar chy.
Likewise, you do not have to copy the process that was attached to the original data model. If
desired, you can also copy a different process and attach it, attach multiple processes or create
a new process from scratch.26/12/2025, 15:46 How-To: Creating a Testing Environment by Cloning a Data Model (Clone & Remap) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206143166-How-To-Creating-a-Testing-Environment-by-Cloning-a-Data-Model-Clone-Remap 9/10

When you clone a data model, it will automatically be associated with the same process as the
original data model. Likewise, when you copy a process, the copied process will inherit any
associations to data models that the original process held. As a best practice, you should ensure
that duplicated data models and processes intended to be used for testing are not connected
with the original data models and processes.
Since Data P ermissions in V ena are created as exceptions when you add a data model via
cloning, the newly cloned model will not include a copy of the data from the original data
model. Y ou must export/import intersections to the newly cloned model. The same limits apply
to tenant migration . 
The remapping instructions in Section 4 also apply to the following situations:
Remapping a new template within an existing process.
Remapping an existing template within a new process.26/12/2025, 15:46 How-To: Creating a Testing Environment by Cloning a Data Model (Clone & Remap) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206143166-How-To-Creating-a-Testing-Environment-by-Cloning-a-Data-Model-Clone-Remap 10/10

