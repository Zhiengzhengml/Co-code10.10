## A typical test case: 
""" {
    "goal_ahead": True,
    "goal_on_left": False,
    "goal_on_right": False,
    "front_blocked": False,
    "left_blocked": False,
    "right_blocked": False
},
"FORWARD" """
## Use the above test case to create more test cases for all the possible states

import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("nav", Path("navigation_logic.py"))
nav = importlib.util.module_from_spec(spec)
spec.loader.exec_module(nav)

decide = nav.decide_next_move

CASES = [
    ({"goal_ahead": True,  "goal_on_left": False, "goal_on_right": False,
      "front_blocked": False, "left_blocked": False, "right_blocked": False}, "FORWARD"),
    
    ({"goal_ahead": False, "goal_on_left": True,  "goal_on_right": False,
      "front_blocked": False, "left_blocked": False, "right_blocked": False}, "LEFT"),
    
    ({"goal_ahead": False, "goal_on_left": False, "goal_on_right": True,
      "front_blocked": False, "left_blocked": False, "right_blocked": False}, "RIGHT"),
    
    ({"goal_ahead": True,  "goal_on_left": False, "goal_on_right": False,
      "front_blocked": True,  "left_blocked": False, "right_blocked": False}, "LEFT"),
    
    ({"goal_ahead": False, "goal_on_left": True,  "goal_on_right": False,
      "front_blocked": False, "left_blocked": True,  "right_blocked": False}, "FORWARD"),
    
    ({"goal_ahead": False, "goal_on_left": False, "goal_on_right": True,
      "front_blocked": False, "left_blocked": False, "right_blocked": True},  "FORWARD"),
    
    ({"goal_ahead": True,  "goal_on_left": False, "goal_on_right": False,
      "front_blocked": True,  "left_blocked": False, "right_blocked": True},  "LEFT"),
    
    ({"goal_ahead": True,  "goal_on_left": False, "goal_on_right": False,
      "front_blocked": True,  "left_blocked": True,  "right_blocked": False}, "RIGHT"),
    
    ({"goal_ahead": True,  "goal_on_left": False, "goal_on_right": False,
      "front_blocked": True,  "left_blocked": True,  "right_blocked": True},  "STOP"),
]

ALLOWED = {"FORWARD", "LEFT", "RIGHT", "STOP"}

for state, expected in CASES:
    result = decide(state)
    assert result in ALLOWED, f"{state} -> illegal action {result!r}"
    assert result == expected, f"{state} -> got {result}, expected {expected}"
    print(f"PASS {state} -> {result}")

print("\ntest_generated_navigation_logic passed")