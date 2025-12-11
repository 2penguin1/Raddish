# Raddish 🥬

<div align="center">
  <img src="extension/icons/raddish.svg" width="120" height="120" alt="Raddish Logo">
  <br>
  <b>The cutest Codeforces Rating Predictor you'll ever see.</b>
  <br>
  <br>
  <p>
    Powered by <b>PyTorch</b>, <b>FastAPI</b>, and <b>MongoDB</b>.
  </p>
</div>

---

## 📖 About
**Raddish** is a premium, real-time rating predictor Chrome Extension for Competitive Programmers. Unlike boring, standard tools, Raddish brings a vibrant **Glassmorphism** design and a friendly mascot to your Codeforces experience.

Behind the cute face lies a powerful **LSTM (Long Short-Term Memory)** neural network that analyzes your contest history to forecast your next rating change with high precision.

## ✨ Features
*   **Deep Learning Core**: Utilizes a PyTorch LSTM model trained on contest history sequences.
*   **Smart Caching**: Integrates with **MongoDB** to store user history and reduce redundant computations.
*   **Premium UI**: A sleek, dark-moded, glassmorphic interface with micro-animations.
*   **Real-time Predictions**: Instant feedback on your predicted rating changes.
*   **Cute Mascot**: Because competitive programming is stressful, and you deserve a smiling radish.

## 🛠️ Tech Stack
*   **Frontend**: HTML5, Vanilla CSS3 (Glassmorphism), JavaScript (ES6+).
*   **Backend**: Python, FastAPI, Uvicorn.
*   **AI/ML**: PyTorch (LSTM), Scikit-Learn, NumPy, Pandas.
*   **Database**: MongoDB.

---

## 🚀 Installation & Setup

Since the `venv` and `__pycache__` are not included in the repository (best practices!), you need to set up the environment locally.

### 1. Clone the Repository
```bash
git clone https://github.com/2penguin1/Raddish.git
cd Raddish
```

### 2. Backend Setup
The backend handles the ML inference and data fetching.

1.  **Navigate to the backend directory and Create a Virtual Environment**:
    ```powershell
    cd backend
    python -m venv venv
    ```

2.  **Activate the Virtual Environment**:
    *   **Windows (PowerShell)**:
        ```powershell
        .\venv\Scripts\Activate.ps1
        ```
    *   **Mac/Linux**:
        ```bash
        source venv/bin/activate
        ```

3.  **Install Dependencies**:
    ```powershell
    pip install -r requirements.txt
    ```

4.  **Database Setup**:
    *   Ensure you have **MongoDB** installed and running locally on port `27017`.
    *   The app will automatically create the `cf_predictor` database.

5.  **Train the Model**:
    Run the training script to generate the `model.pth` file.
    ```powershell
    python train_model.py
    ```

6.  **Start the Server**:
    ```powershell
    uvicorn main:app --reload
    ```
    The server will start at `http://127.0.0.1:8000`.

### 3. Extension Setup (Frontend)
1.  Open Chrome and navigate to `chrome://extensions/`.
2.  Enable **Developer mode** (toggle in the top-right corner).
3.  Click **Load unpacked**.
4.  Select the `extension` folder from the `Raddish` project directory.
5.  Pin **Raddish** to your toolbar!

---

## 🎮 Usage
1.  Ensure the backend server is running (`uvicorn main:app --reload`).
2.  Click the **Raddish** icon in your browser.
3.  Enter a Codeforces Handle (e.g., `tourist`, `Benq` or your own).
4.  Click **Predict Now**.
5.  View your predicted rating and delta with a smile!

---

## 🤝 Contributing
Feel free to open issues or submit pull requests. If you want to improve the model or add more cute animations, go ahead!

## 📄 License
MIT License.
