import requests
import json
import os


# Load credentials from JSON file
def load_config():
    with open("whatsapp_data.json", "r") as file:
        return json.load(file)


config = load_config()

ACCESS_TOKEN = config["ACCESS_TOKEN"]
PHONE_NUMBER_ID = config["PHONE_NUMBER_ID"]
RECIPIENT_PHONE = config["RECIPIENT_PHONE"]


# Function to send WhatsApp message
def send_whatsapp_message(message):
    url = f"https://graph.facebook.com/v18.0/{PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "to": RECIPIENT_PHONE,
        "type": "text",
        "text": {"body": message}
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("✅ WhatsApp message sent successfully!")
    else:
        print(f"❌ Error sending message: {response.text}")


# Example usage
if __name__ == "__main__":
    test_message = "Hello, this is a test message from WhatsApp Cloud API!"
    send_whatsapp_message(test_message)
