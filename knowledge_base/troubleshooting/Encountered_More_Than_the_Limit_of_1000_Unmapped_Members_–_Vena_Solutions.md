# Troubleshooting: Encountered More Than the Limit of 1000 Unmapped Members – Vena Solutions

Troubleshooting: Encountered More
Than the Limit of 1000 Unmapped
Members
Issue summary
When running an ETL job, you may encounter the following error:
Encountered mor e than the limit o f 1000 unmapped member s. Pleas e use a hier archy expor t to create
more than 1000 member s.
 
Suggested solution
This error is returned when too many new dimension members are added during an intersection
ETL load.
There are two possible reasons why you might see this error:
1. These dimension member names should alr eady exist.
This is common with leading 0s in your member names. For example, if your member names
have leading 0s (e.g., 011, 012, 033, etc.) but your source file is missing the leading 0s (e.g., 11,
12, 33), this causes an issue since "011" is different from "11". The system will try to create a new
member "11" instead of loading the data into the already existing member "011". T o fix this,
correct the source file by ensuring the dimension member names are correct, have the correct
format and re-upload it. 
Marjana
Updated  2 years ago26/12/2025, 15:48 Troubleshooting: Encountered More Than the Limit of 1000 Unmapped Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20074506822157-Troubleshooting-Encountered-More-Than-the-Limit-of-1000-Unmapped-Me… 1/2

2. These dimension member names ar e actually new and did not exist befor e the
intersection lo ad.
1. In this case, the fix is to first upload the member names into your hierarchy and then re-
run the intersection load so the system knows where to save the data. 
2. Prepare your hierarchy import file to add the new members to your data model.
3. Create a new ETL job with hierarchy import into the cube.
4. Run the hierarchy ETL job created above to import new dimension members. This will
ensure they reside in your data model hierarchy.
5. Re-run the original intersection load ETL job.
 
Cause 
This may occur if there are too many new dimension members while importing data via an ETL job.
 
Keywords
etl job error, too many unmapped members error 26/12/2025, 15:48 Troubleshooting: Encountered More Than the Limit of 1000 Unmapped Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20074506822157-Troubleshooting-Encountered-More-Than-the-Limit-of-1000-Unmapped-Me… 2/2

