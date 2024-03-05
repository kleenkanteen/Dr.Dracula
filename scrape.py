import urllib.request
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://www.testing.com/tests/ldl-cholesterol/"
print("Retrieving:", url)

<<<<<<< HEAD
=======

>>>>>>> 23f3b3a99a00385111c68ce26966e67822dcffb3
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
<<<<<<< HEAD
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

        # Extracting content following the 'Interpreting test Ressults' h3 tag
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
=======
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

>>>>>>> 23f3b3a99a00385111c68ce26966e67822dcffb3
    else:
        print("No relevant information found on the page.")

except Exception as e:
    print("Error fetching content:", e)
