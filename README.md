# Selenium Bot

This project is a Selenium boilerplate that includes bypass techniques for bot detection and optional proxy support. The code is designed for scraping or automation in web environments where anti-bot measures such as Cloudflare are in place. It also provides proxy configuration to mask the IP address and Selenium detection bypass features to avoid triggering automation detection mechanisms.

## Features
- **Proxy Support**: You can enable proxy usage to mask your IP.
- **Anti-bot Bypass**: Includes an experimental Cloudflare bypass technique.
- **Selenium Detection Bypass**: Custom Chrome options are set to avoid automation detection.
- **Automatic Tab Management**: Automatically clears open tabs except for the main one.

## Requirements
- Python 3.x
- Chrome or Chromium browser
- ChromeDriver (compatible with your Chrome version)

## Setup

1. **Install Dependencies**:
   Make sure you have Selenium installed. You can install it via pip:
   ```bash
   pip install selenium
   ```

2. **ChromeDriver**:
   Download ChromeDriver from the [official site](https://sites.google.com/chromium.org/driver/) and ensure it is placed in the project directory.

3. **Chrome/Chromium Setup**:
   Place your browser binary in the `chrome/` folder within the project directory. Update the `chrome_options.binary_location` in the script to point to your specific browser binary path.

4. **User Data Directory**:
   The browser user data is stored in a folder named `data_dir` in the project root. This will save cookies and sessions between runs.

## Usage

1. **Proxy Configuration**:
   If you want to use a proxy, set `use_proxy = True` in the code and configure the proxy address:
   ```python
   proxy = 'proxy-server.com:1080'
   ```

2. **Selenium Detection Bypass**:
   The following Chrome options are configured to bypass Selenium detection:
   - Removes the `enable-automation` switch.
   - Disables crash reports and background tasks to reduce detection.
   - Prevents image loading to save data.

3. **Running the Script**:
   After configuration, run the script:
   ```bash
   python main.py
   ```
   It will open a Chrome browser, navigate to the specified site, and attempt to bypass anti-bot measures if needed.

## Key Functions

- **`clear_tabs()`**: Closes all but the main tab to manage open tabs.
- **`navigate(site)`**: Opens a site using an unconventional method to bypass anti-bot detection, particularly for Cloudflare.
- **`cloudflare()`**: Experimental function to bypass Cloudflare's "Just a moment" screen by interacting with iframes and checkboxes.

## Notes
- This script is experimental and may not work on all websites.
- Cloudflare and other anti-bot protections are constantly evolving, so results may vary depending on the site's configuration.
- Ensure that your use of this tool complies with the website's terms of service and legal regulations regarding scraping.

## License
This project is licensed under the GNU General Public License v3.0.
