# How-To: Undo a Versioning ETL Job Without Line-Item Details – Vena Solutions

How-To: Undo a Versioning ETL Job
Without Line-Item Details
Avoid duplicate versioning jobs without Line-Item Details by  undoing  them. 
 
Why use this feature?
When we mistakenly run an unintended versioning job, it is important that we undo it properly to
avoid having duplicate or stale data in the cube.
Olalekan Adebayo
Updated  4 months ago26/12/2025, 15:46 How-To: Undo a Versioning ETL Job Without Line-Item Details – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14233953668109-How-To-Undo-a-Versioning-ETL-Job-Without-Line-Item-Details 1/6

 
Before you begin
You must have at least  Modeler  access to follow the steps in this article.
 
Table of contents
How t o
Notes & best practices
How to
Undo a Versioning ETL job 
We'll use this example as the data in this guide--follow along with your own data.
Filter = Y ear 2022 and P eriods 10, 11, 12
From: R eforecast
To: Q2 R eforecast
1. Use the dimensions in the page filter (the year 2022 and periods 10, 11 and 12) and the
destination (scenario Q2 R eforecast) to build an MQL query for your ETL export.
2. Navigate to  Data Modeler > Expor t and set the  Manual Quer y toggle to  ON. 
26/12/2025, 15:46 How-To: Undo a Versioning ETL Job Without Line-Item Details – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14233953668109-How-To-Undo-a-Versioning-ETL-Job-Without-Line-Item-Details 2/6

3. Build an MQL query for your export under  Expor t if following condition is tr ue. Use the
dimensions in the page filter (the year 2022 and periods 10, 11 and 12) and the destination
(scenario Q2 R eforecast).
Note
We are only using the destination dimension in addition to the page filter for the
query since that is what we want to restore. W e are not using the source dimension.26/12/2025, 15:46 How-To: Undo a Versioning ETL Job Without Line-Item Details – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14233953668109-How-To-Undo-a-Versioning-ETL-Job-Without-Line-Item-Details 3/6

4. Select  Advanced Options.
5. Check the box next to  Expor t data fr om a dat e and time in the p ast, then enter the date and
time. Choose a time before the versioning job was run. Since the versioning job ran at 4:12 AM,
we will export data from 4:10 AM. Then select  Save.
26/12/2025, 15:46 How-To: Undo a Versioning ETL Job Without Line-Item Details – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14233953668109-How-To-Undo-a-Versioning-ETL-Job-Without-Line-Item-Details 4/6

6. Select  Expor t.
7. Navigate to  Data Modeler > E TL Templat es and create a  File t o Cube E TL job  to reload the
data back into the cube.
Note
This ETL job must have a Clear Slice configuration. The columns will correspond to
the dimensions used in the page filter and the destination of the versioning
parameters. The Clear Slice will ensure the historical data is restored and any newly
created intersection as a result of that versioning job is also deleted.
Learn mor e about using Clear Slices t o clear int ersections dur ing an E TL lo ad. 
For this example, the clear slice will be Y ear, P eriod and Scenario. This will differ
based on the versioning job you are working with.26/12/2025, 15:46 How-To: Undo a Versioning ETL Job Without Line-Item Details – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14233953668109-How-To-Undo-a-Versioning-ETL-Job-Without-Line-Item-Details 5/6

8. Once the job is complete, the versioning ETL job has been undone or reverted.
9. Check your reports and data to confirm everything is correct.
 
Notes & best practices
This should only be used to undo versioning ETL jobs where  No Line-It em Det ails were selected.
Clear Slices delete data (mostly old data), so be cautious that you aren't deleting something you
don't want to.
Versioning jobs create new intersections, which must be deleted when you want to use a
historical export to undo the job, so be cautious when using Clear Slices.26/12/2025, 15:46 How-To: Undo a Versioning ETL Job Without Line-Item Details – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14233953668109-How-To-Undo-a-Versioning-ETL-Job-Without-Line-Item-Details 6/6

