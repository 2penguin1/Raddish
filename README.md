# Codeforces Rating Predictor

A real-time rating predictor Chrome Extension powered by a PyTorch LSTM model.

## Project Structure

- **backend/**: Python FastAPI application handling data fetching, processing, and ML inference.
- **extension/**: Chrome Extension source code (Manifest V3).

## Prerequisites
- Python 3.8+
- Chrome Browser

## Setup Instructions

### 1. Backend Setup (AI/ML Engine)
The backend fetches data from Codeforces and runs the Neural Network (LSTM) to predict rating changes.

1. Navigate to the `backend` folder:
   ```powershell
   cd backend
   ```
2. Create and activate a virtual environment (already set up):
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
4. **Train the Model** (Initial Run):
   Run the training script to generate the `model.pth` file.
   ```powershell
   python train_model.py
   ```
   > Note: This script checks for data in your local MongoDB (`cf_predictor` db). If empty, it uses synthetic data for demonstration.

5. **Start the API Server**:
   ```powershell
   uvicorn main:app --reload
   ```
   The backend will be running at `http://127.0.0.1:8000`.

### 2. Extension Setup (Frontend)
1. Open Google Chrome and navigate to `chrome://extensions/`.
2. Enable **Developer mode** (top right).
3. Click **Load unpacked**.
4. Select the `extension` directory from this project.
5. The extension "Codeforces Rating Predictor" should appear.

## Usage
1. Ensure your MongoDB service is running (Port 27017).
2. Click the extension icon in your Chrome toolbar.
3. Enter a Codeforces Handle (e.g., `tourist`, `Benq`).
4. Click **Predict Now**.
5. The extension will query the local backend.
   - Predictions are cached in MongoDB for analytics.
   - User history is processed via the PyTorch LSTM model.

## Features
- **Deep Learning**: Uses an LSTM (Long Short-Term Memory) network to model the sequential nature of contest performance.
- **Robust Data Pipeline**: Integrates **MongoDB** to store user history and predictions, enabling time-series analysis.
- **Real-time Pipeline**: Dynamic architecture allows for frequent retraining (`train_model.py`).
- **Glassmorphism UI**: Premium aesthetic design.
- **Robustness**: Handles missing history and provides heuristic fallbacks if the model is uncertain.
