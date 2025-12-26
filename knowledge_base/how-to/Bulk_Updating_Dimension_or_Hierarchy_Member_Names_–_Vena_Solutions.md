# How-To: Bulk Updating Dimension or Hierarchy Member Names – Vena Solutions

How-To: Bulk Updating Dimension or
Hierarchy Member Names
You may have a business change or requirement that requires  bulk updat es
of dimension or hierar chy member names. 
 
Why use this feature?
Some business changes or updates may require you to update your current dimension member
names to a different format. This feature allows you to make these updates in bulk instead of
updating them one by one.
 
Before you begin
To follow the instructions in this article, you will need at least  Modeler  access.
 
How to
1. Navigate to the  Modeler  tab.
2. Select  Data Modeler  in the sidebar.
3. Select  Expor t from the sidebar tab.
4. Under  Choos e what y ou w ould lik e to expor t:, select  Hierar chy.
5. Under  Expor t if follo wing c ondition is tr ue, you can use an  MQL or HQL query  to specify only the
part of the hierarchy you are interested in. If this is blank, then the entire hierarchy will be
exported.
Olalekan Adebayo
Updated  7 months ago26/12/2025, 14:21 How-To: Bulk Updating Dimension or Hierarchy Member Names – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15550666629133-How-To-Bulk-Updating-Dimension-or-Hierarchy-Member-Names 1/5

6. Select  Advanced Options  to refine your export.
7. Under  Wher e would y ou lik e to expor t to?, select  File.
8. Under  File for mat, select  CSV.
9. Check the boxes next to  Include c olumn header s in expor t? and Include member IDs in expor t?.
10. Save the Advanced Options. 
11. Open the file in Excel or Notepad.
If opening with Excel, it’s important to note that it will try to rename the member IDs. However,
member IDs must stay the same. Because of this, follow these steps to ensure the member IDs
remain the same in Excel ( see this article for more details on maintaining dimension member
IDs):
1. Open the exported CSV file in Notepad or Notepad++.
2. Open a blank Excel window and highlight the 7th column which is the _member_id column.
3. Right-click the highlighted column and select  Format cells . 26/12/2025, 14:21 How-To: Bulk Updating Dimension or Hierarchy Member Names – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15550666629133-How-To-Bulk-Updating-Dimension-or-Hierarchy-Member-Names 2/5

4. Change the format to T ext. This ensures that Excel does not try to change the format or
values when we paste the exported hierarchy file.
5. Return to the Notepad file and copy the contents.
6. Then return to the blank Excel file and select cell A1 and paste.  If  Excel  places all of the data
in just column A, use the T ext to Column feature from the Data tab in Excel.  
7. Select  Delimit ed, and then select  Next .
8. Check the box next to the Comma, and then select  Next .
9. Select all the columns or just the 7th column (_member_id) and select  text as the column
data format.
10. Select  Finish .
12. Make the desired changes and save the file. Save as CSV if you used a blank Excel file and re-
import the CSV file with a hierarchy load. Y ou can use an existing load hierarchy ETL job or
create one if it doesn't exist. 
13.  To import:
1. Navigate to the  Modeler  tab.
2. Select  Data Modeler  from the sidebar.
3. Select  ETL Templat es from the sidebar tab. 
4. Select an existing Load Hierarchy job and select the play button.
5. If a Load Hierarchy job doesn’t exist, create one:
1. Select  + Create Templat e
2. Enter "Load Hierarchy" as the name.
3. Select  Add S tep.
4. Select  File t o Cube.
5. Select  Hierar chy in the Data T ype drop-down
6. Select  Add.26/12/2025, 14:21 How-To: Bulk Updating Dimension or Hierarchy Member Names – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15550666629133-How-To-Bulk-Updating-Dimension-or-Hierarchy-Member-Names 3/5

7. Select  Save and then select the  Play button.
6. The ETL T emplate Execution window opens. Drag and drop the CSV file or select  browse
files and select the  CSV file  from your computer.26/12/2025, 14:21 How-To: Bulk Updating Dimension or Hierarchy Member Names – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15550666629133-How-To-Bulk-Updating-Dimension-or-Hierarchy-Member-Names 4/5

7. Select  Run.
8. During the import, the system checks for the Member ID and if it exists, the new name will
be used instead of creating a new member.
9. Once completed, check your hierarchy and confirm everything looks good.
Note
This will also automatically update your templates with the updated member
names since the system references the names using the unique member IDs.26/12/2025, 14:21 How-To: Bulk Updating Dimension or Hierarchy Member Names – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15550666629133-How-To-Bulk-Updating-Dimension-or-Hierarchy-Member-Names 5/5

