import gym
import numpy as np
import random


# ============================================================
# CART-POLE Q-LEARNING
# ============================================================

env = gym.make("CartPole-v1")


# ============================================================
# PARAMETERS
# ============================================================

EPISODES = 5000

LEARNING_RATE = 0.1       # alpha
DISCOUNT = 0.99           # gamma

EPSILON = 1.0
EPSILON_MIN = 0.01
EPSILON_DECAY = 0.995


# ============================================================
# STATE DISCRETIZATION
# ============================================================
# CartPole state:
#
# 0 = cart position
# 1 = cart velocity
# 2 = pole angle
# 3 = pole angular velocity
#
# The environment is continuous, so convert values
# into discrete states for the Q-table.
# ============================================================

bins = [
    np.linspace(-2.4, 2.4, 10),
    np.linspace(-3.0, 3.0, 10),
    np.linspace(-0.2095, 0.2095, 10),
    np.linspace(-3.0, 3.0, 10)
]


def discretize(state):

    state = np.array(state)

    return tuple(
        np.digitize(state[i], bins[i])
        for i in range(4)
    )


# ============================================================
# Q-TABLE
# ============================================================

q_table = np.zeros((11, 11, 11, 11, 2))


# ============================================================
# EPSILON-GREEDY ACTION SELECTION
# ============================================================

def choose_action(state):

    if random.random() < EPSILON:

        # Exploration
        return env.action_space.sample()

    else:

        # Exploitation
        return np.argmax(q_table[state])


# ============================================================
# TRAINING
# ============================================================

for episode in range(EPISODES):

    state, info = env.reset()

    state = discretize(state)

    done = False
    total_reward = 0

    while not done:

        # Choose action
        action = choose_action(state)

        # Take action
        next_state, reward, terminated, truncated, info = env.step(action)

        done = terminated or truncated

        next_state = discretize(next_state)

        # ----------------------------------------------------
        # Q-Learning update
        # ----------------------------------------------------

        old_q = q_table[state + (action,)]

        if done:

            target = reward

        else:

            target = reward + DISCOUNT * np.max(
                q_table[next_state]
            )

        q_table[state + (action,)] = (
            old_q
            + LEARNING_RATE * (target - old_q)
        )

        state = next_state

        total_reward += reward

    # --------------------------------------------------------
    # Epsilon decay
    # --------------------------------------------------------

    EPSILON = max(
        EPSILON_MIN,
        EPSILON * EPSILON_DECAY
    )

    if (episode + 1) % 100 == 0:

        print(
            "Episode:",
            episode + 1,
            "Reward:",
            total_reward,
            "Epsilon:",
            EPSILON
        )


# ============================================================
# TEST TRAINED AGENT
# ============================================================

state, info = env.reset()

state = discretize(state)

done = False
total_reward = 0

while not done:

    action = np.argmax(q_table[state])

    next_state, reward, terminated, truncated, info = env.step(action)

    done = terminated or truncated

    state = discretize(next_state)

    total_reward += reward

print("\nTest Reward:", total_reward)

env.close()