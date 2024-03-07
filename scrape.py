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
    hdr = {'User-Agent': 'Mozilla/5.0'}
    ctx = ssl.create_default_context()

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
            # Initialize the text content
            text_content = ''

            # Process tables separately
            tables = matching_element.find_all('table')
            for table in tables:
                # Extract table data
                table_data = []
                for row in table.find_all('tr'):
                    row_data = [cell.get_text(strip=True) for cell in row.find_all(['td', 'th'])]
                    table_data.append(row_data)

                # Convert table data to an ASCII table
                ascii_table = '\n'.join([' | '.join(row) for row in table_data])
                
                # Append the ASCII table to the text content
                text_content += f'\n\nTable:\n{ascii_table}\n\n'

            # Extract text content from all <p>, <h3>, <li>, <strong> elements within the matching section
            other_content = '\n'.join([element.get_text(strip=True) for element in matching_element.find_all(['p', 'h3', 'li', 'strong'])])

            # Append the other content to the text content
            text_content += other_content

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
    interpreting_result = scrape_section_text(url, "results")
    about_result = scrape_section_text(url, "about")
    result = {
        "name": test_name.text,
        "interpreting_result": interpreting_result,
        "about": about_result,
    }
    return result
