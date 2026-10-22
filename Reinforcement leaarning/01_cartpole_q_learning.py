# ============================================================
# CART-POLE: IMPLEMENT AND TRAIN AN AGENT USING Q-LEARNING
# Install first:  pip install gymnasium matplotlib numpy
#   (older "gym" >= 0.26 also works - see the import below)
#
# State (continuous): cart position, cart velocity,
#                     pole angle, pole angular velocity
# Actions: 0 = push left, 1 = push right
# Reward : +1 for every step the pole stays up (max 500)
# Q-learning update:
#   Q(s,a) <- Q(s,a) + alpha * [ r + gamma * max_a' Q(s',a') - Q(s,a) ]
# Run: python 01_cartpole_q_learning.txt
# Note: Q-learning is random, so results differ each run. A random
# agent scores ~20; a trained agent typically scores 150-500.
# ============================================================
import random
import numpy as np

try:
    import gymnasium as gym
except ImportError:
    import gym

env = gym.make("CartPole-v1")

EPISODES = 3000
ALPHA = 0.1            # learning rate
GAMMA = 0.99           # discount factor
EPSILON = 1.0          # exploration rate
EPS_MIN = 0.01
EPS_DECAY = 0.998

# ---------- discretize the continuous state into bins ----------
BINS = [
    np.linspace(-2.4, 2.4, 4),        # cart position
    np.linspace(-2.0, 2.0, 4),        # cart velocity
    np.linspace(-0.21, 0.21, 10),     # pole angle (most important)
    np.linspace(-2.0, 2.0, 10),       # pole angular velocity
]

def discretize(state):
    return tuple(int(np.digitize(state[i], BINS[i])) for i in range(4))

q_table = np.zeros([len(b) + 1 for b in BINS] + [env.action_space.n])

def choose_action(s):
    if random.random() < EPSILON:
        return env.action_space.sample()          # explore
    return int(np.argmax(q_table[s]))             # exploit

# ---------------------------- TRAINING ----------------------------
rewards = []
for ep in range(EPISODES):
    state, _ = env.reset()
    s = discretize(state)
    total, done = 0, False
    while not done:
        a = choose_action(s)
        nxt, r, terminated, truncated, _ = env.step(a)
        done = terminated or truncated
        s2 = discretize(nxt)
        target = r if terminated else r + GAMMA * np.max(q_table[s2])
        q_table[s + (a,)] += ALPHA * (target - q_table[s + (a,)])
        s = s2
        total += r
    EPSILON = max(EPS_MIN, EPSILON * EPS_DECAY)
    rewards.append(total)
    if (ep + 1) % 200 == 0:
        print(f"Episode {ep + 1:5d} | avg reward (last 200) = "
              f"{np.mean(rewards[-200:]):6.1f} | epsilon = {EPSILON:.3f}")

# ---------------------------- TESTING ----------------------------
test_rewards = []
for _ in range(20):
    state, _ = env.reset()
    s, total, done = discretize(state), 0, False
    while not done:
        state, r, terminated, truncated, _ = env.step(int(np.argmax(q_table[s])))
        s, done = discretize(state), terminated or truncated
        total += r
    test_rewards.append(total)
env.close()

success = sum(t >= 195 for t in test_rewards) / len(test_rewards) * 100
print("\nTest rewards (greedy policy):", test_rewards)
print(f"Average test reward: {np.mean(test_rewards):.1f}")
print(f"Success rate (reward >= 195): {success:.0f}%")

# ------------------- REWARD vs EPISODES GRAPH -------------------
try:
    import matplotlib.pyplot as plt
    moving = np.convolve(rewards, np.ones(50) / 50, mode='valid')
    plt.figure(figsize=(9, 4))
    plt.plot(rewards, alpha=0.3, label="Reward per episode")
    plt.plot(range(49, len(rewards)), moving, label="50-episode moving average")
    plt.xlabel("Episode"); plt.ylabel("Total reward")
    plt.title("Cart-Pole Q-Learning: Reward vs Episodes")
    plt.legend(); plt.tight_layout()
    plt.savefig("cartpole_rewards.png")
    print("Graph saved as cartpole_rewards.png")
    plt.show()
except ImportError:
    print("Install matplotlib to see the reward graph.")
