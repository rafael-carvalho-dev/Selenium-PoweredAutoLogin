# Automated Login Bot

This project automates the login process to a specified web page using Selenium and Python. The credentials are securely loaded from a `.env` file, and the browser window remains open until the user closes it manually.

Project designed for educational purposes.

## Project Structure

├── .env
├── README.md
├── requirements.txt
└── src
├── main.py


## Prerequisites

- Python 3.x
- Google Chrome browser installed
- ChromeDriver installed and accessible in your system PATH

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/automated-login-bot.git
    cd automated-login-bot
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate # On Windows use `venv\Scripts\activate`
    ```

3. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project root directory and add your credentials:
    ```env
    USER_EMAIL=your_email@example.com
    PASSWORD=your_password
    ```

## Usage

1. Navigate to the `src` directory:
    ```sh
    cd src
    ```

2. Run the script:
    ```sh
    python main.py
    ```

3. The browser window will open, navigate to the login page, and perform the login using the provided credentials. The browser window will remain open until you press Enter in the terminal.

## Configuration

- **URL**: You can change the login page URL by modifying the `URL` variable in the `main.py` file.
- **Chrome Options**: Adjust the Chrome options and preferences in the `get_chrome_options` function in the `main.py` file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Use the structure suggested in the README file to organize your project.