## RL-intro

Reinforcement learning involves an agent, a set of states $\mathcal{S}$, and a set $\mathcal{A}$  of actions per state. By performing an action $a \in \mathcal {A}$, the agent transitions from state to state. Executing an action in a specific state provides the agent with a reward (a numerical score).

## 🧱 Step-by-Step Plan
1. Simplified Tetris Environment

We’ll define a Tetris-like grid (e.g., 10×10), a few basic block types (e.g., L, I, O), and simple rules for placement and line-clearing.

2. RL Agent

We’ll use a tabular Q-learning agent for simplicity, or a small neural network (via PyTorch or TensorFlow) for more generalization.

3. Flask Interface

Each step will:

* Display the game state (as an HTML table or canvas),
* Show the action taken by the agent,
* Optionally show Q-values for each possible action.

