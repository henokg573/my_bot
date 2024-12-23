from flask import Flask, request
import telebot
from telebot import types
from telegram.ext import CommandHandler, Updater
import os
from telebot.types import ForceReply
import telegram
from telebot import types
from keep_alive import keep_alive
keep_alive()



# Replace with your API key
API_KEY = '7927894477:AAEFQKCEqdHgLs6fnx6ZyaH1Za0pWyiAALI'
bot = telebot.TeleBot(API_KEY)

# Admin's chat ID (replace with the actual admin chat ID)
ADMIN_CHAT_ID = '793034140'  # You should use your actual chat ID here

bot = telebot.TeleBot(token=os.environ.get("API_KEY"))

app = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(f"Received /start from {message.chat.id}")  # Debugging

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton('Scholarship and admission opportunities')
    btn2 = types.KeyboardButton('Ethiopian Passport application')
    btn3 = types.KeyboardButton('Early US Embassy appointment worldwide')
    btn4 = types.KeyboardButton('E-commerce')
    btn5 = types.KeyboardButton('Online courses')
    btn6 = types.KeyboardButton('International English proficiency tests')
    btn7 = types.KeyboardButton('E-Visa applications')
    btn8 = types.KeyboardButton('International payments')
    btn9 = types.KeyboardButton('International career opportunities')
    btn10 = types.KeyboardButton('Recommend educational travel consultancies')
    btn11 = types.KeyboardButton('Assistance with any Embassy interview practice assistance')
    btn12 = types.KeyboardButton('About Us')
    btn13 = types.KeyboardButton('Feedback')
    # btn14 = KeyboardButton('services')
    # btn15 = KeyboardButton('Continue')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13)
    # markup.add(btn12, btn13, btn14, btn15)


    bot.reply_to(
        message,
        f"""👋 Hi {message.chat.first_name}! 
        👋 Welcome to EasyGate!, 
        welcome to Your 
                        \t\t\t\t\tGateway to Global Opportunities.
                        \t\t\t\t\tSimplifying Your Path to Success.
                        \t\t\t\t\tFrom Dreams to Destinations.
                        \t\t\t\t\tOpen Doors, Easy Journeys.
We’re thrilled to have you here! 🎉

At EasyGate, we specialize in making your goals more accessible, whether it’s education, travel, or career growth. Here's what we can help you with:
            📚 Scholarship and admission opportunities
            🌍 Passport and visa applications
            💼 International career and e-commerce services
            ✈️ Embassy appointments and travel consultancy
            🎓 Online courses and proficiency tests

Let us guide you every step of the way! Simply explore the options below and get started on your journey with us.

Feel free to reach out if you have any questions—we’re here to make things easy for you!
        \n\nSelect a service to proceed:""",
        reply_markup=markup,

        
    )
   


    # Guide Command
@bot.message_handler(commands=['guide'])
@bot.message_handler(func=lambda message: message.text == "Guide")
def send_guide(message):
    bot.reply_to(
        message,
        """📖 **Guide to EasyGate**:
1️⃣ Choose a service from the menu (e.g., 'Scholarship', 'E-commerce').
2️⃣ Follow instructions provided for each service.
3️⃣ Use 'Payment' to handle transactions securely.

Explore and simplify your journey with EasyGate! 🌟""", reply_markup = back_to_main_menu_markup()
    )
# Payment command
@bot.message_handler(commands=['payments'])
@bot.message_handler(func=lambda message: message.text == "Payments")
def initiate_payment(message):
    bot.reply_to(
        message,
        """💳 **Payment Instructions**:
1️⃣ Select the service you wish to pay for.
2️⃣ Use secure payment methods as provided.
3️⃣ Confirm your transaction and keep the receipt.

Now, let us know which service you are paying for.""", reply_markup = payment_main_menu_markup()
    )



