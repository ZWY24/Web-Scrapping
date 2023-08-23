# Zhihu Scraper
## Zhihu Scraper is a simple Python package designed to scrape questions and their associated answers from the popular Chinese Q&A platform Zhihu.

## Features
Scrape question details including creation time, update time, title, comment count, vote count, follower count, and view count.
Scrape answers for a specific question, capturing details such as author, content, creation and update time, comment count, vote count, and answer URL.

## Requirements
1. Python 3.6 or newer
2. Required Python packages:
    - `requests`
    - `beautifulsoup4`
    - `pandas`
    - `selectolax`

## Installation
1. Clone this repository to your local machine.
    - `git clone [URL of this repository]`
2. Navigate to the directory containing the zhihu_scraper package.
    - `cd path_to_directory_containing_zhihu_scraper`
3. Install the required Python packages.
    - `pip install -r requirements.txt`
4. Installing Locally: 
Navigate to the directory containing setup.py in your terminal and run:`pip install .`

Note: You might want to create a virtual environment to manage the dependencies.

## Usage

1. Prepare a CSV file named all_data.csv containing the list of Zhihu question IDs to be scraped.
2. Navigate to the directory containing the zhihu_scraper package.
    - `cd path_to_directory_containing_zhihu_scraper`
3. Execute the scraper: `python -m zhihu_scraper.main`
4. After successful execution, the scraped data will be saved in a file named zhihu_data.csv.

## Limitations
The scraper is designed to fetch up to a maximum of 216 questions in one go, assuming an average of 4000 answers per question. Please split your list of question IDs accordingly to avoid potential scraping limits set by Zhihu.

## License
This project is open-sourced and available for personal and research use. Please ensure to respect Zhihu's terms of service and use responsibly.
