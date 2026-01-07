# How-To: Build Your Chart of Accounts Hierarchy in Quick Start – Vena Solutions

How-To: Build Your Chart of
Accounts Hierarchy in Quick Start
Quick S tart is a new, centralized tool that allows you to set up your data model faster
and speed up the time to get value out of V ena. In step four of Quick S tart, you can
build your chart of accounts hierarchy.
This allows you to add members (GL account numbers), edit member names and aliases
(account descriptions) and assign range rules (define groupings of accounts). 
 
Why use this feature?
There are two existing ways you can build your account hierarchy in V ena: direct CSV upload or
manual creation through the Modeler interface. Direct CSV upload requires a specific V ena format
that can be time-consuming to transpose to, and manual through the Modeler can be a slow
process. For setting up your data model from scratch, there is now a better way. Using V ena’s Quick
Start Hierarchy Build, you can significantly reduce the effort and time needed to set up your data
model. 
This article focuses on step four of V ena’s Quick S tart feature and will teach you how to build your
chart of accounts hierarchy and provide examples of how this feature will help you start using V ena
faster.
 
Before you begin
To complete the steps outlined on this page, you will need at least  Modeler  access. 
You will also need to complete the first three steps of Quick S tart; uploading your GL transaction,
matching dimensions and customizing your transaction table.
 
Mia Shabsove
Updated  7 months ago26/12/2025, 15:42 How-To: Build Your Chart of Accounts Hierarchy in Quick Start – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15220805304717-How-To-Build-Your-Chart-of-Accounts-Hierarchy-in-Quick-Start 1/11

Table of contents
How to
Add a child or sibling member
Assign range rules to your standard hierarchy 
Operating Expenses example
Operating Expenses example outcome
Notes & limitations
 
How to
Part 1: Add a child or sibling member
You’ll notice when you land on this step, there is already a default standard hierarchy in place with
top-level members as a starting point. Y our goal is to expand on the starting structure and create
additional levels to reflect your company’s account hierarchy for reporting. At the lowest level
parent of a group, you’ll want to set a range rule to define which group of account ranges roll up to
that parent.
For example:
1. Select the  
 vertical ellipsis  icon in the Actions column next to the Member Name you would
like to add a child or sibling member.
2. Select  Add Sibling  or Add Child .
Note
Adding a sibling will create another member at the same level of the member and
adding a child will create another level below the member. 26/12/2025, 15:42 How-To: Build Your Chart of Accounts Hierarchy in Quick Start – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15220805304717-How-To-Build-Your-Chart-of-Accounts-Hierarchy-in-Quick-Start 2/11

3. Enter the  Member Name .
4. Enter a  Start Range  and an  End Range  for your new member .
5. If you want to add another child or sibling member, select  Add Another Member .
6. Once you’re finished adding members, select  Save Item.
 
Part 2: Assign range rules to your standard hierarchy
1. Under the Set Range Rule column, select the  
  Pencil  icon in the Set Range Rule column
next to the Member Name you would like to assign a range rule.
2. Enter the  Start Range  and End Range  for your member.
For example, if you are entering a range rule for your Cash accounts. Enter the account numbers
that correspond to your Cash member. If your Cash includes accounts 1000-1099 the start range
would be 1000 and the end range would be 1099.
3. Select the  check mark  to save the range rule.
 
Part 3: Delete a member
1. Select the  
  vertical ellipsis  icon in the Actions column next to the Member Name you
would like to delete.26/12/2025, 15:42 How-To: Build Your Chart of Accounts Hierarchy in Quick Start – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15220805304717-How-To-Build-Your-Chart-of-Accounts-Hierarchy-in-Quick-Start 3/11

2. Select  Delet e Member .
3. If you’re sure you want to delete the member, select  Delet e.
 
Operating Expenses example 
You'll notice  when you land on this step, there is already a default standard hierarchy. Y our goal is
to expand on the starting structure and create additional levels to reflect your company’s account
hierarchy for reporting. At the lowest level parent of a group, set a range rule to define which group
of accounts (members) the numbers/ranges will roll up to. 
This is the starting point for the income statement:
You’ll notice it goes as far as Operating Expenses. This is where we can use the tool to expand and
build out the hierarchy custom to your business needs.
Let’s say one level down from Operating Expenses, we need to add these nine account groups
(members):
Salaries & R elated Costs
Workers Compensation
Benefits & R elated Costs
Interest Expense26/12/2025, 15:42 How-To: Build Your Chart of Accounts Hierarchy in Quick Start – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15220805304717-How-To-Build-Your-Chart-of-Accounts-Hierarchy-in-Quick-Start 4/11

Depreciation & Amortization
Lease on F acilities
Marketing Expense
Corporate Overhead
Other Admin Expenses
To do this, right-click  Operating Expenses  and select  Add Child  to add members a level below it. 
 