@bot.message_handler(func=lambda message: True)
def handle_options(message):
    print(f"Message received: {message.text}")  # Debugging
    service_selected = message.text  # Define service_selected
    if message.text == 'Scholarship and admission opportunities':
        bot.reply_to(message, """Scholarship and Admission Opportunities

Explore the latest scholarships and admission openings for international and local universities.
✅ Fully funded scholarships
✅ Partial scholarships
✅ Admission tips and guidance for top universities worldwide

For more details, provide specific interests or countries of choice. 😊

Our services 
-Updating customers with scholarship and admission opportunities worldwide 

- Giving detailed informations about the admission(open and close dates, eligibility criteria, admission requirements, acceptance rate, application fee etc)

- Connecting customers directly with the University by giving the University's admission link 

- Paying any international payments related to the process(if needed)

-consulting in every step of your journey(reliable customer service)
                     
                     which country are you interested in?
""", 
reply_markup=scholarship_options_markup())
        







    elif message.text == 'Ethiopian Passport application':
        bot.reply_to(message, """🛂 Ethiopian Passport Application

📋 Note: We offer assistance with your Ethiopian Passport application! Here’s what we can help you with:

📝 Application Guidance – We’ll walk you through the entire passport application process.
📑 Document Checklist – Know exactly what documents you'll need (ID, proof of citizenship, etc.).
💳 Fee Information – Learn about the applicable fees and payment methods.
🌍 Where to Apply – Get details on the nearest Ethiopian embassy or consulate, or apply online.
🚶‍♂️ Step-by-Step Assistance – We'll provide you with easy-to-follow instructions and updates.
🔍 How to Get Started: Just follow the instructions and we’ll guide you through each step to get your passport application submitted!

                     **🛂 PASSPORT SERVICE FEES 🛂**

- **New Passport**:  
   - Price: 5,000 ETB  
   - Validity: 5 Years → 20,000 ETB | 2 Years → 25,000 ETB  

- **Passport Renewal**:  
   - Price: 5,000 ETB  
   - Validity: 5 Years → 20,000 ETB | 2 Years → 25,000 ETB  

- **Lost Passport Replacement**:  
   - Price: 5,000 ETB  
   - Validity: 5 Years → 20,000 ETB | 2 Years → 25,000 ETB  

- **Emergency Travel Document**:  
   - Price: 12,500 ETB  
   - Validity: 5 Years → 27,500 ETB | 2 Years → 32,500 ETB  

- **Change of Details/Amendment**:  
   - Price: 13,000 ETB  
   - Validity: 5 Years → 28,000 ETB | 2 Years → 33,000 ETB  

- **Special Passport (Official Purposes)**:  
   - Price: 20,500 ETB  
   - Validity: 5 Years → 35,500 ETB | 2 Years → 40,500 ETB  

For more information, visit our website:  
[🌐 Immigration and Citizenship Service](https://www.ics.gov.et)"""
                     , reply_markup=ethiopassport_options_markup())
        


    elif service_selected == 'Continue':
        bot.reply_to(message, """Thank you for your interest!

        We are currently open for registration! 
        The registration period will close on December 30th, and we will start providing services from January 1, 2025.

        Please complete your registration through the link below:
        [Registration Form](https://forms.gle/your-google-form-link)
        
        Don't miss the chance to be part of our services!""")
        


    elif message.text == 'New Passport application':
        bot.reply_to(message, """Thank you for choosing our service to assist you with your Ethiopian passport application! 🇪🇹

To get started, we require a service fee of [amount] to process your application and assist you throughout the entire process.

💸 **Payment Instructions:**
1. Please make the payment of [amount] to the following account: 
   Use the payment method that is most convenient for you.
2. After the payment is verified, we will send you a Google Form to collect your personal details and the required documents for your passport application.

Once your payment is confirmed, we will proceed with the application process and guide you every step of the way.

If you have any questions or need help with the payment process, don't hesitate to reach out. We're here to assist you!

Thank you for trusting us to assist you with your passport application. 🙏

Please let us know once the payment is made, and we'll proceed with sending the form to complete your application!
                     """, reply_markup=payment_options_markup())
        

    elif message.text == 'Renewal/Replacement appointment':
        bot.reply_to(message, """Thank you for choosing our service to assist you with your Ethiopian passport renewal or replacement! 🇪🇹

To proceed with your passport renewal or replacement, we require a service fee of [amount] to assist with booking your appointment and ensuring all required documents are in order.

💸 **Payment Instructions:**
1. Please make the payment of [amount] to the following account:
   - [Payment method or account details]
2. Once your payment is verified, we will schedule your appointment and provide further instructions.

After payment confirmation, you will receive an email with the appointment details and the required documents for your passport renewal or replacement. We will guide you through the entire process!

If you have any questions or need assistance with the payment process, feel free to reach out. We're here to help you every step of the way!

Thank you for trusting us with your passport renewal or replacement. 🙏

Once you've made the payment, please let us know, and we will proceed with the appointment scheduling and guide you through the next steps.
                     """, reply_markup=payment_options_markup())
    elif message.text == 'Lost/stolen Passport application appointment':
        bot.reply_to(message, """We're sorry to hear that your passport has been lost or stolen, and we're here to help you get it sorted out. 🌍✈️

To proceed with the application for a lost or stolen passport, we require a service fee of [amount] to assist you with the application process, reporting, and appointment scheduling.

💸 **Payment Instructions:**
1. Please make the payment of [amount] to the following account:
   - [Payment method or account details]
2. Once your payment is verified, we will guide you through the next steps and help you schedule an appointment for your passport replacement.

You will receive detailed instructions on the necessary documents, forms, and procedures for reporting your lost or stolen passport, as well as the steps to secure a new passport.

Our team will be here to assist you through each step, ensuring a smooth and swift process.

If you have any questions or need help with the payment process, don’t hesitate to contact us. We’re here to help you get your passport back! 🙏

Once your payment is confirmed, we'll send you further instructions and a Google form to complete the process
                     """, reply_markup=payment_options_markup())
    elif message.text == 'main menu':
        bot.reply_to(message, """Main Menu
                     """, reply_markup=back_to_main_menu_markup())
        
    elif message.text == 'Back':
        bot.reply_to(message, """Ethiopian Passport application
                     """, reply_markup=ethiopassport_options_markup())






    elif message.text == 'Early US Embassy appointment worldwide':
        bot.reply_to(message, """🇺🇸 Early US Embassy Appointment Worldwide

📋 Note: Our bot can help you secure an early appointment at a US Embassy anywhere in the world! Here’s what we offer:

📅 Appointment Scheduling – Get assistance with scheduling an early US visa appointment.
🛂 Visa Application Support – Receive guidance on filling out your visa application correctly.
📑 Document Preparation – We’ll provide a list of the required documents for your appointment.
🌍 Worldwide Service – No matter where you are, we can help you with the process.
🕒 Quick Response – We’ll help expedite your appointment as much as possible.
🔍 How to Get Started: Simply follow the instructions, and we will assist you in securing your US Embassy appointment quickly and easily.
""", reply_markup=earlyUS_options_markup())
        






    elif message.text == 'E-commerce':
        bot.reply_to(message, """🛒 E-commerce, Dropshipping and Online Marketing 🛒

We offer services to help you start and grow your online business.

Our services include:
- E-commerce platform setup
- Dropshipping business guidance
- Online marketing strategies

To get started, no payment is required! 

Feel free to explore our offerings and get in touch for further assistance:

1. Join our Telegram channel: [Your Channel Link]
2. Create your account in the mini app: [Your Mini App Link]
""", reply_markup=back_to_main_menu_markup())
        




    
    elif message.text == 'Online courses':
        bot.reply_to(message, """📚 Online Courses 📚
                    """, reply_markup=back_to_main_menu_markup())
        


    elif message.text == 'main menu':
        bot.reply_to(message, """📚 Online Courses 📚
                    """, reply_markup=back_to_main_menu_markup())






    elif message.text == 'International English proficiency tests':
        bot.reply_to(message, """🌍 International English Proficiency Tests

📋 Note: We can assist you with International English proficiency tests, helping you prepare and register for exams like TOEFL, IELTS, and more! Here's how we can support you:

📚 Test Information – Get detailed information on available English proficiency tests (e.g., TOEFL, IELTS).
📝 Registration Assistance – We’ll guide you through the registration process step-by-step.
🎯 Test Preparation – Access study materials and tips to help you ace your exam.
📅 Test Scheduling – Assistance with scheduling your test at available centers worldwide.
🌍 Worldwide Access – Whether you're in Africa, Europe, or anywhere else, we’ve got you covered!
🔍 How to Get Started: Simply follow the steps in our bot, and we’ll help you register, prepare, and schedule your English proficiency test with ease!
""", reply_markup=english_options_markup())






    elif message.text == 'Bank Transfer':
        bot.reply_to(message, """Please make the payment to the following account:
Bank Name: XYZ Bank
Account Number: 1234567890
SWIFT/BIC: ABCDEF123

Once you have made the payment, please send us the receipt (PDF or image).""")
        bot.reply_to(message, "Do you want to choose a different payment method or confirm payment? Select an option.", reply_markup=back_to_payment_markup())

    elif message.text == 'Telebirr':
        bot.reply_to(message, """Please use the following Telebirr number to make the payment:
Telebirr Number: 0912345678

Once you have made the payment, please send us the receipt (PDF or image).""")
        bot.reply_to(message, "Do you want to choose a different payment method or confirm payment? Select an option.", reply_markup=back_to_payment_markup())

    elif message.text == 'PayPal':
        bot.reply_to(message, """Please use the following PayPal account to make the payment:
PayPal Account: example@paypal.com

Once you have made the payment, please send us the receipt (PDF or image).""")
        bot.reply_to(message, "Do you want to choose a different payment method or confirm payment? Select an option.", reply_markup=back_to_payment_markup())

    elif message.text == 'Already Paid? (Submit receipt)':
        bot.reply_to(message, """Please send your payment receipt (PDF or image) to confirm your payment.""")
        # Save the user receipt or process further to verify the payment with the admin
        bot.register_next_step_handler(message, process_receipt)

    elif message.text == 'Choose Different Payment Method':
        bot.reply_to(message, """Payment options:
""", reply_markup=payment_options_markup())




    elif message.text == 'E-Visa applications':
        bot.reply_to(message, """🌍 E-Visa Applications

📋 Information:

We can assist you with E-Visa applications for various countries. Whether you're applying for a tourist, business, or other types of visas, we guide you through the entire online application process.

Here’s how we can help you:

🌐 Choose Your Destination – Get information about the countries offering e-Visas and determine your eligibility.
📝 Application Process – We'll guide you step-by-step in filling out the e-Visa application form.
📑 Document Submission – Assistance with submitting required documents, such as your passport, photos, and other necessary paperwork.
💳 Payment Guidance – We’ll explain the payment methods and fees for e-Visa applications.
📅 Application Status – Track your e-Visa status and provide updates on approvals and rejections.
📞 Contact Us:

For personalized assistance or any questions regarding your e-Visa application, feel free to contact us:

    - Telegram: @easygate
   - Phone: 0964255107
   - Email: contact.easygate@gmail.com
   - WhatsApp: [Insert WhatsApp link]
   - Instagram: @easygate_internationalm
                     """, reply_markup=back_to_main_menu_markup())
        




    elif message.text == 'International payments':
        bot.reply_to(message, """🌍 International Payments

📋 Information:

We provide assistance with international payments, ensuring you can send or receive money across borders with ease. Whether you need help with currency exchange, wire transfers, or digital payments, we’re here to make the process simple and secure.

Here’s how we can assist you:

💸 Payment Methods – Learn about different international payment methods (e.g., PayPal, bank transfers, money transfer services).
💱 Currency Exchange – Get information on the best exchange rates for transferring money globally.
🌐 Global Transfers – We’ll help you navigate cross-border payments and ensure they’re processed smoothly.
🔒 Security and Protection – We provide tips on ensuring your international payments are safe and secure.
💳 Payment Tracking – Assistance with tracking your international payments and managing transactions.
📞 Contact Us:

For more details or if you need personalized assistance with your international payments, feel free to contact us:

    - Telegram: @easygate
   - Phone: 0964255107
   - Email: contact.easygate@gmail.com
   - WhatsApp: [Insert WhatsApp link]
   - Instagram: @easygate_internationalm
We’re here to ensure your payments are processed quickly and securely!
                    """, reply_markup=back_to_main_menu_markup())




    elif message.text == 'International career opportunities':
        bot.reply_to(message, """🌍 International Career Opportunities

📋 Information:

Looking for career opportunities abroad? We provide detailed support for those seeking international job openings in various fields across the globe. Whether you’re looking for work in North America, Europe, Asia, or beyond, we’re here to guide you in the right direction.

Here’s how we can assist you:

💼 Job Listings – Access information about international job vacancies in multiple industries.
🌎 Global Opportunities – Explore career options in various countries and regions.
📝 Application Guidance – Get help with job applications, CV/resume writing, and interview tips.
🌐 Remote Jobs – We also provide details on remote job opportunities that allow you to work from anywhere in the world.
💼 Work Visa Support – Receive assistance with understanding visa requirements and application processes for working abroad.
🔗 For More Details: Join our dedicated Telegram channel for continuous updates and detailed information on international career opportunities:

👉 Join our Telegram Channel

📞 Contact Us:

For personalized assistance or if you have any questions, feel free to contact us directly:

   - Telegram: @easygate
   - Phone: 0964255107
   - Email: contact.easygate@gmail.com
   - WhatsApp: [Insert WhatsApp link]
   - Instagram: @easygate_internationalm
We’re here to help you take the next step in your global career!
                    """, reply_markup=back_to_main_menu_markup())
        


    elif message.text == 'Recommend educational travel consultancies':
        bot.reply_to(message, """🌍 Recommend Educational Travel Consultancies

📋 Information:

We specialize in recommending educational travel consultancies to help you achieve your academic goals abroad. Whether you’re looking to study in Europe, North America, or other destinations, we connect you with trusted agencies that will guide you every step of the way.

Here’s how we can assist you:

🎓 Study Abroad Options – Get information on various study abroad programs and opportunities in top universities.
🌍 Consultancy Recommendations – We recommend trusted educational consultancies that can help you plan your studies overseas.
📝 Application Process – Get expert advice on applying to universities, scholarships, and visas for studying abroad.
🌐 Destinations – Learn about the best countries and institutions for international education.
🤝 Personalized Guidance – We’ll help connect you with consultancies that offer personalized support for your educational journey.
🔗 For More Details: Join our Telegram channel for detailed information and updates on recommended educational travel consultancies:

👉 Join our Telegram Channel

📞 Contact Us:

If you have any questions or would like personalized assistance, don’t hesitate to reach out to us:

    - Telegram: @easygate
   - Phone: 0964255107
   - Email: contact.easygate@gmail.com
   - WhatsApp: [Insert WhatsApp link]
   - Instagram: @easygate_internationalm
We’re here to help you connect with the right consultancies for your academic journey!
                    """, reply_markup=back_to_main_menu_markup())
        
    



    elif message.text == 'Assistance with any Embassy interview practice assistance':
        bot.reply_to(message, """🎤 Assistance with Any Embassy Interview Practice

📋 Information:

Preparing for an embassy interview can be stressful, but we’re here to help you succeed! Whether you’re applying for a visa to the US, Canada, UK, or any other country, our interview practice sessions are designed to boost your confidence and ensure you’re well-prepared.

Here’s how we can assist you:

🎯 Mock Interviews – We offer mock embassy interviews tailored to the specific visa you’re applying for, simulating the real interview environment.
📝 Personalized Guidance – Get expert feedback on how to improve your answers, body language, and overall presentation.
📚 Visa-Specific Tips – We provide tips and strategies based on the type of visa you're applying for, whether it's a tourist, student, or work visa.
🌍 Country-Specific Preparation – Understand the specific requirements and expectations of the embassy you’ll be interviewing with.
💬 Confidence Building – We help you improve your communication skills to present yourself clearly and confidently during the interview.
                     
📞 Contact Us:

For personalized assistance or if you need more information about embassy interview practice, feel free to contact us:

   - Telegram: @easygate
   - Phone: 0964255107
   - Email: contact.easygate@gmail.com
   - WhatsApp: [Insert WhatsApp link]
   - Instagram: @easygate_international
We’re here to help you succeed in your embassy interview and secure your visa!
                    """, reply_markup=educational_options_markup())  
                

    elif service_selected == 'Study visa interview':
        bot.reply_to(message, """🎓 **Study Visa Interview Assistance**

Preparing for your study visa interview can be stressful, but we're here to make it easy for you.

We offer:
1️⃣ **Mock Interviews**: We will simulate a real interview environment to help you practice your responses.
2️⃣ **Guidance on Common Questions**: We'll guide you on the types of questions typically asked in a study visa interview and how to answer them confidently.
3️⃣ **Document Review**: We'll help you ensure your documents are in order for the interview.
4️⃣ **Personalized Coaching**: Tailored advice to help you improve your presentation and communication skills.

📞 **Contact Us**: Reach us via any of these platforms for more details:
   - Telegram: @easygate
   - Phone: 0964255107
   - Email: contact.easygate@gmail.com
   - WhatsApp: [Insert WhatsApp link]
   - Instagram: @easygate_international

💳 **Payment**: A small fee is required for our interview preparation services. After contacting us, we’ll send you the payment details, and once the payment is confirmed, we’ll schedule your mock interview and coaching sessions.

We are committed to making sure you're fully prepared!

Click below to proceed with payment:
""", reply_markup=payment_options_markup())

    elif service_selected == 'Work visa interview':
        bot.reply_to(message, """💼 **Work Visa Interview Assistance**

We understand how important your work visa interview is, and we're here to help you succeed!

Our services include:
1️⃣ **Mock Interviews**: We'll conduct mock interviews to help you feel more confident.
2️⃣ **Role-Playing Scenarios**: We will create real-world work visa interview scenarios to practice your responses.
3️⃣ **Resume & Cover Letter Review**: We’ll help you refine your resume and cover letter for the interview.
4️⃣ **Visa Requirements**: We’ll guide you on the specific documents and requirements for a successful work visa interview.

📞 **Contact Us**: You can reach us through:
   - Telegram: @easygate
   - Phone: 0964255107
   - Email: contact.easygate@gmail.com
   - WhatsApp: [Insert WhatsApp link]
   - Instagram: @easygate_international

💳 **Payment**: A fee applies for our interview preparation services. Please get in touch with us, and we will send you the payment information. Upon payment confirmation, we will schedule your mock interviews and coaching sessions.

We’re here to ensure you ace your interview!

Click below to proceed with payment:
""", reply_markup=payment_options_markup())

    elif service_selected == 'Visitor Visa Interview':
        bot.reply_to(message, """✈️ **Visitor Visa Interview Assistance**

Preparing for your visitor visa interview is crucial, and we're here to help you get it right.

Here’s what we offer:
1️⃣ **Interview Simulations**: Practice with mock interviews to gain confidence and improve your answers.
2️⃣ **Visa Document Preparation**: We’ll guide you through the visa documents and help ensure they meet all the requirements.
3️⃣ **Visa Interview Questions**: Learn the most common questions asked during a visitor visa interview and how to answer them.
4️⃣ **Professional Coaching**: Receive personalized coaching to improve your presentation and increase your chances of approval.

📞 **Contact Us**: You can reach us via:
   - Telegram: @easygate
   - Phone: 0964255107
   - Email: contact.easygate@gmail.com
   - WhatsApp: [Insert WhatsApp link]
   - Instagram: @easygate_international

💳 **Payment**: A small fee is required for our preparation services. Once you reach out, we will send you the payment details. After payment confirmation, we’ll schedule your mock interview session.

We’re committed to your success!

Click below to proceed with payment:
""", reply_markup=payment_options_markup())

    elif service_selected == 'Other':
        bot.reply_to(message, """🌍 **Other Embassy Interview Assistance**

If you're preparing for a visa interview not listed here, we can still help!

Our services include:
1️⃣ **Customized Mock Interviews**: We can simulate the specific type of interview you're preparing for.
2️⃣ **Document Review**: We’ll help you make sure you have the necessary documents in order.
3️⃣ **Tailored Coaching**: Receive advice and coaching specific to your type of interview and the country you’re applying to.
4️⃣ **Guidance on Interview Protocol**: We’ll provide tips on what to expect and how to present yourself confidently.

📞 **Contact Us**: You can reach us through:
   - Telegram: @easygate
   - Phone: 0964255107
   - Email: contact.easygate@gmail.com
   - WhatsApp: [Insert WhatsApp link]
   - Instagram: @easygate_international

💳 **Payment**: A fee applies for our services. Contact us to receive payment details. After payment is confirmed, we’ll arrange your mock interviews and coaching sessions.

We are here to help you succeed in any embassy interview!

Click below to proceed with payment:
""", reply_markup=payment_options_markup())

                
    


    elif message.text == 'About Us':
        bot.reply_to(message, """
                     Welcome to EasyGate! 

    We are a team of young Ethiopians, currently studying and working across the globe. Our mission is to simplify the process of accessing international education and career opportunities by reducing costs and eliminating the need for expensive intermediaries. 

    We aim to make services that can be accessed easily from home, such as visa applications, scholarship opportunities, and career guidance, more affordable and accessible to you.

    At EasyGate, we're dedicated to guiding you through every step of your global journey, whether it's education, work, or travel. Let us help you unlock your future, right from the comfort of your home!.
    Stay connected with us on our social media platforms to explore our services further:

    📱 Telegram: [@easygate](https://t.me/easygate)
    📱 WhatsApp: [0964255107](https://wa.me/0964255107)
    📸 Instagram: [@easygate](https://www.instagram.com/easygate)
    💼 Facebook: [EasyGate](https://www.facebook.com/easygate)
    📧 Email: easygate@example.com

    Feel free to contact us via any of the platforms above for more information or to get started! 
    """)



    elif message.text == 'America':
        bot.reply_to(message, """"🎓 **Welcome to the American Scholarships Program!** 
            Are you dreaming of studying in the USA? 🌟 We've got you covered! Here’s how we can help:
            ✅ Access exclusive scholarship opportunities for various fields and levels of study.
            ✅ Get personalized guidance on scholarship applications and admissions.
            ✅ Receive resources for preparing for international English exams (IELTS, TOEFL, etc.).
            ✅ Explore links to trusted channels, apps, and tools for detailed scholarship insights.
            ✅ Contact our experts for tailored assistance.
            💳 **Service Fee**: To proceed, we require a small one-time payment of [amount]. After payment, you will receive:
            - Direct access to scholarship channels and apps.
            - Our exclusive usernames for personal support.
            - Step-by-step guidance for exam preparation and scholarship applications.
            📲 **How to Proceed**:
            1️⃣ Make the payment through the available options (Bank Transfer, Telebirr, PayPal, etc.).
            2️⃣ Submit your payment receipt for verification.
            3️⃣ Once verified, you’ll receive all the resources and assistance you need to kickstart your journey!
            👉 Click on the **'Feedback'** button anytime to share your thoughts or ask questions.
            Start your American scholarship journey today! 🇺🇸✨

Payment options:
""", reply_markup=payment_options_markup())
        

    elif message.text == 'Canada':
        bot.reply_to(message, """ "🎓 **Welcome to the Canada Scholarships Program!** 
            Are you aspiring to study in one of the most welcoming countries in the world? Here's how we can assist you:
            ✅ Access exclusive scholarship opportunities for undergraduate, postgraduate, and research programs.
            ✅ Step-by-step guidance on admissions and visa processes.
            ✅ Resources for preparing for international English exams (IELTS, TOEFL, etc.).
            ✅ Explore trusted channels, apps, and resources for Canadian scholarships.
            ✅ Contact our experts for personalized assistance.
            💳 **Service Fee**: To proceed, a one-time payment of [amount] is required. Once paid, you'll receive:
            - Access to exclusive scholarship resources.
            - Direct support from our experts via private usernames.
            - Detailed guidance for scholarship and admission processes.
            📲 **How to Proceed**:
            1️⃣ Make the payment through the available methods.
            2️⃣ Submit your receipt for verification.
            3️⃣ Once verified, you'll receive access to all resources and support!
            Start your Canadian scholarship journey today! 🇨🇦✨
Payment options:
""", reply_markup=payment_options_markup())
    

    elif message.text == 'Europe':
        bot.reply_to(message, """ "🎓 **Welcome to the European Scholarships Program!** 🌍
            Explore educational opportunities in top European universities with our support:
            ✅ Access scholarships for Bachelor's, Master's, and PhD programs across Europe.
            ✅ Guidance on application processes, including Erasmus+ and DAAD scholarships.
            ✅ Resources for preparing for English and other language proficiency tests.
            ✅ Direct links to trusted platforms and apps for European scholarships.
            ✅ Personalized support from our team.
            💳 **Service Fee**: A one-time payment of [amount] is required. After payment, you'll get:
            - Comprehensive scholarship links and resources.
            - One-on-one assistance from our experts.
            - Tools for acing applications and exams.
            📲 **How to Proceed**:
            1️⃣ Complete the payment using available options.
            2️⃣ Send your receipt for verification.
            3️⃣ Gain access to all resources and guidance!
            Kickstart your European scholarship journey now! 🌍✨

Payment options:
""", reply_markup=payment_options_markup())
        
    
    elif message.text == 'Asia':
        bot.reply_to(message, """"🎓 **Welcome to the Asian Scholarships Program!** 🌏
            Unlock opportunities in some of the fastest-growing education hubs in the world:
            ✅ Scholarships for Bachelor's, Master's, and specialized programs in top Asian countries.
            ✅ Guidance on university admissions and visa applications.
            ✅ Resources for English and local language proficiency exams.
            ✅ Trusted channels, apps, and tools for Asian scholarships.
            ✅ Personalized guidance from our experts.
            💳 **Service Fee**: A one-time payment of [amount] is needed. After payment, you'll get:
            - Access to scholarships and application resources.
            - Personalized support from our team.
            - Links and tools for successful applications.
            📲 **How to Proceed**:
            1️⃣ Make the payment via your preferred method.
            2️⃣ Submit your receipt for verification.
            3️⃣ Receive all the necessary resources and support!
            Start your journey to top Asian universities today! 🌏✨

Payment options:
""", reply_markup=payment_options_markup())
        

    elif message.text == 'Australia':
        bot.reply_to(message, """ "🎓 **Welcome to the Australian Scholarships Program!** 
            Let us help you explore top educational opportunities in Australia:
            ✅ Scholarships for undergraduate, postgraduate, and research programs.
            ✅ Guidance on admissions and student visa processes.
            ✅ Resources for English proficiency tests (IELTS, PTE, etc.).
            ✅ Links to trusted scholarship channels and platforms.
            ✅ One-on-one support from our team.
            💳 **Service Fee**: A one-time payment of [amount] is required. After payment, you'll receive:
            - Detailed scholarship resources and links.
            - Personalized guidance for applications and tests.
            - Contact with our experts for tailored assistance.
            📲 **How to Proceed**:
            1️⃣ Pay the service fee using the listed methods.
            2️⃣ Send us the receipt for verification.
            3️⃣ Get access to all resources and expert support!
            Begin your journey to Australian universities now! 🇦🇺✨

Payment options:
""", reply_markup=payment_options_markup())
        


    elif message.text == 'Africa':
        bot.reply_to(message, """"🎓 **Welcome to the African Scholarships Program!** 🌍
            Discover amazing scholarship opportunities across African universities:
            ✅ Access scholarships for Bachelor's, Master's, and PhD programs.
            ✅ Support for regional and international African scholarship programs.
            ✅ Guidance on applications and visa requirements.
            ✅ Trusted resources and links for African scholarships.
            ✅ Personalized assistance from our team.
            💳 **Service Fee**: A one-time payment of [amount] applies. After payment, you'll get:
            - Comprehensive resources for scholarships.
            - Personalized guidance for applications and tests.
            - Contact with experts for tailored support.
            📲 **How to Proceed**:
            1️⃣ Make the payment through the available channels.
            2️⃣ Submit your payment receipt for verification.
            3️⃣ Gain access to resources and expert help!
            Start your African scholarship journey today! 🌍✨
       

Payment options:
""", reply_markup=payment_options_markup())
        



    elif message.text == 'Online/Conditional':
        bot.reply_to(message, """ "🎓 **Welcome to the Online/Conditional Scholarships Program!** 💻
            Learn from top institutions without borders with online and conditional scholarships:
            ✅ Scholarships for online degree programs and short courses.
            ✅ Flexible, conditional scholarships tailored for part-time learners.
            ✅ Resources for application and guidance on eligibility requirements.
            ✅ Links to trusted platforms and tools for online scholarships.
            ✅ Support from our team for a seamless process.
            💳 **Service Fee**: A one-time payment of [amount]. After payment, you'll get:
            - Access to online scholarship resources and links.
            - Personalized guidance from our team.
            - Tools to successfully apply for online programs.
            📲 **How to Proceed**:
            1️⃣ Pay the fee through the available methods.
            2️⃣ Share your payment receipt for verification.
            3️⃣ Receive access to all resources and support!
            Start your online learning journey today! 💻✨

Payment options:
""", reply_markup=payment_options_markup())
        

    elif message.text == 'Ielts':
        bot.reply_to(message, """🎓 Scholarships and related informations 🎓

We provide support in securing scholarships and provide other related to America.

Services include:
- Scholarship search and application assistance
- English proficiency test preparation materials

To begin, please make a payment of 500 birr. After your payment, send us the receipt for activation.

Payment options:
""", reply_markup=payment_options_markup())
    
    elif message.text == 'TORFL':
        bot.reply_to(message, """🎓 Scholarships and related informations 🎓

We provide support in securing scholarships and provide other related to America.

Services include:
- Scholarship search and application assistance
- English proficiency test preparation materials

To begin, please make a payment of 500 birr. After your payment, send us the receipt for activation.

Payment options:
""", reply_markup=payment_options_markup())
        
    elif message.text == 'Doulingo':
        bot.reply_to(message, """🎓 Scholarships and related informations 🎓

We provide support in securing scholarships and provide other related to America.

Services include:
- Scholarship search and application assistance
- English proficiency test preparation materials

To begin, please make a payment of 500 birr. After your payment, send us the receipt for activation.

Payment options:
""", reply_markup=payment_options_markup())
        
    elif message.text == 'TOEIC':
        bot.reply_to(message, """🎓 Scholarships and related informations 🎓

We provide support in securing scholarships and provide other related to America.

Services include:
- Scholarship search and application assistance
- English proficiency test preparation materials

To begin, please make a payment of 500 birr. After your payment, send us the receipt for activation.

Payment options:
""", reply_markup=payment_options_markup())
        
    elif message.text == 'SAT':
        bot.reply_to(message, """🎓 Scholarships and related informations 🎓

We provide support in securing scholarships and provide other related to America.

Services include:
- Scholarship search and application assistance
- English proficiency test preparation materials

To begin, please make a payment of 500 birr. After your payment, send us the receipt for activation.

Payment options:
""", reply_markup=payment_options_markup())
        

    
    elif service_selected == 'for Scholarship and admission opportunities':
        
        bot.reply_to(message, """🎓 You can find scholarships and related information on our Telegram channel. 
        Stay updated with the latest opportunities by clicking the button below:""",  reply_markup=channel_markup())

    elif service_selected == 'Join Channel':
        markup = types.InlineKeyboardMarkup()
        channel_button = types.InlineKeyboardButton("Join Scholarship Channel", url="https://t.me/+9_7fZiQKyoQ3NWJk")
        markup.add(channel_button)
        bot.reply_to(message, """🎓 You can find scholarships and related information on our Telegram channel. 
    Stay updated with the latest opportunities by clicking the button below:""",  reply_markup=markup)
                     
                    
    

        
        
    elif service_selected == 'for Ethiopian Passport application':
        bot.reply_to(message, """please choose which option you are looking
                     for from the button below:""",  reply_markup=passport_markup())  
    elif service_selected == 'for New Passport application':
        markup = types.InlineKeyboardMarkup()
        channel_button = types.InlineKeyboardButton("please fill these google forms so we can schedule your passport", url="https://forms.gle/ELLajSwRt5BT3RXQA")
        markup.add(channel_button)
        bot.reply_to(message, """🎓 You can find scholarships and related information on our Telegram channel. 
    Stay updated with the latest opportunities by clicking the button below:""",  reply_markup=markup)
    elif service_selected == 'for Passport Renewal':
        markup = types.InlineKeyboardMarkup()
        channel_button = types.InlineKeyboardButton("please fill these google forms so we can schedule your passport", url="https://forms.gle/ELLajSwRt5BT3RXQA")
        markup.add(channel_button)
        bot.reply_to(message, """🎓 You can find scholarships and related information on our Telegram channel. 
    Stay updated with the latest opportunities by clicking the button below:""",  reply_markup=markup)
    elif service_selected == 'for Lost/Stolen Passport':
        markup = types.InlineKeyboardMarkup()
        channel_button = types.InlineKeyboardButton("please fill these google forms so we can schedule your passport", url="https://forms.gle/ELLajSwRt5BT3RXQA")
        markup.add(channel_button)
        bot.reply_to(message, """🎓 You can find scholarships and related information on our Telegram channel. 
    Stay updated with the latest opportunities by clicking the button below:""",  reply_markup=markup)
    elif service_selected == 'for Emergency Travel Document':
       markup = types.InlineKeyboardMarkup()
       channel_button = types.InlineKeyboardButton("please fill these google forms so we can schedule your passport", url="https://forms.gle/ELLajSwRt5BT3RXQA")
       markup.add(channel_button)
       bot.reply_to(message, """🎓 You can find scholarships and related information on our Telegram channel. 
    Stay updated with the latest opportunities by clicking the button below:""",  reply_markup=markup)
    elif service_selected == 'for Change of Details/Amendment':
        markup = types.InlineKeyboardMarkup()
        channel_button = types.InlineKeyboardButton("please fill these google forms so we can schedule your passport", url="https://forms.gle/ELLajSwRt5BT3RXQA")
        markup.add(channel_button)
        bot.reply_to(message, """🎓 You can find scholarships and related information on our Telegram channel. 
    Stay updated with the latest opportunities by clicking the button below:""",  reply_markup=markup)
    elif service_selected == 'for Special Passport (Official Purposes)':
        markup = types.InlineKeyboardMarkup()
        channel_button = types.InlineKeyboardButton("please fill these google forms so we can schedule your passport", url="https://forms.gle/ELLajSwRt5BT3RXQA")
        markup.add(channel_button)
        bot.reply_to(message, """🎓 You can find scholarships and related information on our Telegram channel. 
    Stay updated with the latest opportunities by clicking the button below:""",  reply_markup=markup)
    



         

            
    elif service_selected == 'for Early US Embassy appointment worldwide':
            bot.reply_to(message, """🎓 use this methods to contact us

We offer early scheduling for your B1/B2 and F1/J1 visa appointment at a time that suits you best.

To proceed:
1️⃣ **Payment**:make sure you have paid the fees
2️⃣ **Contact Us**: You can reach us via any of the following platforms:
   - Telegram: @easygate
   - Phone Number: 0964255107
   - Email: contact.easygate@gmail.com
   - WhatsApp: [Insert WhatsApp link]
   - Instagram: @easygate_international
   - Other Social Media: [Insert links]

Once your payment is confirmed, we will book your appointment according to your preferred timing.

If you need assistance, please don't hesitate to contact us.

📞 For more immediate support, call 0964255107!""", reply_markup=payment_main_menu_markup())
    elif service_selected == 'for E-commerce':
            bot.reply_to(message, """🛒 E-commerce, Dropshipping, and Online Marketing 🛒
            [E-commerce Link or Information]""", reply_markup=payment_main_menu_markup())
    elif service_selected == 'for Online courses':
            bot.reply_to(message, """📚 Online Courses 📚
            [Courses Link or Information]""", reply_markup=payment_main_menu_markup())

            
    elif service_selected == 'for International English proficiency tests':
            bot.reply_to(message, """please choose which option you are looking
            """, reply_markup=English_markup())
            
    # IELTS Option
    elif service_selected == 'for Ielts':
        markup = types.InlineKeyboardMarkup()
    # General Channel Button
        channel_button1 = types.InlineKeyboardButton("Join General IELTS Preparation Channel", url="https://t.me/general_ielts_channel")
    # Specific Channel Button
        channel_button2 = types.InlineKeyboardButton("Join IELTS Specific Channel", url="https://t.me/ielts_specific_channel")
        markup.add(channel_button1, channel_button2)
        bot.reply_to(message, """📚 **IELTS Preparation**\nStay updated with resources and opportunities by clicking one of the buttons below:""", reply_markup=markup)

