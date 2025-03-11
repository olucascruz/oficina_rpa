# Import for the Desktop Bot
from botcity.core import DesktopBot

# Import for the Web Bot
from botcity.web import WebBot, Browser, By

from app import news
from app import powerpoint
from selenium.webdriver.common.keys import Keys

def main():
    webbot = WebBot()
    desktop_bot = DesktopBot()

    # Configure whether or not to run on headless mode
    webbot.headless = False
    # Uncomment to change the default Browser to Firefox
    webbot.browser = Browser.FIREFOX
    # Uncomment to set the WebDriver path
    webbot.driver_path = r"webdriver\geckodriver.exe"

    search_text = "Dólar"
    titles = news.get_titles_news(webbot, search_text)
    powerpoint.create_pptx(desktop_bot, search_text, titles)
    

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
