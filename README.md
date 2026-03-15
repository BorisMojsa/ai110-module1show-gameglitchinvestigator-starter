# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

This project is a Streamlit number guessing game where the player tries to guess a secret number within a limited number of attempts. While debugging it, I found that the hint logic was backwards, the game prompt did not always match the difficulty settings, and the New Game flow had state reset issues. To repair it, I moved core logic like `parse_guess` and `check_guess` into `logic_utils.py`, fixed the high/low hint behavior, added pytest tests for winning, too high, and too low guesses, and then verified the fixes in the live Streamlit app.

## 📸 Demo

- ![Winning game screenshot](images/winning-game.png)
## Pytest Results

- ![Pytest passing screenshot](images/pytest-results.png)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
