from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import os

# Login page URL
URL = 'https://membros.devaprender.com/'

def start_driver():
    """
    Configure and start the Chrome WebDriver with specific options.
    
    Returns:
        WebDriver: The configured Chrome WebDriver.
    """
    # Configure the WebDriver to use Chrome
    chrome_options = Options()

    # Define specific behaviors
    arguments = ['--lang=pt-BR', '--start-maximized']

    # Add behaviors to the options list
    for argument in arguments:
        chrome_options.add_argument(argument)

    # Define the default location for saving downloads
    default_download_path = '/home/lonewolf/Downloads'

    # Add experimental options
    chrome_options.add_experimental_option('prefs', {
        'download.default_directory': default_download_path,  # Update default download directory
        'download.directory_upgrade': True,  # Upgrade directory
        'download.prompt_for_download': False,  # Set whether the browser should ask for download
        'profile.default_content_setting_values.notifications': 2,  # Disable notifications
        'profile.default_content_setting_values.automatic_downloads': 1,  # Allow multiple downloads
        'detach': True,  # Do not automatically close the window
    })

    # Initialize the browser
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def load_credentials():
    """
    Load user credentials from the .env file.
    
    Returns:
        tuple: A tuple containing the user email and password.
    """
    # Load the .env file
    load_dotenv(dotenv_path='../.env')
    user_email = os.getenv('USER_EMAIL')
    password = os.getenv('PASSWORD')
    return user_email, password

def login(driver, user_email, password):
    """
    Automate the login process on the web page.
    
    Args:
        driver (WebDriver): The Selenium WebDriver.
        user_email (str): The user email.
        password (str): The user password.
    """
    # Find the email field and type the email
    email_field = driver.find_element(By.ID, 'AcessoEmail')
    email_field.send_keys(user_email)

    # Find the password field and type the password
    password_field = driver.find_element(By.ID, 'AcessoSenha')
    password_field.send_keys(password)

    # Find and click the login button
    login_button = driver.find_element(By.CLASS_NAME, 'auth-btn')
    login_button.click()

def main():
    """
    Main function to open the browser, load credentials, and log in.
    """
    try:
        # Open the desired URL
        driver = start_driver()
        driver.get(URL)

        # Wait for the page to load
        sleep(10)

        # Load credentials from the .env file
        user_email, password = load_credentials()

        # Log in using the loaded credentials
        login(driver, user_email, password)

        # Wait until the user closes the window
        input('Press Enter to close the window...')

    finally:
        # Optionally, close the driver when done
        driver.quit()

if __name__ == '__main__':
    main()
