# GMap Directions Scraper for Hawker Stall Applicants

This project is designed to assist individuals in Singapore who wish to apply for hawker stalls. It automates the process of extracting hawker stall locations from tender notices (PDFs) and calculates the travel time, distance, and best transport options to these locations using Google Maps. The results are saved in a CSV file for easy reference.

## Features

- **PDF Parsing**: Extracts hawker stall locations from tender notice PDFs.
- **Google Maps Integration**: Uses Google Maps to calculate travel time, distance, and transport options.
- **Data Export**: Outputs the results as a CSV file for further analysis.

## Tools and Technologies

- **Python**: Core programming language.
- **Selenium**: For web scraping and interacting with Google Maps.
- **Pandas**: For data manipulation and exporting results to CSV.
- **PyPDF2 or Similar**: For extracting text from PDF files.
- **Google Chrome WebDriver**: To automate browser interactions.

## Methodology

1. **Extract Locations**:
   - The script reads a tender notice PDF (e.g., `apr-2025-tender-notice.pdf`) and extracts the list of hawker stall locations.
2. **Set Up Web Scraper**:
   - A headless Chrome browser is initialized using Selenium for efficient scraping.
3. **Calculate Travel Details**:
   - For each location, the script queries Google Maps to retrieve travel time, distance, and the best transport options.
4. **Data Cleaning**:
   - Filters and sorts the results to ensure accuracy and relevance.
5. **Export Results**:
   - The processed data is saved as a CSV file (`distance.csv`) with columns for location, travel time, and transport options.

## How to Use

1. **Install Dependencies**:

   - Ensure you have Python installed.
   - Install the required Python libraries:
     ```bash
     pip install -r requirements.txt
     ```
2. **Prepare the PDF**:

   - Place the tender notice PDF (e.g., [apr-2025-tender-notice.pdf](http://_vscodecontentref_/1)) in the project directory.
3. **Run the Script**:

   - Execute the script:
     ```bash
     python main.py
     ```
4. **View Results**:

   - Open the generated `distance.csv` file to view the travel details.

## File Structure

- [main.py](http://_vscodecontentref_/2): The main script that handles the scraping and data processing.
- [helper.py](http://_vscodecontentref_/3): Contains helper functions for PDF parsing, URL loading, and data extraction.
- [apr-2025-tender-notice.pdf](http://_vscodecontentref_/4): Example tender notice PDF (replace with your own).
- `distance.csv`: Output file containing the travel details.

## Notes

- Ensure you have a stable internet connection as the script interacts with Google Maps.
- The script is optimized for use in Singapore but can be adapted for other locations with minor modifications.

## Future Improvements

- Add error handling for specific edge cases (e.g., invalid locations or network issues).
- Implement multi-threading to speed up the scraping process.
- Integrate a GUI for easier use by non-technical users.

## Disclaimer

This project is intended for educational and personal use. Ensure compliance with Google Maps' terms of service when using this tool.

---

Feel free to contribute to this project by submitting issues or pull requests!
