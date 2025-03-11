from botcity.web import By

def get_titles_news(webbot, search_text):

    webbot.browse("https://news.google.com/home?hl=pt-BR&gl=BR&ceid=BR:pt-419")
    webbot.maximize_window()
    
    input_el = webbot.find_element("/html/body/div[4]/header/div[2]/div[2]/div[2]/form/div[1]/div/div/div/div/div[1]/input[2]", by=By.XPATH)
    input_el.click()
    
    webbot.wait(3000)
    webbot.paste(search_text)
    webbot.enter()
   
    list_text_news = []

    webbot.wait(2000)
    news1 = webbot.find_element('//html/body/c-wiz[2]/div/main/div[2]/c-wiz/c-wiz[1]/c-wiz/article/div[1]/div[2]/div/a', by=By.XPATH).text
    news2 = webbot.find_element('/html/body/c-wiz[2]/div/main/div[2]/c-wiz/c-wiz[2]/c-wiz/article/div[1]/div[2]/div/a', by=By.XPATH).text
    news3 = webbot.find_element('//html/body/c-wiz[2]/div/main/div[2]/c-wiz/c-wiz[3]/c-wiz/article/div[1]/div[2]/div/a', by=By.XPATH).text
    news4 = webbot.find_element('//html/body/c-wiz[2]/div/main/div[2]/c-wiz/c-wiz[4]/c-wiz/article/div[1]/div[2]/div/a', by=By.XPATH).text
    news5 = webbot.find_element('//html/body/c-wiz[2]/div/main/div[2]/c-wiz/c-wiz[5]/c-wiz/article/div[1]/div[2]/div/a', by=By.XPATH).text
    

    webbot.stop_browser()
    list_text_news.append(news1)
    list_text_news.append(news2)
    list_text_news.append(news3)
    list_text_news.append(news4)
    list_text_news.append(news5)

    return list_text_news