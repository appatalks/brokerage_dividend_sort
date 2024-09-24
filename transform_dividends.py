#!/usr/bin/env python3
import csv
import sys
import argparse
from collections import defaultdict

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='Transform dividends CSV data.')
    parser.add_argument('input_file', help='Path to the input CSV file.')
    parser.add_argument('-m', '--monthly', action='store_true', help='Aggregate payouts by month.')
    args = parser.parse_args()

    input_file = args.input_file
    output_file = 'transformed_dividends.csv'
    aggregate_by_month = args.monthly

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

            # If aggregating by month, extract month and year
            if aggregate_by_month:
                month, day, year = map(int, trade_date.split('/'))
                trade_date = f'{month:02d}/{year}'

            payouts[ticker][trade_date] += net_amount
            dates_set.add(trade_date)
            tickers_set.add(ticker)

    # Sort the dates and tickers
    def date_key(date_str):
        # Convert date from 'MM/DD/YYYY' or 'MM/YYYY' to a tuple for proper sorting
        parts = date_str.split('/')
        if len(parts) == 3:
            month, day, year = map(int, parts)
        elif len(parts) == 2:
            month, year = map(int, parts)
            day = 1  # default day
        else:
            raise ValueError(f"Invalid date format: {date_str}")
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

if __name__ == '__main__':
    main()

