import smtplib, os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

load_dotenv()


def send_email(recipient_email: str, company_name: str, resume_path: str):


    EMAIL = os.getenv('SENDER_MAIL')
    PASSWORD = os.getenv('SENDER_PASSWORD')
    RECIPIENT_EMAIL = recipient_email
    SUBJECT = f"Application for a role at {company_name}"
    BODY = f"""    Dear Hiring Manager,

    I hope this email finds you well. I am writing to express my interest in joining {company_name} as a Software Developer.
    With 1 year of experience in Python development, automation and API handling, I am eager to contribute my skills to your team.

    I have attached my resume for your review. Please let me know a convenient time for a conversation.
    I would appreciate the opportunity to discuss how my skills align with the requirements at {company_name}. 
    

    Thank you for your time and consideration. I look forward to your response.

    Best regards,
    Irfan Mohammed  
    +917619139262
    """

    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = SUBJECT
    msg.attach(MIMEText(BODY, 'plain'))


    #attaching resume
    try:
        with open(resume_path, 'rb') as resume_file:
            part = MIMEApplication(resume_file.read(), Name=os.path.basename(resume_path))
            part['Content-Disposition'] = f'attachement; filename="{os.path.basename(resume_path)}"'
            msg.attach(part)
    except Exception as e:
        return f'Error attaching resume: {e}'

    #sending email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  
            server.login(EMAIL, PASSWORD) 
            server.sendmail(EMAIL, RECIPIENT_EMAIL, msg.as_string())
            print(f'Email sent successfully to {company_name}!')  
            return '200'
    except Exception as e:
        return(f'Error: {e}')
    


