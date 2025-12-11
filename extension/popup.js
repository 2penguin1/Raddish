document.addEventListener('DOMContentLoaded', () => {
    const handleInput = document.getElementById('handleInput');
    const predictBtn = document.getElementById('predictBtn');
    const searchBtn = document.getElementById('searchBtn');
    const resultArea = document.getElementById('resultArea');
    const loader = document.getElementById('loader');
    const errorMsg = document.getElementById('errorMsg');
    const newRatingEl = document.getElementById('newRating');
    const deltaEl = document.getElementById('deltaVal');

    // Load saved handle
    chrome.storage.local.get(['lastHandle'], (result) => {
        if (result.lastHandle) {
            handleInput.value = result.lastHandle;
        }
    });

    function predict() {
        const handle = handleInput.value.trim();
        if (!handle) return;

        // Save handle
        chrome.storage.local.set({ lastHandle: handle });

        // UI State
        resultArea.style.display = 'none';
        loader.style.display = 'block';
        errorMsg.textContent = '';
        predictBtn.disabled = true;

        fetch(`http://localhost:8000/predict/${handle}`)
            .then(response => {
                if (!response.ok) throw new Error('Prediction failed or user not found');
                return response.json();
            })
            .then(data => {
                // data = { current_rating: 1200, predicted_rating: 1250, delta: 50 }
                newRatingEl.textContent = data.predicted_rating;
                const delta = data.delta;
                deltaEl.textContent = (delta >= 0 ? '+' : '') + delta;
                
                deltaEl.className = 'delta ' + (delta >= 0 ? 'positive' : 'negative');
                
                resultArea.style.display = 'block';
            })
            .catch(err => {
                errorMsg.textContent = err.message;
            })
            .finally(() => {
                loader.style.display = 'none';
                predictBtn.disabled = false;
            });
    }

    predictBtn.addEventListener('click', predict);
    searchBtn.addEventListener('click', predict);
    handleInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') predict();
    });
});
