# How-To: Formatting an Excel-Based CSV to Maintain Leading Zeros for ETL Jobs – Vena Solutions

How-To: Formatting an Excel-Based
CSV to Maintain Leading Zeros for
ETL Jobs
Closing and re-opening your Excel-based CSV files may result in a loss of leading zeros.
Read this article to learn how to format an Excel-based CSV to maintain leading zeros.
 
Why use this feature?
If you have dimension members with leading zeros (0055, 00100, 098899, etc.), there is an Excel
limitation that suppresses them and causes the ETL job to unintentionally create new dimension
members. Y ou'll need to edit your CSV file in Excel to maintain the leading zeros. 
 
How to
Format an Excel-based CSV file to maintain leading zeros
1. Open the file in Excel.
2. Select all the cells or columns that should have leading zeros.
3. Right-click on the selection. 
4. Select  Format Cells…
5. Select  Custom from the Category options.
Olalekan Adebayo
Updated  7 months ago26/12/2025, 15:42 How-To: Formatting an Excel-Based CSV to Maintain Leading Zeros for ETL Jobs – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14233859678989-How-To-Formatting-an-Excel-Based-CSV-to-Maintain-Leading-Zeros-for-ET… 1/3

6. Select  #,##0 .
7. In the   T ype: field, enter in the number of leading zeros you want. For example, if you want only
one leading zero, enter 0#,##0. If you want two leading zeros, then enter 00#,##0.
8. Select  OK. 
9. Save the file. There are now leading zeros in the cells you specified.
10. To confirm that leading zeros are present, open the file in Notepad and it should have the
leading zeros.
 26/12/2025, 15:42 How-To: Formatting an Excel-Based CSV to Maintain Leading Zeros for ETL Jobs – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14233859678989-How-To-Formatting-an-Excel-Based-CSV-to-Maintain-Leading-Zeros-for-ET… 2/3

Notes
Making this formatting chan ge to have leading zeros should be done once all editing in the file is
complete, as  reopening the Excel file may cause the leading zeros to be suppressed again.
 
Was this ar ticle help ful?
 
0 out of 0 found this helpful
Recently viewed articles
How-T o: Build Y our Chart of Accounts Hierarchy in Quick S tart
Explainer: What is Data Model S tandardization?
Troubleshooting: V ersioning Copy T o and Copy From must Contain the Same Set of Dimensions
Troubleshooting: Error While Processing the Model Slice Expression When Previewing
Intersections
Reference: Export Intersections and Line-Item Details26/12/2025, 15:42 How-To: Formatting an Excel-Based CSV to Maintain Leading Zeros for ETL Jobs – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14233859678989-How-To-Formatting-an-Excel-Based-CSV-to-Maintain-Leading-Zeros-for-ET… 3/3