# TORFL Option
    elif service_selected == 'for TORFL':
        markup = types.InlineKeyboardMarkup()
    # General Channel Button
        channel_button1 = types.InlineKeyboardButton("Join General TORFL Preparation Channel", url="https://t.me/general_torfl_channel")
    # Specific Channel Button
        channel_button2 = types.InlineKeyboardButton("Join TORFL Specific Channel", url="https://t.me/torfl_specific_channel")
        markup.add(channel_button1, channel_button2)
        bot.reply_to(message, """📚 **TORFL Preparation**\nStay updated with resources and opportunities by clicking one of the buttons below:""", reply_markup=markup)

# Duolingo Option
    elif service_selected == 'for Doulingo':
        markup = types.InlineKeyboardMarkup()
    # General Channel Button
        channel_button1 = types.InlineKeyboardButton("Join General Duolingo Channel", url="https://t.me/general_duolingo_channel")
    # Specific Channel Button
        channel_button2 = types.InlineKeyboardButton("Join Duolingo Specific Channel", url="https://t.me/duolingo_specific_channel")
        markup.add(channel_button1, channel_button2)
        bot.reply_to(message, """📚 **Duolingo Preparation**\nStay updated with resources and opportunities by clicking one of the buttons below:""", reply_markup=markup)

# TOEIC Option
    elif service_selected == 'for TOEIC':
        markup = types.InlineKeyboardMarkup()
    # General Channel Button
        channel_button1 = types.InlineKeyboardButton("Join General TOEIC Channel", url="https://t.me/general_toeic_channel")
    # Specific Channel Button
        channel_button2 = types.InlineKeyboardButton("Join TOEIC Specific Channel", url="https://t.me/toeic_specific_channel")
        markup.add(channel_button1, channel_button2)
        bot.reply_to(message, """📚 **TOEIC Preparation**\nStay updated with resources and opportunities by clicking one of the buttons below:""", reply_markup=markup)

