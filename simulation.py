import random
from collections import Counter

def draw_tokens(urn, draw_count=3):
    return random.sample(urn, draw_count)

def is_event_all_different(tokens):
    return len(set(tokens)) == len(tokens)

def simulate_event(urn, event_func, trials=10000):
    success = 0
    for _ in range(trials):
        draw = draw_tokens(urn)
        if event_func(draw):
            success += 1
    return success / trials
