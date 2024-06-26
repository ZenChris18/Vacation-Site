document.addEventListener('DOMContentLoaded', function() {
    const vacationContainer = document.getElementById('vacation-container');
    const loadingIndicator = document.getElementById('loading');
    let page = 1;

    function loadVacationSpots() {
        fetch(`/load_more_vacations?num_spots=6&dataset=philippine`)
            .then(response => response.json())
            .then(data => {
                data.forEach((spot, index) => {  // Use 'index' provided by forEach
                    const col = document.createElement('div');
                    col.className = 'col-md-4';

                    const card = document.createElement('div');
                    card.className = 'card mb-4';

                    const img = document.createElement('img');
                    img.src = spot.Image;
                    img.alt = spot.Name;
                    img.className = 'card-img-top';
                    img.style.height = '200px';
                    img.style.objectFit = 'cover';
                    img.onerror = function() {
                        this.onerror = null;
                        this.src = '{{ url_for("static", filename="images/fallback.jpg") }}';
                    };

                    const cardBody = document.createElement('div');
                    cardBody.className = 'card-body';

                    const cardTitle = document.createElement('h5');
                    cardTitle.className = 'card-title';
                    cardTitle.textContent = spot.Name;

                    const cardText = document.createElement('p');
                    cardText.className = 'card-text';
                    cardText.textContent = `Location: ${spot.Location}`;

                    cardBody.appendChild(cardTitle);
                    cardBody.appendChild(cardText);
                    card.appendChild(img);
                    card.appendChild(cardBody);
                    col.appendChild(card);

                    // Link each card to details page
                    card.addEventListener('click', function() {
                        window.location.href = `/details/${spot.Name}?dataset=philippine`;
                    });

                    vacationContainer.appendChild(col);
                });

                loadingIndicator.style.display = 'none';
            })
            .catch(error => {
                console.error('Error loading vacation spots:', error);
                loadingIndicator.style.display = 'none';
            });
    }

    function handleScroll() {
        if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 500) {
            loadingIndicator.style.display = 'block';
            loadVacationSpots();
        }
    }

    // Initial load
    loadVacationSpots();

    // Infinite scroll
    window.addEventListener('scroll', handleScroll);
});
