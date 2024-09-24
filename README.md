# Transform Dividends Script

This script transforms a CSV file containing dividend and interest data into a new format where dates are columns, stock symbols are rows, and payouts are placed in the corresponding cells. It supports aggregating payouts by individual dates or by months.

## Features

- **Input File**: Accepts an input CSV file containing dividend data.
- **Aggregation Options**: Use the `-m` flag to aggregate payouts by month.
- **Output File**: Generates `transformed_dividends.csv` with the organized data.

## Usage Instructions

1. **Run the Script with Required Arguments**:

   - **Basic Usage** (aggregate by individual dates):

     ```bash
     python3 transform_dividends.py dividends.csv
     ```

   - **Aggregate by Month** (using the `-m` flag):

     ```bash
     python3 transform_dividends.py dividends.csv -m
     ```

     or

     ```bash
     python3 transform_dividends.py dividends.csv --monthly
     ```

3. **Check the Output**:

   After running the script, a new file named `transformed_dividends.csv` will be created. Open this file with a spreadsheet application like Microsoft Excel or Google Sheets to view the transformed data.

## Example Outputs

### **Without `-m` Flag (By Date)**

The output will have individual dates as columns:

```csv
Ticker,1/12/2024,1/16/2024,2/1/2024,2/15/2024,3/1/2024,3/12/2024,3/15/2024,...
AG,,,,,,,1.58,,,,,,1.58,,,,,,,1.58,,,,,
```

### **With `-m` Flag (Aggregated by Month)**

The output will have months as columns (formatted as ```MM/YYYY```):

```csv
Ticker,01/2024,02/2024,03/2024,04/2024,05/2024,06/2024,07/2024,08/2024,09/2024
AG,,,1.58,,,1.58,,,1.58,,,
FLKR,,,,,,129.49,,,,
GOLD,,,127.52,,128.37,,,129.07
```

**Note**: The payouts for the same ticker within the same month are summed together.

### Additional Notes

- **Date Format**: The script expects dates in the `MM/DD/YYYY` format in the input CSV file.
- **Dependencies**: Uses standard Python libraries (`csv`, `sys`, `argparse`, `collections`). No additional packages are required.
- **Python Version**: Ensure you're using Python 3.x to run the script.



