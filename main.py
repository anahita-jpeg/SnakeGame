import argparse
from snake_game import SnakeGame
from agent import Agent

def main():
    parser = argparse.ArgumentParser(description='Snake Game')
    parser.add_argument('--player', type=str, default='human', choices=['human', 'ai'],
                        help='Choose the player type: human or ai')
    args = parser.parse_args()

    if args.player == 'human':
        game = SnakeGame()
        while True:
            _, game_over, _ = game.play_step()
            if game_over:
                break
    elif args.player == 'ai':
        agent = Agent()
        game = SnakeGame(ai_player=True)
        while True:
            state_old = agent.get_state(game)
            final_move = agent.get_action(state_old)
            reward, done, score = game.play_step(final_move)
            state_new = agent.get_state(game)
            agent.train_short_memory(state_old, final_move, reward, state_new, done)
            agent.remember(state_old, final_move, reward, state_new, done)

            if done:
                game.reset()
                agent.n_games += 1
                agent.train_long_memory()
                agent.save_model()
                print('Game', agent.n_games, 'Score', score)

if __name__ == '__main__':
    main()
