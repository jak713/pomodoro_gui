#!/usr/bin/env python3

import sys
import os
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt6.QtGui import QFont, QIcon, QPixmap

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setWindowTitle("Pomodoro")
        self.setFixedSize(250,190)
        self.setStyleSheet("background-color: forestgreen")



        self.seconds = 1500
        self.counter = 0

        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_time)

        self.setUpMainWindow()

    def setUpMainWindow(self):
        
        self.time_label = QLabel(f"{str(self.seconds)}s", self)
        self.time_label.setFont(QFont("Arial",70))
        self.time_label.setStyleSheet("color: lightgreen; padding: 2px;")
        self.time_label.resize(250,120)
        self.time_label.move(12, 15)

        self.start_button = QPushButton("Start Timer", self)
        self.start_button.resize(150,40)
        self.start_button.move(50,130)
        self.start_button.setStyleSheet("color: lightgreen; background-color: darkgreen;")
        self.start_button.clicked.connect(self.start_timer)

        self.focus_time_label = QLabel(f"Focused for 0 minutes", self)
        self.focus_time_label.resize(200,20)
        self.focus_time_label.move(55,10)
        self.focus_time_label.setStyleSheet("color: darkgreen")
        
    def start_timer(self):
        """Start 25:00 minute timer and turn the colour scheme to red."""
        self.start_button.setStyleSheet("color: lightpink; background-color:darkred;")
        self.start_button.setText("Reset")
        self.start_button.clicked.connect(self.reset)
        self.setStyleSheet("background-color: #c3423f")
        self.time_label.setStyleSheet("color: pink; padding: 2px")
        self.focus_time_label.setStyleSheet("color: darkred")
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