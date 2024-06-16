import requests
from bs4 import BeautifulSoup
import time

def fetch_description(name, location):
    # Step 1: Perform a search query on Wikipedia API
    search_term = f"{name} {location}"
    wiki_search_url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch={search_term}"

    try:
        # Send request to Wikipedia API for search results
        response = requests.get(wiki_search_url)
        response.raise_for_status()
        data = response.json()

        # Extract the title of the first search result
        search_results = data['query']['search']
        if search_results:
            first_result = search_results[0]
            title = first_result['title']

            # Step 2: Fetch the Wikipedia page for the first result to get the description
            wikipedia_url = f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}"
            wikipedia_response = requests.get(wikipedia_url)
            wikipedia_response.raise_for_status()

            # Parse the Wikipedia page content to get the brief description
            soup = BeautifulSoup(wikipedia_response.content, 'html.parser')
            paragraphs = soup.find_all('p')
            description = None
            for paragraph in paragraphs:
                text = paragraph.get_text().strip()
                if text:
                    description = text
                    break

            return description if description else None

        return None  # If no search results found

    except requests.RequestException as e:
        print(f"Error fetching description: {e}")
        return None
