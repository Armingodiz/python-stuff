from bs4 import BeautifulSoup as soup 

from urllib.request import urlopen as uReq 


url_doller = "https://www.tgju.org/%D9%82%DB%8C%D9%85%D8%AA-%D8%AF%D9%84%D8%A7%D8%B1"
url_total = "https://www.tgju.org/"
my_client = uReq(url_doller)
my_client2 = uReq(url_total)




page_total = soup(my_client2.read(),"html.parser")
my_client2.close()


gold = page_total.findAll("li",{"id":"l-geram18"})
print("GOLD : "+ str(gold[0].span.span.text) + " RIAL ")

doller = page_total.findAll("li",{"id":"l-price_dollar_rl"})
print("DOLLER : "+ str(doller[0].span.span.text)+ " RIAL ")


page_doller = soup(my_client.read(), "html.parser")
my_client.close()
containers = page_doller.findAll("div", {"class": "market-medium-excerpt excerpt"})
print("\n")
print("MORE INFO ABOUT DOLLER : "+"\n" +containers[0].p.text)