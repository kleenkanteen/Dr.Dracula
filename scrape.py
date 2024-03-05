import urllib.request
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def scrape_data(url):
    print("Retrieving:", url)

    hdr = {'User-Agent': 'Mozilla/5.0'}

    # Add a user-agent header to the request
    req = urllib.request.Request(url, headers=hdr)
    try:
        html = urllib.request.urlopen(req, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')

        # Find the title
        test_title = soup.find('h1')
        if test_title:
            print("Test Title:", test_title.text.strip())  # Use text attribute to get the text content
        else:
            print("Could not find the test title.")

        # Find relevant sections containing information about cholesterol testing
        test_about = soup.find('h2', string='About the Test')
        test_results = soup.find('h2', string='LDL Cholesterol Test Results')

        if test_about:
            # Extracting what the test measures
            test_measures = test_about.find_next_sibling('h3', string='What does the test measure?')
            if test_measures:
                print("What the test measures:")
                # Print the text content of any <p> tags
                for paragraph in test_measures.find_next_siblings('p'):
                    print(paragraph.text.strip())
                # Print the text content of any <ul> tags
                for ul in test_measures.find_next_siblings('ul'):
                    for li in ul.find_all('li'):
                        print("-", li.text.strip())
            else:
                print("No content found for what the test measures.")

            # Extracting content following the 'Interpreting test Results' h3 tag
            interpret_test = test_results.find_next_sibling('h3', string='Interpreting test results')
            if interpret_test:
                print("Interpret test results:")
                # Print the text content of any <p> tags
                for paragraph in interpret_test.find_next_siblings('p'):
                    print(paragraph.text.strip())
                # Print the text content of any <ul> tags
                for ul in interpret_test.find_next_siblings('ul'):
                    for li in ul.find_all('li'):
                        print("-", li.text.strip())
            else:
                print("No content found for the purpose of the test.")
        else:
            print("No relevant information found on the page.")

    except Exception as e:
        print("Error fetching content:", e)

# List of URLs to scrape
urls = [
    "https://www.testing.com/tests/ldl-cholesterol/",
    "https://www.testing.com/tests/non-high-density-lipoprotein-cholesterol/"
    # Add more URLs here
]

# Scrape data from each URL in the list
for i, url in enumerate(urls, start=1):
    scrape_data(url)
    if i < len(urls):
        print("-" * 40)  # Add a separator between URL outputs