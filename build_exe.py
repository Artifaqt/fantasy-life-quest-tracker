"""
Build script for Fantasy Life Quest Tracker executable
Run this script to create a standalone .exe file
"""
import PyInstaller.__main__
import os

# Get the directory of this script
base_dir = os.path.dirname(os.path.abspath(__file__))

PyInstaller.__main__.run([
    'FantasyLifeQuestTracker_Modern.py',
    '--name=FantasyLifeQuestTracker',
    '--onefile',
    '--windowed',
    '--icon=Images/icon.ico',
    f'--add-data={os.path.join(base_dir, "modules")}{os.pathsep}modules',
    f'--add-data={os.path.join(base_dir, "Images")}{os.pathsep}Images',
    f'--add-data={os.path.join(base_dir, "FLData.xlsx")}{os.pathsep}.',
    f'--add-data={os.path.join(base_dir, "currentprogress.txt")}{os.pathsep}.',
    f'--add-data={os.path.join(base_dir, "placenames.txt")}{os.pathsep}.',
    f'--add-data={os.path.join(base_dir, "imagenames.txt")}{os.pathsep}.',
    '--hidden-import=PIL._tkinter_finder',
    '--collect-all=customtkinter',
    '--noconfirm',
])

print("\n" + "="*70)
print("Build complete! Executable created in 'dist' folder")
print("File: dist/FantasyLifeQuestTracker.exe")
print("="*70)
