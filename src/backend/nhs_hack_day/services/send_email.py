# send_email.py
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64
from jinja2 import Environment, FileSystemLoader

# Authenticate and create a Gmail API service
def create_gmail_service():
    creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/gmail.send'])
    service = build('gmail', 'v1', credentials=creds)
    return service

# Create email message with Jinja2 template
def create_message(sender, to, subject, template_name, context):
    env = Environment(loader=FileSystemLoader('src/backend/nhs_hack_day/services/templates'))
    template = env.get_template(template_name)
    body = template.render(context)
    # Create email message
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    message.attach(MIMEText(body, 'html'))
    # Encode the message to send via Gmail API
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw_message}

# Send email through Gmail API
def send_email(service, sender, recipient_email, subject, template_name, context):
    try:
        message = create_message(sender, recipient_email, subject, template_name, context)
        sent_message = service.users().messages().send(userId='me', body=message).execute()
        print(f'Email sent successfully to {recipient_email}: Message ID {sent_message["id"]}')
    except HttpError as error:
        print(f'An error occurred: {error}')
