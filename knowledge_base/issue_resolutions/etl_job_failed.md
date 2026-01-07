# Issue Resolution: ETL Job Failed

## Problem Description
An ETL (Extract, Transform, Load) job has failed, preventing data from loading into Vena.

## Immediate Steps

### Step 1: Check Error Message
1. Open Process Manager
2. Find the failed job
3. Click to view job details
4. Note the error message and error code

### Step 2: Common Error Codes

| Error Code | Meaning | Solution |
|------------|---------|----------|
| ETL-001 | Connection failed | Check source system connectivity |
| ETL-002 | Authentication error | Verify credentials are current |
| ETL-003 | Data format error | Review source data format |
| ETL-004 | Timeout | Increase timeout or reduce batch size |
| ETL-005 | Duplicate key | Check for duplicate records in source |

### Step 3: Review Source Data
- Verify source system is accessible
- Check that expected data exists
- Look for format changes in source
- Validate data types match expectations

### Step 4: Retry the Job
If the issue was transient:
1. Navigate to the failed job
2. Click "Retry"
3. Monitor the job progress

### Step 5: Manual Data Load
If automated ETL cannot be fixed immediately:
1. Export data from source manually
2. Format according to Vena template
3. Use manual upload feature
4. Document the workaround

## Prevention
- Set up monitoring alerts for ETL failures
- Implement retry logic for transient failures
- Maintain source system connectivity checks
- Document ETL dependencies and contacts







