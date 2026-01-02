# Troubleshooting: Slow Performance in Vena

## Symptom
Templates, reports, or queries are taking a long time to load or execute.

## Diagnostic Steps

### 1. Check System Status
- Review Vena status page for any known issues
- Check server CPU and memory utilization
- Verify network connectivity

### 2. Identify the Bottleneck

#### Template Performance
- Too many dimensions on rows/columns
- Large data range without filters
- Complex conditional formatting

#### Query Performance
- Unoptimized VenaQL queries
- Missing indexes on frequently queried dimensions
- Large result sets without pagination

#### Calculation Performance
- Complex calculation chains
- Circular or near-circular dependencies
- Excessive use of cross-model references

## Optimization Strategies

### Template Optimization
1. Limit visible dimensions to essentials
2. Use filters to reduce data scope
3. Implement drill-down instead of showing all detail
4. Remove unnecessary formatting rules

### Query Optimization
1. Add WHERE clauses to filter early
2. Select only required columns
3. Use appropriate aggregation levels
4. Consider pre-aggregated summary tables

### Calculation Optimization
1. Simplify calculation rules where possible
2. Use batch calculations for large updates
3. Schedule heavy calculations off-peak
4. Consider denormalizing frequently accessed calculations

## Quick Fixes

- Clear browser cache
- Try a different browser
- Reduce the date range
- Export data and work offline for analysis







