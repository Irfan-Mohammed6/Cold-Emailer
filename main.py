from email_handler import send_email
from file_handler import extract_emails, update_email_status

csv_file_path = ".\emails.xlsx"
resume_path = "Resume.pdf"
status = "Not Sent"

email_data = extract_emails(csv_file_path)

# for entry in email_data:
#     ID = entry["ID"]
#     recipient_email = entry["Email_ID"]
#     company_name = entry["Company"]

#     email_status = send_email(recipient_email, company_name, resume_path)

#     if email_status == '200':
#         status = "Sent"

#     update_email_status(csv_file_path, ID, status)
    


send_email('irfan.mohammed00@gmail.com', 'IBM', resume_path)