# SAT Option
    elif service_selected == 'for SAT':
        markup = types.InlineKeyboardMarkup()
    # General Channel Button
        channel_button1 = types.InlineKeyboardButton("Join General SAT Channel", url="https://t.me/general_sat_channel")
    # Specific Channel Button
        channel_button2 = types.InlineKeyboardButton("Join SAT Specific Channel", url="https://t.me/sat_specific_channel")
        markup.add(channel_button1, channel_button2)
        bot.reply_to(message, """🎓 **SAT Preparation**\nStay updated with resources and opportunities by clicking one of the buttons below:""", reply_markup=markup)

 



    elif service_selected == 'for E-Visa applications':
            bot.reply_to(message, """🛂 E-Visa Applications
            [E-Visa Application Link or Information]""", reply_markup=payment_main_menu_markup())
    elif service_selected == 'for International payments':
            bot.reply_to(message, """💳 International Payments
            [Payments Link or Information]""", reply_markup=payment_main_menu_markup())
    elif service_selected == 'for International career opportunities':
            bot.reply_to(message, """🌍 International Career Opportunities
            [Career Opportunities Link or Information]""", reply_markup=payment_main_menu_markup())
    elif service_selected == 'for Recommend educational travel consultancies':
            bot.reply_to(message, """🌍 Educational Travel Consultancies Recommendations
            [Travel Consultancy Link or Information]""", reply_markup=payment_main_menu_markup())
    elif service_selected == 'for Assistance with any Embassy interview practice assistance':
            bot.reply_to(message, """🎓 Embassy Interview Assistance
            [Interview Assistance Link or Information]""", reply_markup=payment_main_menu_markup())
    
    
   
    elif message.text == '/help':
        bot.reply_to(message, """🆘 Help Menu:
            - Type '/start' to restart the bot
            - Type '/service' to view available services
            - Type '/contact' to contact us""")
    elif message.text == '/service':
        bot.reply_to(message, """💼 Our Services:
            1️⃣ Embassy Interview Assistance
            2️⃣ Document Review
            3️⃣ Travel Advice
            4️⃣ Visa Application Assistance
            5️⃣ Scholarship Opportunities
            6️⃣ English Proficiency Test Preparation
            7️⃣ Passport Services
            8️⃣ E-Visa Applications
            9️⃣ International Payments
            🔟 International Career Opportunities
            1️⃣1️⃣ Recommend Educational Travel Consultancies
            1️⃣2️⃣ Assistance with Any Embassy Interview Practice
            1️⃣3️⃣ Other Services
           """)
    elif service_selected == 'services':
        bot.reply_to(message, """💼 Our Services:
            1️⃣ Embassy Interview Assistance
            2️⃣ Document Review
            3️⃣ Travel Advice
            4️⃣ Visa Application Assistance
            5️⃣ Scholarship Opportunities
            6️⃣ English Proficiency Test Preparation
            7️⃣ Passport Services
            8️⃣ E-Visa Applications
            9️⃣ International Payments
            🔟 International Career Opportunities
            1️⃣1️⃣ Recommend Educational Travel Consultancies
            1️⃣2️⃣ Assistance with Any Embassy Interview Practice
            1️⃣3️⃣ Other Services
           """)
    elif message.text == '/contact':
        bot.reply_to(message, """📞 Contact Us:
            - Email: contact@easygate@gmail.com
            - Phone: +251964255107
            - Telegram: @easygate2""")
        
    elif message.text == 'Feedback':
        markup = types.InlineKeyboardMarkup()
        form_button = types.InlineKeyboardButton("📝 Fill Out Feedback Form", url="https://forms.gle/AezntVfbzwscHAdy9")
        markup.add(form_button)

        bot.reply_to(message, """📝 **Feedback**  
Please feel free to send us feedback; it's always great to hear from you!  
Click the button below to share your thoughts:""", reply_markup=markup)
        
    elif service_selected == 'F1/J1 Visa':
        bot.reply_to(message, """🎓 **F1/J1 Visa Assistance**

We can help you schedule an early appointment for your F1/J1 visa at a time that works best for you.

To proceed:
1️⃣ **Payment**: A small fee is required to schedule your appointment. The payment can be done via various secure methods.
2️⃣ **Contact Us**: Reach out to us through any of the following channels for more details and to finalize your booking:
   - Telegram: @easygate
   - Phone Number: 0964255107
   - Email: contact.easygate@gmail.com
   - WhatsApp: [Insert WhatsApp link]
   - Instagram: @easygate_international
   - Other Social Media: [Insert links]

Once we receive your payment and confirm your details, we will schedule the appointment at a time that is convenient for you.

Feel free to contact us for further assistance.

📞 You can also call us at 0964255107 for quick assistance!

Click below to proceed with payment:""",reply_markup=payment_options_markup())
        
    elif service_selected == 'B1/B2 Visa':
        bot.reply_to(message,"""🎓 **B1/B2 Visa Assistance**

We offer early scheduling for your B1/B2 visa appointment at a time that suits you best.

To proceed:
1️⃣ **Payment**: A fee is required for scheduling the appointment. Please complete the payment through one of our secure methods.
2️⃣ **Contact Us**: You can reach us via any of the following platforms:
   - Telegram: @easygate
   - Phone Number: 0964255107
   - Email: contact.easygate@gmail.com
   - WhatsApp: [Insert WhatsApp link]
   - Instagram: @easygate_international
   - Other Social Media: [Insert links]

Once your payment is confirmed, we will book your appointment according to your preferred timing.

If you need assistance, please don't hesitate to contact us.

📞 For more immediate support, call 0964255107!

Click below to proceed with payment:""",reply_markup=payment_options_markup())
        

    else:
        bot.reply_to(message, """
    I'm sorry, I didn't understand that.
    Here’s how to use the bot:
             - Type '/start' to begin
             - Type '/help' to see available commands
             - Type '/service' to learn about our services
             - Type '/contact' to get contact details
    """)
    



