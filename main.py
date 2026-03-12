
import re
import csv
import os

# ---------------------------------------------------------
# SETUP: Create the dummy data file (for testing purposes)
# ---------------------------------------------------------
def create_raw_data_file():
    """Creates the raw_data.txt file with sample data if it doesn't exist."""
    content = """Log Report - Date: 08-03-2026
System ID: 4421-AX | User Entry: Mahi | Email: mahi_123@gmail.com | Phone: 9876543210 | Status: Active
Noise detected in sector 7... skip... 0x99212
User: Amit Sharma | Ph: 8877665544 | Contact: amit.mca@yahoo.in | Priority: High
Garbage_Data_1234567890_Ignore_This_Line_###
Registration: Sonia_99 | sonia.official@outlook.com | Mobile: 7766554433 | Verified: Yes
Abhi Gupta | abhi.gupta@gmail.com | 9001122334 | Remarks: Student
Zoya | zoya.ai@startup.co | 6655443322 | Dept: AI/ML
System Alert: Memory low in block 4
Deepak Kumar | deepak.kumar@hotmail.com | 9988776655 | Location: Jaipur
User: Divya | divya.dev@gmail.com | 8899001122 | Status: Pending
Random String: !@#$%^&*() | 1234567890 | Error_Code_404
Priya Singh | priya.singh@edu.in | 7788990011 | Role: Admin
User: Rohit | rohit_mca@gmail.com | 9911223344 | City: Delhi
Karan | karan_90@yahoo.com | 8822334455 | Batch: 2026
Noise: xxxxx-yyyyy-zzzzz
Sneha | sneha.official@gmail.com | 7733445566 | City: Mumbai
Vikas Verma | vikas.v@outlook.com | 9944556677 | ID: 102
User: Megha | megha_ai@gmail.com | 8855667788 | Priority: Mid
Dummy Line: No User Data Here 1122334455
Suresh Raina | s.raina@gmail.com | 7766778899 | Status: Active
Pooja | pooja_dev@yahoo.in | 9977889900 | Remarks: Follow_up
Ankit | ankit_mca@gmail.com | 8888990011 | City: Jaipur
Garbage: %%%%%%%%%% 0000000000 %%%%%%%%%%
Jaya | jaya_gupta@gmail.com | 7799001122 | Dept: CSE
Ravi | ravi_kumar@outlook.com | 9911001100 | Verified: No
User: Tanmay | tanmay_dev@gmail.com | 8822112233 | Status: Active
Final User: Shweta | shweta.official@gmail.com | 7733223344 | End_of_Record
End of Raw Data Stream. Total Records Logged: 20"""
    
    if not os.path.exists('raw_data.txt'):
        with open('raw_data.txt', 'w') as f:
            f.write(content)
        print("Created 'raw_data.txt' for testing.")

# ---------------------------------------------------------
# Phase 2: Generators (Memory Management)
# ---------------------------------------------------------
def raw_data_generator(file_path):
    """
    Generator function to read the file line by line.
    Yields lines one at a time to ensure memory efficiency.
    """
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                yield line
    else:
        print(f"Error: {file_path} not found!")

# ---------------------------------------------------------
# Phase 1: Regex & File Handling (Extraction)
# ---------------------------------------------------------
def extract_user_data(line):
    """
    Parses a single line of text to extract Name, Email, and Phone.
    Returns a dictionary if data is found, otherwise None.
    """
    user_data = {}

    # 1. Extract Email
    email_match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", line)
    if email_match:
        user_data['Email'] = email_match.group(0)

    # 2. Extract Phone Number (10 digits)
    # We use \b boundaries to ensure we don't match parts of longer ID strings
    phone_match = re.search(r"\b\d{10}\b", line)
    if phone_match:
        user_data['Phone'] = phone_match.group(0)

    # 3. Extract Name
    # Logic: Prioritize "User:" or "User Entry:" labels.
    # Fallback: Check for Capitalized words at the start of the line.
    name = None
    
    # Check for labels: "User: John" or "User Entry: John"
    label_match = re.search(r"(?:User Entry|User):\s*([A-Z][a-z]+(?: [A-Z][a-z]+)?)", line)
    if label_match:
        name = label_match.group(1)
    
    # Fallback: Check for "Name |..." at the very start of the line
    if not name:
        start_match = re.search(r"^([A-Z][a-z]+(?: [A-Z][a-z]+)?)", line)
        if start_match:
            name = start_match.group(1)

    if name:
        user_data['Name'] = name

    # Only return if we found at least an email or phone
    if 'Email' in user_data or 'Phone' in user_data:
        return user_data
    
    return None

# ---------------------------------------------------------
# Main Processing Function
# ---------------------------------------------------------
def process_assignment():
    create_raw_data_file()  # Ensure input file exists
    
    file_path = 'raw_data.txt'
    output_file = 'cleaned_users.csv'
    
    extracted_data = []

    # Step 1: Use the generator to fetch lines
    lines = raw_data_generator(file_path)

    # Step 2: Extract data line-by-line
    for line in lines:
        user_info = extract_user_data(line)
        if user_info:
            extracted_data.append(user_info)

    # Phase 3: Comprehensions & Sorting
    
    # Filter: Keep only Gmail users
    gmail_users = [
        user for user in extracted_data 
        if 'gmail.com' in user.get('Email', '')
    ]

    # Sort: Alphabetically by Name
    sorted_users = sorted(gmail_users, key=lambda x: x.get('Name', ''))

    # Phase 4: CSV Handling (Final Storage)
    if sorted_users:
        try:
            with open(output_file, 'w', newline="") as csvfile:
                fieldnames = ['Name', 'Email', 'Phone']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                writer.writerows(sorted_users)
                
            print(f"Success! {len(sorted_users)} Gmail user records saved to '{output_file}'.")
            
        except IOError as e:
            print(f"Error writing to CSV: {e}")
    else:
        print("No matching user data found to save.")

if __name__ == "__main__":
    process_assignment()
```
