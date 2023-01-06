import random
import smtplib


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("prajwaltupare@gmail.com", "password")

def generate_otp():
    otp = random.randint(100000, 999999)
    return otp


def send_email(msg, email_id):
    sender_email = 'prajwaltupare@gmail.com'
    server.sendmail(sender_email, email_id, msg)


def otp_verification(otp):
    user_input = input("Enter Your OTP >>:")
    if user_input == otp:
        print("Verified")
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


def main():
    otp = str(generate_otp())
    msg = otp + " is your OTP"
    email_id = input("Enter your email: ")
    send_email(msg, email_id)
    otp_verification(otp)

if __name__ == "main":
    main()  
    
