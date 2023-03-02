from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time



link = 'https://idiomasic.com/noticias/las-1000-palabras-mas-comunes-en-ingles/'
#Expresiones regulares
import re

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument("--headless") # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")
    
    
chrome_options = webdriver.ChromeOptions() 

driver = webdriver.Chrome(chrome_options=options)

# Iniciarla en la pantalla 2
driver.set_window_position(2000, 0)
driver.maximize_window()
time.sleep(1)


# Inicializamos el navegador
driver.get(link)
time.sleep(4)

texto_columnas = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[1]/div/article/div[3]/div[2]/figure/table/tbody')
texto_columnas = texto_columnas.text
texto_columnas = texto_columnas.split('\n')



def dividir_por_palabras():
    texto_palabras = []
    for i in range(0,len(texto_columnas)):
        palabra = texto_columnas[i].split(' ')
        texto_palabras.append(palabra)
        
    return texto_palabras 


def sacar_parte_ingles():
    palabras_ingles = []
    for i in range(0,len(texto_columnas)):
        palabra = dividir_por_palabras()[i]
        palabras_ingles.append(palabra[1])
        
    return palabras_ingles
        
def sacar_parte_espanol():
    palabras_espanol = []
    nuevo_vector = []
    for i in range(0,len(texto_columnas)):
        palabra = dividir_por_palabras()[i]
        palabras_espanol.append(palabra[2:]) 
        
    # Recorremos cada subvector en el vector original
    for subvector in palabras_espanol:
        # Si el subvector tiene una sola palabra, la agregamos directamente al nuevo vector
        if len(subvector) == 1:
            nuevo_vector.append(subvector[0])
        # Si el subvector tiene dos o más palabras, las unimos en una sola cadena y la agregamos al nuevo vector
        else:
            nueva_palabra = ' '.join(subvector)
            nuevo_vector.append(nueva_palabra)       

    return nuevo_vector





