# Explainer: What’s the Difference Between an Alternate Hierarchy and Calculated Members: – Vena Solutions

Explainer: What’s the Difference Between an Alternate
Hierarchy and Calculated Members?
 
What is an Alt ernate Hierar chy?
An Alternate Hierar chy allows you to create alternate groupings of members from an existing data model to simplify mapping and allow for
automatic updates to the data from your source system. In an Alternate Hierarchy, you can repeat the same members in both hierarchies but revise
the order of your members via your alternate hierarchy.  For example, if you need a breakdown by a particular set (e.g., projects in a particular month),
you can create an alternate hierarchy to list the projects in the order of the month they start.
 
What is a Calculat ed Member?
In Vena, you have the ability to create special members that are composed of other members through an MQL statement. These members are
called  Calculat ed Member s. In practice, Calculated Members are most often used when you want to create a special roll-up that is not supported by
your regular hierarchy. This roll-up can then be used as a custom reporting bucket, representing a useful shortcut when building reports. Calculated
members are displayed on a template as a total of the expression in a single member.
 
How do I choose which one t o use?
Depending on the scenario, you may have the option of choosing either an alternate hierarchy or calculated members. There are benefits and
limitations to both of these options, outlined below:
 
Alternate Hierar chy  Calculat ed Member
Only bottom-level members can be shared members.  Can contain members from any level of the hierarchy, in any combin
When you set up an alternate hierarchy, it remains static unless you modify it.  Can be dynamic, static or a combination of the two.  
The visualization of members is simplified.  Visualization occurs via the MQL statement. Visualization in the tem
member (components are not broken down).
Supported in Drill Down.  Not supported in Drill Down.
Supported in Drill T ransactions.  Not supported in Drill T ransactions.
Can build multiple levels into a hierarchy.  Can only be a total.
Can be automatically updated through channels.  Not supported.
Can have multiple different alternate hierarchies. This is not easy to accomplish
using attributes or calculated members . Can have multiple different calculated members.
Can be difficult to maintain if you don’t have this information stored somewhere
else. AH ar e an arbitr ary rollup and typically y ou hav e to duplicat e every single Easy to maintain since it is in one expression. 
Vena Support T eam
Updated  7 months ago26/12/2025, 14:22 Explainer: What’s the Difference Between an Alternate Hierarchy and Calculated Members? – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360059243651-Explainer-What-s-the-Difference-Between-an-Alternate-Hierarchy-and-Calcula… 1/2

member in the hier archy becaus e they need t o be p art of your alt ernate rollups
somewher e.
 
Help ful links
 
How-T o: Build an Alternate Hierarchy
How-T o: Build a Custom roll-up using Calculated Members26/12/2025, 14:22 Explainer: What’s the Difference Between an Alternate Hierarchy and Calculated Members? – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360059243651-Explainer-What-s-the-Difference-Between-an-Alternate-Hierarchy-and-Calcula… 2/2

