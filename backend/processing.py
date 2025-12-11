import requests
import numpy as np
import torch

CF_API_URL = "https://codeforces.com/api"

def fetch_user_history(handle):
    try:
        resp = requests.get(f"{CF_API_URL}/user.rating?handle={handle}")
        data = resp.json()
        if data['status'] != 'OK':
            return None
        return data['result']
    except Exception as e:
        print(f"Error fetching history: {e}")
        return None

def prepare_sequence(history, seq_len=10):
    # History item: {rank, oldRating, newRating, ...}
    # Features: [Rank, OldRating, ContestID]
    # We want to predict NewRating.
    
    if not history:
        return None
        
    data = []
    for contest in history:
        # Simple normalization (approximate)
        rank = float(contest['rank'])
        old_rating = float(contest['oldRating'])
        # We can add more features later
        data.append([rank, old_rating, 0.0, 0.0]) # Padding 4 features
        
    # Pad or truncate to seq_len
    if len(data) < seq_len:
        # Pad with zeros or first element
        padding = [[0.0, 1500.0, 0.0, 0.0]] * (seq_len - len(data))
        data = padding + data
    else:
        data = data[-seq_len:]
        
    return torch.tensor([data], dtype=torch.float32) # Batch size 1

def fetch_user_info(handle):
    try:
        resp = requests.get(f"{CF_API_URL}/user.info?handles={handle}")
        data = resp.json()
        if data['status'] == 'OK':
            return data['result'][0]
    except:
        pass
    return None
