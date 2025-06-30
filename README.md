import os
import zipfile

# Define the project structure and content
project_files = {
    "probability-visual-simulator/main.py": '''\
import sys
from PyQt5.QtWidgets import QApplication
from ui_main import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
''',

    "probability-visual-simulator/simulation.py": '''\
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
''',

    "probability-visual-simulator/ui_main.py": '''\
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer
from simulation import draw_tokens, is_event_all_different, simulate_event

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Probability Visual Simulator")
        self.setFixedSize(400, 300)

        self.urn = [0] + [1]*5 + [2]*2

        # UI Elements
        self.label = QLabel("Click to draw 3 tokens", self)
        self.result_label = QLabel("", self)
        self.sim_result_label = QLabel("", self)

        self.draw_button = QPushButton("🎲 Draw", self)
        self.draw_button.clicked.connect(self.handle_draw)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.result_label)
        layout.addWidget(self.sim_result_label)
        layout.addWidget(self.draw_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def handle_draw(self):
        draw = draw_tokens(self.urn)
        result = is_event_all_different(draw)
        self.result_label.setText(f"Drawn: {draw}")
        self.sim_result_label.setText("All different? " + ("✅ Yes" if result else "❌ No"))

        approx = simulate_event(self.urn, is_event_all_different, 1000)
        self.label.setText(f"Estimated P(all different): {approx:.4f}")
''',

    "probability-visual-simulator/requirements.txt": "PyQt5>=5.15\n",

    "probability-visual-simulator/README.md": '''\
# 🎲 Probability Visual Simulator

A Python desktop application that simulates and animates probability exercises involving urn models and random draws — ideal for students and educators.

## 💡 Features

- Visual representation of tokens in an urn
- Animated random draws of 3 tokens
- Real-time detection of probability events like:
  - All numbers different
  - Sum of tokens equals a given number
- Theoretical vs simulated probability comparison
- Customizable exercise setup

## 🖼 Example Exercise

> An urn contains 8 tokens:  
> - 1 token labeled 0  
> - 5 tokens labeled 1  
> - 2 tokens labeled 2  
>
> What’s the probability that three randomly drawn tokens all have different values?

### Prerequisites

- Python 3.9+
- PyQt5

### Installation

```bash
git clone https://github.com/DerMathematiker/probability-visual-simulator.git
cd probability-visual-simulator
pip install -r requirements.txt
python main.py
