# Display the banner at the beginning
print("""
===================================================
             ██████╗  ███╗   ███╗ █████╗ ██╗     
            ██╔═══██╗ ████╗ ████║██╔══██╗██║     
            ██║   ██║ ██╔████╔██║███████║██║     
            ██║   ██║ ██║╚██╔╝██║██╔══██║██║     
            ╚██████╔╝ ██║ ╚═╝ ██║██║  ██║███████╗
             ╚═════╝  ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝
       Automated Gmail Account Creator - By SHADOWHACKER
       Website: https://www.shadowhackr.com
===================================================
""")
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import random
import time
import tempfile
from unidecode import unidecode
import uuid
from fp.fp import FreeProxy  # Import FreeProxy

# User Agents list for random selection
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 YaBrowser/21.8.1.468 Yowser/2.5 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0",
    "Mozilla/5.0 (X11; CrOS x86_64 14440.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4807.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14467.0.2022) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4838.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14469.7.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.13 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14455.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4827.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14469.11.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.17 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14436.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4803.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14475.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4840.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14469.3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.9 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14471.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4840.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14388.37.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.9 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14409.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4829.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14395.0.2021) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4765.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14469.8.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.14 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14484.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4840.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14450.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4817.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14473.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4840.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14324.72.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.91 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14454.0.2022) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4824.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14453.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4816.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14447.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4815.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14477.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4840.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14476.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4840.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14469.8.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.9 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14588.67.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14588.67.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14526.69.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.82 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14695.25.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.22 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14526.89.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.91 Safari/537.36"
]

# Arabic names written in English letters
arabic_first_names = [
    "Ali", "Ahmed", "Omar", "Youssef", "Ayman", "Khaled", "Salma", "Nour", "Rania", "Hassan",
    "Fadi", "Sara", "Fatma", "Heba", "Lina", "Rami", "Amir", "Yasmin", "Hala", "Tamer",
    "Mohammed", "Yasser", "Sami", "Amira", "Zain", "Khalil", "Nabil", "Ziad", "Farah", "Layla",
    "Jamal", "Hadi", "Tariq", "Mahmoud", "Ranya", "Rashed", "Alaa", "Kareem", "Basma", "Nadia",
    "Yasmeen", "Hussain", "Saeed", "Iman", "Reem", "Joud", "Nourhan", "Khadija", "Sahar", "Maya",
    "Tala", "Hiba", "Dalia", "Nisreen", "Mariam", "Haneen", "Alaa", "Wissam", "Amani", "Ibtihaj",
    "Khalida", "Dania", "Loubna", "Ranya", "Hanan", "Nora", "Rawan", "Salim", "Fouzia", "Zayna",
    "Tamer", "Adnan", "Jawad", "Mansour", "Waleed", "Zuhair", "Hisham", "Hadi", "Ibrahim", "Yasmina",
    "Samira", "Huda", "Yasmin", "Rami", "Hossain", "Layal", "Kareema", "Zaki", "Aliya", "Salah",
    "Safaa", "Marwan", "Dina", "Yasmeen", "Asma", "Naima", "Tamara", "Tania", "Sabah", "Mona",
    "Firas", "Zayd", "Taha", "Yasin", "Sakina", "Madiha", "Rasha", "Sufyan", "Nafisa", "Othman",
    "Safa", "Nabilah", "Hala", "Faten", "Aisha", "Hassan", "Zainab", "Nouran", "Raneem", "Youssef",
]
arabic_last_names = [
    "Mohamed", "Ahmed", "Hussein", "Sayed", "Ismail", "Abdallah", "Khalil", "Soliman", "Nour", "Kamel",
    "Samir", "Ibrahim", "Othman", "Fouad", "Zaki", "Gamal", "Farid", "Mansour", "Adel", "Salem",
    "Hossam", "Nasser", "Qassem", "Khatib", "Rashed", "Moussa", "Naim", "Abdulaziz", "Anwar", "Younes",
    "Osama", "Bilal", "Fahd", "Rami", "Abdulrahman", "Maher", "Salim", "Tariq", "Amjad", "Ibtisam",
    "Ranya", "Sami", "Laith", "Hassan", "Saif", "Alaa", "Mujahid", "Ibrahim", "Zuhair", "Hadi",
    "Attar", "Said", "Jabari", "Ashraf", "Abu", "Ali", "Nasr", "Darwish", "Azzam", "Hussein",
    "Yasin", "Zidan", "Farhan", "Khaled", "Mahmoud", "Qureshi", "Sheikh", "Abdulkareem", "Sharif", "Abdelaziz",
    "Yunus", "Hasan", "Shakir", "Musa", "Salem", "Taha", "Ali", "Khalaf", "Khalid", "Karim",
    "Rashid", "Siddiqi", "Sulaiman", "Almasri", "Alhussein", "Sami", "Tarek", "Noor", "Husseini", "Jamil",
    "Ramzi", "Khalifa", "Hamed", "Anis", "Hussein", "Mahdi", "Samir", "Wahab", "Bakkar", "Najib",
    "Abdulhadi", "Alhaj", "Shahrani", "Sulieman", "Majeed", "Nazari", "Saber", "Tawfiq", "Sabry", "Sharif",
]

