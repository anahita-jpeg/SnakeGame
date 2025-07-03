from snake_ai import SnakeGameAI

game = SnakeGameAI()

while True:
    action = [1, 0, 0]  # always go straight
    reward, game_over, score = game.play_step(action)

    if game_over:
        break

print('Final Score:', score)

