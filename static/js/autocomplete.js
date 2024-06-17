const form = document.querySelector('form');
const queryInput = form.querySelector('input[name="query"]');
const suggestionsList = form.querySelector('.suggestions');

queryInput.addEventListener('input', function() {
    const query = this.value.trim().toLowerCase();
    const dataset = window.location.pathname.includes('worldwide') ? 'worldwide' : 'philippine';

    fetch(`/autocomplete?query=${query}&dataset=${dataset}`)
        .then(response => response.json())
        .then(data => {
            suggestionsList.innerHTML = ''; // Clear previous suggestions
            data.forEach(suggestion => {
                const li = document.createElement('li');
                li.textContent = suggestion;
                suggestionsList.appendChild(li);
            });
            suggestionsList.style.display = data.length ? 'block' : 'none';
        })
        .catch(error => {
            console.error('Error fetching autocomplete suggestions:', error);
        });
});

// Handle click outside to close suggestions
document.addEventListener('click', function(event) {
    if (!form.contains(event.target)) {
        suggestionsList.style.display = 'none';
    }
});
