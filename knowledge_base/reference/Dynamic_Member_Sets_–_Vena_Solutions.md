# Reference: Dynamic Member Sets – Vena Solutions

Reference: Dynamic Member Sets
Learn about the scope of each of the available  Dynamic Member Sets .
 
Overview
When you map a template or create Form V ariables or Expressions, V ena allows you to select
hierarchy members dynamically, if desired. This is done using dynamic member sets, which are
specified groups of members defined by their position in the member hierarchy.
Selecting members using dynamic member sets is useful if you want your mapping/Form
Variable/Expression to be able to accommodate changes to your data model, such as when
members are added, removed or modified. The available dynamic member sets are:
Children
IChildren
Descendants
IDescendants
Bottom Level
This reference guide illustrates which members are included in each of these sets.
 
Reference Guide
Hierarchy Diagram
To illustrate how the available sets define groups of members, consider this diagram that describes
a portion of a member hierarchy:
 
Laura Harris
Updated  1 year ago26/12/2025, 14:24 Reference: Dynamic Member Sets – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115001776786-Reference-Dynamic-Member-Sets 1/7

 
In this example, our highest-level member is  Global Consolidat ed. This is a parent member, as it
contains sub-members, which are referred to as children:  Peak US Oper ations  and Peak Mexic o
Oper ations .
However, while they are children, both  Peak US Oper ations  and Peak Mexic o Oper ations  are also
parents, as they themselves have children:  US001, US002  and US003  and  MX001,
MX002  and MX003 , respectively. These members representing the operation areas are referred to as
bottom-level members, as they do not have any children themselves. Thus, they represent the
lowest level of the hierarchy relative to  Global Consolidat ed.
As shown above, it is important to note that the meanings of the terms parent and child are
relative, and are determined by the frame of reference. This applies in particular to the dynamic
member sets, which are named in reference to the selected member. In the context of using
dynamic member sets, the  selected member  is the member which you specified prior to choosing
the dynamic member set (e.g., when mapping a template, the member you right-clicked on to see
the dynamic member set options).
In all of the examples below, the selected member is  Global Consolidat ed.
 
Children
Definition:  One level below the selected member in the hierarchy, but no levels below that.
Descr iption:  Includes the children of the selected member, but not any of the individual members
at lower levels, i.e., the selected member's children's children.
Illustration:26/12/2025, 14:24 Reference: Dynamic Member Sets – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115001776786-Reference-Dynamic-Member-Sets 2/7

Includes the member s highlight ed:
 
IChildren
Definition:  The selected member itself and one level below the selected member in the hierarchy,
but no levels below that.
Descr iption:  The same as children, except that this set also includes the selected member.
Illustration:
Includes the member s highlight ed:26/12/2025, 14:24 Reference: Dynamic Member Sets – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115001776786-Reference-Dynamic-Member-Sets 3/7

 
Descendants
Definition:  All levels below the selected member in the hierarchy.
Descr iption:  Includes all children of the selected member, the children's children, and so on until
the lowest level of the hierarchy related to the selected member.
Illustration:
Includes the member s highlight ed:26/12/2025, 14:24 Reference: Dynamic Member Sets – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115001776786-Reference-Dynamic-Member-Sets 4/7

 
IDescendants
Definition:  The selected member itself and all levels below the selected member in the hierarchy.
Descr iption:  The same as descendants, except that this set also includes the selected member
itself.
Illustration:
Includes the member s highlight ed:26/12/2025, 14:24 Reference: Dynamic Member Sets – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115001776786-Reference-Dynamic-Member-Sets 5/7

 
Bottom-level
Definition:  Only the lowest level in the hierarchy under the selected member.
Descr iption:  Includes all members under the selected member that are children only, and no
members from any levels above that.
Illustration:
Includes the member s highlight ed:26/12/2025, 14:24 Reference: Dynamic Member Sets – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115001776786-Reference-Dynamic-Member-Sets 6/7

26/12/2025, 14:24 Reference: Dynamic Member Sets – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115001776786-Reference-Dynamic-Member-Sets 7/7

