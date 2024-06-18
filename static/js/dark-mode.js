// Function to toggle dark mode
function toggleDarkMode() {
    const body = document.body;
    body.classList.toggle('dark-mode');
    // Store user preference in localStorage
    const isDarkMode = body.classList.contains('dark-mode');
    localStorage.setItem('darkMode', isDarkMode);
}

// Function to initialize dark mode based on user preference
function initializeDarkMode() {
    const darkMode = localStorage.getItem('darkMode') === 'true';
    const body = document.body;
    if (darkMode) {
        body.classList.add('dark-mode');
    } else {
        body.classList.remove('dark-mode');
    }
}

// Toggle dark mode on button click
const darkModeToggle = document.getElementById('dark-mode-toggle');
if (darkModeToggle) {
    darkModeToggle.addEventListener('click', toggleDarkMode);
}

// Initialize dark mode based on user preference
document.addEventListener('DOMContentLoaded', initializeDarkMode);
