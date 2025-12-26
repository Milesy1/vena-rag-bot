# How-To: Downloading All Vena Data From Your Tenant or Environment – Vena Solutions

How-To: Downloading All Vena Data
From Your Tenant or Environment
Do you need access to all your V ena data in a downloadable format? R ead on to to learn
more.
 
Why use this feature?
You may want to export and download your V ena data (intersection data and templates) in some
scenarios. The following instructions will help you do so quickly and easily. 
 
Before you begin
To follow the instructions in this article, you will need  Modeler , Manager  and Admin  access. If Data
Permissions are set up in your environment, you will also need the appropriate data and application
permissions for the data you are working with.
 
Table of contents
How to
Download all V ena templates or reports
Download all Data Model or Cube intersection data
Notes & Best Practices
 
Olalekan Adebayo
Updated  6 months ago26/12/2025, 15:47 How-To: Downloading All Vena Data From Your Tenant or Environment – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/27857117466509-How-To-Downloading-All-Vena-Data-From-Your-Tenant-or-Environment 1/4

How to
Download all Vena templates or reports
All reports and templates must be manually downloaded from the  Manager  tab. T o manually
download all reports and templates:
1. Log in to vena.io.
2. Navigate to the  Manager  tab. 
3. Select the appropriate  folder .
4. Select the appropriate  process .
5. Select  Files  Librar y.
6. Select the appropriate  folder . You may want to create the same folder structure on your
computer for easy tracking.
7. Select the  vertical ellipsis  for the report or template you want to download.
8. Select  Audit  History.
26/12/2025, 15:47 How-To: Downloading All Vena Data From Your Tenant or Environment – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/27857117466509-How-To-Downloading-All-Vena-Data-From-Your-Tenant-or-Environment 2/4

9. Select  Templat e Sav e for Save T ype.
This will only show file audit entries where the template structure was changed and saved, This is
not the same as  Data Sav e. 
10. Look for the most recent entry. This will be sorted by the latest modified date but you may
change the sort order by selecting  Modified Time .
11. Select the  blue downlo ad icon  (
 ) on the most recent version of the template or report. 
12. An offline copy of the template is downloaded to your computer's default download location.
13. Move the file into the appropriate folder or location on your local computer.
14. Repeat the same steps for all your other reports or templates.
 
Download all Data Model or Cube intersection data
You can leverage our ETL export tool to download your data model or cube intersection data.
1. Log in to vena.io.
2. Navigate to the  Modeler  tab.
3. Visit this article on how to export intersection data .
4. Open the downloaded file to confirm the data is accurate.
 
Notes & best practicesNote
When exporting data from your data model, break them into smaller chunks by
checking the appropriate boxes for the dimension members you would like to export
each time (e.g., you could break your data down by different years and/or periods).
You could also use the Manual Query's export condition and MQL query. This will
ensure the ETL export jobs run faster.  Visit this article to learn more about MQL .26/12/2025, 15:47 How-To: Downloading All Vena Data From Your Tenant or Environment – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/27857117466509-How-To-Downloading-All-Vena-Data-From-Your-Tenant-or-Environment 3/4

Cube intersection data can be exported in multiple file formats (CSV, PSV, TDF, XLSX).
Only one user can download the CSV file and you can only download this file once. Y ou must re-
run an export if you need to download the file a second time.
 
Was this ar ticle help ful?
 
0 out of 0 found this helpful
Related articles
How-T o: Exporting CSV Files for ETL Job
How-T o: Using V ena Ad Hoc T o View Y our Data and Make Simple R eports
How-T o: Bulk Attach/Detach Attributes and Filter by Attributes
How-T o: Enabling Line Item Details (LIDs) in a T emplate or R eport
Troubleshooting: Unable T o Log Into Sandbox
Recently viewed articles
How-T o: Undoing a V ersioning ETL job with Line-Item Details (LIDs)
How-T o: Undo a V ersioning ETL Job Without Line-Item Details
How-T o: Creating a T esting Environment by Cloning a Data Model (Clone & R emap)
How-T o: Adjusting How V ena T reats Zero V alues in the Database
How-T o: Building Alternate Hierarchies26/12/2025, 15:47 How-To: Downloading All Vena Data From Your Tenant or Environment – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/27857117466509-How-To-Downloading-All-Vena-Data-From-Your-Tenant-or-Environment 4/4

