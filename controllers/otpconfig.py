from models.main import Model
from views.main import View

import customtkinter
from PIL import Image

import sqlite3
import segno
import pyotp
import os


class OtpController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["otpconfig"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.cancel_btn.configure(command=self.home)

    def home(self) -> None:
        self.view.switch("home")
        self.update_qr_code()

    def generate_otp(self) -> None:
        current_user = self.model.auth.current_user

        print("Generating OTP")
        if current_user:
            try:
                # Verify if the user already has a secret key
                mydb = sqlite3.connect("test.db")
                mycursor = mydb.cursor()
                sql = "SELECT otp_key FROM users WHERE username = ?"
                val = (current_user["username"],)
                mycursor.execute(sql, val)
                result = mycursor.fetchone()  # Use fetchone() to get a single result
                print("fetching otp key")                

                if result and result[0]:  # Check if result is not empty and has a valid OTP key
                    otp_key = result[0]
                    print("otp key found")
                    print("otp key is " + otp_key)
                    qr = segno.make(f"otpauth://totp/{current_user['username']}?secret={otp_key}&issuer=MSInnov")
                    print(qr)
                    qr.save("otp.png")
                    self.update_qr_code()
                else:
                    print("otp key not found")
                    username = current_user["username"]
                    # Generate a random secret key for the user
                    otp_key = pyotp.random_base32()
                    # Generate a QR code for the user
                    print("Generating QR code")
                    qr = segno.make(f"otpauth://totp/{username}?secret={otp_key}&issuer=MSInnov")
                    qr.save("otp.png")
                    self.update_qr_code()
                    # Save the secret key to the database
                    print("Saving secret key to the database")
                    sql = "UPDATE users SET otp_key = ? WHERE username = ?"
                    val = (otp_key, username)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print("Secret key saved to the database")
            except sqlite3.Error as e:
                print(f"An error occurred: {e}")
            finally:
                mydb.close()  # Ensure the database connection is closed
                
    def update_qr_code(self) -> None:
        # Suppress old QR code image
        self.frame.qr_code_label.configure(image=None)
        self.frame.qr_code_label.image = None
        current_path = os.path.dirname(os.path.realpath(__file__))
        image_path = current_path + "../../otp.png"
        pil_image = Image.open(image_path)
        
        # Convert the PIL image to CTkImage
        new_qr_code_image = customtkinter.CTkImage(pil_image, size=(250, 250))
        
        # Update the image in the label
        self.frame.qr_code_label.configure(image=new_qr_code_image)
        self.frame.qr_code_label.image = new_qr_code_image
    
            
            


