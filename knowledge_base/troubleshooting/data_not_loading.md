# Troubleshooting: Data Not Loading in Vena

## Symptom
Data appears blank or shows zeros when it should display values.

## Common Causes and Solutions

### 1. Intersection Not Valid
**Problem**: The combination of dimensions doesn't exist in the model.

**Solution**: 
- Verify the intersection exists in Vena's model structure
- Check that all dimension members are spelled correctly
- Ensure the intersection is enabled for data entry

### 2. Security Permissions
**Problem**: User doesn't have access to view the data.

**Solution**:
- Check user's role assignments
- Verify intersection-level security settings
- Review dimension member security

### 3. ETL Process Not Complete
**Problem**: Data hasn't been loaded from source system yet.

**Solution**:
- Check ETL job status in Process Manager
- Review ETL logs for errors
- Verify source system connectivity

### 4. Filter Applied
**Problem**: A filter is hiding the data.

**Solution**:
- Clear all filters and try again
- Check for hidden dimension filters
- Review template filter settings

### 5. Wrong Version or Scenario
**Problem**: Looking at the wrong data version.

**Solution**:
- Verify you're viewing the correct scenario (Actual vs Budget)
- Check the version dimension selection
- Confirm the time period is correct

## Diagnostic Steps

1. Try viewing the same data as an admin user
2. Check the audit log for recent changes
3. Compare with a working intersection
4. Review the model calculation status

