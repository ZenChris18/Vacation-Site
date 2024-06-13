async function fetchRandomDestinations() {
    try {
        const url = 'https://query.wikidata.org/sparql?query=' + encodeURIComponent(sparql_query);
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error('Failed to fetch data');
        }
        const data = await response.json();
        displayDestinations(data.results.bindings);
    } catch (error) {
        console.error('Error fetching data:', error);
        // Handle error display or fallback
    }
}

function displayDestinations(destinations) {
    const destinationContainer = document.getElementById('random-destination');
    destinationContainer.innerHTML = ''; // Clear previous content

    destinations.forEach(item => {
        const destinationName = document.createElement('h2');
        destinationName.textContent = item.itemLabel.value;
        destinationContainer.appendChild(destinationName);

        const destinationDesc = document.createElement('p');
        destinationDesc.textContent = item.itemDescription ? item.itemDescription.value : 'No description available';
        destinationContainer.appendChild(destinationDesc);

        if (item.image) {
            const destinationImg = document.createElement('img');
            destinationImg.src = item.image.value;
            destinationImg.alt = item.itemLabel.value;
            destinationImg.style.maxWidth = '400px';
            destinationContainer.appendChild(destinationImg);
        }
    });
}

document.addEventListener('DOMContentLoaded', function () {
    fetchRandomDestinations();
});
