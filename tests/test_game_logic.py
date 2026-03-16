from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

# --- Tests targeting the reversed-hint bug ---

def test_too_high_message_says_go_lower():
    # Bug: when guess > secret, the message incorrectly said "Go HIGHER!"
    # Fix: it should say "Go LOWER!" because the player needs to guess lower
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'LOWER' in message, got: '{message}'"

def test_too_low_message_says_go_higher():
    # Bug: when guess < secret, the message incorrectly said "Go LOWER!"
    # Fix: it should say "Go HIGHER!" because the player needs to guess higher
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected 'HIGHER' in message, got: '{message}'"

def test_too_high_message_does_not_say_go_higher():
    # Regression guard: ensure the old wrong message is never returned when guess is too high
    outcome, message = check_guess(99, 1)
    assert outcome == "Too High"
    assert "HIGHER" not in message, f"Message should not say 'HIGHER' when guess is too high, got: '{message}'"

def test_too_low_message_does_not_say_go_lower():
    # Regression guard: ensure the old wrong message is never returned when guess is too low
    outcome, message = check_guess(1, 99)
    assert outcome == "Too Low"
    assert "LOWER" not in message, f"Message should not say 'LOWER' when guess is too low, got: '{message}'"

def test_win_message():
    # Winning guess should return the correct outcome and celebratory message
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message or "🎉" in message
