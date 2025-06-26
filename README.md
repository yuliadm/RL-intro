# 🎮 Playing Tetris with Reinforcement Learning (RL): Applying Computer Vision (CV) to RL for video games  

Inspired by the paper "Playing Tetris with Deep Reinforcement Learning" by Matt Stevens and Sabeek Pradhan:
https://cs231n.stanford.edu/reports/2016/pdfs/121_Report.pdf

**Tetris** is a game that involves placing pieces of different shapes on top of each other so that they fill in the rectangular grid.
A common human approach to this problem involves looking for open spaces that match the shape of the current piece, which is ultimately a task in visual pattern detection and object recognition.

The Deep Reinforcement Learning approach utilizes raw pixel data rather than explicit featurization (e.g., features relating the contour and height of the game board and the numebr of holes present).

### Method

The NN is used to approximate
$
Q^{*}(s,a) = \max_{\pi} \mathbb{E}[r_t + \gamma r_{t+1} + \gamma^2 r_{t+2} + \dots | s_t = s, a_t = a, \pi]
$


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

