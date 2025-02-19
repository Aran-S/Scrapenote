from flask import jsonify
import os

class Notepad:
    def __init__(self, notes_file='notes.txt'):
        self.notes_file = notes_file
        self.ensure_notes_file_exists()

    def ensure_notes_file_exists(self):
        if not os.path.exists(self.notes_file):
            with open(self.notes_file, 'w') as f:
                f.write('')

    def save_note(self, note):
        with open(self.notes_file, 'a') as f:
            f.write(note + '\n')

    def load_notes(self):
        with open(self.notes_file, 'r') as f:
            return f.readlines()