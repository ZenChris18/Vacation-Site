document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.querySelector('input[name="query"]');
    const suggestionsBox = document.querySelector('.suggestions');

    searchInput.addEventListener('input', function () {
        const query = searchInput.value;
        if (query.length > 2) {
            fetch(`/autocomplete?query=${query}`)
                .then(response => response.json())
                .then(suggestions => {
                    suggestionsBox.innerHTML = '';
                    suggestionsBox.style.display = 'block';
                    suggestions.slice(0, 5).forEach(suggestion => { // Limit to 5 suggestions
                        const li = document.createElement('li');
                        li.textContent = suggestion;
                        li.addEventListener('click', () => {
                            searchInput.value = suggestion;
                            suggestionsBox.innerHTML = '';
                            suggestionsBox.style.display = 'none';
                        });
                        suggestionsBox.appendChild(li);
                    });
                });
        } else {
            suggestionsBox.innerHTML = '';
            suggestionsBox.style.display = 'none';
        }
    });

    document.addEventListener('click', function (e) {
        if (!searchInput.contains(e.target) && !suggestionsBox.contains(e.target)) {
            suggestionsBox.innerHTML = '';
            suggestionsBox.style.display = 'none';
        }
    });
});
