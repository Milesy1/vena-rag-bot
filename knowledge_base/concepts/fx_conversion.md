# FX Conversion in Vena

Foreign Exchange (FX) conversion is a critical feature in Vena for multinational organizations.

## How FX Works

Vena handles currency conversion through rate tables that map source currencies to target currencies at specific points in time.

### Rate Table Structure

| Source Currency | Target Currency | Rate | Effective Date |
|----------------|-----------------|------|----------------|
| USD | EUR | 0.92 | 2024-01-01 |
| GBP | EUR | 1.17 | 2024-01-01 |
| CAD | USD | 0.74 | 2024-01-01 |

## Conversion Methods

### 1. Average Rate
Used for income statement items. Applies the average exchange rate for the period.

### 2. Closing Rate
Used for balance sheet items. Applies the rate at period end.

### 3. Historical Rate
Used for equity items. Applies the rate at the time of the original transaction.

## Common Issues

1. **Missing Rate**: If no rate exists for a currency pair, conversion fails silently
2. **Wrong Period**: Ensure rate effective dates align with your reporting period
3. **Rounding Errors**: Small discrepancies can occur due to decimal precision

## Troubleshooting

If FX conversion isn't working:
1. Check the rate table has the required currency pair
2. Verify the effective date covers your reporting period
3. Ensure the source data has the correct currency code
4. Review the conversion method setting on the account

