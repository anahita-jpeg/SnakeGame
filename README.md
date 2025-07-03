# SnakeGame AI

A Python-based Snake game AI that learns to play using Deep Q-Learning (DQN) with PyTorch and Pygame.

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
├── run.py
├── snake_game.py
├── model.py
├── scores_log.csv
├── .gitignore
├── README.md
├── requirements.txt
├── setup.py
└── CONTRIBUTING.md
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

### 3. Run the game

To play the game yourself:

```bash
python main.py --player human
```

To train the AI:

```bash
python run.py --mode train
```

To test the AI:

```bash
python run.py --mode test
```

## License

This project is licensed under the [MIT License](./LICENSE)

## Author

Anahita Bhalme
[GitHub](https://github.com/anahita-jpeg)

## Contributions

Pull requests are welcome. If you find bugs or want to improve something, please read our [contributing guidelines](./CONTRIBUTING.md) and submit a PR.