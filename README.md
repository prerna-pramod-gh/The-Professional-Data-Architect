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

## How to Run

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd <your-repo-name>
2. Create the Input File:
Create a file named raw_data.txt in the root directory and paste the raw log data provided in the assignment.
3. Run the Script:
Execute the Python script from your terminal: python main.py
5. Check the Output:
6. Open the newly created cleaned_users.csv file to view the sorted, filtered user data.
