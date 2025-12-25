# Issue Resolution: Calculations Not Running

## Problem Description
Calculations in Vena are not executing, resulting in stale or incorrect derived values.

## Resolution Steps

### Step 1: Check Calculation Status
Navigate to Process Manager and verify:
- Calculation engine is running
- No jobs are stuck in queue
- Server resources are available

### Step 2: Verify Calculation Rules
Review the calculation rules:
1. Open the model in Designer
2. Navigate to Calculations tab
3. Check that rules are enabled
4. Verify rule dependencies are correct

### Step 3: Check for Circular References
Circular references will block calculations:
- Review account hierarchies
- Check cross-model references
- Use the Dependency Analyzer tool

### Step 4: Force Recalculation
If needed, trigger a manual recalculation:
1. Go to Process Manager
2. Select the affected model
3. Click "Recalculate All"
4. Monitor the job status

### Step 5: Review Logs
Check calculation logs for errors:
- Look for timeout messages
- Check for memory warnings
- Review any error codes

## Prevention
- Schedule calculations during off-peak hours
- Keep calculation rules simple and efficient
- Regularly review and optimize complex rules
- Monitor calculation performance metrics

