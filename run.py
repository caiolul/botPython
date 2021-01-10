from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


option = Options()
option.binary_location = "/usr/bin/brave-browser"
driver_path = "/usr/local/bin/chromedriver"

#drv = webdriver.Chrome(options = option, executable_path = driver_path)
drv = webdriver.Chrome()
drv.get("https://cosmos.bluesoft.com.br/")


assert "Catálogo de Produtos" in drv.title
elem = drv.find_element_by_name("q")
elem.clear()
elem.send_keys("7899508900539")
elem.send_keys(Keys.RETURN)
assert "No results found." not in drv.page_source



drv.close()