def scholarship_options_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton(' America')
    btn2 = types.KeyboardButton('Canada')
    btn3 = types.KeyboardButton('Europe')
    btn4 = types.KeyboardButton('Asia')
    btn5 = types.KeyboardButton('Australia')
    btn6 = types.KeyboardButton('Africa')
    btn7 = types.KeyboardButton('Online/Conditional')
    btn8 = types.KeyboardButton('main menu')
    btn9 = types.KeyboardButton('Feedback')
    # btn9 = KeyboardButton('back')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
    return markup

def channel_markup():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        btn1 = types.KeyboardButton('Join Channel')
        btn2 = types.KeyboardButton('main menu')
        markup.add(btn1, btn2)
        return markup
def English_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton('for Ielts')
    btn2 = types.KeyboardButton('for TORFL')
    btn3 = types.KeyboardButton('for Duolingo')
    btn4 = types.KeyboardButton('for TOEIC')
    btn5 = types.KeyboardButton('for SAT')
    btn6 = types.KeyboardButton('main menu')
    btn7 = types.KeyboardButton('Feedback')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    return markup

def passport_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)  
    btn1 = types.KeyboardButton('for New Passport application')
    btn2 = types.KeyboardButton('for Passport Renewal')
    btn3 = types.KeyboardButton('for Lost/Stolen Passport')
    btn4 = types.KeyboardButton('for Emergency Travel Document')
    btn5 = types.KeyboardButton('for Change of Details/Amendment')
    btn7 = types.KeyboardButton('for Special Passport (Official Purposes)')
    btn6 = types.KeyboardButton('main menu')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    return markup



