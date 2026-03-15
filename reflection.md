# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The first time I ran the game, it looked clean and playable, but once I started testing it, several things were clearly broken. One bug I noticed right away was that the difficulty settings did not fully match the actual game, because the sidebar showed one range while the main prompt still said to guess a number between 1 and 100. Another bug was that the hints were backwards, since the game told me to go higher when my guess was already above the secret number and lower when my guess was below it. I also found that the game accepted guesses outside the allowed range instead of rejecting them, and the New Game button did not fully reset the game state after a round ended.

---

## 2. How did you use AI as a teammate?

I mainly used VS Code Copilot as my AI teammate during this project, and I used ChatGPT only a little for extra clarification when I got stuck. One correct suggestion from Copilot was to separate the game logic from the UI by moving functions like `parse_guess` and `check_guess` out of `app.py` and into `logic_utils.py`. I verified that suggestion by checking the imports in the code, running `pytest`, and then testing the game in Streamlit to confirm the hints worked correctly in the live app. One incorrect or misleading suggestion from Copilot was a version of the refactor that changed the function behavior in a way that did not match the rest of my app. I caught that by comparing the suggestion to my existing code, noticing that my app still expected the original return structure, and then verifying the correct version by rerunning tests and checking the game manually.
---

## 3. Debugging and testing your fixes

To make sure the bug was really fixed, I tested it in more than one way. I used `pytest` to check that `check_guess` returned the correct results for winning, too high, and too low guesses, and all of those tests passed after the fix. I also ran the Streamlit app and manually tested different guesses to confirm that the hint shown on screen matched the actual comparison with the secret number. Copilot helped with the general testing direction, but I still had to review the code and confirm that the tests matched how my functions actually worked.

---

## 4. What did you learn about Streamlit and state?

At first, Streamlit state was one of the most confusing parts of this project for me. I would explain it to a friend like this: every time you click a button or enter something, Streamlit basically reruns the script from top to bottom, so without `session_state` the app would forget everything each time. `session_state` is what lets the game remember things like the secret number, the score, the attempts, and whether you already won or lost. This project made it clear to me that a lot of bugs in Streamlit are not just regular logic bugs, but also state-management bugs.

---

## 5. Looking ahead: your developer habits

One habit from this project that I want to reuse is testing one bug at a time instead of trying to fix everything at once. That made the debugging process feel more organized and helped me verify each change before moving on. I also want to keep using `pytest` together with manual testing in the live app, because that gave me more confidence that the bug was actually fixed.

One thing I would do differently next time is be more careful before accepting AI suggestions. Some of the suggestions sounded correct at first, but after comparing them to my actual code, I realized they would have broken the app or changed behavior in the wrong way. Next time I would use smaller and more specific prompts earlier so the AI stays focused on one change at a time.

This project changed the way I think about AI-generated code because I no longer see it as something I should trust automatically. I now see AI more as a helper that can speed up the process, but I still need to check the logic, test the code, and make the final decision myself.