This will open a side drawer where you can begin to add the new members:
 
If the GL Account codes roll up to this level directly, you can begin assigning the Account ranges. If
there is another level to be created, add the members,  Save Changes  and return to the table to
continue. For this example, that is what we will do.
Once changes are saved, you can see the new members are created and added in the table, nested
under Operating Expenses as its children.26/12/2025, 15:42 How-To: Build Your Chart of Accounts Hierarchy in Quick Start – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15220805304717-How-To-Build-Your-Chart-of-Accounts-Hierarchy-in-Quick-Start 5/11

Now let’s go one more level below for  Benefits & R elated Costs.  
Right-click  Benefits & R elated Costs  and select  Add Child.  The side drawer opens again and you
can now add children to the  Benefits & R elated Costs  member. W e’ll proceed to add the next
level groups as follows:26/12/2025, 15:42 How-To: Build Your Chart of Accounts Hierarchy in Quick Start – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15220805304717-How-To-Build-Your-Chart-of-Accounts-Hierarchy-in-Quick-Start 6/11

 
Now, this is the lowest-level parent for this account group (member). Under these four buckets are
the actual, numeric GL account codes. Since this is the case, we can define the range of accounts
that roll up to each new parent.
It should look something like this - of course, the actual account codes will be unique to your Chart
of Accounts. Y ou may receive an error message if you make an invalid input - see  Notes &
Limitations for more information.  You will need to fix them before changes can be saved. For
example:26/12/2025, 15:42 How-To: Build Your Chart of Accounts Hierarchy in Quick Start – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15220805304717-How-To-Build-Your-Chart-of-Accounts-Hierarchy-in-Quick-Start 7/11

 
Once changes are saved, you can see the next level of account groups created under  Benefits &
Related Costs  and the corresponding ranges set for each one.26/12/2025, 15:42 How-To: Build Your Chart of Accounts Hierarchy in Quick Start – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15220805304717-How-To-Build-Your-Chart-of-Accounts-Hierarchy-in-Quick-Start 8/11

 
If you need to make any changes, you can select the  Pencil  icon to edit a specific member name or
range. 
You will then need to repeat this process for all the other account groupings.
When the data load process runs in V ena, we will place those numeric GL Account codes under the
corresponding parent set by the account ranges in this step. In short, we will build out the rest of
your hierarchy for you after your first data load, putting all the loaded account members in their
defined position.
 Note
Only create members for the lowest-level parent/account group (member). The
individual numerical GL account codes only need to be defined within the ranges. A
generally easy way to think about this is that we only need to create up to the "text"
based levels in the hierarchy table view. 26/12/2025, 15:42 How-To: Build Your Chart of Accounts Hierarchy in Quick Start – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15220805304717-How-To-Build-Your-Chart-of-Accounts-Hierarchy-in-Quick-Start 9/11

Operating Expenses example outcome
Once you complete  Quick S tart, you’ll land on the Data Model page. Y ou can explore the hierarchy
you just built by expanding the levels. P er the example we just walked through, you’d see:
The 9 children/subgroups created under Operating Expenses. 
The 4 children/subgroups created under Benefits & R elated Costs.
The actual, bottom-level GL account codes nested under the parent as defined in your account
Range Rules.
If you matched the account alias in the  Match Dimensions  step of Quick S tart, you’d also see
that reflected here.
Any members that did not fit in a defined range, would be placed in an  Unmapped  folder.
You can bulk select, drag and drop those members into their position.
Members and aliases can be edited in this table view.
 
To edit your account ranges, select  Manage > Ranges.26/12/2025, 15:42 How-To: Build Your Chart of Accounts Hierarchy in Quick Start – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15220805304717-How-To-Build-Your-Chart-of-Accounts-Hierarchy-in-Quick-Start 10/11

 
Notes & limitations
End ranges must be greater than start ranges. For example, if your start range is 1499, the end
range must be 1500 or higher.
Ranges cannot overlap. For example, the start range for your Cash account is 1000 and the end
range is 1499. When adding Accounts R eceivable as the next child member, it cannot have a
start range of 1499. The start range cannot overlap with the Cash account.
Decimals are permitted for numeric ranges.
Character limit for the range input field is 15.
You cannot create two members with the same name. 
Member names and ranges cannot contain invalid characters, only alphanumeric characters are
allowed. 
A start or end range cannot be left blank, both must be entered to save your member.
Set ranges do not move existing bottom-level members in your model. This occurs as part of
the data load step. Once ranges are set, net new members that are uploaded will be placed
according to the ranges, or under  Unmapped .
 26/12/2025, 15:42 How-To: Build Your Chart of Accounts Hierarchy in Quick Start – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15220805304717-How-To-Build-Your-Chart-of-Accounts-Hierarchy-in-Quick-Start 11/11

