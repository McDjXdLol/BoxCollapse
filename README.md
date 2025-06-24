# 📦 BoxCollapse

A minimalist terminal game where the playfield shrinks every time you score.  
Collect the `X`, avoid falling off the grid, and survive the collapsing box!

## 🎮 About the Game

You control the `•` character on a grid-based board. Your goal is simple:  
**collect as many `X` symbols as possible.**

But here's the twist — each point you score **shrinks the board**, making it harder to move, react, and survive.

Lose focus for a second, and boom — you're out of bounds.  
Keep going until the board is no more, or you've reached the win condition.

## 🕹️ Controls

| Key     | Action        |
|---------|---------------|
| `W`     | Move up       |
| `S`     | Move down     |
| `A`     | Move left     |
| `D`     | Move right    |
| `ESC`   | Exit the game |

## ⚙️ Requirements

- Python 3.x
- [`keyboard`](https://pypi.org/project/keyboard/) module (`pip install keyboard`)
- Terminal that supports ANSI escape codes (Git Bash / Windows Terminal / most UNIX terminals)

## 🚀 How to Run

```bash
python main.py <grid_size> <width_bonus>
```

Example:

```bash
python main.py 10 5
```

This starts a grid of 10x15.

# 🧠 Features
Real-time movement

Dynamic shrinking of the game board

Center reset on each point

Win condition based on points

Simple visuals, but addictive gameplay

# 🧪 Coming Soon (maybe...)
Obstacles and hazards

Enemies that move

Power-ups

"CHAOS MODE" 🌀

# 💡 Idea
This project was created for fun and experimentation —
a bite-sized arcade experience powered entirely by Python and your keyboard.
---
Created with ❤️ and a little bit of frustration.
