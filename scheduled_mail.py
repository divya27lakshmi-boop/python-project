import os
import smtplib
import time
from datetime import datetime
from email.message import EmailMessage

sender_email = "mdivya07kumar@gmail.com"
sender_password = "ukhtxerwztntjiky"

receiver_email = "mdivya07kumar@gmail.com"

file_path = r"C:\Users\Muthu\Desktop\sample.docx"

send_hour = 14      
send_minute = 39   

print("⌛ Waiting for scheduled time...")

while True:

    now = datetime.now()

    current_hour = now.hour
    current_minute = now.minute

    if current_hour == send_hour and current_minute == send_minute:

        print("✅ Time matched! Sending Mail...")


        msg = EmailMessage()

        msg["Subject"] = "Scheduled Mail with Attachment"
        msg["From"] = sender_email
        msg["To"] = receiver_email

        msg.set_content(
            "Hi,\n\n"
            "This mail was sent automatically at scheduled time."
        )

        
        with open(file_path, "rb") as f:
            file_data = f.read()

        msg.add_attachment(
            file_data,
            maintype="application",
            subtype="octet-stream",
            filename=os.path.basename(file_path)
        )

        # Send Mail
        with smtplib.SMTP("smtp.gmail.com", 587) as server:

            server.starttls()

            server.login(sender_email, sender_password)

            server.send_message(msg)

        print("🎉 Mail Sent Successfully!")

        break

    # Wait 30 seconds before checking again
    time.sleep(30)
