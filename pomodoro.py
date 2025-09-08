#!/usr/bin/env python3

import sys
import os
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QHBoxLayout,QComboBox
from PyQt6.QtGui import QFont, QIcon, QPixmap

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setWindowTitle("Pomodoro")
        self.setStyleSheet("background-color: forestgreen")

        self.seconds = 1500
        self.counter = 0

        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_time)

        self.setUpMainWindow()

    def setUpMainWindow(self):
        self.central_widget = QWidget()
        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)

        self.time_label = QLabel(f"{str(self.seconds)}s", self)
        self.time_label.setFont(QFont("Arial",70))
        self.time_label.setStyleSheet("color: lightgreen; padding: 2px;")
        self.time_label.setFixedSize(250,90)



        self.start_button = QPushButton("Start Timer", self)
        self.start_button.setFixedSize(150,40)
        self.start_button.setStyleSheet("color: lightgreen; background-color: darkgreen;")
        self.start_button.clicked.connect(self.start_timer)

        self.focus_time_label = QLabel(f"Focused for 0 minutes", self)
        self.focus_time_label.setFixedSize(200,20)
        self.focus_time_label.setStyleSheet("color: darkgreen")
        self.focus_time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        hours = QComboBox(self)
        hours.setStyleSheet("""border: 1px dashed black;
    padding: 1px 10px 1px 3px;
    min-width: 5em;
    combobox-popup: 0;""")
        for hour in range(7):
            hours.addItem(str(hour) + " hours")

        minutes = QComboBox(self)
        minutes.setStyleSheet("""border: 1px dashed black;
    padding: 1px 10px 1px 3px;
    min-width: 6em;
    combobox-popup: 0;
    """)
    
        for minute in range(60):
            minutes.addItem(str(minute) + " minutes")

        self.set_time_button = QPushButton("Set time", self)
        self.set_time_button.setFixedSize(60,30)
        self.set_time_button.setStyleSheet("color: lightgreen;")
        self.set_time_button.clicked.connect(lambda: self.set_timer(hours.currentText(), minutes.currentText()))
        
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.focus_time_label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.time_label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.start_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.set_time_layout = QHBoxLayout()
        self.set_time_layout.addWidget(hours)
        self.set_time_layout.addWidget(minutes)
        self.set_time_layout.addWidget(self.set_time_button)

        self.main_layout.addLayout(self.set_time_layout)
        
    def set_timer(self, hours, minutes):
        hours = hours.split()
        minutes = minutes.split()
        hours = int(hours[0])
        minutes = int(minutes[0])
        seconds = hours * 60**2 + minutes*60
        self.seconds = seconds
        self.time_label.setText(f"{str(self.seconds)}s")

    def start_timer(self):
        """Start 25:00 minute timer and turn the colour scheme to red."""
        self.start_button.setStyleSheet("color: lightpink; background-color:darkred;")
        self.start_button.setText("Reset")
        self.start_button.clicked.connect(self.reset)
        self.setStyleSheet("background-color: #c3423f")
        self.time_label.setStyleSheet("color: pink; padding: 2px")
        self.focus_time_label.setStyleSheet("color: darkred")
        self.set_time_button.setStyleSheet("color: pink; background-color:darkred")
        self.set_time_button.setDisabled(True)
        self.timer.start()
        return
    
    def update_time(self):
        if self.seconds > 0:
            self.seconds -= 1
            self.time_label.setText(f"{str(self.seconds)}s")
            self.counter += 1
            self.show_focus_time()
        else:
            self.reset()
            self.show_focus_time()

    def reset(self):
        self.timer.stop()
        self.seconds = 1500
        self.time_label.setText(f"{str(self.seconds)} s")
        self.start_button.setText("Start Timer")
        self.start_button.setStyleSheet("color: lightgreen; background-color: darkgreen;")
        self.start_button.clicked.connect(self.start_timer)
        self.setStyleSheet("background-color: forestgreen")
        self.time_label.setStyleSheet("color:  lightgreen; padding: 2px;")
        self.focus_time_label.setStyleSheet("color: darkgreen")
        self.set_time_button.setStyleSheet("color: lightgreen;")
        self.set_time_button.setDisabled(False)
        return
    
    def show_focus_time(self):
        # self.counter += 1
        # minutes = 25 * self.counter
        minutes = int(self.counter / 60)
        if minutes >= 60:
            hours = int(minutes / 60)
            minutes = int(minutes - (hours * 60))
            self.focus_time_label.move(30,10)
            if hours == 1:
                self.focus_time_label.setText(f"Focused for {hours} hour {minutes} minutes")
            else:
                self.focus_time_label.setText(f"Focused for {hours} hours {minutes} minutes")
        else:
            self.focus_time_label.setText(f"Focused for {minutes} minutes")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())