def ethiopassport_options_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton('New Passport application')
    btn2 = types.KeyboardButton('Renewal/Replacement appointment')
    btn3 = types.KeyboardButton(' Lost/stolen Passport application appointment')
    btn4 = types.KeyboardButton('main menu')
    btn5 = types.KeyboardButton('Feedback')
    btn6 = types.KeyboardButton('back')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    return markup



def earlyUS_options_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton('F1/J1 Visa')
    btn2 = types.KeyboardButton('B1/B2 Visa')
    btn3 = types.KeyboardButton('main menu')
    btn4 = types.KeyboardButton('Feedback')
    btn5 = types.KeyboardButton('back')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    return markup




def english_options_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton('Ielts')
    btn2 = types.KeyboardButton('TORFL')
    btn3 = types.KeyboardButton('Duolingo')
    btn4 = types.KeyboardButton('TOEIC')
    btn5 = types.KeyboardButton('SAT')
    btn6 = types.KeyboardButton('main menu')
    btn8 = types.KeyboardButton('back')
    btn7 = types.KeyboardButton('Feedback')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    return markup



def educational_options_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton('Study visa interview')
    btn2 = types.KeyboardButton(' Work visa interview')
    btn3 = types.KeyboardButton('Visitor visa interview')
    btn4 = types.KeyboardButton('Other')
    btn5 = types.KeyboardButton('main menu')
    btn6 = types.KeyboardButton('Feedback')
    btn7 = types.KeyboardButton('back')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    return markup




