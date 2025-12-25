# VenaQL Basics

VenaQL is Vena's proprietary query language for retrieving and manipulating data within the Vena platform.

## Key Constraints

1. **No Aliasing**: VenaQL does not support column aliasing. You must use explicit column names.
2. **Character Limit**: Queries are limited to 8192 characters maximum.
3. **Explicit Columns**: Always specify columns explicitly rather than using wildcards.

## Basic Syntax

```sql
SELECT 
    [Account],
    [Department],
    [Amount]
FROM 
    [ModelName]
WHERE 
    [Year] = 2024
```

## Common Functions

- `SUM()` - Aggregate sum of values
- `AVG()` - Average of values
- `COUNT()` - Count of records
- `FILTER()` - Filter results based on conditions

## Best Practices

1. Always test queries in a development environment first
2. Use meaningful dimension names
3. Keep queries as simple as possible
4. Break complex queries into smaller parts

