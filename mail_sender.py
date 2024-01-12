import requests
import configparser

# Load API Key from a configuration file
config = configparser.ConfigParser()
config.read('config_mailgun.ini')

# Mailgun API settings
API_KEY = config.get('DEFAULT', 'API_KEY')
DOMAIN = config.get('DEFAULT', 'DOMAIN')


def send_email(sender_email, recipient_email, subject, message):
    # Mailgun API endpoint
    MAILGUN_API_URL = f'https://api.mailgun.net/v3/{DOMAIN}/messages'

    # Create a dictionary with the email data
    email_data = {
        'from': sender_email,
        'to': recipient_email,
        'subject': subject,
        'html': message
    }

    # Send the email using Mailgun's API
    response = requests.post(MAILGUN_API_URL, auth=('api', API_KEY), data=email_data)

    # Check the response
    if response.status_code == 200:
        print(f"Email sent successfully to {recipient_email}")
    else:
        print(f"Email delivery failed. Status code: {response.status_code}")
        print(response.text)

if __name__ == '__main__':
    sender_email = 'bruno.rodriguez.sep@gmail.com'
    recipient_email = 'brunors1204@gmail.com'
    subject = 'Hello from Mailgun'
    message = 'This is a test email sent from Mailgun via Python.'

    send_email(sender_email, recipient_email, subject, message)
