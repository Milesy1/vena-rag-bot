# Troubleshooting: The Bulk Copy Parameters Were Invalid – Vena Solutions

Troubleshooting: The Bulk Copy
Parameters Were Invalid
Issue summary
When cloning a data model, you may encounter an error:
The BulkC opy paramet ers were invalid. - C opy to and C opy from must c ontain the s ame s et of
dimensions - The v ersioning c onfiguration "X" is in valid. Delet e it and att empt the oper ation again.
 
Suggested solution
1. Navigate to the  Modeler  tab.
2. Select the  Data Model  you are trying to clone.
3. Select  Versioning .
4. In the  Versioning Configuration  section, select the configuration name referenced in the error
message from the drop-down menu.
Olalekan Adebayo
Updated  2 years ago26/12/2025, 15:47 Troubleshooting: The Bulk Copy Parameters Were Invalid – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20468926961805-Troubleshooting-The-Bulk-Copy-Parameters-Were-Invalid 1/3

5. Fix the versioning parameters and select  Save.
1. If the configuration is no longer required, select  Delet e Configuration .
6. Re-clone the data model.
 
Cause 
This may occur if the data model you are trying to clone contains a saved versioning configuration
that is incorrect or has errors.
 
Keywords
bulkcopy parameters, clone model, versioning.  
Was this ar ticle help ful?
 26/12/2025, 15:47 Troubleshooting: The Bulk Copy Parameters Were Invalid – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20468926961805-Troubleshooting-The-Bulk-Copy-Parameters-Were-Invalid 2/3

0 out of 0 found this helpful
Recently viewed articles
How-T o: Downloading All V ena Data From Y our T enant or Environment
How-T o: Undoing a V ersioning ETL job with Line-Item Details (LIDs)
How-T o: Undo a V ersioning ETL Job Without Line-Item Details
How-T o: Creating a T esting Environment by Cloning a Data Model (Clone & R emap)
How-T o: Adjusting How V ena T reats Zero V alues in the Database26/12/2025, 15:47 Troubleshooting: The Bulk Copy Parameters Were Invalid – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20468926961805-Troubleshooting-The-Bulk-Copy-Parameters-Were-Invalid 3/3

