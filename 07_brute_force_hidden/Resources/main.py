import requests
from bs4 import BeautifulSoup
import time
import os

BASE_URL = "http://10.11.200.35/.hidden/"
LOG_FILE = os.path.join(os.path.dirname(__file__), "output.log")

def log_to_file(message):
    """Write message to log file"""
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(message + '\n')

def get_directories(url):
    """Get all directories from a page"""
    try:
        time.sleep(0.05)  # Small delay to avoid overwhelming the server
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        directories = []
        for link in links:
            href = link.get('href')
            if href and href.endswith('/') and href != '../':
                directories.append(href)
        return directories
    except Exception as e:
        return []

def get_readme_content(url):
    """Get README content from a URL"""
    try:
        time.sleep(0.05)  # Small delay
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            content = response.text.strip()
            # Log everything to file
            log_entry = f"\n{'='*70}\nURL: {url}\nContent: {content}\n{'='*70}"
            log_to_file(log_entry)
            return content
        return None
    except Exception as e:
        return None

def crawl_directory(url, depth=0):
    """Recursively crawl directories and read README files"""
    if depth > 10:  # Limit depth to prevent infinite loops
        return

    # Try to read README at current level
    readme_url = url + "README"
    get_readme_content(readme_url)

    # Get subdirectories and crawl them
    directories = get_directories(url)
    for directory in directories:
        new_url = url + directory
        crawl_directory(new_url, depth + 1)

if __name__ == "__main__":
    start_time = time.time()

    # Clear the log file at start
    with open(LOG_FILE, 'w', encoding='utf-8') as f:
        f.write(f"Crawl started at {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Base URL: {BASE_URL}\n")
        f.write("="*70 + "\n")

    print(f"Starting to crawl hidden directories and writing to {LOG_FILE}...")
    print("This may take several minutes...\n")

    crawl_directory(BASE_URL)

    end_time = time.time()
    elapsed_time = end_time - start_time

    log_to_file(f"\n\nCrawl completed at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    log_to_file(f"Total time: {elapsed_time:.2f} seconds ({elapsed_time/60:.2f} minutes)")

    print(f"\nCrawling complete! All README contents saved to {LOG_FILE}")
    print(f"Total time: {elapsed_time:.2f} seconds ({elapsed_time/60:.2f} minutes)")
