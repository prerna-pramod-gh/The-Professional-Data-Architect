# The-Professional-Data-Architect
This project is a Python utility designed to process raw, unstructured log files containing mixed user information and system noise. It extracts valid user details (Names, Emails, Phone Numbers), filters them based on specific criteria, and exports a clean, professional CSV report.


## Key Features
- Regex Extraction: Utilizes Python's re module to accurately parse Names, Emails, and 10-digit Phone Numbers from noisy text.
- Memory Efficient: Implements a Generator pattern to read files line-by-line, ensuring the program can handle large datasets without overloading RAM.
- Data Filtering: Uses List Comprehensions to filter specific domains (e.g., gmail.com).
- Sorted Output: Automatically sorts the final dataset alphabetically by Name.
- Structured Export: Generates a standard CSV file using csv.DictWriter.
