# How-To: Undoing a Versioning ETL job with Line-Item Details (LIDs) – Vena Solutions

How-To: Undoing a Versioning ETL
job with Line-Item Details (LIDs)
 
Why use this feature?
When we mistakenly run an unintended versioning job, it is important that we undo it properly to
avoid having duplicate or stale data in the cube since versioning involves the creation of new ETL
jobs.
 
Before you begin
You will need at least  Modeler  access to follow the steps in this article
The clear slice columns in the configuration will be based on the “P age Filter” parameters used in
the versioning job and then the destination parameter.
 
Table of contents
Undo a V ersioning ETL job with  Link t o originals  Selected
Olalekan Adebayo
Updated  4 months ago
Warning
Be careful when using Clear Slices. V ersioning jobs create new intersections, and we
need a way to delete those newly created intersections when we want to undo the job
by using a historical export.26/12/2025, 15:47 How-To: Undoing a Versioning ETL job with Line-Item Details (LIDs) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17163939866381-How-To-Undoing-a-Versioning-ETL-job-with-Line-Item-Details-LIDs 1/5

Undo a V ersioning ETL job with  Make Sep arate Copies  Selected
Notes
 
How to
Undo a Versioning ETL job with  Link to originals  Selected
This is the same as undoing a versioning ETL job with  No Line-It ems deleted. This is because we
only want to delete these newly created intersections but not the Line-Item Details they are linked
to. When you delete or update Line-Item Details that are linked to multiple intersections, all the
linked intersections will be affected. 
To undo a versioning ETL job with  Link t o originals  selected, please visit this  article .
 
Undo a Versioning ETL Job with  Make Separate Copies  Selected
Step 1: Expor t LIDs for p aramet ers befor e Versioning
Let's use this versioning ETL job as an example of what we want to undo.
Filter: Y ear = 2024 and P eriods = 10, 11, 12
From: R eforecast
To: Q2 R eforecast
Use the dimensions in the page filter (the year 2024, periods 10, 11, 12) and the destination
(scenario Q2 R eforecast) to build an MQL query for your ETL export. This export will be for Line-
Item Details. W e will also pick a time  before  the versioning job was run.
1. Select the same date but  five minutes before  you ran the ETL job.26/12/2025, 15:47 How-To: Undoing a Versioning ETL job with Line-Item Details (LIDs) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17163939866381-How-To-Undoing-a-Versioning-ETL-job-with-Line-Item-Details-LIDs 2/5

2. Select  Expor t
3. Save this file as All-LIDs-For-This-P arameter-Before-V ersioning.csv.
Step 2:  Expor t LIDs for p aramet ers after Versioning
1. Perform another ETL export of LIDs with the same query but this time will be the live data and
not the historical data.
2. Save this file as All-LIDs-For-This-P arameter-After-V ersioning.csv. 
3. Open the exported CSV file from S tep 2 in Notepad++ or Excel. If you use Excel, be careful that
the leading 0s for dimension members are not removed.
4. Change the values in the  “_cmd” column from + (plus) to - (minus)  since we are trying to delete
those LIDs. 
5. Save the CSV file.26/12/2025, 15:47 How-To: Undoing a Versioning ETL job with Line-Item Details (LIDs) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17163939866381-How-To-Undoing-a-Versioning-ETL-job-with-Line-Item-Details-LIDs 3/5

 
Step 3: Cr eate a File t o Cube E TL job
1. Create a File to Cube ETL job that will be used to reload the LID CSV files back into the cube.
2. Set the data type for this ETL job to  Line-It em Details .
3. Upload the CSV file  All-LIDs-For -This-P aramet er-After-Versioning.cs v with the ETL job created
above. This will delete all the current LIDs for these intersections. Confirm that these LIDs were
in fact deleted before going to the next step. 
4. Upload the CSV file  All-LIDs-For -This-P aramet er-Befor e-Versioning.cs v with the same ETL job
created above. This will re-add all the LIDs that were in the cube before the versioning job for
these intersections.
5. We have now successfully deleted the new LIDs that were created by the versioning job and re-
added LIDs that were in the cube before the versioning job. V erify this by doing an ETL export of
LIDs to confirm.
6. Now that we have successfully deleted those LIDs linked to the newly created intersections by
the versioning ETL job, we want to undo a versioning job without LIDs.  Learn more about
undoing a versioning job without Line-Item Details in this article.Note
Do not make any changes to the CSV file (All-LIDs-For-This-P arameter-Before-
Versioning.csv) from S tep 1. 26/12/2025, 15:47 How-To: Undoing a Versioning ETL job with Line-Item Details (LIDs) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17163939866381-How-To-Undoing-a-Versioning-ETL-job-with-Line-Item-Details-LIDs 4/5

7. Check your reports and data to confirm that everything looks good.
 
Notes 
These steps should only be used to undo versioning ETL jobs where  No Line It ems was selected.
Clear Slice can cause data deletion. It is important that be cautious when doing this. 
When doing a versioning job with  Make Sep arate Copies  selected, it is important to follow the
steps in the order outlined.
 26/12/2025, 15:47 How-To: Undoing a Versioning ETL job with Line-Item Details (LIDs) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17163939866381-How-To-Undoing-a-Versioning-ETL-job-with-Line-Item-Details-LIDs 5/5

