# VenaQL Pattern: Data Validation

## Use Case
Validate data integrity before closing a reporting period.

## Balance Check Query

```sql
SELECT 
    [Account_Type],
    SUM([Debit]) AS [Total_Debits],
    SUM([Credit]) AS [Total_Credits],
    SUM([Debit]) - SUM([Credit]) AS [Difference]
FROM 
    [JournalEntries]
WHERE 
    [Period] = '2024-12'
GROUP BY 
    [Account_Type]
HAVING 
    SUM([Debit]) - SUM([Credit]) <> 0
```

## Intercompany Elimination Check

```sql
SELECT 
    [IC_Partner],
    [Account],
    SUM([Amount]) AS [Net_Balance]
FROM 
    [ConsolidationModel]
WHERE 
    [Account_Type] = 'Intercompany'
GROUP BY 
    [IC_Partner], [Account]
HAVING 
    SUM([Amount]) <> 0
```

## Validation Checklist

1. **Trial Balance**: Debits equal credits
2. **Intercompany**: Net to zero after elimination
3. **Retained Earnings**: Prior year close matches current year open
4. **Cash Flow**: Change in cash ties to balance sheet

## Automated Validation

Set up validation rules in Vena to:
- Block period close if validations fail
- Send alerts for out-of-balance conditions
- Log validation results for audit trail

