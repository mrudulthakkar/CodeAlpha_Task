import re

# Regex pattern to match emails
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}"

with open("contain_emails.txt", "r", encoding="utf-8") as f1, open("emails.txt", "w", encoding="utf-8") as f2:
    text = f1.read()                          # read the whole file
    emails = re.findall(pattern, text)        # extract all emails
    
    

    for email in set(emails):
        f2.write(email + "\n")                # write each email

print("Done. Emails saved in emails.txt")
