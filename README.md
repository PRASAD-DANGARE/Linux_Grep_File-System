# Linux style Grep JSON Utility

### Description:
The JSON Grep Utility is a command-line Python tool designed to search and manipulate JSON data efficiently. It allows users to search for specific patterns within JSON logs or structured data files, leveraging the power of Pandas for data manipulation and argparse for command-line interface management. This tool provides flexible options for case-insensitive search, exclusion of matched results, counting occurrences, and handling invalid JSON entries within files.

### Features:
1. Pattern Search:
* Search for a specific pattern or substring across all columns in a JSON dataset.
* Supports case-sensitive and case-insensitive search.

2. Column Filtering:
* Extract specific columns from the dataset by searching for column names.
* Count or display the number of matching columns.
* Option to invert matches (exclude certain columns from results).

3. Search Data Filtering:
* Retrieve rows that match a specific pattern in any column.
* Count the number of rows containing the search pattern.

4. Invalid JSON Handling:
* Detect and display invalid JSON lines in the input file.

### Command-Line Options:

* -k: Search for patterns in the column names.
* -v: Invert the search result, showing rows or columns that don't match the pattern.
* -i: Case-insensitive search.
* -c: Count the number of matches instead of displaying them.
* -d: Exclude matching rows or columns from the result.
* -x: Skip displaying invalid JSON line numbers.
