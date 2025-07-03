# SnakeGame AI

A Python-based Snake game AI that learns to play using Deep Q-Learning (DQN) with PyTorch and Pygame.

## Demo




## What It Does

This AI plays the classic Snake game by learning through trial and error using Reinforcement Learning. It improves over time using a neural network to predict the best moves.

## Features

- Pygame-based snake game environment  
- Deep Q-Learning (DQN) agent  
- Auto-saves model checkpoints  
- Logs training scores  
- Visualize and test trained AI

## Tech Stack

- Python 3  
- PyTorch  
- Pygame  
- NumPy  
- Matplotlib

## File Structure

```
├── agent.py
├── train.py
├── test_ai.py
├── model.py
├── snake_game.py
├── scores_log.csv
├── .gitignore
└── README.md
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/anahita-jpeg/SnakeGame.git
cd SnakeGame
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install manually:

```bash
pip install pygame torch numpy matplotlib
```

### 3. Train the model

```bash
python train.py
```

### 4. Test the AI

```bash
python test_ai.py
```

## License

This project is licensed under the [MIT License](./LICENSE)

## Author

Anahita Bhalme  
[GitHub](https://github.com/anahita-jpeg)

## Contributions

Pull requests are welcome. If you find bugs or want to improve something, fork the repo and submit a PR.
