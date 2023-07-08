import smtplib
from email.message import EmailMessage
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SMTPHelper():
    def __init__(self, sender, password) -> None:
        self.sender = sender
        self.password = password

    def send_email(self, email, subject, body):
        try:
            msg = EmailMessage()
            msg['Subject'] = subject
            msg['From'] = self.sender
            msg['To'] = email
            msg.set_content(body)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(self.sender, self.password)
                smtp.send_message(msg)
        except:
            print("Error while sending mail to " + email)

    def send_welcome_mail(self, email):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Welcome to Brainbrew!"
        msg['From'] = self.sender
        msg['To'] = email

        # Create the body of the message (a plain-text and an HTML version).
        html = f"""\
<html>

<head></head>

<body>
    <p
        style="font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">
        Dear {email.split("@")[0]},<br/>
        <br/>
        I am Zac Hana, co-founder of Brainbrew, an AI-enabled learning platform that is designed to make learning more
        efficient, personalised, and enjoyable. On behalf of our team, I want to welcome you to the Brainbrew community.
        <br/>
        <br/>

        To join our community:<br/>
        - Discord<br/>
        - TikTok<br/>
        - Instagram<br/>
        - Twitter<br/>
        <br/>

        We believe that everyone has the potential to learn and grow, and our platform is designed to help you unlock
        your full potential. Whether you are looking to learn a new skill, prepare for an exam, or simply expand your
        knowledge, Brainbrew has everything you need to succeed.
        <br/>
        <br/>
        As a new member of the Brainbrew community, you will have access to a wide range of features, including
        personalised learning paths, real-time feedback, interactive lessons, and much more. Our AI-powered platform
        will analyse your learning preferences, strengths, and weaknesses to provide you with a customized learning
        experience that is tailored to your needs.
        <br/>
        <br/>

        We are committed to helping you achieve your learning goals, and our team is always here to support you. If you
        have any questions, comments, or suggestions, please don't hesitate to reach out to us at support@brainbrew.com.
        <br/>
        <br/>

        Thank you for joining us on this exciting journey, and we look forward to helping you unleash your full
        potential.
        <br/>
        <br/>

        Best regards,<br/>
        Zac Hana<br/>
        Co-founder, Brainbrew<br/>
    </p>
</body>

</html>
        """

        msg.attach(MIMEText(html, 'html'))

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.sender, self.password)
            smtp.send_message(msg)

    def send_password_reset_mail(self, email, password_token):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Password Reset for Your Brainbrew Account."
        msg['From'] = self.sender
        msg['To'] = email

        # Create the body of the message (a plain-text and an HTML version).
        html = f"""\
        <html>
        <head></head>
        <body>
            Dear {email},<br/>
            <br/>
            I hope this email finds you well. I am Zac Hana, co-founder of Brainbrew, an AI-enabled learning platform that is transforming the way people learn.<br/>
            <br/>
            We have noticed that you have recently requested a password reset for your Brainbrew account. If you have not made this request, please ignore this email. However, if you did request a password reset, please follow the link below to reset your password.<br/>
            <br/>
            https://beta.brainbrew.io/reset-password?token={password_token}
            <br/>
            <br/>
            Please note that the password reset link is only valid for 24 hours. If you don't reset your password within that time frame, you will need to request another password reset.<br/><br/>

            If you continue to have issues logging in or resetting your password, please don't hesitate to contact our support team at support@brainbrew.com.<br/><br/>

            Thank you for using Brainbrew, and we look forward to helping you on your learning journey.<br/><br/>

            Best regards,<br/><br/>

            Zac Hana<br/>
            Co-founder, Brainbrew<br/>

        </body>
        </html>
        """

        msg.attach(MIMEText(html, 'html'))

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.sender, self.password)
            smtp.send_message(msg)
