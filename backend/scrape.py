import urllib.request, os, ssl
from bs4 import BeautifulSoup
from supabase import create_client, Client

# supabase docs: https://supabase.com/docs/reference/python/insert
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

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
            print(test_title.text.strip())  # Use text attribute to get the text content
        else:
            print("Could not find the test title.")


        test_measures = soup.find('h3', string='What does the test measure?')
        if test_measures:
            # the following code does not work for different patterns of paragraph and lists. it only looks for paragraphs, then lists. 
            # we have to handle multiple cases, for example with 2 pages:
            # https://www.testing.com/tests/ldl-cholesterol/, in the section "What does the test measure?", the order is p, then p, then ul, then p, then ul, then p
            # https://www.testing.com/tests/non-high-density-lipoprotein-cholesterol/, in the section "What does the test measure?", has a different pattern then above.
            # it is p, then ul, then p.

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


        interpret_test = soup.find('h3', string='Interpreting test results')
        if interpret_test:
            # the following code does not work for tables where the value ranges are shown
            # it also does not work on different patterns of paragraph and lists like the above block of code
            
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

    except Exception as e:
        print("Error fetching content:", e)

# List of URLs to scrape
urls = [
    # just test one at a time
    "https://www.testing.com/tests/ldl-cholesterol/"
    # "https://www.testing.com/tests/non-high-density-lipoprotein-cholesterol/",
    # "https://www.testing.com/tests/at-home-cholesterol-test/",
    # "https://www.testing.com/tests/hdl-cholesterol/",
    # "https://www.testing.com/tests/direct-ldl-cholesterol/"
    # Add more URLs here
]

# Scrape data from each URL in the list
for i, url in enumerate(urls, start=1):
    scrape_data(url)
    if i < len(urls):
        print("-" * 40)  # Add a separator between URL outputs
