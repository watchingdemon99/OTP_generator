import unittest
import re
from mail_otp_functional_decomposition import generate_otp
from mail_otp_functional_decomposition import send_email 
from mail_otp_functional_decomposition import verify_otp
class TestOTPFunctions(unittest.TestCase):
    def test_generate_otp(self):
        # Test if the function returns a 6-digit OTP
        otp = generate_otp()
        self.assertEqual(len(str(otp)), 6)

        # Test if the OTP returned is a number
        self.assertIsInstance(otp, int)

        # Test if the OTP returned is within the range of 100000 and 999999
        self.assertTrue(100000 <= otp <= 999999)

  
    def test_verify_otp(self):
        # Test if the function prompts the user to enter the OTP
        otp = "123"
        user_otp = "123"
            # Test if the function returns True when the correct OTP is entered
        self.assertTrue(verify_otp(user_otp,otp))

        
        # Test if the function returns False when an incorrect OTP is entered
        self.assertFalse(verify_otp('123456',otp))
        
    def test_valid_email(self):
        reciever_mail = "prajwaltupare@gmail.com"
        self.assertTrue(is_valid_email(reciever_mail))

def is_valid_email(email):
    regex = '^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$'
    if re.search(regex, email):
        return True
    else:
        return False

if __name__ == '__main__':
    unittest.main()
