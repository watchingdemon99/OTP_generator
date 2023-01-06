import random
import smtplib

def generate_otp():
    """Generate a 6-digit OTP"""
    return random.randint(100000, 999999)

def send_email(otp, email_id):
    """Send an email with the OTP to the given email address"""
    msg = f"{otp} is your OTP"
    sender_email = 'prajwaltupare@gmail.com'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("prajwaltupare@gmail.com", "password")
    server.sendmail(sender_email, email_id, msg)

def verify_otp(user_input,otp):
    """Prompt the user to enter the OTP and verify it"""

    if user_input == otp:
        return True
    else:
        return False

def main():
    """Send the OTP to the user's email and verify it"""
    otp = str(generate_otp())
    email_id = input("Enter your email: ")
    user_input = input("Enter Your OTP >>:")
    send_email(otp, email_id)
    if(verify_otp(otp,user_input)):
        print("OTP veriied")
    else:
        print("Please Check your OTP again")
        print("Press\n 1 To retry \n 2 To resend OTP \n 3 To Stop")
        choice = input("Enter you choice")
        if choice == 1:
            otp_verification(otp)
        elif choice == 2:
            main()
        else:
            print("Thank You!")
    

if __name__ == "__main__":
    main()  
