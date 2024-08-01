from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import os

# Login page URL
URL = 'https://membros.devaprender.com/'


def get_chrome_options(download_path='/home/lonewolf/Downloads'):
    """
    Configure Chrome options for the WebDriver.

    Args:
        download_path (str): Path for default download directory.

    Returns:
        Options: Configured Chrome options.
    """
    chrome_options = Options()
    # Set Chrome arguments
    arguments = ['--lang=pt-BR', '--start-maximized']
    for argument in arguments:
        chrome_options.add_argument(argument)
    
    # Set Chrome preferences
    prefs = {
        'download.default_directory': download_path,
        'download.directory_upgrade': True,
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,
    }
    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_experimental_option('detach', True)
    
    return chrome_options


def start_driver(chrome_options):
    """
    Initialize and return the Chrome WebDriver.

    Args:
        chrome_options (Options): Configured Chrome options.

    Returns:
        WebDriver: Initialized Chrome WebDriver.
    """
    # Initialize the Chrome WebDriver with the specified options
    return webdriver.Chrome(options=chrome_options)


def load_credentials(env_file='.env'):
    """
    Load user credentials from the .env file.

    Args:
        env_file (str): Path to the .env file.

    Returns:
        tuple: User email and password.
    """
    # Load environment variables from the specified .env file
    load_dotenv(dotenv_path=env_file)
    user_email = os.getenv('USER_EMAIL')
    password = os.getenv('PASSWORD')
    
    # Raise an error if credentials are not found
    if not user_email or not password:
        raise ValueError("Credentials not found in the .env file.")
    
    return user_email, password


def login(driver, user_email, password):
    """
    Automate the login process on the web page.

    Args:
        driver (WebDriver): Selenium WebDriver.
        user_email (str): User email.
        password (str): User password.
    """
    # Locate the email field and enter the user email
    driver.find_element(By.ID, 'AcessoEmail').send_keys(user_email)
    # Locate the password field and enter the user password
    driver.find_element(By.ID, 'AcessoSenha').send_keys(password)
    # Locate and click the login button
    driver.find_element(By.CLASS_NAME, 'auth-btn').click()


def main():
    """
    Main function to open the browser, load credentials, and log in.
    """
    # Get configured Chrome options
    chrome_options = get_chrome_options()
    # Start the Chrome WebDriver
    driver = start_driver(chrome_options)

    try:
        # Open the login page URL
        driver.get(URL)
        # Wait for the page to load
        sleep(10)

        # Load user credentials from the .env file
        user_email, password = load_credentials()
        # Perform login using the loaded credentials
        login(driver, user_email, password)

        # Keep the browser window open until user input
        input('Press Enter to close the window...')
    finally:
        # Close the browser window
        driver.quit()


if __name__ == '__main__':
    main()
