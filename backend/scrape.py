import requests
import os
from bs4 import BeautifulSoup
import ssl
import urllib.request
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

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

    reqOpen = urllib.request.urlopen(req, context=ctx)

    html = reqOpen.read()

    if reqOpen.getcode() == 200:
        soup = BeautifulSoup(html, 'html.parser')

        # Find the element with the matching ID string
        matching_element = soup.find(lambda tag: tag.name == 'section' and id_string in (tag.get('id') or ''))

        # Check if the matching element is found
        if matching_element:
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

            text_content += other_content

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

    reqOpen = urllib.request.urlopen(req, context=ctx)

    html = reqOpen.read()
    soup = BeautifulSoup(html, 'html.parser')

    test_name = soup.find('h1')
    about_result = scrape_section_text(url, "about")
    interpreting_result = scrape_section_text(url, "results")
    result = {
        "source": f"Source: {url}",
        "name": test_name.text,
        "about": about_result,
        "interpreting_result": interpreting_result,
    }
    return result

urls = [
    "https://www.testing.com/tests/creatinine/",
    "https://www.testing.com/tests/sodium/",
    "https://www.testing.com/tests/potassium/",
    "https://www.testing.com/tests/alkaline-phosphatase-alp/",
    "https://www.testing.com/tests/alanine-aminotransferase-alt/",
    "https://www.testing.com/tests/cholesterol/",
    "https://www.testing.com/tests/triglycerides/",
    "https://www.testing.com/tests/hdl-cholesterol/",
    "https://www.testing.com/tests/ldl-cholesterol/",
    "https://www.testing.com/tests/non-high-density-lipoprotein-cholesterol/",
    "https://www.testing.com/tests/bilirubin/",
    "https://www.testing.com/tests/ldl-cholesterol/",
    "https://www.testing.com/tests/at-home-cholesterol-test/",
    "https://www.testing.com/tests/hdl-cholesterol/",
    "https://www.testing.com/tests/direct-ldl-cholesterol/"
]

# supabase docs: https://supabase.com/docs/reference/python/insert
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

with open("backend/biomarker_reference.txt", "w", encoding='utf-8') as file:
    for url in urls:
        result = create_test_dict(url)
        
        # Write the test dictionary to the file
        for key, value in result.items():
            file.write(f"{value}\n")
        
        data, count = supabase.table('biomarker_reference').insert({"biomarker": result["name"], "about": result["about"], "interpreting_result": result["interpreting_result"], "source": result["source"]}).execute()

        file.write("\n")