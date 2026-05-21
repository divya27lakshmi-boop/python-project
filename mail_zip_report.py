import imaplib
import email
import smtplib
import zipfile
from email.message import EmailMessage

# Gmail Details
EMAIL = "mdivya07kumar@gmail.com"
PASSWORD = "ukhtxerwztntjiky"

# Connect to Gmail Inbox
mail = imaplib.IMAP4_SSL("imap.gmail.com")

mail.login(EMAIL, PASSWORD)

mail.select("inbox")

# Get ALL mails
status, messages = mail.search(None, "ALL")

mail_ids = messages[0].split()

total_mails = len(mail_ids)

print("Total Inbox Mail Count:", total_mails)

# Create Text Report
report_file = "mail_report.txt"

with open(report_file, "w", encoding="utf-8") as f:

    f.write(f"Total Inbox Mails: {total_mails}\n\n")

    # Last 10 mails details
    for num in mail_ids[-10:]:

        status, data = mail.fetch(num, "(RFC822)")

        raw_email = data[0][1]

        msg = email.message_from_bytes(raw_email)

        subject = msg["Subject"]

        sender = msg["From"]

        if subject is None:
            subject = "No Subject"

        f.write(f"From: {sender}\n")
        f.write(f"Subject: {subject}\n")
        f.write("-" * 50 + "\n")

print("✅ Text file created")

# Create ZIP File
zip_file = "mail_report.zip"

with zipfile.ZipFile(zip_file, "w") as zipf:

    zipf.write(report_file)

print("✅ ZIP file created")

# Create Mail
msg = EmailMessage()

msg["Subject"] = "Inbox Mail ZIP Report"
msg["From"] = EMAIL
msg["To"] = EMAIL

msg.set_content(
    "Hi,\n\n"
    "Attached is your Inbox Mail ZIP Report."
)

# Attach ZIP File
with open(zip_file, "rb") as f:

    file_data = f.read()

msg.add_attachment(
    file_data,
    maintype="application",
    subtype="zip",
    filename=zip_file
)

# Send Mail
with smtplib.SMTP("smtp.gmail.com", 587) as server:

    server.starttls()

    server.login(EMAIL, PASSWORD)

    server.send_message(msg)

print("🎉 ZIP file mailed successfully!")

# Logout
mail.logout()
