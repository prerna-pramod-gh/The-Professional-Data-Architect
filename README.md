# The-Professional-Data-Architect
This project is a Python utility designed to process raw, unstructured log files containing mixed user information and system noise. It extracts valid user details (Names, Emails, Phone Numbers), filters them based on specific criteria, and exports a clean, professional CSV report.


## Key Features
- Regex Extraction: Utilizes Python's re module to accurately parse Names, Emails, and 10-digit Phone Numbers from noisy text.
- Memory Efficient: Implements a Generator pattern to read files line-by-line, ensuring the program can handle large datasets without overloading RAM.
- Data Filtering: Uses List Comprehensions to filter specific domains (e.g., gmail.com).
- Sorted Output: Automatically sorts the final dataset alphabetically by Name.
- Structured Export: Generates a standard CSV file using csv.DictWriter.


## Technologies Used
- Python 3.x
- Modules: re (Regex), csv, os

## Logic Breakdown
1. Extraction Phase: The script scans every line using specific Regex patterns.
- Emails: Matches standard email formats.
- Phones: Identifies 10-digit sequences (ignoring longer system codes).
- Names: Identifies capitalized words, prioritizing explicit labels like "User:".

2. Filtering Phase:
Raw data is refined using a list comprehension: [user for user in data if 'gmail.com' in user['Email']].

3. Storage Phase:
The filtered data is sorted by Name and written to cleaned_users.csv with proper headers (Name, Email, Phone).


## Contact
If you have any questions or would like to discuss commercial licensing, feel free to reach out:

LinkedIn: https://www.linkedin.com/in/prerna-pramod-671667301/
