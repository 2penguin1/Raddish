# Codeforces Rating Predictor - Implementation Plan

## Project Overview
A Chrome Extension that predicts rating changes for Codeforces users in real-time or post-contest, leveraging robust Machine Learning models (Gradient Boosting & Neural Networks). The system includes a dynamic retraining pipeline to adapt to new contests and rules.

## Architecture
**Hybrid Stack**:
- **Database**: MongoDB (Stores historical contest data, processed features, user logs).
- **ML/Backend**: Python (FastAPI)
  - Selected over Node.js for direct integration with Scikit-Learn, PyTorch/TensorFlow, and Pandas.
  - Handles API requests from the extension.
  - Runs background jobs for data fetching and model retraining.
- **Frontend/Extension**: React (Maneft V3 Chrome Extension)
  - "M" (Mongo) + "R" (React) + Python Backend.

## Phase 1: Environment & Data Pipeline [COMPLETED]
1.  **Project Structure Setup**: Initialize monorepo (`/extension`, `/backend`, `/data`).
2.  **MongoDB Setup**: (Optional/Skipped for MVP Local File).
3.  **Data Collector**:
    -   Implemented in `processing.py`.
4.  **Preprocessing**:
    -   Implemented sequence generation in `processing.py`.

## Phase 2: Advanced ML System [COMPLETED]
1.  **Feature Engineering**:
    -   Sequences of [Rank, Rating, etc.].
2.  **Model Selection**:
    -   **Advanced (Time-Series)**: LSTM implemented in `ml_model.py` using **PyTorch**.
3.  **Dynamic Update Pipeline**:
    -   `train_model.py` script provided.

## Phase 3: Backend API (FastAPI) [COMPLETED]
1.  **Endpoints**:
    -   `GET /predict/{handle}`: Implemented.

## Phase 4: Chrome Extension (Frontend) [COMPLETED]
1.  **Manifest V3 Setup**: `manifest.json` created.
2.  **Popup UI**: Glassmorphism UI in `popup.html` and `style.css`.
3.  **Content Script**: `content.js` for injection.

## Phase 5: Deployment & Polish [READY]
-   Use `start_backend.bat` and `train_model.bat`.
