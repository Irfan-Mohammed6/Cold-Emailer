import pandas as pd
from email_handler import send_email


# csv_file_path = ".\emails.xlsx"
# df = pd.read_excel(csv_file_path)
# print("Columns in Excel:", df.columns) 


def extract_emails(csv_file_path: str):
    """
    Extracts Email and company name from excel file and returns a list of dictionaries.
    """

    df = pd.read_excel(csv_file_path)
    email_data = []

    
    for _, row in df.iterrows():
        if str(row['Email Status']).lower() != 'sent':
            email_data.append({
                "ID": row["ID"],
                "Company": row["Company"],
                "Email_ID": row["Email ID"]
            })
    
    return email_data

def update_email_status(csv_file_path, id, status):
    """
    Updates the email sending status in the Excel file.
    """
    df = pd.read_excel(csv_file_path)

    if "Email Status" in df.columns:
        df["Email Status"] = df["Email Status"].astype(str)

    df.loc[df["ID"] == id, "Email Status"] = status

    df.to_excel(csv_file_path, index=False)

    print("Status Updated Successfully")