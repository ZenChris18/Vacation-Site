// Function to update title text based on screen width
function updateTitle() {
    const titleElement = document.getElementById('tourist-spots-title');
    if (window.innerWidth <= 768) {  // Adjust this breakpoint as needed
        titleElement.textContent = 'Philippines';
    } else {
        titleElement.textContent = 'Philippines Tourist Spots';
    }
}

// Call updateTitle initially and on window resize
document.addEventListener('DOMContentLoaded', function() {
    updateTitle();  // Initial call
    window.addEventListener('resize', updateTitle);  // Call on resize
});
