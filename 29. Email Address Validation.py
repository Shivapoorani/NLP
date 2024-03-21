import re
def validate_email(email):
     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
     if re.match(pattern, email):
        return True
     else:
        return False

def extract_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)
if __name__ == "__main__":
    sample_text = "Contact us at support@example.com or info@company.com for assistance."
    email_addresses = extract_emails(sample_text)
    for email in email_addresses:
        print("Email:", email)
        print("Valid:", validate_email(email))
