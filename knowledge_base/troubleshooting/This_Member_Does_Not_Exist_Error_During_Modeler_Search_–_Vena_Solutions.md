# Troubleshooting: This Member Does Not Exist Error During Modeler Search – Vena Solutions

Troubleshooting: This Member Does
Not Exist Error During Modeler
Search
Issue summary
When searching in the Modeler tab, you may receive the following error message:
This member does not exist in XXXXXXX
Suggested solution
If you are not a V ena Admin you will need the assistance of a V ena Admin to help you follow the
steps below.
1. Navigate to the Admin tab and check the User Groups assigned to your account.
2. Check each User Group you or the affected user are assigned to ensure that there are no
restrictions on the dimension that you search in when receiving the error. If there are, amend the
data permissions. K eep in mind that any changes to data permissions will affect all users that
belong to the same User Group.
3. If there are no restrictions in any of the User Groups for the dimension you’re searching for,
check to see if the dimension is linked.
In the  Modeler  tab, select the  chain icon  next to the dimension name.
4. If it is a linked dimension, you will need at least R ead access to all data models that this
dimension is linked to. For further information on managing data permissions, please see this
article.
 
Omair Riasat
Updated  2 years ago26/12/2025, 15:47 Troubleshooting: This Member Does Not Exist Error During Modeler Search – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/21567965458061-Troubleshooting-This-Member-Does-Not-Exist-Error-During-Modeler-Search 1/2

Cause 
This error can occur if there are restrictions on data permissions or if there are linked dimensions
where the user does not have R ead access to all linked data models.
 
Keywords
modeler search, search function, unable to search, member not found, member does not exist,
modeler tab
Was this ar ticle help ful?
 
0 out of 0 found this helpful
Related articles
How-T o: Add Images to V ena Insights Dashboards
Troubleshooting: ETL - Member "" Not Found in Dimension
Recently viewed articles
Troubleshooting: The Bulk Copy P arameters W ere Invalid
How-T o: Downloading All V ena Data From Y our T enant or Environment
How-T o: Undoing a V ersioning ETL job with Line-Item Details (LIDs)
How-T o: Undo a V ersioning ETL Job Without Line-Item Details
How-T o: Creating a T esting Environment by Cloning a Data Model (Clone & R emap)26/12/2025, 15:47 Troubleshooting: This Member Does Not Exist Error During Modeler Search – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/21567965458061-Troubleshooting-This-Member-Does-Not-Exist-Error-During-Modeler-Search 2/2

