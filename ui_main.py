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

        # Optional: Show probability estimate
        approx = simulate_event(self.urn, is_event_all_different, 1000)
        self.label.setText(f"Estimated P(all different): {approx:.4f}")
