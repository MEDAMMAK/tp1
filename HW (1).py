from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Configurez le chemin de votre pilote (ici, pour Chrome)
driver_path = 'C:\\chrome\\chromedriver.exe'  # Remplacez par le chemin de chromedriver

# Créez une instance de Service avec le chemin du pilote
service = Service(driver_path)

# Initialisez le driver avec le service configuré
driver = webdriver.Chrome(service=service)

try:
    # Accédez au site
    driver.get("https://demo.guru99.com/")

    # Remplissez le champ Email ID
    email_field = driver.find_element(By.NAME, "emailid")
    email_field.send_keys("votre_email@example.com")  # Remplacez par une adresse e-mail valide

    # Cliquez sur le bouton Submit
    submit_button = driver.find_element(By.NAME, "btnLogin")
    submit_button.click()

    # Attendez quelques secondes pour que la page se charge
    time.sleep(3)

    # Lisez les données User ID et Password
    user_id = driver.find_element(By.XPATH, "//td[contains(text(),'User ID')]/following-sibling::td").text
    password = driver.find_element(By.XPATH, "//td[contains(text(),'Password')]/following-sibling::td").text

    # Affichez les résultats
    print(f"User ID: {user_id}")
    print(f"Password: {password}")




    # Go to the login page
    driver.get("https://demo.guru99.com/V1/index.php")
    time.sleep(2)  # Wait for the login page to load

    # Enter User ID and Password
    user_id_field = driver.find_element(By.NAME, "uid")
    user_id_field.send_keys(user_id)

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(password)

    # Click on Login button
    login_button = driver.find_element(By.NAME, "btnLogin")
    login_button.click()

    time.sleep(2)  # Wait for the login process to complete

    # Step 4: Verify the login
    # Check for a successful login by looking for a specific element on the dashboard or main page
    success_message = driver.find_element(By.XPATH, "//h2[text()='Welcome To Manager's Page of Guru99']")
    print(success_message.text)  # Print the success message

except Exception as e:
    print(f"An error occurred: {e}")



# Step 5: Navigate to 'New Customer' and fill out form details
new_customer_link = driver.find_element(By.LINK_TEXT, "New Customer")
new_customer_link.click()
time.sleep(2)

# Fill in the 'New Customer' form
customer_name = driver.find_element(By.NAME, "name")
customer_name.send_keys("JohnDoe")


dob = driver.find_element(By.NAME, "dob")
dob.send_keys("01-01-1990")  # format: DD-MM-YYYY

address = driver.find_element(By.NAME, "addr")
address.send_keys("123 Main St")

city = driver.find_element(By.NAME, "city")
city.send_keys("NewYork")

state = driver.find_element(By.NAME, "state")
state.send_keys("NY")

pin = driver.find_element(By.NAME, "pinno")
pin.send_keys("123456")

mobile = driver.find_element(By.NAME, "telephoneno")
mobile.send_keys("1234567890")

email = driver.find_element(By.NAME, "emailid")
email.send_keys("johndoe@example.com")



driver.find_element(By.NAME, "sub").click()

time.sleep(2)  # Wait for the login process to complete

    
# Verify if customer was added successfully by checking for specific elements on the result page
try:
    success_message = driver.find_element(By.XPATH, "//p[text()='Customer Registered Successfully!!!']")
    print("Customer added successfully:", success_message.is_displayed())
except:
    print("Failed to add customer.")
    

#finally:
    # Fermez le navigateur
    #driver.quit()
