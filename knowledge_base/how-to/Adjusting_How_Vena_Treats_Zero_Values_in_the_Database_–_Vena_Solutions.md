# How-To: Adjusting How Vena Treats Zero Values in the Database – Vena Solutions

How-To: Adjusting How Vena Treats Zero
Values in the Database
In most databases, blanks and zeros are functionally identical, and V ena treats them as equivalent for
performance reasons. But in some specific cases, it's important to make a distinction between a zero
value and a blank value .
 
Why use this feature?
In most databases, blank intersections and zero values are treated the same way. R emoving zeros and leaving
intersections blank typically has no practical impact.
However, V ena processes zeros like any other data, while blank intersections are ignored. R eplacing zeros with
blanks can improve template performance by reducing template load times, so V ena replaces zeros with blanks by
default.
In some industries, especially those with regulatory requirements (e.g., C CAR), it is essential to retain zero values.
In such cases, you may need to adjust how V ena handles zero values to ensure they remain intact.
This guide explains how to configure your data model to modify V ena's treatment of zeros and how to replace
existing zeros with blanks if needed.
Before you begin
In order to complete the steps described in this article, you will require at least  Modeler  access. Y ou will also need
the necessary Application P ermissions to read and update the data model you will be working with.
 
How to
Basic Functionality
You can turn ON/OFF the feature that retains zeros in your data model. By default, it is OFF, meaning zeros are
saved as blanks. If turned ON, V ena will keep zeros and not replace them with blanks. This setting applies to the
entire data model but only affects new data inputs after the change.
 
Vena Support T eam
Updated  6 months ago26/12/2025, 15:46 How-To: Adjusting How Vena Treats Zero Values in the Database – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/207427413-How-To-Adjusting-How-Vena-Treats-Zero-Values-in-the-Database 1/6

 
To change how V ena handles zer o values:
1. Navigate to the  Modeler  tab.
2. Select  Data Modeler  from the sidebar.
3. Select  Settings  from the sidebar tab.
4. Select the  toggle  next to  Retain zer os for this model :
ON will save any zero input into the database as a value.
OFF will discard any zero input into the database and keep that intersection blank.
5. Any changes you make take effect immediately; there is no need to save.
 
Advanced functionality
Add Slice
For more specific control, use the Add Slice feature to retain zeros in select parts of the data model. This feature
works only to retain zeros for specified slices, not to discard them selectively.
With Add Slice, you can target single members, multiple members or dynamic groups (e.g., bottom-level,
IDescendants). If you leave any dimensions unconfigured, V ena treats them as if all members in those dimensions
are selected (e.g., IDescendants).Note
Changing this setting affects only standalone zero values which are exactly zero. It will not affect any
values that greater or lesser than zero (e.g., 0.1, etc.), nor will it remove zeros from values containing
them (e.g., 10.05 will not become 1.5).
Caution
Zeros will only be retained for the configured slices if the  ON/OFF  toggle is set to  ON. If
the ON/OFF  toggle is in the  OFF position, zeros will not be retained for any slices listed under  Retain
zeros for thes e slic es of the model .26/12/2025, 15:46 How-To: Adjusting How Vena Treats Zero Values in the Database – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/207427413-How-To-Adjusting-How-Vena-Treats-Zero-Values-in-the-Database 2/6

 
To only r etain zer os for specific p arts of the Data Model:
1. Navigate to the  Modeler  tab.
2. Select  Data Modeler  from the sidebar.
3. Select  Settings  from the sidebar tab.
4. Ensure that  Retain zer os for this model  is set to  ON.
5. Select  +Add Slice  to open the  Add/Edit R estrictions  drawer.
6. Use the  Select Dimension  drop-down menu to choose the  dimension  to define your slice.
7. In the  Member s section, navigate to the member you would like to use to define the slice. Right-click on the
member to see selection options.
8. Select the option that describes the slice (or part of the slice) you want. The corresponding members will be
added to the  Restrictions  section. This is a preview string of all configured restrictions in the green-colored26/12/2025, 15:46 How-To: Adjusting How Vena Treats Zero Values in the Database – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/207427413-How-To-Adjusting-How-Vena-Treats-Zero-Values-in-the-Database 3/6

panel below.
To make changes to the restrictions you've configured so far, select the trash can icon next to the item
you'd like to remove in the  Restrictions  section.
9. Select  Save Changes  once you have finished configuring the slice.
10. You will return to the main  Settings  screen, where your configured slice is added under  Retain zer os for thes e
slices of the model.  To modify or remove an existing slice, select the slice under  Retain zer os for this model ,
select either the  Edit or Delet e button.
Delet e Existing Zer os
As noted above, modifying the  Retain zer os for this model  setting only affects zeros that are entered into the
database going forward, after the change is made. If you already have zeros in your database (either because they
were input manually or from ETL loads) and you would like to replace them with nulls/blanks to improve
performance, you can do this with the  Delet e Existing Z eros function.
This finds and removes all existing zeros from your database upon activation. How this works depends on how
you have configured the  Retain zer os for this model  setting:
 
Retain Zer os Setting Data Model Slices Delet e Existing Zer os Behavior
OFF No Clears  all zeros from  entir e database
ON No Will not clear  any zeros
ON or OFF Yes Clears all zeros  except from the slices
 
To delet e any existing zer o values fr om y our datab ase and r eplace them with blanks:
1. Navigate to the  Modeler  tab.
2. Select  Data Modeler  from the sidebar.
3. Select  Settings  from the sidebar tab.
4. Verify your  Retain zer os for this model  setting and whether you have configured any slices to determine what
will happen when you use  Delet e Existing Z eros (refer to the table above).26/12/2025, 15:46 How-To: Adjusting How Vena Treats Zero Values in the Database – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/207427413-How-To-Adjusting-How-Vena-Treats-Zero-Values-in-the-Database 4/6

5. Select  Delet e existing zer os.
6. This opens a warning pop-up. Select  Yes to confirm that you would like to delete zeros.
7. A confirmation lets you know that a delete zeros job was scheduled and added to your ETL jobs queue. Y ou
can check on the progress of this job by selecting  History in the Modeler sidebar menu.
8. Once the ETL job finishes, all zeros will be removed from your database and replaced with blanks.
 
Blank empty r ollups for this model
When enabled, the  Blank Empty R ollups  setting changes how V ena handles parent-level rollups if child
intersections are blank or contain non-numeric values (e.g., text). If ON, parent rollups without numerical data at
the child level appear as blanks. If OFF, they display as zeros.26/12/2025, 15:46 How-To: Adjusting How Vena Treats Zero Values in the Database – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/207427413-How-To-Adjusting-How-Vena-Treats-Zero-Values-in-the-Database 5/6

 
Caution
This is a compatibility setting for users migrating to V ena Cloud from V ena OnSite. If you are not
migrating from V ena OnSite, we strongly recommend that you do  not change this setting.26/12/2025, 15:46 How-To: Adjusting How Vena Treats Zero Values in the Database – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/207427413-How-To-Adjusting-How-Vena-Treats-Zero-Values-in-the-Database 6/6

