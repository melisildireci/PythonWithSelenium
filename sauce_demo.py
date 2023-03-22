from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

# Main class for testing
class Test_sauce:
#Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
    def empty_login():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(2)
        login_btn = driver.find_element(By.ID, "login-button")
        login_btn.click()
        error_message = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        test_result = error_message.text == "Epic sadface: Username is required"
        print(f"No input and password: {test_result}")
        driver.quit()
#Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.   
    def only_username():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(2)
        name_input = driver.find_element(By.ID, "user-name")
        name_input.send_keys("1")
        login_btn = driver.find_element(By.ID, "login-button")
        login_btn.click()
        error_message = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        test_message = error_message.text == "Epic sadface: Password is required"
        print(f"result error: {test_message}")
        driver.quit()
#Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir. 
    def locked_out():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(2)
        name_input = driver.find_element(By.ID, "user-name")
        name_input.send_keys("locked_out_user")
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("secret_sauce")
        login_btn = driver.find_element(By.ID, "login-button")
        login_btn.click()
        error_message = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3")
        test_message = error_message.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"result error: {test_message}")
        driver.quit()
#Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.
    def true_login():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")    
        driver.maximize_window()
        sleep(3)
        name_input.send_keys("standard_user")
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("secret_sauce")
        login_btn = driver.find_element(By.ID, "login-button")
        login_btn.click()
        sleep(5)
        driver.get("https://www.saucedemo.com/inventory.html")
        driver.quit
        
#Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.  
    def products():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")    
        driver.maximize_window()
        sleep(2)
        name_input = driver.find_element(By.ID, "user-name")
        name_input.send_keys("standard_user")
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("secret_sauce")
        login_btn = driver.find_element(By.ID, "login-button")
        login_btn.click()
        sleep(5)
        driver.get("https://www.saucedemo.com/inventory.html")
        list_product = driver.find_elements(By.CLASS_NAME, "inventory_item")
        print(f"products: {len(list_product)}")
        driver.quit()
    
#Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır.
#Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır.
    def x_icon():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")    
        driver.maximize_window()
        sleep(2)
        name_input = driver.find_element(By.ID, "user-name")
        password_input = driver.find_element(By.ID, "password")
        login_btn = driver.find_element(By.ID, "login-button")
        login_btn.click()
        sleep(3)
        error_exitIcon = driver.find_element(By.CLASS_NAME, "error-button")
        error_exitIcon.click()



def main():
    
    test_sauce = Test_sauce()

    
    test_sauce.empty_login()
#   test_sauce.only_username()
#   test_sauce.locked_out()
#    
#   test_sauce.true_login()
#   test_sauce.x_icon()
#   test_sauce.products()


# main function
if __name__ == "__main__":
    main()
        
        

        
        
        
        
        
        
    