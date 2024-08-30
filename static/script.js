document.getElementById('search-form').addEventListener('submit', function() {
    document.getElementById('spinner').style.display = 'block'; // Show spinner
});

window.onload = function() {
    document.getElementById('spinner').style.display = 'none'; // Hide spinner on load
};
