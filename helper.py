import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pdfplumber
transport_map = {
        "Walk": "Walking",
        "Underground": "MRT",
        "Bus": "Bus"
    }


def convert_to_min(time_str):
    
    # Extract hours and minutes using regex
    import re
    match = re.match(r"(?:(\d+)\s*hr)?\s*(?:(\d+)\s*min)?", time_str)
    if match:
        hours = int(match.group(1)) if match.group(1) else 0
        minutes = int(match.group(2)) if match.group(2) else 0
        total_minutes = hours * 60 + minutes
        return total_minutes
    

def extract_locations_from_pdf(pdf_path):
    """
    Extracts locations from the PDF file.
    """
    locations =[]
    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:
            (page.extract_table())
            k = page.extract_table() 
            if k is not None and k[0] is not None and "COOKED FOOD" in str(k[0][0]):
                for i in k[2:]:
                    if i[0] is not None and i[0] != "":
                        locations.append(i[0].replace('\n', ' ').replace('  ', ' ').strip().replace("*",""))
                        
                        
    return locations

def load_url(driver, locationFrom, locationTo):
    link = f'https://www.google.com/maps/dir/{str(locationFrom)}/{str(locationTo)}/'.replace(" ", "+")
     
    driver.get(link)
    assert locationFrom in driver.title
    
    

def scroll_until_xpath(driver):
    '''
    The xpath is the element that we want to scroll to.
    '''
    xpath = '/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[5]/div[1]'
    
    while True:
        try:
            # Check if the element is present
            element = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            # Scroll to the element
            driver.execute_script("arguments[0].scrollIntoView();", element)
            break
        except:
            # Scroll down incrementally
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)  # Wait for the page to load more content
            
def extract_data(driver):
        
    
    driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[8]/div[3]/div[1]/div[2]/div/div[2]/div/div/div/div[4]/button").click()
    scroll_until_xpath(driver)
    datas = driver.find_elements(By.CLASS_NAME,'MespJc')
    alt_pattern = re.compile(r'alt="([^"]+)"')
    result = []
    for data in datas:

        time = convert_to_min(data.find_element(By.CLASS_NAME, 'XdKEzd').text)
        journey = [time]
        transport_methods = data.find_elements(By.CLASS_NAME, 'mTOalf')
        for transport in transport_methods:
            outer_html = transport.get_attribute('outerHTML')
            match = alt_pattern.search(outer_html)
            if match:
                alt_text = match.group(1)  # Extract the value of 'alt'
                
                journey.append(transport_map.get(alt_text))
                
        result.append(journey)
    return result