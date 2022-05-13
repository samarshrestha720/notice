from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# ChromeDriverManager().install()
opt=Options()
opt.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=opt)

driver.get(
    "http://nec.edu.np/index.php?option=com_content&view=category&id=47&Itemid=74"
)

whole_page = driver.find_element_by_tag_name("html")
page = whole_page.find_element_by_xpath("//tbody")
first_elem = page.find_element_by_xpath(
    "//tr[@class='sectiontableentry1']/td[3]").text
link = page.find_element_by_xpath("//tr[@class='sectiontableentry1']")

hits = int(first_elem)
flag = 0
if hits < 100 and flag == 0:
    print("Link: ", link)
    print("HITS: ", hits)
    driver.close()
    flag = 1
else:
    print("NO NEW NOTICES!!")
    print("HITS: ", hits)
    driver.close()
