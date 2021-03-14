# Smart Fit Booking

Website bot to book an hour in the Smart Fit gym and send QR code via WhatsApp automatically.

<p align="center">
<img src="https://blog.smartfit.com.mx/wp-content/uploads/2020/10/gimnasio-smart-fit-mi-plan.png">
</p>

## Environment variables

Here it's important to know the way to fill the .env files:

- **DRIVER_PATH**: It means the directory where the chromedriver is located in the computer.
- **OUTPUT_PATH**: Directory where the QR code will be saved temporary before sending to WhatsApp.
- **WEBSITE_URL**: In this case is https://www.smartfitreserva.com/login.
- **IDENTIFICATION**: That's the field of your identification number.
- **PASSWORD**: That's the password you registered in Smart Fit previously.
- **HEADQUARTER_NAME**: It's the name of the headquarter, e.g san ignacio.
- **DESIRED_DATE**: That's the date I want to book, e.g 14/03/2020.
- **DESIRED_TIME**: It is in 24 hour format, e.g I want to book at 3:00 PM, I must write 15:00.
- **WHATSAPP_URL**: In this case is https://web.whatsapp.com/.
- **CHAT_NAME**: It's the name of chat that you want to receive the WhatsApp message.
- **PERSON_NAME**: It just indicates the person name who books an hour in the gym.
- **CHROME_PROFILE_PATH**: It means the directory where the chrome profile will be saved to avoid scan the WhatsApp QR Code next time you want to book an hour in the gym.

## How to run

    $ pip install -r requirements.txt
    $ export ENV=production
    $ python main.py