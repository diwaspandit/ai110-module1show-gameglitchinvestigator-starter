# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
=> It showed the enter the guess text box to enter the number to guess.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  => First, show hint show backwards, like: if it is higher, it shows lower; if it is lower, it shows higher. It should perform opposite.
   Second, the new game doesnot start when clicked new game. It should reset and start new game when new game button is clicked.
   Third, when difficulty level changed, the secret key doesnot follow the range rule. Based on the range selected, it should show the secret number range.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
=> Copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
=> Ai game me game state and reset logic across difficulty/new game which was bug before. AI suggesting me to import get_range_for_difficulty, parse_guess,check_guess, update_score from logic_utils instead of duplicating on app.py
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
=> One incorrect/misleading AI suggestion was to rely on pytest config (pythonpath = .) as the full fix for the import error.That sounded right, but when I ran pytest in terminal, it still failed with ModuleNotFoundError: No module named 'logic_utils' under my default Anaconda interpreter. I verified the issue by comparing runs: plain pytest failed, but running with the project venv Python worked. So I used a more reliable fix by adding the project root to sys.path at the top of the test file, then re-ran pytest and confirmed all tests passed.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
=> I created the test cases and also verified with manual testing with UI.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
=> One pytest test I ran was test_too_high_message_says_go_lower, where check_guess(60, 50) had to return outcome "Too High" and a message containing "LOWER". This showed me the hint-direction bug was actually fixed and not just the label. I also ran the full suite with pytest and got all tests passing, which confirmed there were no regressions in win/low/high behavior. For manual testing, I used the Streamlit UI and checked that clicking New Game reset score/history and generated a new secret, which confirmed the session-state fix in the app.
- Did AI help you design or understand any tests? How?
=> Yes, AI helped me design clearer tests by suggesting I check both the outcome and the hint message, not just one value. 
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
