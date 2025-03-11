# Import for the Desktop Bot
from botcity.core import DesktopBot

# Import for the Web Bot
from botcity.web import WebBot, Browser, By

from app import news
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
    titles = news.get_titles_news(webbot, "Dólar")

    desktop_bot.type_windows()
    desktop_bot.paste("LibreOffice Impress")
    desktop_bot.enter()
    if desktop_bot.find("fechar_btn"):
        desktop_bot.click()


    if desktop_bot.find("title_field"):
        desktop_bot.click()

    desktop_bot.paste(f"Principais notícias sobre: {search_text}")


    if desktop_bot.find("text_field"):
        desktop_bot.click()
    
    for title in titles:
        desktop_bot.paste(title)
        desktop_bot.enter()
    desktop_bot.backspace()

    desktop_bot.control_a()
    for _ in range(4):
        desktop_bot.control_key("[")

    if not desktop_bot.find("formatte_bt"):
        not_found("formatte_bt")
        return
    desktop_bot.click()

    if desktop_bot.find("list_bt"):
        desktop_bot.click()
    
    if desktop_bot.find("unordered_list_bt"):
        desktop_bot.click()

    desktop_bot.control_s()
    desktop_bot.wait(2000)
    desktop_bot.kb_type("novo_file")

    desktop_bot.enter()
    input()


    webbot.wait(3000)


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
