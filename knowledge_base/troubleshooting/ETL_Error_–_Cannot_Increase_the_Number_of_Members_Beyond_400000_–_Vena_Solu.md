# Troubleshooting: ETL Error – Cannot Increase the Number of Members Beyond 400000 – Vena Solutions

Troubleshooting: ETL Error – Cannot
Increase the Number of Members
Beyond 400000
Issue summary
When running an ETL Job with a hierarchy upload you may come
across the following error:
Exceeded max allo wable r ow err ors (1 in valid r ows). L ast at r ow xxxxx:
Cannot incr ease the number o f member s bey ond 400000
 
Suggested solution #1
1. Review the data model for members that are no longer being used.
2. Remove these members to make space for the new ones.
Miguel Buan
Updated  1 year ago26/12/2025, 15:48 Troubleshooting: ETL Error – Cannot Increase the Number of Members Beyond 400000 – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20125010992525-Troubleshooting-ETL-Error-Cannot-Increase-the-Number-of-Members-Beyo… 1/2

Suggested solution #2
Redesign the data model to move the bulk dimension into the value dimension. This treats the
members as values to save space in the data model.
If assistance is required when doing so, reach out to your Customer Success Manager to connect
with the Professional Services team.
Cause 
There is a limit of 400,000 members per data model. Attempting to load more members gives this
error.  Visit this article for more information on maximum members and member characters .
Keywords
etl, error, hierarchy, max, rows, invalid, increase, members26/12/2025, 15:48 Troubleshooting: ETL Error – Cannot Increase the Number of Members Beyond 400000 – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20125010992525-Troubleshooting-ETL-Error-Cannot-Increase-the-Number-of-Members-Beyo… 2/2

