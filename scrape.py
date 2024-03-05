import urllib.request
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://www.testing.com/tests/ldl-cholesterol/"
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
        test_measures = test_about.find_next('h3', string='What does the test measure?')
        if test_measures:
            print("What the test measures:", test_measures.text.strip())  # Use text attribute
        else:
            print("Could not find the purpose of the test.")

        # Extracting test result interpretation
        test_interpretation = test_about.find_next('h3', string='Interpreting test results')
        if test_interpretation:
            print("Purpose of the Test:", test_interpretation.text.strip())  # Use text attribute
        else:
            print("Could not find the purpose of the test.")

        # Extracting bullet points within specific sections
        bullet_points = test_about.find_next('ul')  # Find the next unordered list
        if bullet_points:
            print("Bullet Points:")
            for li in bullet_points.find_all('li'):  # Find all list items within the unordered list
                print("-", li.text.strip())  # Use text attribute to get the text content
        else:
            print("No bullet points found.")

    else:
        print("No relevant information found on the page.")

except Exception as e:
    print("Error fetching content:", e)
