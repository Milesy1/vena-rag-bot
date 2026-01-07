# Reference: Exporting Hierarchies in Vena Using HQL – Vena Solutions

Reference: Exporting Hierarchies in
Vena Using HQL
Learn how to export hierarchies in Vena using HQL.
 
Reference
There are several types of expressions that you can use to export hierarchies in V ena using HQL.
These return member positions, so a shared member with two positions would give two rows. The
export type is hierarchy. Below are six examples of different HQL expressions and what they would
return.
Example 1:
Get all members named 2010.
Note: "member" is a reserved keyword, so use "_member" instead.
_member .name = '2010'
Example 2:
Get all members whose name starts with "2".
_member .name LIKE '2%'
Example 3:
Get all members that are parents, in the "Y ear" dimension.
dimension.name = 'Y ear' and _member .numChildr en > 0
Example 4:
Get all shared members.
_member .numP ositions > 1
Jun Barrozo
Updated  1 year ago26/12/2025, 14:25 Reference: Exporting Hierarchies in Vena Using HQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/207465596-Reference-Exporting-Hierarchies-in-Vena-Using-HQL 1/2

Example 5:
Get all member positions with operator (+).
Note: use 1 for add (+), 0 for ignore (~), and -1 for subtract (-).
operator = 1
Example 6:
Get all bottom level members, in the "Accounts" dimension.
dimension.name = 'Ac counts' and _member .numChildr en = 026/12/2025, 14:25 Reference: Exporting Hierarchies in Vena Using HQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/207465596-Reference-Exporting-Hierarchies-in-Vena-Using-HQL 2/2

