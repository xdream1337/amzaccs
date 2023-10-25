import time, random, string
from threading import Thread
import pyautogui
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import undetected_chromedriver as uc

proxies = [
    "192.142.71.240:2135:lmfao:ahPheo2phu",
    "192.142.71.241:2135:lmfao:ahPheo2phu",
    "192.142.71.242:2135:lmfao:ahPheo2phu",
    "192.142.71.243:2135:lmfao:ahPheo2phu",
    "192.142.71.244:2135:lmfao:ahPheo2phu",
    "192.142.71.245:2135:lmfao:ahPheo2phu",
    "192.142.71.246:2135:lmfao:ahPheo2phu",
    "192.142.71.247:2135:lmfao:ahPheo2phu",
    "192.142.71.248:2135:lmfao:ahPheo2phu",
    "192.142.71.249:2135:lmfao:ahPheo2phu",
]

random_proxy = random.choice(proxies)
proxy_components = random_proxy.split(":")
host = proxy_components[0]
port = proxy_components[1]
user = proxy_components[2]
passw = proxy_components[3]

print(f"Using proxy: {host}:{port}")

chrome_options = uc.ChromeOptions()
chrome_options.headless = False
chrome_options.add_argument("--proxy-server={}".format(host + ":" + port))

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.99 Safari/537.36"
chrome_options.add_argument(f"--user-agent={user_agent}")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--window-size=1280,800")
chrome_options.add_argument("--disable-webgl")
chrome_options.add_argument("--disable-webrtc")
chrome_options.add_argument("--disable-remote-fonts")
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("--disable-features=InfiniteSessionRestore")
chrome_options.add_argument("--disable-features=VizDisplayCompositor")
chrome_options.add_argument("--disable-features=VizHitTestSurfaceLayer")
chrome_options.add_argument("--disable-gpu-compositing")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-logging")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-software-rasterizer")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--disable-logging")
chrome_options.add_argument("--safebrowsing-disable-auto-update")
chrome_options.add_argument("--use-mock-keychain")
chrome_options.add_argument("--disable-features=TranslateUI")
chrome_options.add_argument("--disable-features=WebRtcHideLocalIpsWithMdns")

driver = uc.Chrome(options=chrome_options)


def enter_proxy_auth(proxy_username, proxy_password):
    time.sleep(1)
    pyautogui.typewrite(proxy_username)
    pyautogui.press("tab")
    pyautogui.typewrite(proxy_password)
    pyautogui.press("enter")


def input_element(driver, element_ID, text, random_click):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, element_ID))
    )
    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()

    time.sleep(random.uniform(0.5, 1.5))
    for char in text:
        typing_interval = random.gauss(0.5, 0.05)
        time.sleep(typing_interval)
        element.send_keys(char)

        if random.random() < 0.1:
            time.sleep(random.uniform(0.3, 0.7))

    if random_click:
        actions.move_to_element(element).move_by_offset(200, 150).click().perform()


def delete_element(driver, element_id, text):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, element_id))
    )

    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()

    for i in range(len(text)):
        typing_interval = random.gauss(0.5, 0.05)
        time.sleep(typing_interval)
        element.send_keys(Keys.BACKSPACE)


