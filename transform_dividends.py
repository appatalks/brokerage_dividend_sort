#!/usr/bin/env python3
import csv
from collections import defaultdict

input_file = 'dividends.csv'
output_file = 'transformed_dividends.csv'

# Read the data
payouts = defaultdict(lambda: defaultdict(float))
dates_set = set()
tickers_set = set()

with open(input_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        trade_date = row['Trade Date'].strip('"')
        ticker = row['Ticker'].strip('"')
        amount_usd = row['Amount USD'].strip('"')
        tax_withheld = row['Tax Withheld'].strip('"')

        # Convert amounts to float, handling empty strings
        amount_usd = float(amount_usd) if amount_usd else 0.0
        tax_withheld = float(tax_withheld) if tax_withheld else 0.0

        net_amount = amount_usd + tax_withheld

        payouts[ticker][trade_date] += net_amount
        dates_set.add(trade_date)
        tickers_set.add(ticker)

# Sort the dates and tickers
def date_key(date_str):
    # Convert date from 'MM/DD/YYYY' to a tuple (YYYY, MM, DD) for proper sorting
    month, day, year = map(int, date_str.split('/'))
    return (year, month, day)

dates = sorted(dates_set, key=date_key)
tickers = sorted(tickers_set)

# Write the transformed data
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # Header row
    header = ['Ticker'] + dates
    writer.writerow(header)
    # Data rows
    for ticker in tickers:
        row = [ticker]
        for date in dates:
            amount = payouts[ticker].get(date, '')
            if amount != '':
                amount = f'{amount:.2f}'
            row.append(amount)
        writer.writerow(row)

print(f"Transformation complete. Output saved to {output_file}.")
