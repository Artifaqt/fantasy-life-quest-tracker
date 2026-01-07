# Fantasy Life Quest Tracker - Modernization Guide

## What's New in the Modern Edition

The Quest Tracker has been completely overhauled with modern technologies and features.

### Major Upgrades

#### **1. Modern UI with Dark Mode**
- CustomTkinter framework for professional appearance
- Built-in dark/light mode toggle (top-left switch)
- Color-coded quest rows:
  - Red = Unobtained
  - Yellow = Obtained
  - Green = Completed
  - Blue = Turned In
- Smooth, modern buttons and controls
- Resizable window with responsive layout

#### **2. Virtual Scrolling (No More Pagination!)**
- View **all 1296 quests** in one scrollable list
- Instant navigation - no more clicking Back/Forward
- Multi-column sortable table
- Smooth scrolling with scrollbars

#### **3. SQLite Database Backend**
- Fast, reliable database instead of text files
- Automatic import from your existing `currentprogress.txt` + `FLData.xlsx`
- Supports quest notes, tags, and statistics
- Better data integrity and performance

#### **4. Advanced Search & Filtering**
- **Enhanced search** with field selector dropdown:
  - Search by: Name, Life, NPC, Description, or All
  - Real-time filtering as you type (debounced for performance)
- **Life filtering** - 12 Life buttons in left sidebar with quest counts
- **Status filtering** - Filter by: All, Unobtained, Obtained, Completed, Turned In
- **Custom rank sorting** - Quests sort by progression (Novice → Creator)
- Sort by: Name, Life, Rank, Status, Last Modified

#### **5. Multi-Select & Bulk Operations**
- **Ctrl+Click** to select multiple quests
- **Shift+Click** to select range
- **Bulk Edit** button to update multiple quests at once
- Right-click context menu for quick actions

#### **6. Quest Notes System**
- Add personal notes to any quest
- Notes panel in right sidebar
- "Save Note" button to persist your notes
- Great for tracking quest requirements or strategies

#### **7. Life Progress Tracking**
- **12 progress bars** showing completion for each Life
- Live percentage and quest counts (e.g., "31/78 (40%)")
- Automatically updates when you mark quests
- Horizontal scrolling to see all Lives
- Visual progress at a glance

#### **8. Keyboard Shortcuts**
- **Ctrl+F** - Focus search box
- **Ctrl+E** - Export data
- **Ctrl+B** - Bulk operations
- **Ctrl+1** - Mark selected as Unobtained
- **Ctrl+2** - Mark selected as Obtained
- **Ctrl+3** - Mark selected as Completed
- **Ctrl+4** - Mark selected as Turned In
- **Esc** - Clear search

#### **9. Wiki Integration**
- "Open Wiki" button for each quest
- Click to open the Fantasy Life Wiki page
- Learn quest requirements and walkthroughs
- Integrated into quest details panel

#### **10. Import/Export**
- Export all quest data to JSON format
- Includes notes, tags, and timestamps
- Backup your progress easily

## How to Run

### Option 1: Standalone Executable (Recommended)

**Download the latest release:**
1. Go to [Releases](../../releases)
2. Download `FantasyLifeQuestTracker.exe`
3. Double-click to run - no installation needed!

### Option 2: Running from Source

**Install dependencies (first time only):**
```bash
pip install -r requirements.txt
# Or manually: pip install customtkinter pillow openpyxl
```

**Run the modern version:**
```bash
python FantasyLifeQuestTracker_Modern.py
```

**Run the original version:**
```bash
python FantasyLifeQuestTracker.py
```

## How to Use

### First Launch
1. The app will **automatically import** your existing data from `currentprogress.txt` and `FLData.xlsx`
2. A new `quest_tracker.db` file will be created
3. All your progress is preserved!

### Updating Quest Status

**Method 1: Right Panel Buttons**
1. Click a quest in the table
2. Use the colored status buttons in the right panel

**Method 2: Bulk Operations**
1. Select multiple quests (Ctrl+Click or Shift+Click)
2. Click "Bulk Edit" button
3. Choose new status

**Method 3: Context Menu**
1. Right-click on a quest
2. Select status from menu

**Method 4: Keyboard Shortcuts**
1. Select quest(s)
2. Press Ctrl+1/2/3/4

### Searching & Filtering

**Enhanced Search:**
1. Choose search field from dropdown (Name, Life, NPC, Description, All)
2. Type in the search box
3. Results filter in real-time
4. Press Ctrl+F to quickly focus search
5. Press Esc to clear search

**Filter by Life:**
- Click any of the 12 Life buttons in the left sidebar
- See only quests for that specific Life
- Click "All Lives" to see everything
- Button shows quest count for each Life

**Filter by Status:**
- Click radio buttons in toolbar: All, Unobtained, Obtained, Completed, Turned In

**Sort:**
- Use the "Sort" dropdown to order by Name, Life, Rank, Status, or Last Modified
- Rank sorting follows progression: Novice → Fledgling → Apprentice → Adept → Expert → Master → Hero → Legend → Demi-Creator → Creator

### Adding Notes

1. Select a quest
2. Type notes in the "Notes" text box (right panel)
3. Click "Save Note"
4. Notes are saved to the database

### Viewing Quest Details

- **Double-click** any quest to view full details
- Details panel shows: Name, Life, Rank, Giver (NPC), Turn In location, Description, Wiki URL
- Click "Open Wiki" button to open the quest's wiki page in your browser

