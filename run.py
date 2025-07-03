import argparse
from agent import Agent
from snake_game import SnakeGame
import matplotlib.pyplot as plt

plt.ion()

def plot(scores, mean_scores):
    from IPython import display
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.ylim(ymin=0)
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores)-1, mean_scores[-1], str(round(mean_scores[-1], 2)))
    plt.show()
    plt.pause(0.1)

def train():
    print("\n✅ Training started...")

    scores = []
    mean_scores = []
    total_score = 0
    record = 0
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

            if score > record:
                record = score
                agent.save_model()

            if agent.n_games % 10 == 0:
                agent.save_model(backup=True)

            print(f"[Game {agent.n_games}] Score: {score}, Record: {record}, Epsilon: {agent.epsilon}")

            scores.append(score)
            total_score += score
            mean_score = total_score / agent.n_games
            mean_scores.append(mean_score)

            with open("scores_log.csv", "a") as f:
                f.write(f"{agent.n_games},{score},{mean_score}\n")

            plot(scores, mean_scores)

def test():
    game = SnakeGame(ai_player=True)
    agent = Agent()
    agent.epsilon = 0  # No random moves in testing

    while True:
        state_old = agent.get_state(game)
        final_move = agent.get_action(state_old)
        _, game_over, score = game.play_step(final_move)

        if game_over:
            break

    print('Final Score:', score)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Snake Game AI')
    parser.add_argument('--mode', type=str, default='train', choices=['train', 'test'],
                        help='Choose the mode: train or test')
    args = parser.parse_args()

    if args.mode == 'train':
        train()
    elif args.mode == 'test':
        test()
