import torch
import torch.nn as nn
import torch.optim as optim
from ml_model import RatingPredictorLSTM, save_model
import numpy as np

from database import db
import random

def fetch_training_data(seq_len=10):
    # Fetch data from MongoDB
    contests = db.get_contest_data()
    
    # If no data in DB, use dummy data for demonstration so it runs locally for the user
    if not contests or len(contests) < 10:
        print("Not enough data in MongoDB. Generating synthetic data...")
        return generate_dummy_data(500, seq_len)
        
    print(f"Indices fetched: {len(contests)}. (Real data logic placeholder)")
    # Here you would convert the contest documents into sequences
    # [ Logic to parse 'contests' list into X, y tensors ]
    # For MVP safety, we return dummy data even if DB connects, until real schema is populated.
    return generate_dummy_data(500, seq_len)

def generate_dummy_data(num_samples=100, seq_len=10):
    X = []
    y = []
    for _ in range(num_samples):
        # Generate random sequence of [Rank, OldRating, Feature3, Feature4]
        seq = []
        rating = 1500
        for _ in range(seq_len):
            rank = np.random.randint(1, 5000)
            change = np.random.randint(-50, 60)
            seq.append([rank, rating, 0, 0])
            rating += change
            
        target_change = np.random.randint(-50, 60)
        X.append(seq)
        y.append([target_change])
        
    return torch.tensor(X, dtype=torch.float32), torch.tensor(y, dtype=torch.float32)

def train():
    print("Initializing Model...")
    model = RatingPredictorLSTM()
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    
    print("Generating Training Data...")
    X_train, y_train = fetch_training_data()
    
    epochs = 50
    print(f"Starting Training for {epochs} epochs...")
    
    model.train()
    for epoch in range(epochs):
        optimizer.zero_grad()
        outputs = model(X_train)
        loss = criterion(outputs, y_train)
        loss.backward()
        optimizer.step()
        
        if (epoch+1) % 10 == 0:
            print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}")
            
    print("Training Complete.")
    save_model(model)
    print("Model saved to model.pth")

if __name__ == "__main__":
    train()