def payment_options_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton('Bank Transfer')
    btn2 = types.KeyboardButton('Telebirr')
    btn3 = types.KeyboardButton('PayPal')
    btn4 = types.KeyboardButton('Already Paid? (Submit receipt)')
    btn5 = types.KeyboardButton('Choose Different Payment Method')
    btn6 = types.KeyboardButton('main menu')
    btn7 = types.KeyboardButton('Feedback')
    btn8 = types.KeyboardButton('back')
    markup.add(btn1, btn2, btn3, btn4, btn5,btn6, btn7, btn8)
    return markup


def entry_payment_options_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton('Bank')
    btn2 = types.KeyboardButton('Telebirr transfer')
    btn3 = types.KeyboardButton('PayPal transfer')
    btn4 = types.KeyboardButton('Already Paid? (send receipt)')
    btn5 = types.KeyboardButton('Choose Different method')
    btn6 = types.KeyboardButton('main menu')
    btn7 = types.KeyboardButton('Feedback')
    btn8 = types.KeyboardButton('back')
    markup.add(btn1, btn2, btn3, btn4, btn5,btn6, btn7, btn8)
    return markup

def back_to_payment_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton('Choose Different Payment Method')
    btn2 = types.KeyboardButton('Already Paid? (Submit receipt)')
    btn3 = types.KeyboardButton('main menu')
    btn4 = types.KeyboardButton('Feedback')
    btn5 = types.KeyboardButton('back')
    markup.add(btn1, btn2,btn3, btn4, btn5)
    return markup

def back_to_main_menu_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton('Scholarship and admission opportunities')
    btn2 = types.KeyboardButton('Ethiopian Passport application')
    btn3 = types.KeyboardButton('Early US Embassy appointment worldwide')
    btn4 = types.KeyboardButton('E-commerce')
    btn5 = types.KeyboardButton('Online courses')
    btn6 = types.KeyboardButton('International English proficiency tests')
    btn7 = types.KeyboardButton('E-Visa applications')
    btn8 = types.KeyboardButton('International payments')
    btn9 = types.KeyboardButton('International career opportunities')
    btn10 = types.KeyboardButton('Recommend educational travel consultancies')
    btn11 = types.KeyboardButton('Assistance with any Embassy interview practice assistance')
    btn12 = types.KeyboardButton('About Us')
    btn13 = types.KeyboardButton('Feedback')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13)
    return markup


def payment_main_menu_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton('Scholarship and admission opportunities')
    btn2 = types.KeyboardButton('Ethiopian Passport application')
    btn3 = types.KeyboardButton('Early US Embassy appointment worldwide')
    btn4 = types.KeyboardButton('E-commerce')
    btn5 = types.KeyboardButton('Online courses')
    btn6 = types.KeyboardButton('International English proficiency tests')
    btn7 = types.KeyboardButton('E-Visa applications')
    btn8 = types.KeyboardButton('International payments')
    btn9 = types.KeyboardButton('International career opportunities')
    btn10 = types.KeyboardButton('Recommend educational travel consultancies')
    btn11 = types.KeyboardButton('Assistance with any Embassy interview practice assistance')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11)
    return markup






