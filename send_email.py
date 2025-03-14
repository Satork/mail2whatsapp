import base64
from email.mime.text import MIMEText
from googleapiclient.discovery import build
import pickle


# Load Gmail API credentials
def get_gmail_service():
    with open("token.pickle", "rb") as token:
        creds = pickle.load(token)
    return build("gmail", "v1", credentials=creds)


# Send an email
def send_email(sender, to, subject, message_text):
    service = get_gmail_service()

    # Create email message
    message = MIMEText(message_text)
    message["to"] = to
    message["from"] = sender
    message["subject"] = subject
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    # Send email using Gmail API
    try:
        message = (
            service.users()
            .messages()
            .send(userId="me", body={"raw": raw_message})
            .execute()
        )
        print(f"Email sent! Message ID: {message['id']}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    sender_email = "your-email@gmail.com"  # Change this to your email
    receiver_email = "receiver-email@gmail.com"  # Change this to recipient email
    subject = "Test Email from Gmail API"
    message_body = "Hello, this is a test email sent via Gmail API in Python!"

    send_email(sender_email, receiver_email, subject, message_body)
