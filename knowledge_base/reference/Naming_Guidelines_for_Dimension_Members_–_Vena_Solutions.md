# Reference: Naming Guidelines for Dimension Members – Vena Solutions

Reference: Naming Guidelines for
Dimension Members
Refer to this article for a list of naming considerations for
dimension members used in Calcs, ETLs & Vena Copilot.
Overview
When naming dimension members, it’s important to follow specific character requirements to
ensure compatibility across V ena features, including Calcs, ETL and V ena Copilot. This article
outlines supported characters, known limitations and considerations for multi-language
environments.
 
Calc Naming Rules
Dimension member names can begin with: 
A letter
A number
An asterisk (*)
After the first character, member names can include:
Letters and numbers
Special characters : @ \ - , = < > + ' _ | *
Vena Support T eam
Updated  2 months ago
Caution_Icon_Small.png   Caution
Avoid using apostrophes (') in member names. Apostrophes can:
Cause errors when setting Data P ermissions.
Split member names into separate words in staging queries. 26/12/2025, 14:25 Reference: Naming Guidelines for Dimension Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/207371936-Reference-Naming-Guidelines-for-Dimension-Members 1/3

 
ETL Naming Rules
There are two known issues with special characters in ETL:
Apostr ophes (')
Member names containing apostrophes may fail during drill-across operations due to syntax
errors.
Leading Under scores (_)
If a member name in the first column of an upload file begins with an underscore, the ETL job
may fail to write or update data.
Workar ound:  Add a space before the underscore ( _). The ETL job will remove the space during
processing.
There are no other known issues with special characters in ETL for V ena Cloud.
 
Multi-Language and Vena Copilot Support
Unicode characters used in multi-language member names are currently not supported in Calcs or
ETL. The V ena team is actively working on a solution to support these characters.
 
Vena Copilot Limitation:
Vena Copilot cannot retrieve data from dimension members that contain special characters (e.g., ö,
ç, ñ).
To ensure compatibility and accuracy, avoid using special characters in member names when asking
Copilot questions. As a best practice, design data models without special characters in member
names whenever possible.
 
 Apostraphes can be wrapped in quotation marks (") to avoid the issues above.  26/12/2025, 14:25 Reference: Naming Guidelines for Dimension Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/207371936-Reference-Naming-Guidelines-for-Dimension-Members 2/3

 Dimension Member Names Dos and Donts.pdf 300 KB26/12/2025, 14:25 Reference: Naming Guidelines for Dimension Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/207371936-Reference-Naming-Guidelines-for-Dimension-Members 3/3

