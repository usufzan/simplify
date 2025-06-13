// Add an event listener for when the popup's HTML has fully loaded.
document.addEventListener('DOMContentLoaded', function () {
    // Find the button in our popup.html
    const simplifyButton = document.getElementById('simplify-button');

    // Add a click event listener to the button.
    simplifyButton.addEventListener('click', function() {
        // Use the Chrome tabs API to get information about the current tabs.
        chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
            // 'tabs' is an array of tabs that match the query.
            // Since we passed { active: true, currentWindow: true },
            // the first element (tabs[0]) will be the currently active tab.
            
            // This is where we get the URL and store it in the constant.
            const url = tabs[0].url;

            // For now, let's just log it to the console to prove it works.
            console.log("Captured URL:", url);

            // You can also display it in the popup for feedback.
            document.body.innerHTML += `<p>URL found:<br>${url}</p>`;

        });
    });
});