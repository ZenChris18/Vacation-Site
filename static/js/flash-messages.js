document.addEventListener('DOMContentLoaded', function () {
    var flashMessage = document.getElementById('flash-message');
    if (flashMessage) {
        setTimeout(function () {
            flashMessage.remove();
        }, 5000); // 5000 milliseconds = 5 seconds
    }
});