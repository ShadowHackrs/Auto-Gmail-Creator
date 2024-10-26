# Auto-Gmail-Creator
A Python script that automates the creation of Gmail accounts. This script utilizes Selenium for web automation to navigate through the Gmail account creation process, allowing users to create accounts with random user details, proxy support, and a variety of user agents.
### Auto-Gmail-Creator Script Documentation

![imsage alt](https://github.com/ShadowHackrs/Auto-Gmail-Creator/blob/0c2a186b388d29cd2b1787277615e9d3e79f8d4a/Screenshot%202024-10-26%20015006.png)

---

## Table of Contents
1. [Features](#features)
2. [Requirements](#requirements)
3. [Setup and Installation](#setup-and-installation)
4. [Usage](#usage)
5. [Configuration](#configuration)
6. [Troubleshooting](#troubleshooting)

---

### Features

- **Automated Gmail Creation**: Uses Selenium to automate the Gmail sign-up process.
- **Random User Details**: Generates random Arabic names, user agents, and other details to create a unique account each time.
- **Proxy Support**: Integrates with `FreeProxy` to avoid IP bans during account creation.
- **Randomized User Agent**: Randomly chooses from a list of user agents to prevent detection by Gmail.
- **Logging and Debugging**: Provides banners and notifications for ease of debugging and monitoring the process.

---

### Requirements

1. **Python** 3.6 or higher
2. **Google Chrome** (Browser)
3. **Chromedriver** (Corresponding to your Chrome version)
4. **Python Packages**:
   - `selenium`
   - `requests`
   - `unidecode`
   - `fp` (FreeProxy)

To install the required packages, use the following command:

```bash
pip install selenium requests unidecode fp
```

---

### Setup and Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/ShadowHackrs/Auto-Gmail-Creator.git
   cd Auto-Gmail-Creator
   ```

2. **Install Google Chrome and Chromedriver**
   - Ensure Google Chrome is installed.
   - Download Chromedriver from [Chromedriver's official website](https://sites.google.com/chromium.org/driver/).
   - Place the `chromedriver` in your PATH or the root directory of the project.

3. **Install Required Python Packages**
   ```bash
   pip install -r requirements.txt
   ```

---

### Usage

1. **Run the Script**
   - Simply run the script using the command:
     ```bash
     python auto_gmail_creator.py
     ```
   - The script will display a banner and start creating a Gmail account using randomly generated details.

2. **Script Flow**
   - Displays a custom banner with author information.
   - Launches Chrome in automated mode.
   - Uses a randomly chosen user agent for each session.
   - Connects to a proxy server to mask the IP address.
   - Creates an account with a randomly generated Arabic name and other details.

---

### Configuration

- **Proxy Configuration**: This script uses `FreeProxy` for handling proxies. To change proxy settings, refer to the `FreeProxy` documentation.
- **User Agents**: User agents are stored in a list, and you can add or modify entries to improve randomization or cater to specific needs.

### Code Overview

Here’s a breakdown of the main components:

1. **Banner Display**: A visual banner with ASCII art and author information.
2. **Proxy Integration**: Uses `FreeProxy` to fetch a proxy IP, reducing the chances of getting blocked.
3. **User Agent Randomization**: Randomly selects a user agent from the list to emulate various devices and browsers.
4. **Account Creation**: Uses Selenium commands to automate filling out the Gmail sign-up form.
5. **Error Handling**: Contains try-except blocks to manage common issues and delays to prevent detection.

### Troubleshooting

- **Chromedriver Compatibility**: Ensure that the version of Chromedriver matches your installed Chrome version.
- **Proxy Errors**: Some proxies may be unreliable. Restart the script to fetch a new proxy if errors persist.
- **Element Not Found**: If Gmail updates its sign-up form, some elements may need to be updated in the code.

---

### Example Code Snippet

Here’s an example of how the script initializes the WebDriver:

```python
options = ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")

# Set a random user agent
user_agent = random.choice(user_agents)
options.add_argument(f"user-agent={user_agent}")

# Set a proxy
proxy = FreeProxy().get()
options.add_argument(f"--proxy-server={proxy}")

driver = webdriver.Chrome(service=ChromeService(), options=options)
```

This code configures Chrome with a randomized user agent and proxy to improve anonymity.

---

### License

This project is licensed under the MIT License. For more information, check the `LICENSE` file.

--- 

This documentation should help you set up, configure, and troubleshoot the Auto-Gmail-Creator script.
