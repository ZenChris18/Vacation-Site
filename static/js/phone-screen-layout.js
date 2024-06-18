// Function to update navbar links and title based on screen size
function updateNavbarAndTitle() {
    const worldwideLink = document.getElementById('worldwide-link');
    const philippineLink = document.getElementById('philippine-link');
    const titleElement = document.getElementById('tourist-spots-title');

    if (window.innerWidth <= 768) {
        worldwideLink.textContent = 'World';
        philippineLink.textContent = 'Philippines';
        titleElement.textContent = '{{ title_mobile }}';
    } else {
        worldwideLink.textContent = '{{ nav_worldwide }}';
        philippineLink.textContent = '{{ nav_philippine }}';
        titleElement.textContent = '{{ title_desktop }}';
    }
}

// Call updateNavbarAndTitle initially and on window resize
document.addEventListener('DOMContentLoaded', updateNavbarAndTitle);
window.addEventListener('resize', updateNavbarAndTitle);
