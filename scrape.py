import requests
from bs4 import BeautifulSoup
import ssl
import urllib.request

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

hdr = {'User-Agent': 'Mozilla/5.0'}

def scrape_section_text(url, id_string):
    """
    Scrape the text content of a section with a matching ID on a website.

    Parameters:
    - url (str): The URL of the website.
    - id_string (str): The string to match against element IDs.

    Returns:
    - str: The extracted text content.
    """
    req = urllib.request.Request(url, headers=hdr)

    # Send a GET request to the URL
    reqOpen = urllib.request.urlopen(req, context=ctx)

    html = reqOpen.read()

    # Check if the request was successful (status code 200)
    if reqOpen.getcode() == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')

        # Find the element with the matching ID string
        matching_element = soup.find(lambda tag: tag.name == 'section' and id_string in (tag.get('id') or ''))

        # Check if the matching element is found
        if matching_element:
            # Extract text content from all <p> and <h3> elements within the matching section
            text_content = '\n'.join([element.get_text(strip=True) for element in matching_element.find_all(['p', 'h3', 'li'])])

            # Return the extracted text content
            return text_content
        else:
            return f"Element with ID containing '{id_string}' not found on the page."
    else:
        return f"Failed to retrieve the page. Status code: {reqOpen.getcode()}"

def create_test_dict(url):
    """
    Returns a dictionary with the name, about, and interpreting results of a test, to be ready
    for inserting into the database
    """
    req = urllib.request.Request(url, headers=hdr)

    # Send a GET request to the URL
    reqOpen = urllib.request.urlopen(req, context=ctx)

    html = reqOpen.read()
    soup = BeautifulSoup(html, 'html.parser')
    test_name = soup.find('h1')
    interpreting_result = scrape_section_text(url, "interpreting")
    about_result = scrape_section_text(url, "about")
    result = {
        "name": test_name.text,
        "interpreting_result": interpreting_result,
        "about": about_result,
    }
    return result
