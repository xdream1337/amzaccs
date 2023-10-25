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


# click 10 times on random links on loaded url
def iterate_domain_links(driver, url):
    wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed

    driver.get(url)

    for i in range(10):
        try:
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "a")))
        except TimeoutException:
            pass

        a_list = driver.find_elements(By.TAG_NAME, "a")
        all_links = [item.get_attribute("href") for item in a_list]
        link = random.choice(all_links)
        driver.get(link)
        time.sleep(random.randint(5, 10))


def woot_registration_flow(driver):
    driver.get("https://woot.com")

    # hover over account signin
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "signin"))
    )
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    # click on signup button
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "signup"))
    )
    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()
    time.sleep(1)

    # click on create account button
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "createAccountSubmit"))
    )
    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()

    # click on create amazon account link
    time.sleep(1)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Create an Amazon"))
    )
    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()

    register_form_with_email_check(driver)


def amazon_registration_flow(driver):
    driver.get("https://amazon.com")

    # hover over account signin
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Account & Lists"))
    )
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(0.5)

    # click on signup button
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Start here."))
    )
    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()

    register_form_without_email_check(driver)


def audible_registration_flow(driver):
    driver.get("https://audible.com")

    # click on sign up link
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Sign Up"))
    )
    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()
    time.sleep(1)

    # click on create account button
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "createAccountSubmit"))
    )
    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()
    time.sleep(1)

    register_form_without_email_check(driver)


def register_form_without_email_check(driver):
    time.sleep(5)

    input_element(driver, "ap_customer_name", "Greg Kulinaai", True)
    time.sleep(1)
    input_element(driver, "ap_email", "gregkulinski@gmail.com", True)
    time.sleep(0.8)
    input_element(driver, "ap_password", "abcdefghtp123", True)
    time.sleep(0.75)
    input_element(driver, "ap_password_check", "abcdefghtp123", True)
    time.sleep(0.89)
    delete_element(driver, "ap_customer_name", "nski")
    time.sleep(0.67)
    input_element(driver, "ap_customer_name", "nski", True)
    time.sleep(0.89)

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "continue"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()
    except:
        pass

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "continue-signup"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()
    except:
        pass


def register_form_with_email_check(driver):
    time.sleep(4)

    input_element(driver, "ap_customer_name", "Johnnz Grazson", True)
    time.sleep(1)
    input_element(driver, "ap_email", "graysonjohnny@gmail.com", True)
    time.sleep(0.8)
    input_element(driver, "ap_email_check", "graysonjohnny", True)
    time.sleep(0.9)
    input_element(driver, "ap_password", "abcdefghtp123", True)
    time.sleep(0.75)
    input_element(driver, "ap_password_check", "abcdefghtp123", True)
    time.sleep(0.89)
    delete_element(driver, "ap_customer_name", "z Grazson")
    time.sleep(0.67)
    input_element(driver, "ap_customer_name", "y Grayson", True)
    time.sleep(0.89)
    delete_element(driver, "ap_email_check", "graysonjohnny@gmail.com")
    time.sleep(0.6)
    input_element(driver, "ap_email_check", "graysonjohnny@gmail.com", True)
    time.sleep(0.99)

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "continue"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()
    except:
        pass

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "continue-signup"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()
    except:
        pass


def mainn(driver):
    # iterate_domain_links(driver, "https://github.com")
    # iterate_domain_links(driver, "https://twitter.com")
    # iterate_domain_links(driver, "https://reddit.com")
    # iterate_domain_links(driver, "https://amazon.com")
    # iterate_domain_links(driver, "https://woot.com")
    # iterate_domain_links(driver, "https://6pm.com")

    amazon_registration_flow(driver)


Thread(
    target=mainn,
    args=(driver,),
).start()

Thread(target=enter_proxy_auth, args=(user, passw)).start()

input("Press Enter to close the browser...")

driver.quit()