### Exporting Data

1. Click "Export" button (top-right)
2. Choose filename and location
3. Data exported as JSON with all notes and tags

### Dark/Light Mode

- Toggle the "Dark Mode" switch (top-left)
- Your preference is saved

## Pro Tips

### Multi-Select Power
- **Ctrl+Click** individual quests to select them
- **Shift+Click** to select a range
- Great for bulk updating all quests in a Life

### Efficient Workflow
1. Filter by Life (e.g., "Paladin")
2. Sort by Rank to see progression
3. Search for specific quests
4. Multi-select and bulk update

### Keyboard Ninja Mode
- Ctrl+F → type search → Select quests → Ctrl+3 → Done!
- Update dozens of quests in seconds

### Track Your Journey
- Watch the progress bars fill up as you complete quests
- Use the quest notes to remember tricky requirements
- Export your progress to backup or share

### Color-Coding
- Rows are color-coded so you can see status at a glance
- Red quests = not started (Unobtained)
- Yellow quests = obtained (but not completed)
- Green quests = completed (but not turned in)
- Blue quests = fully done (Turned In)

## Technical Details

### Architecture Improvements
- **Class-based design** (no more global variables!)
- **Modular structure** - Separate modules for constants, progress tracking, and image management
- **MVC pattern** - Model (Database), View (UI), Controller (Logic)
- **Debounced search** - 300ms delay prevents lag while typing
- **SQLite database** - Supports complex queries, indexing, transactions
- **Virtual scrolling** - Renders 1000+ rows smoothly
- **Modern Python** - Type hints, proper error handling
- **3-panel layout** - Left sidebar (Life filters), center (quest table), right panel (details)

### Performance Gains
- **100x faster filtering** (database queries vs nested loops)
- **Instant sorting** (database indexes)
- **No UI rebuilding** (reuses widgets)
- **Debounced saves** (no more save-on-every-change)

### Database Schema
```sql
quests: row_id, status, name, life, rank, giver, description, turn_in, url, last_modified
quest_locations: quest_id, location (many-to-many)
quest_notes: quest_id, note
quest_tags: quest_id, tag
statistics: date, completed_count, turned_in_count
```

**Note:** Database columns are correctly mapped from Excel:
- `giver` column = NPC name (Excel column 4)
- `rank` column = Rank (Excel column 6)

### Module Structure
```
modules/
├── __init__.py
├── constants.py         # LIVES, RANK_ORDER, STATUS_COLORS
├── region_mapping.py    # Regional data (for future features)
├── image_manager.py     # Image loading/caching
└── progress_tracker.py  # Progress calculations
```

## Original vs Modern

| Feature | Original (2020) | Modern (2026) |
|---------|----------------|---------------|
| UI Framework | tkinter | CustomTkinter |
| Appearance | Basic grey | Modern with dark mode |
| Data Storage | Text file + Excel | SQLite database |
| Quest Display | 29 per page | All 1296 (virtual scroll) |
| Search | Name only | Name/Life/NPC/Description/All |
| Sorting | Name, Life, Location, Status | Same + Custom Rank progression |
| Multi-select | No | Yes (Ctrl/Shift+Click) |
| Life Filters | No | 12 Life buttons with counts |
| Progress Tracking | No | 12 Life progress bars |
| Wiki Integration | Links only | Clickable "Open Wiki" button |
| Bulk Operations | No | Yes |
| Quest Notes | No | Yes (per-quest notes) |
| Keyboard Shortcuts | No | 10+ shortcuts |
| Color Coding | No | Yes (status colors) |
| Export | No | JSON export |
| Performance | Slow (Excel reads) | Fast (database) |
| Window | Fixed 1500x1000 | Resizable |
| Executable | No | Yes (standalone .exe) |

## Troubleshooting

### "No module named 'customtkinter'"
```bash
pip install customtkinter pillow
```

### Database not created
- Ensure `currentprogress.txt` and `FLData.xlsx` exist in the same directory
- Check file permissions
- Look for error messages in console

### Dark mode looks weird
- Try toggling dark/light mode switch
- Some systems may need theme updates

### Quests not showing
- Check your filter settings (try "All" status)
- Clear the search box (press Esc)
- Restart the application

## Building the Executable

To build your own standalone executable:

```bash
# Install PyInstaller
pip install pyinstaller

# Run the build script
python build_exe.py
```

The executable will be created in the `dist/` folder as `FantasyLifeQuestTracker.exe`.

For detailed build instructions, see [BUILD_INSTRUCTIONS.md](BUILD_INSTRUCTIONS.md).

## Future Enhancements (Potential)

- Location-based filtering with images
- Quest dependencies tracking
- Recommended next quests
- Time tracking & graphs
- Multiple save profiles
- Cloud sync (Google Drive, Dropbox)
- Plugin system
- Web version (Flask + React)
- Mobile app (React Native)

## Migration Notes

### Data Compatibility
- Your original `currentprogress.txt` is **NOT modified**
- Original tracker still works alongside modern version
- Database is imported once on first run
- You can export from modern version back to JSON if needed

### Reverting to Original
- Just run `FantasyLifeQuestTracker.py` instead
- Your progress in `currentprogress.txt` is unchanged
- Delete `quest_tracker.db` to reset modern version

---

Questions or issues? Check the GitHub issues page.
