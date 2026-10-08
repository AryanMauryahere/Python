import email
import re

def extract_forensics(raw_email_content):
    # 1. Parse the raw email string into an email object
    msg = email.message_from_string(raw_email_content)
    
    # 2. Grab the easy, visible headers
    sender = msg.get("From")
    subject = msg.get("Subject")
    date = msg.get("Date")
    
    # 3. Pull ALL the hidden "Received" routing headers
    # get_all() returns a list because an email usually has multiple Received headers
    received_headers = msg.get_all("Received") 
    
    # 4. Set up a Regular Expression (Regex) pattern to find IPv4 addresses
    ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
    routing_ips = []
    
    if received_headers:
        for header in received_headers:
            # Search the header text for anything matching an IP format
            found_ips = ip_pattern.findall(header)
            routing_ips.extend(found_ips)
            
    # Remove duplicates but keep the data clean
    unique_ips = list(set(routing_ips))
    
    return {
        "Sender": sender,
        "Subject": subject,
        "Date": date,
        "Found_IPs": unique_ips
    }

# --- How to test it ---
dummy_email = """From: boss@yourcompany.com
To: employee@yourcompany.com
Subject: URGENT: Wire Transfer Required
Date: Sat, 22 Aug 2026 10:00:00 +0000
Received: from mail.suspicious-server.net (198.51.100.14) by yourcompany.com
Received: from [10.0.0.5] (hacker-machine.local [203.0.113.50])

Please send the money immediately."""

results = extract_forensics(dummy_email)
print(results)