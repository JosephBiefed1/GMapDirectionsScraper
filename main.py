


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
from time import sleep
from helper import extract_locations_from_pdf, load_url, extract_data

# Load the PDF
pdf_path = "apr-2025-tender-notice.pdf"

locations = extract_locations_from_pdf(pdf_path)


# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model (Linux)
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

# Initialize the WebDriver with headless options
driver = webdriver.Chrome(options=chrome_options)

driver.implicitly_wait(5)

locationFrom = ""  # Postal code

distance_tracker = []
for locationTo in locations:
    load_url(driver, locationFrom, locationTo)
    attempt_count = 0
    while attempt_count < 3:
        try:
            result = extract_data(driver)
            result = [x for x in result if x[0] != 0]
            result = sorted(sorted(result, key=lambda x: x[0], reverse=False), key=lambda x: len(x[1:]), reverse=False)
            distance_tracker.append(result)
            break
        except:
            sleep(2)
            attempt_count += 1

    sleep(2)

# Close the driver after use
driver.quit()


stats = []
distance_tracker = [x for x in distance_tracker if x[0] != 0]

for i in range(len(locations)):
    stats.append([locations[i], distance_tracker[i][0][0], distance_tracker[i][0][1:]])
    
df = pd.DataFrame(stats, columns=["Location", "Time", "Transport"])
df.to_csv("distance.csv", index=False)
