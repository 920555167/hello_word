from time import sleep
from selenium import webdriver

chrome = webdriver.Chrome()
def getfile(url):

    chrome.get(url)
    texts=chrome.find_elements_by_xpath("//div[@id='BookText']/p")
    for t in texts:
        with open ('1.txt','a')as f:
           f.write(t.text+"\n")

    sleep(1)
    next_url=chrome.find_elements_by_xpath("//div[@class='link']/a")
    if next_url:
        next_urls=next_url[2].get_attribute("href")
        chrome.find_elements_by_xpath("//div[@class='link']/a")[2].click()
        getfile(next_urls)
    else:
        chrome.close()
        return
getfile("http://www.jianlaixiaoshuo.com/book/17.html")