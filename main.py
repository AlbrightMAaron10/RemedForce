# library for web requests
import requests
from requests.exceptions import HTTPError
# library for browser nav
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



# ___________________________________________________________________________________________
# Website/System - URL for Report Generation
# Remedy Force Reports - Created By Me - >
# Report Name: SAP Firefighters (FY 24)
# Sidebar -> click "Run"
# Edit - Sidebar -> click "Export"
# Export View - "Details Only"
# Format: Excel Format .xls
# Encoding : ISO-8859-1 (General US & Western European, ISO-LATIN-1)
# click "export"
# report1706884651375
# Format report: Rename, borders, Center, Allign
# ____________________________________________________________________________________________
# <button aria-live="off" type="button" title="Export" class="slds-button slds-button--neutral uiButton--default uiButton--brand uiButton" aria-label="" data-aura-rendered-by="2646:0" data-aura-class="uiButton--default uiButton--brand uiButton"><!--render facet: 2647:0--><span dir="ltr" class="buttonLabel label bBody" data-aura-rendered-by="2649:0">Export</span><!--render facet: 2651:0--></button>
# document.querySelector("body > div.desktop.container.forceStyle.oneOne.navexDesktopLayoutContainer.lafAppLayoutHost.forceAccess.tablet > div.DESKTOP.uiContainerManager > div.DESKTOP.uiModal.open.active > div.panel.slds-modal.slds-fade-in-open > div > div.modal-footer.slds-modal__footer > button.slds-button.slds-button--neutral.uiButton--default.uiButton--brand.uiButton")
# Remedy force Export view - Export button XPath : /html/body/div[5]/div[2]/div/div[2]/div/div[3]/button[2]

url = "https://cliffsnr.lightning.force.com/lightning/r/Report/00OUM000000SDtZ2AW/view"

mydriver = webdriver.Chrome()
mydriver.get(url)
mydriver.maximize_window()
time.sleep(10)

#mydriver.find_element(by=By.XPATH, value='//*[@id="tFI1TXPUX4-item-3"]').click()
iframe = mydriver.find_element(By.XPATH, value="//*[@id='brandBand_2']/div/div/div/iframe")
#mydriver.find_element(by=By.XPATH, value = '//*[@id="tFI1TXPUX4"]/button/svg/path').click()
mydriver.switch_to.frame(iframe)
mydriver.find_element(By.XPATH, value="/html/body/div[9]/div/div[1]/div/div[1]/div[1]/div[1]/div[2]/div/div/div/div[6]/div/div/button").send_keys(Keys.ENTER)

time.sleep(2)

mydriver.find_element(By.XPATH, value="/html/body/div[9]/div/div[1]/div/div[1]/div[1]/div[1]/div[2]/div/div/div/div[6]/div/div/div/ul/li[4]/a").click()



time.sleep(2)


#webelement = mydriver.find_element(By.ID, value="/html/body/div[5]/div[2]/div[2]")
mydriver.switch_to.default_content()


time.sleep(2)

time.sleep(2)
try:
    mydriver.find_element(By.CSS_SELECTOR, value="body > div.desktop.container.forceStyle.oneOne.navexDesktopLayoutContainer.lafAppLayoutHost.forceAccess.tablet > div.DESKTOP.uiContainerManager > div.DESKTOP.uiModal.open.active > div.panel.slds-modal.slds-fade-in-open > div > div.modal-footer.slds-modal__footer > button.slds-button.slds-button--neutral.uiButton--default.uiButton--brand.uiButton").click()
#mydriver.switch_to.frame(iframe)
    mydriver.switch_to.frame(iframe)
    WebDriverWait(mydriver ,5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[aria-labelledby="title_3140:0"]')))
except:
    print("done")






