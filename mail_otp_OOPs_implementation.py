import random
import smtplib

class OTPVerification:
    def __init__(self):
        self.otp = None
        self.email_id = None
    
    def generate_otp(self):
        """Generate a 6-digit OTP"""
        self.otp = random.randint(100000, 999999)
    
    def send_email(self):
        """Send an email with the OTP to the given email address"""
        msg = f"{self.otp} is your OTP"
        sender_email = 'prajwaltupare@gmail.com'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("prajwaltupare@gmail.com", "lzmetvnxubglxicv")
        server.sendmail(sender_email, self.email_id, msg)
    
    def verify_otp(self):
        """Prompt the user to enter the OTP and verify it"""
        user_input = int( input("Enter Your OTP >>:"))
        return user_input == self.otp
    
    def main(self):
        """Send the OTP to the user's email and verify it"""
        self.email_id = input("Enter your email: ")
        self.generate_otp()
        self.send_email()
        if(self.verify_otp()):
            print("OTP veriied")
        else:
            print("Incorrect OTP")
            
        

if __name__ == "__main__":
    verification = OTPVerification()
    verification.main()
