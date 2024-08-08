from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/index.html")
sleep(2)

# Registro
# boton de registro en home
boton = driver.find_element(By.XPATH, "//*[@id='signin2']")
boton.click()
sleep(2)

# input de usuario en modal - registro
escribir = driver.find_element(By.XPATH, "//*[@id='sign-username']")
escribir.send_keys("AnthonyLuzonITSQMET")

# input de contraseña en modal - registro
escribir = driver.find_element(By.XPATH, "//*[@id='sign-password']")
escribir.send_keys("user123")

# boton de envio en modal - registro
boton = driver.find_element(By.XPATH, "//*[@id='signInModal']/div/div/div[3]/button[2]")
boton.click()
sleep(2)

alert = driver.switch_to.alert 
alert.accept()

# Login
# boton de login en home
boton = driver.find_element(By.XPATH, "//*[@id='login2']")
boton.click()
sleep(2)

# input de usuario en modal - login
escribir = driver.find_element(By.XPATH, "//*[@id='loginusername']")
escribir.send_keys("AnthonyLuzonITSQMET")

# input de contraseña en modal - login
escribir = driver.find_element(By.XPATH, "//*[@id='loginpassword']")
escribir.send_keys("user123")

# boton de envio en modal - login
boton = driver.find_element(By.XPATH, "//*[@id='logInModal']/div/div/div[3]/button[2]")
boton.click()
sleep(2)

# Seleccionar productos
# producto 1
# seleccionar
boton = driver.find_element(By.XPATH, "//*[@id='tbodyid']/div[8]/div/div/h4/a")
boton.click()
sleep(2)

# añadir al carrito
boton = driver.find_element(By.XPATH, "//*[@id='tbodyid']/div[2]/div/a")
boton.click()
sleep(2)

alert = driver.switch_to.alert 
alert.accept()

# volver a los productos
boton = driver.find_element(By.XPATH, "//*[@id='navbarExample']/ul/li[1]/a")
boton.click()
sleep(2)

# producto 2
# seleccionar
boton = driver.find_element(By.XPATH, "//*[@id='tbodyid']/div[3]/div/div/h4/a")
boton.click()
sleep(2)

# añadir al carrito
boton = driver.find_element(By.XPATH, "//*[@id='tbodyid']/div[2]/div/a")
boton.click()
sleep(2)

alert = driver.switch_to.alert 
alert.accept()

# Carrito
# ingresar
boton = driver.find_element(By.XPATH, "//*[@id='navbarExample']/ul/li[4]/a")
boton.click()
sleep(2)

# pulsar place order
boton = driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div/div[2]/button")
boton.click()
sleep(2)

# rellenar informacion
escribir = driver.find_element(By.XPATH, "//*[@id='name']")
escribir.send_keys("Anthony Luzon")

escribir = driver.find_element(By.XPATH, "//*[@id='country']")
escribir.send_keys("Ecuador")

escribir = driver.find_element(By.XPATH, "//*[@id='city']")
escribir.send_keys("Quito")

escribir = driver.find_element(By.XPATH, "//*[@id='card']")
escribir.send_keys("9999-9999-9999-9999")

escribir = driver.find_element(By.XPATH, "//*[@id='month']")
escribir.send_keys("19")

escribir = driver.find_element(By.XPATH, "//*[@id='year']")
escribir.send_keys("2028")

# pulsar purchase
boton = driver.find_element(By.XPATH, "//*[@id='orderModal']/div/div/div[3]/button[2]")
boton.click()
sleep(2)

# pulsar ok
boton = driver.find_element(By.XPATH, "/html/body/div[10]/div[7]/div/button")
boton.click()
sleep(2)

# Deslogearse
boton = driver.find_element(By.XPATH, "//*[@id='logout2']")
boton.click()
sleep(2)