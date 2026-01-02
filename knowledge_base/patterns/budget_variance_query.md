# VenaQL Pattern: Budget vs Actual Variance

## Use Case
Calculate the variance between budgeted and actual values for financial reporting.

## Query Pattern

```sql
SELECT 
    [Account],
    [Department],
    [Period],
    [Actual_Amount],
    [Budget_Amount],
    [Actual_Amount] - [Budget_Amount] AS [Variance_Amount]
FROM 
    [FinancialModel]
WHERE 
    [Year] = 2024
    AND [Period] IN ('Q1', 'Q2', 'Q3', 'Q4')
ORDER BY 
    [Department], [Account]
```

## Key Considerations

1. **Ensure both scenarios exist**: Actual and Budget must both have data
2. **Time alignment**: Compare same periods
3. **Currency consistency**: Both should be in same currency

## Variance Analysis Tips

- **Favorable variance**: Actual revenue > Budget, or Actual expense < Budget
- **Unfavorable variance**: Actual revenue < Budget, or Actual expense > Budget
- **Materiality threshold**: Focus on variances above 5% or $10,000

## Common Modifications

### Percentage Variance
```sql
([Actual_Amount] - [Budget_Amount]) / [Budget_Amount] * 100 AS [Variance_Pct]
```

### YTD Variance
Add a time filter for year-to-date calculations based on current period.

### Department Rollup
Group by parent department for summary view.







