# Explainer: What Are Linked Dimensions: – Vena Solutions

Explainer: What Are Linked
Dimensions?
Linked Dimensions  are denoted by a chain link icon ( ) next to the dimension name in
the Modeler  tab:
By linking a dimension, it can appear in multiple data models simultaneously. In other words, the
dimension exists once within your V ena environment but is associated with several different data
models.
 
Why link a dimension?
Vena environments often contain multiple data models tailored to specific functions, such as
operational expenses and personnel costs. These models may share common dimensions like
Entity, which outlines company divisions or departments.
Maintaining identical Entity dimensions across multiple models can be time-consuming due to
manual updates. This manual work is prone to errors, causing inconsistencies between models.
Linking dimensions eliminates this issue by synchronizing changes across all linked models. Any
modification—such as adding, renaming or deleting members—automatically updates the
dimension across all models, ensuring consistency and saving time.
 
Are ther e any constraints t o linking dimensions?
There are a few notes and limitations when utilizing linked dimensions:
Once dimensions ar e link ed, they cannot be unlink ed. The only way to revert a linked
dimension is to delete all but one of the linked data models. This reverts the dimension to a
standalone state but also results in data loss from the deleted models. Therefore, linking a
Laura Harris
Updated  6 months ago
26/12/2025, 14:22 Explainer: What Are Linked Dimensions? – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360055067111-Explainer-What-Are-Linked-Dimensions 1/6

dimension should be considered a permanent action.    
You cannot "unlink" a dimension by deleting it and r eplacing it with a copy .  Deleting a
linked dimension will destroy all intersection data in that data model. If you were to do this, and
then re-add the dimension, all historical data will need to be re-uploaded to the data model.   
Linked dimensions cannot hav e differ ent granular ity betw een data models.  Linked
dimensions are always identical, meaning they have identical member hierarchies across the
models in which they are linked.  
Hierar chy changes t o the link ed dimension in one data model affect all the data models
with which it is link ed. Ensure Modelers within your V ena environment are aware of any linked
dimensions and understand that changes to them affect multiple data models.  
Linking a dimension affects all link ed data models.  When you link a dimension, it becomes
connected to  all link ed data models immediately. Ensure the "linked from" data model is
correct, as this action also applies to any other linked data models.  
Linked dimensions r espect Application P ermissions but may seem other wise due t o
linking mechanics.  Only users with specific permissions can modify a data model and its
dimensions. However, if a user can modify all dimensions in a model with a linked dimension, or
the linked dimension itself, changes will reflect in other models that include the linked
dimension, even ones without explicit permissions.   
A user can indirectly modify a data model via the linked dimension. This is not a permission gap
but rather an effect of linking. Y ou can set permissions for linked dimensions to allow
modifications by certain users while keeping them read-only for others.
 
Deleting a data model with link ed dimensions does not affect other models.  Linked
dimensions remain after deletion, but if the deleted model shared dimensions exclusively with
one other model, the linked dimension icon will vanish from that remaining model.  
Deleting a data model with link ed dimensions does not affect other models.  Normal
dimensions and members are deleted, but linked dimensions remain intact in other models.  
Proceed with caution when r unning E TL jobs concurr ently fr om multiple data models with
linked dimensions . Running these jobs at the same time can cause calculation errors and data
conflicts. 
How do I link a dimension?
  W ar ning
Linking dimensions cannot be reversed without data loss. Ensure you’ve read the notes
in the previous section before continuing to prevent significant negative effects on your26/12/2025, 14:22 Explainer: What Are Linked Dimensions? – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360055067111-Explainer-What-Are-Linked-Dimensions 2/6

1. Navigate to the  Modeler  tab, then select  Data Modeler > Member s.
2. Choose a  data model  from the drop-down menu, then select the  pencil icon  (
)to open
the Dimensions  sidebar.
3. Select  + Add Dimension  to open the drop-down menu.
data models.
It is strongly recommended that you only link dimensions when setting up a new data
model. Linking a dimension with an existing data model is functionally identical to
adding a new dimension, in that doing so will break all previously mapped templates
attached to that data model. This is because every dimension in a data model must be
mapped in the P age, R ow or Column mappings for a template to function. When you
link a new dimension, you must update mappings for all affected templates, as well as
any channels that have the data model as a source or destination.
 26/12/2025, 14:22 Explainer: What Are Linked Dimensions? – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360055067111-Explainer-What-Are-Linked-Dimensions 3/6

4. Select  Link Dimension .
5. Select a  data model , then select the  dimension  that you wish to link to your model.
If you have existing data in the data model that you are linking a dimension to, V ena will
automatically extend the model to the ‘Undefined’ member of the new dimension. This is
necessary because an intersection must reference each dimension that exists in the data model.
When linking a new dimension, existing data within intersections must also be attributed to a
member within the newly linked dimension.
26/12/2025, 14:22 Explainer: What Are Linked Dimensions? – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360055067111-Explainer-What-Are-Linked-Dimensions 4/6

6. Select  Link.
7. Select  Link Dimension  in the pop-up to confirm.
8. Your newly linked dimension will now be listed in the Dimensions section for the selected data
model, marked with a link symbol ( ) .
 
Which dimensions ar e suitable for linking?
Link dimensions only when appropriate. Suitable ones often include Accounts, Entity and Y ear,
which are common in reports across models.
For example, link the Department dimension in Financial and W orkforce data models to
synchronize department codes. Similarly, linking the Product dimension across sales and inventory
26/12/2025, 14:22 Explainer: What Are Linked Dimensions? – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360055067111-Explainer-What-Are-Linked-Dimensions 5/6

models ensures consistency in product updates.
Aside from being applicable to multiple data models, dimensions suitable for linking typically also
have the following characteristics:
No v ariability in str uctur e betw een data models:  Linked dimensions must be identical in all
data models. They work best for dimensions that naturally stay the same over time. For example,
an Entity  dimension will usually consist of the same entities, such as  1 - Canada  and 2 - USA ,
regardless of the data model. If a dimension is likely to need specific changes for different
models in the future, it is not suitable for linking because it cannot be unlinked.
Tendency t o requir e hierar chy changes:  Hierarchy changes refer to modifications in the
structure or levels within a dimension, such as adding new departments or changing
department names. Linked dimensions are useful if such adjustments are needed because the
change only needs to be made once, and it will automatically apply to all data models that use
the linked dimension. However, dimensions that rarely or never require changes, such as
a Period dimension (e.g., months of the year), may not benefit from being linked.
In all cases, you should carefully consider the potential downsides before linking a dimension,
remembering that the process is irreversible.26/12/2025, 14:22 Explainer: What Are Linked Dimensions? – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360055067111-Explainer-What-Are-Linked-Dimensions 6/6

