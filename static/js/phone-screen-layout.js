// Function to update navbar links based on screen width
function updateNavbarLinks() {
    const worldwideLink = document.getElementById('worldwide-link');
    const philippineLink = document.getElementById('philippine-link');
    const homeLink = document.getElementById('home-link');

    if (window.innerWidth <= 768) {  // Adjust this breakpoint as needed
        worldwideLink.textContent = 'World';
        philippineLink.textContent = 'Philippines';
        homeLink.textContent = 'PHGetaway';
    } else {
        worldwideLink.textContent = 'Worldwide Tourist Spots';
        philippineLink.textContent = 'Philippine Tourist Spots';
        homeLink.textContent = 'PHGetaway';
    }
}

// Call updateNavbarLinks initially and on window resize
document.addEventListener('DOMContentLoaded', function() {
    updateNavbarLinks();  // Initial call
    window.addEventListener('resize', updateNavbarLinks);  // Call on resize
});
