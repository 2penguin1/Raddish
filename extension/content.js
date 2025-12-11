console.log("Raddish: Content Script Loaded");

// Listen for messages or just run
// For standings pages, we might want to fetch predictions for everyone visible
// But that might spam the backend. For now, let's just look for the user's handle.

chrome.storage.local.get(['lastHandle'], (result) => {
    const handle = result.lastHandle;
    if (handle) {
        highlightUser(handle);
    }
});

function highlightUser(handle) {
    // Codeforces standings table rows usually have 'participantId' or links to profile
    // Simplistic approach: searching for links to /profile/handle
    const links = document.querySelectorAll(`a[href$="/profile/${handle}"]`);
    links.forEach(link => {
        const row = link.closest('tr');
        if (row) {
            row.style.border = "2px solid #00d2ff";

            // Inject a prediction cell if we can
            // This would require fetch from backend for this handle
            fetch(`http://localhost:8000/predict/${handle}`)
                .then(r => r.json())
                .then(data => {
                    const cell = document.createElement('td');
                    cell.classList.add('cf-predictor-cell');
                    if (data.delta >= 0) {
                        cell.classList.add('cf-predictor-positive');
                    } else {
                        cell.classList.add('cf-predictor-negative');
                    }
                    cell.innerText = `Δ ${data.delta}`;
                    row.appendChild(cell);
                    row.classList.add('cf-predictor-highlight');
                })
                .catch(e => console.log("Prediction fetch error", e));
        }
    });
}