user_data = {}
pending_verifications = {}
user_states = {}


    

# Handle the receipt submission and forward to admin
@bot.message_handler(content_types=['document', 'photo'])
def process_receipt(message):
    user_id = message.chat.id
    user_first_name = message.chat.first_name

    if message.document:
        file_name = message.document.file_name
        file_extension = file_name.split('.')[-1].lower()  # Extract file extension
        
        # Check if the document is a PDF
        if file_extension == 'pdf':
            receipt_file = message.document.file_id
            file_type = 'PDF'
            bot.send_document(ADMIN_CHAT_ID, receipt_file)
        else:
            bot.reply_to(message, "Please send a valid receipt in PDF format.")
            return

    elif message.photo:
        receipt_file = message.photo[-1].file_id  # Get the highest quality photo
        file_type = 'Photo'
        bot.send_photo(ADMIN_CHAT_ID, receipt_file)

    else:
        bot.reply_to(message, "Please send a valid receipt in PDF or image format.")
        return

    # Inform the admin about the receipt submission
    pending_verifications[user_id] = {'file_id': receipt_file, 'file_type': file_type, 'user_name': user_first_name}
    bot.reply_to(message, "Your payment receipt has been sent for verification. The admin will confirm your payment shortly.")
    bot.send_message(ADMIN_CHAT_ID, f"📩 New Payment Receipt from {user_first_name} ({user_id}):")

    # Send Inline buttons to Admin for verification
    markup = types.InlineKeyboardMarkup()
    verify_button = types.InlineKeyboardButton("✅ Verify User", callback_data=f"verify_{user_id}")
    invalid_button = types.InlineKeyboardButton("❌ Invalid Payment", callback_data=f"invalid_{user_id}")
    markup.add(verify_button, invalid_button)
    bot.send_message(ADMIN_CHAT_ID, "Please verify the payment from the user:", reply_markup=markup)


# Handle admin verification actions
@bot.callback_query_handler(func=lambda call: call.data.startswith('verify_') or call.data.startswith('invalid_'))
def handle_admin_response(call):
    user_id = int(call.data.split('_')[1])

    if call.data.startswith('verify_'):
        if user_id in pending_verifications:
            user_data[user_id] = pending_verifications.pop(user_id)
            bot.send_message(user_id, "✅ Your payment has been verified! Please proceed to select your service.")

            # Ask the user to specify the service
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            markup.add(types.KeyboardButton('for Scholarship and admission opportunities'),
                       types.KeyboardButton('for Ethiopian Passport application'),
                       types.KeyboardButton('for Early US Embassy appointment worldwide'),
                       types.KeyboardButton('for E-commerce'),
                       types.KeyboardButton('for Online courses'),
                       types.KeyboardButton('for International English proficiency tests'),
                       types.KeyboardButton('for E-Visa applications'),
                       types.KeyboardButton('for International payments'),
                       types.KeyboardButton('for International career opportunities'),
                       types.KeyboardButton('for Recommend educational travel consultancies'),
                       types.KeyboardButton('for Assistance with any Embassy interview practice assistance')
                       )

            bot.send_message(user_id, "Please select the service you made the payment for:", reply_markup=markup)
        else:
            bot.send_message(ADMIN_CHAT_ID, "The user ID is not in the pending verifications.")

    elif call.data.startswith('invalid_'):
        if user_id in pending_verifications:
            pending_verifications.pop(user_id)
            bot.send_message(user_id, "❌ Your payment could not be verified. Please contact support.")
            bot.send_message(ADMIN_CHAT_ID, f"Payment invalid for {user_id}. User has been notified.")
        else:
            bot.send_message(ADMIN_CHAT_ID, "The user ID is not in the pending verifications.")

    bot.answer_callback_query(call.id)  # Close the callback button

# Handle service selection
# Handle service selection
@bot.message_handler(func=lambda message: message.text in [
    'for Scholarship and admission opportunities',
    'for Ethiopian Passport application',
    'for Early US Embassy appointment worldwide',
    'for E-commerce',
    'for Online courses',
    'for International English proficiency tests',
    'for E-Visa applications',
    'for International payments',
    'for International career opportunities',
    'for Recommend educational travel consultancies',
    'for Assistance with any Embassy interview practice assistance'
])
def handle_service_selection(message):
    user_id = message.chat.id
    service_selected = message.text

    # Debug log
    print(f"User {user_id} selected the service: {service_selected}")

    if user_id in user_data:
        receipt_details = user_data[user_id]
        file_id = receipt_details['file_id']
        file_type = receipt_details['file_type']

        # Forward the receipt and service selection to the admin
        bot.send_message(ADMIN_CHAT_ID, f"📩 Verified Payment Receipt from {receipt_details['user_name']} ({user_id}):\n\nService: {service_selected}")
        if file_type == 'Document':
            bot.send_document(ADMIN_CHAT_ID, file_id)
        elif file_type == 'Photo':
            bot.send_photo(ADMIN_CHAT_ID, file_id)

        # Respond with specific service information based on user selection
        if service_selected == 'for Scholarship and admission opportunities':
           bot.reply_to(message, """🎓 You can find scholarships and related information on our Telegram channel. 
            Stay updated with the latest opportunities here: [Scholarship Channel](https://t.me/+9_7fZiQKyoQ3NWJk)""", reply_markup=payment_main_menu_markup())
        elif service_selected == 'for Ethiopian Passport application':
            bot.reply_to(message, """🛂 Ethiopian Passport Application
            [Passport Application Link or Information]""", reply_markup=payment_main_menu_markup())
        elif service_selected == 'for Early US Embassy appointment worldwide':
            bot.reply_to(message, """🇺🇸 Early US Embassy Appointment Worldwide
            [Embassy Appointment Link or Information]""", reply_markup=payment_main_menu_markup())
        elif service_selected == 'for E-commerce':
            bot.reply_to(message, """🛒 E-commerce, Dropshipping, and Online Marketing 🛒
            [E-commerce Link or Information]""", reply_markup=payment_main_menu_markup())
        elif service_selected == 'for Online courses':
            bot.reply_to(message, """📚 Online Courses 📚
            [Courses Link or Information]""", reply_markup=payment_main_menu_markup())
        elif service_selected == 'for International English proficiency tests':
            bot.reply_to(message, """🌍 International English Proficiency Tests
            [Test Link or Information]""", reply_markup=payment_main_menu_markup())
        elif service_selected == 'for E-Visa applications':
            bot.reply_to(message, """🛂 E-Visa Applications
            [E-Visa Application Link or Information]""", reply_markup=payment_main_menu_markup())
        elif service_selected == 'for International payments':
            bot.reply_to(message, """💳 International Payments
            [Payments Link or Information]""", reply_markup=payment_main_menu_markup())
        elif service_selected == 'for International career opportunities':
            bot.reply_to(message, """🌍 International Career Opportunities
            [Career Opportunities Link or Information]""", reply_markup=payment_main_menu_markup())
        elif service_selected == 'for Recommend educational travel consultancies':
            bot.reply_to(message, """🌍 Educational Travel Consultancies Recommendations
            [Travel Consultancy Link or Information]""", reply_markup=payment_main_menu_markup())
        elif service_selected == 'for Assistance with any Embassy interview practice assistance':
            bot.reply_to(message, """🎓 Embassy Interview Assistance
            [Interview Assistance Link or Information]""", reply_markup=payment_main_menu_markup())

        # Clear the user's data after the service has been provided
        del user_data[user_id]
    else:
        bot.reply_to(message, "We could not find your payment details. Please resend your receipt.")


# Start the bot
bot.polling(none_stop=True)





