# Function to get a working proxy
def get_working_proxy():
    proxy = FreeProxy(rand=True, timeout=1).get()
    print(f"Using proxy: {proxy}")
    return proxy

# Function to save emails to a text file
def save_email_to_file(email, password):
    with open("emails.txt", "a") as file:
        file.write(f"Gmail: {email}, Password: {password}\n")

# Generate username from random first and last name
def generate_username():
    first_name = random.choice(arabic_first_names)
    last_name = random.choice(arabic_last_names)
    random_number = random.randint(1000, 9999)
    first_name_normalized = unidecode(first_name).lower()
    last_name_normalized = unidecode(last_name).lower()
    return f"{first_name_normalized}.{last_name_normalized}{random_number}"

# Account info
your_birthday = "02 4 1995"
your_gender = "2"
your_password = "lissin002020"

# Fill out Gmail registration form
def fill_form(driver):
    try:
        device_uuid = uuid.uuid4()
        print(f"Using device UUID: {device_uuid}")
        your_username = generate_username()
        driver.get("https://accounts.google.com/signup/v2/createaccount?flowName=GlifWebSignIn&flowEntry=SignUp")
        
        # Fill in the name fields
        first_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "firstName")))
        last_name = driver.find_element(By.NAME, "lastName")
        first_name.clear()
        first_name.send_keys(your_username.split('.')[0])
        last_name.clear()
        last_name.send_keys(your_username.split('.')[1])
        next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "VfPpkd-LgbsSe")))
        next_button.click()

        # Fill birthday and gender
        wait = WebDriverWait(driver, 20)
        day = wait.until(EC.visibility_of_element_located((By.NAME, "day")))
        birthday_elements = your_birthday.split()
        month_dropdown = Select(driver.find_element(By.ID, "month"))
        month_dropdown.select_by_value(birthday_elements[1])
        day_field = driver.find_element(By.ID, "day")
        day_field.clear()
        day_field.send_keys(birthday_elements[0])
        year_field = driver.find_element(By.ID, "year")
        year_field.clear()
        year_field.send_keys(birthday_elements[2])
        gender_dropdown = Select(driver.find_element(By.ID, "gender"))
        gender_dropdown.select_by_value(your_gender)
        next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "VfPpkd-LgbsSe")))
        next_button.click()

        # Create custom email
        time.sleep(2)
        if driver.find_elements(By.ID, "selectionc4"):
            create_own_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "selectionc4")))
            create_own_option.click()
        create_own_email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "Username")))
        username_field = driver.find_element(By.NAME, "Username")
        username_field.clear()
        username_field.send_keys(your_username)
        next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "VfPpkd-LgbsSe")))
        next_button.click()

        # Enter and confirm password
        password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "Passwd")))
        password_field.clear()
        password_field.send_keys(your_password)
        confirm_passwd_div = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "confirm-passwd")))
        password_confirmation_field = confirm_passwd_div.find_element(By.NAME, "PasswdAgain")
        password_confirmation_field.clear()
        password_confirmation_field.send_keys(your_password)
        next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "VfPpkd-LgbsSe")))
        next_button.click()

        # Skip phone number and recovery email
        try:
            skip_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Skip')]")))
            skip_button.click()
        except Exception as skip_error:
            print("No phone number verification step.")

        # Agree to terms
        agree_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")))
        agree_button.click()

        print(f"Your Gmail successfully created:\n{{\ngmail: {your_username}@gmail.com\npassword: {your_password}\n}}")
        save_email_to_file(f"{your_username}@gmail.com", your_password)

    except Exception as e:
        print("Failed to create your Gmail, Sorry")
        print(e)


# Create multiple accounts
def create_multiple_accounts(number_of_accounts):
    for i in range(number_of_accounts):
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--disable-infobars")
        
        # Criar um diretório temporário exclusivo para evitar conflitos
        temp_dir = tempfile.mkdtemp()
        chrome_options.add_argument(f"--user-data-dir={temp_dir}")
        
        user_agent = random.choice(user_agents)
        chrome_options.add_argument(f'user-agent={user_agent}')
        
        proxy = get_working_proxy()
        chrome_options.add_argument(f'--proxy-server={proxy}')
        
        driver = webdriver.Chrome(options=chrome_options)
        fill_form(driver)
        driver.quit()
        
        # Remover o diretório temporário após o uso
        shutil.rmtree(temp_dir, ignore_errors=True)
        
        # Adicionar um intervalo aleatório entre as criações de contas
        time.sleep(random.randint(5, 15))


if __name__ == "__main__":
    number_of_accounts = 5  # Número de contas a serem criadas
    create_multiple_accounts(number_of_accounts)
