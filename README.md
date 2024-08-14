# Cross-Browser Testing with Selenium

## Overview

This project uses Selenium WebDriver with Python to perform cross-browser testing on a simple HTML page. The goal is to ensure that the website is compatible across different web browsers, including Chrome, Firefox, and Edge.

## Project Structure

- `index.html`: A simple HTML file used for testing cross-browser compatibility.
- `test_cross_browser.py`: A Python script that uses Selenium WebDriver to perform cross-browser testing on `index.html`.

## Prerequisites

Before running the tests, ensure you have the following installed:

- [Python 3.x](https://www.python.org/downloads/)
- [Selenium](https://www.selenium.dev/documentation/en/selenium_installation/)
- [ChromeDriver](https://sites.google.com/chromium.org/driver/)
- [GeckoDriver](https://github.com/mozilla/geckodriver/releases)
- [EdgeDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/rahul-gupta-2004/cross-browser-testing.git
   cd cross-browser-testing

2. Install the required Python packages:

   ```bash
   pip install selenium

3. Download the appropriate WebDriver for your browsers.

## Usage

1. Make sure the `index.html` file is located in the path specified in the test_cross_browser.py script:
   
   ```bash
   url = "path_to_your_local_file/index.html"
   ```

   Adjust the path to match the location of index.html on your system.
   
2. Run the `test_cross_browser.py` script:

   ```bash
   python test_cross_browser.py
   
3. The script will open the `index.html` file in each specified browser, perform a basic test, and print the results.

## Test Details
- Title Check: The script asserts that the page title contains "Cross-Browser Testing".
- Button Interaction: Simulates a click on a button with the ID `testButton` to verify that interactive elements work as expected.

## Troubleshooting
- Make sure your browser versions are compatible with the WebDriver versions you are using.
