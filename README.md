# Fantasy Life Quest Tracker - Modern Edition

A comprehensive desktop application for tracking all 1296 quests in Fantasy Life (3DS).

![Version](https://img.shields.io/badge/version-2.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-blue)

## Features

### Modern UI with Dark Mode
- CustomTkinter interface with professional styling
- Built-in dark/light mode toggle
- Color-coded quest rows by status:
  - Red = Unobtained
  - Yellow = Obtained
  - Green = Completed
  - Blue = Turned In

### Advanced Search & Filtering
- Enhanced search with field selector:
  - Search by: Name, Life, NPC, Description, or All Fields
  - Real-time filtering as you type
- Life filtering: 12 Life buttons with quest counts
- Status filtering: Filter by completion status
- Custom rank sorting: Quests sort by progression (Novice to Creator)

### Life Progress Tracking
- 12 progress bars showing completion for each Life
- Live percentage and quest counts
- Automatically updates when you mark quests
- Horizontal scrolling to view all Lives

### Wiki Integration
- "Open Wiki" button for each quest
- Opens the Fantasy Life Wiki page in your browser
- Quick access to quest requirements and walkthroughs

### Performance & Quality of Life
- Virtual scrolling: View all 1296 quests at once
- Multi-select quests (Ctrl+Click, Shift+Click)
- Bulk operations: Update multiple quests at once
- Quest notes: Add personal notes to any quest
- SQLite database: Fast, reliable data storage
- Auto-import: Automatically loads data on first run

### Keyboard Shortcuts
- `Ctrl+F` - Focus search box
- `Ctrl+E` - Export data
- `Ctrl+B` - Bulk operations
- `Ctrl+1/2/3/4` - Mark selected quests by status
- `Esc` - Clear search

## Download & Installation

### Option 1: Standalone Executable (Recommended)

**Download the latest release:**
1. Go to [Releases](../../releases)
2. Download `FantasyLifeQuestTracker.exe`
3. Double-click to run - no installation needed!

### Option 2: Run from Source

**Requirements:**
- Python 3.8 or higher
- pip (Python package manager)

**Installation:**
```bash
# Clone or download this repository
git clone https://github.com/yourusername/fantasy-life-quest-tracker.git
cd fantasy-life-quest-tracker

# Install dependencies
pip install -r requirements.txt

# Run the tracker
python FantasyLifeQuestTracker_Modern.py
```

## Usage

### First Run
The tracker will automatically import all 1296 quests from the included `FLData.xlsx` file. All quests start as "Unobtained".

### Tracking Your Progress

**Update Quest Status:**
1. Click a quest in the table
2. Use the colored status buttons on the right, or
3. Select multiple quests (Ctrl+Click) and use "Bulk Edit"

**Filter by Life:**
- Click any of the 12 Life buttons in the left sidebar
- See only quests for that specific Life
- Click "All Lives" to see everything

**Search for Quests:**
1. Choose search field from dropdown (Name, Life, NPC, etc.)
2. Type in the search box
3. Results filter in real-time

**View Quest Details:**
- Double-click any quest to see full details
- Click "Open Wiki" to learn more about the quest

**Add Personal Notes:**
1. Select a quest
2. Type notes in the "Notes" box
3. Click "Save Note"

### Export Your Progress
Click the "Export" button to save all your quest data (including notes) as a JSON file.

## Pro Tips

### Keyboard Ninja
- Use `Ctrl+F` → type search → `Ctrl+1/2/3/4` to quickly mark quests
- Use `Shift+Click` to select a range of quests for bulk updates

### Efficient Workflow
1. Filter by Life (e.g., "Paladin")
2. Sort by Rank to see progression
3. Search for specific quests
4. Multi-select and bulk update

### Track Your Journey
- Watch the progress bars fill up as you complete quests
- Use the quest notes to remember tricky requirements
- Export your progress to backup or share

## File Structure

```
fantasy-life-quest-tracker/
├── FantasyLifeQuestTracker_Modern.py  # Main application
├── modules/                            # Helper modules
│   ├── constants.py                   # Lives, ranks, colors
│   ├── region_mapping.py              # Regional data
│   ├── image_manager.py               # Image loading
│   └── progress_tracker.py            # Progress calculations
├── Images/                            # Location thumbnails
├── FLData.xlsx                        # Quest database source
├── currentprogress.txt                # Progress file
├── quest_tracker.db                   # SQLite database (auto-created)
└── README.md                          # This file
```

## Building the Executable

To build your own executable:

```bash
# Install PyInstaller
pip install pyinstaller

# Run build script
python build_exe.py
```

The executable will be created in the `dist/` folder.

## Original vs Modern

| Feature | Original (2020) | Modern (2026) |
|---------|----------------|---------------|
| UI Framework | tkinter | CustomTkinter |
| Appearance | Basic grey | Modern with dark mode |
| Data Storage | Text file + Excel | SQLite database |
| Quest Display | 29 per page | All 1296 (virtual scroll) |
| Search | Name only | Name/Life/NPC/Description/All |
| Multi-select | No | Yes (Ctrl/Shift+Click) |
| Progress Tracking | No | 12 Life progress bars |
| Wiki Integration | Links only | Clickable "Open Wiki" button |
| Life Filters | No | 12 Life buttons with counts |
| Notes System | No | Yes (per-quest notes) |
| Keyboard Shortcuts | No | 10+ shortcuts |
| Performance | Slow (Excel reads) | Fast (database) |

## Troubleshooting

**"No module named 'customtkinter'"**
```bash
pip install customtkinter pillow openpyxl
```

**Database not importing**
- Ensure `FLData.xlsx` and `currentprogress.txt` are in the same folder
- Delete `quest_tracker.db` and restart the app

**Quests not showing**
- Check your filters (click "All Lives" and "All" status)
- Clear the search box (press Esc)

**Dark mode looks weird**
- Try toggling the dark/light mode switch (top-left)

## Credits

- **Original Creator:** Sarah (2020)
- **Modernization:** 2026
- **Game:** Fantasy Life © Level-5

## License

MIT License - Feel free to use, modify, and distribute!

## Contributing

Issues and pull requests are welcome. Help make this tracker even better.
