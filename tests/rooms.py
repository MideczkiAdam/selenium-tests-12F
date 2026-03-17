from selenium.webdriver.common.by import By

def first_room(driver):
    # USERNAME
    username_input = driver.find_element(By.XPATH, '//*[@id="root"]/main/div[1]/input[1]')
    username_input.send_keys('admin')

    # PASSWORD
    password_input = driver.find_element(By.XPATH, '//*[@id="root"]/main/div[1]/input[2]')

    password_p = driver.find_element(By.CSS_SELECTOR, '#root > main > div.flip-card > div > div.flip-card-back > p:nth-child(3)')

    pwd = password_p.get_attribute("textContent")

    password_input.send_keys(pwd)

    # LOGIN BUTTON CLICK
    login_btn = driver.find_element(By.TAG_NAME, 'button')
    login_btn.click()

    print("Első szoba kész!")

def second_room(driver):
    driver.implicitly_wait(5)

    gen_table_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/button[1]')

    while(True):
        try:
            gen_table_btn.click()
        except:
            break
    
    test_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/button')
    test_btn.click()

def third_room(driver):
    driver.implicitly_wait(5)

    tipp_input = driver.find_element(By.XPATH, '//*[@id="root"]/main/div/input')
    tipp_btn = driver.find_element(By.XPATH, '//*[@id="root"]/main/div/button')
    
    for i in range(0, 99):
        tipp_input.send_keys(i)
        tipp_btn.click()
        driver.implicitly_wait(5)
        result_h2 = driver.find_element(By.XPATH, '//*[@id="root"]/main/div/h2')
        if '✅' in result_h2.get_attribute("textContent"):
            break
        tipp_input.clear()
    
    next_page_link = driver.find_element(By.XPATH, '//*[@id="root"]/main/div/a')
    next_page_link.click()

def fourth_room(driver):
    driver.implicitly_wait(5)

    binary_num = driver.find_element(By.XPATH, '//*[@id="root"]/div/p[2]').get_attribute("textContent")
    num_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/label/input')
    tipp_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div/button')

    decimal_num = int(binary_num, 2)
    num_input.send_keys(decimal_num)
    tipp_btn.click()

musics = []

def fifth_room(driver):
    driver.implicitly_wait(5)

    while (True):
        driver.implicitly_wait(5)
        try:
            try_again = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/button')
            try_again.click()
        except:
            pass

        num1 = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/p[2]').get_attribute("textContent")
        music = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/h2')
        data = {
            "title": music.get_attribute("textContent"),
            "streams": int(num1.replace("streams", "").replace(".", ""))
        }

        right_title = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/h2')
        right_string = right_title.get_attribute("textContent")

        right_data = next(filter(lambda x:x['title'] == right_string, musics), None)

        if right_data != None and right_data['streams'] > data['streams']:
            right_title.click()

        musics.append(data) 
        music.click()

def sixth_room(driver):
    driver.implicitly_wait(5)
    

