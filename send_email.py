import base64
from email.mime.text import MIMEText
from googleapiclient.discovery import build
import pickle
from whatsapp_cloud_api import send_whatsapp_message  # Import WhatsApp function


# Load Gmail API credentials
def get_gmail_service():
    with open("token.pickle", "rb") as token:
        creds = pickle.load(token)
    return build("gmail", "v1", credentials=creds)


# Send an email and WhatsApp notification
def send_email(sender, to, subject, message_text):
    service = get_gmail_service()

    message = MIMEText(message_text)
    message["to"] = to
    message["from"] = sender
    message["subject"] = subject
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    try:
        # Send email via Gmail API
        message = (
            service.users()
            .messages()
            .send(userId="me", body={"raw": raw_message})
            .execute()
        )
        print(f"📧 Email sent! Message ID: {message['id']}")

        # Send WhatsApp notification
        whatsapp_message = f"📧 New Email Sent!\nSubject: {subject}\nMessage: {message_text}"
        send_whatsapp_message(whatsapp_message)

    except Exception as e:
        print(f"❌ An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    sender_email = "jmarrero3499@gmail.com"
    receiver_email = "jmarrero3499@gmail.com"
    subject = "Email & WhatsApp Notification"
    message_body = "This is a test email that also sends a WhatsApp notification!"

    send_email(sender_email, receiver_email, subject, message_body)