def main(driver, url):
    """driver.get("https://github.com/SeleniumHQ/selenium/issues/10025")
    time.sleep(10)
    driver.get(
        "https://www.endtest.io/blog/a-practical-guide-for-finding-elements-with-selenium"
    )
    time.sleep(10)
    driver.get("https://www.selenium.dev/documentation/webdriver/elements/finders/")
    time.sleep(10)
    driver.get(
        "https://www.reddit.com/r/selenium/comments/wjv59o/selenium_cant_find_element_with_idname/"
    )
    time.sleep(10)
    driver.get(
        "https://subscription.packtpub.com/book/programming/9781784392512/2/ch02lvl1sec22/finding-elements-by-tag-name"
    )
    time.sleep(10)
    driver.get("https://pythonexamples.org/python-selenium-find-element-by-tag-name/")
    time.sleep(10)
    driver.get("https://twitter.com/")
    time.sleep(10)
    driver.get("https://amazon.com")
    time.sleep(10)
    driver.get(
        "https://www.amazon.com/2021-Apple-10-2-inch-iPad-Wi-Fi/dp/B09G9FPHY6/ref=lp_16225009011_1_2?sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D"
    )
    time.sleep(10)
    driver.get(
        "https://www.amazon.com/s?i=specialty-aps&bbn=16225006011&rh=n%3A%2116225006011%2Cn%3A3777891&_encoding=UTF8&ref=pd_gw_unk"
    )
    time.sleep(10)
    driver.get(
        "https://www.amazon.com/deal/7def8902/?_encoding=UTF8&showVariations=false&moreDeals=11461066&_ref=dlx_gate_dd_dcl_tlt_7def8902_dt&ref_=pd_gw_unk"
    )
    time.sleep(10)
    driver.get(
        "https://www.amazon.com/Team-Fan-Apparel-Lightweight-Semi-Fitted/dp/B09K63NCK1?ref_=Oct_DLandingS_D_7def8902_2"
    )
    time.sleep(10)
    driver.get(
        "https://www.audible.com/pd/Atomic-Habits-Audiobook/1524779261?ref_pageloadid=not_applicable&ref=a_hp_c6_p13n-mpl-dt-c_1_4&pf_rd_p=54cb6340-d253-4ab5-a77b-9d49d89f9640&pf_rd_r=JTV08HGV5FN3CER5FM27&pageLoadId=arXkf4mdipk4ViET&ref_plink=not_applicable&creativeId=41d14d25-162f-48fb-9d54-1ae394965020"
    )
    time.sleep(10)
    driver.get("https://www.shopbop.com")
    time.sleep(10)
    driver.get("https://www.boxofficemojo.com/?ref_=amzn_nav_ftr")
    time.sleep(10)
    driver.get(
        "https://news.google.com/articles/CBMilAFodHRwczovL3d3dy50aGVndWFyZGlhbi5jb20vY29tbWVudGlzZnJlZS8yMDIzL29jdC8yNC90aGUtZ3VhcmRpYW4tdmlldy1vbi10aGUtcG93ZXItb2YtZm9yZ2l2ZW5lc3MtYS1mcmVlZC1ob3N0YWdlcy1nZXN0dXJlLXNob3VsZC1ub3QtYmUtZm9yZ290dGVu0gEA?hl=en-US&gl=US&ceid=US%3Aen"
    )
    time.sleep(10)
    driver.get("https://www.youtube.com/watch?v=E17P_aq_UaI")
    time.sleep(10)"""

    # woot flow
    """element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "signin"))
    )
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "signup"))
    )
    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()
    time.sleep(1)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "createAccountSubmit"))
    )
    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()
    time.sleep(1)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Create an Amazon"))
    )
    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()"""

    driver.get("https://audible.com")
    time.sleep(4)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Sign Up"))
    )
    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()
    time.sleep(1)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "createAccountSubmit"))
    )
    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()
    time.sleep(1)
    # driver.get(url)

    input_element(driver, "ap_customer_name", "Johnnz Grazson", True)
    time.sleep(1)
    input_element(driver, "ap_email", "graysonjohnny@gmail.com", True)
    time.sleep(0.8)
    # input_element(driver, "ap_email_check", "graysonjohnny", True)
    time.sleep(0.9)
    input_element(driver, "ap_password", "abcdefghtp123", True)
    time.sleep(0.75)
    input_element(driver, "ap_password_check", "abcdefghtp123", True)
    time.sleep(0.89)
    delete_element(driver, "ap_customer_name", "z Grazson")
    time.sleep(0.67)
    input_element(driver, "ap_customer_name", "y Grayson", True)
    time.sleep(0.89)
    # delete_element(driver, "ap_email_check", "graysonjohnny@gmail.com")
    time.sleep(0.6)
    # input_element(driver, "ap_email_check", "graysonjohnny@gmail.com", True)
    time.sleep(0.99)

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "continue"))
    )
    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()


Thread(
    target=main,
    args=(
        driver,
        "https://www.amazon.com/ap/register?openid.pape.max_auth_age=1209600&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&siteState=131-4116517-6138845&marketPlaceId=AF2M0KC94RCEA&pageId=amzn_audible_bc_us&openid.return_to=https%3A%2F%2Fwww.audible.com%2Fsubscription%2Fconfirmation%3Fref_pageloadid%3Dnot_applicable%26ref%3Da_hp_c1_member_cta1%26pf_rd_p%3D0b9dcaaa-04f3-44aa-ace6-e1cb47945f3f%26membershipAsin%3DB076FLV3HT%26pf_rd_r%3DZY0TJW68629V4A4PASDJ%26pageLoadId%3Dj2QsQl8cOIk941Kq%26ref_plink%3Dnot_applicable%26creativeId%3D711b5140-9c53-4812-acee-f4c553eb51fe%26loginAttempt%3Dtrue&prevRID=WPEMRBTGC72HK7TAA3Q2&openid.assoc_handle=audible_shared_web_sso_us&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0",
    ),
).start()
Thread(target=enter_proxy_auth, args=(user, passw)).start()

input("Press Enter to close the browser...")

driver.quit()
