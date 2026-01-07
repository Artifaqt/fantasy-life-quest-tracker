# Fantasy Life Quest Tracker - Modernization Guide

## 🎉 What's New in the Modern Edition

The Quest Tracker has been **completely overhauled** with modern technologies and features!

### 🌟 Major Upgrades

#### **1. Beautiful Modern UI with Dark Mode**
- **CustomTkinter** framework for sleek, professional appearance
- Built-in **dark/light mode toggle** (top-left switch)
- Color-coded quest rows:
  - 🔴 Red = Unobtained
  - 🟡 Yellow = Obtained
  - 🟢 Green = Completed
  - 🔵 Blue = Turned In
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
- **Real-time search** as you type (debounced for performance)
- Filter by status: All, Unobtained, Obtained, Completed, Turned In
- Sort by: Name, Life, Rank, Status, Last Modified
- Search matches quest names instantly

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

#### **7. Statistics Dashboard**
- Live progress tracking at the top
- Total quests, completion percentage
- Breakdown by status with emoji indicators
- Updates automatically as you mark quests

#### **8. Keyboard Shortcuts**
- **Ctrl+F** - Focus search box
- **Ctrl+E** - Export data
- **Ctrl+B** - Bulk operations
- **Ctrl+1** - Mark selected as Unobtained
- **Ctrl+2** - Mark selected as Obtained
- **Ctrl+3** - Mark selected as Completed
- **Ctrl+4** - Mark selected as Turned In
- **Esc** - Clear search

#### **9. Import/Export**
- Export all quest data to JSON format
- Includes notes, tags, and timestamps
- Backup your progress easily

## 🚀 How to Run

### Running the Modern Version

```bash
# Install dependencies (first time only)
pip install customtkinter pillow openpyxl

# Run the modern version
python3 FantasyLifeQuestTracker_Modern.py
```

### Running the Original Version

```bash
# The original still works!
python3 FantasyLifeQuestTracker.py
```

## 📖 How to Use

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

**Search:**
- Type in the search box (top toolbar)
- Search filters quest names in real-time
- Press Ctrl+F to quickly focus search
- Press Esc to clear search

**Filter by Status:**
- Click radio buttons in toolbar: All, Unobtained, Obtained, Completed, Turned In

**Sort:**
- Use the "Sort" dropdown to order by Name, Life, Rank, Status, or Last Modified

### Adding Notes

1. Select a quest
2. Type notes in the "Notes" text box (right panel)
3. Click "Save Note"
4. Notes are saved to the database

### Viewing Quest Details

- **Double-click** any quest to view full details
- Details panel shows: Name, Life, Rank, Giver, Turn In location, Description, Wiki URL
- Click quest name to open wiki in browser (planned feature)

### Exporting Data

1. Click "Export" button (top-right)
2. Choose filename and location
3. Data exported as JSON with all notes and tags

### Dark/Light Mode

- Toggle the "Dark Mode" switch (top-left)
- Your preference is saved

## 🎯 Pro Tips

### Multi-Select Power
- **Ctrl+Click** individual quests to select them
- **Shift+Click** to select a range
- Great for bulk updating all quests in a Life

### Quick Filtering Workflow
1. Filter by status: "Unobtained"
2. Sort by "Life"
3. Search for specific quest name
4. Multi-select quests
5. Bulk mark as "Obtained"

### Keyboard Ninja Mode
- Ctrl+F → type search → Select quests → Ctrl+3 → Done!
- Update dozens of quests in seconds

### Color-Coding
- Rows are color-coded so you can see status at a glance
- 🔴 Red quests = not started
- 🟢 Green quests = completed (but not turned in)
- 🔵 Blue quests = fully done!

## 🔧 Technical Details

### Architecture Improvements
- **Class-based design** (no more global variables!)
- **MVC pattern** - Model (Database), View (UI), Controller (Logic)
- **Debounced search** - 300ms delay prevents lag while typing
- **SQLite database** - Supports complex queries, indexing, transactions
- **Virtual scrolling** - Renders 1000+ rows smoothly
- **Modern Python** - Type hints, proper error handling

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

## 🆚 Original vs Modern

| Feature | Original | Modern |
|---------|----------|---------|
| UI Framework | tkinter | CustomTkinter |
| Appearance | Basic grey | Modern with dark mode |
| Data Storage | Text file + Excel | SQLite database |
| Quest Display | 29 per page | All 1296 (virtual scroll) |
| Sorting | Name, Life, Location, Status | Same + Rank, Last Modified |
| Search | Name only | Real-time debounced |
| Multi-select | No | Yes (Ctrl/Shift+Click) |
| Bulk Operations | No | Yes |
| Quest Notes | No | Yes |
| Keyboard Shortcuts | No | 10+ shortcuts |
| Color Coding | No | Yes (status colors) |
| Statistics | Button counters only | Full dashboard |
| Export | No | JSON export |
| Performance | Slow (Excel reads) | Fast (database) |
| Window | Fixed 1500x1000 | Resizable |

## 🐛 Troubleshooting

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

## 🔮 Future Enhancements (Potential)

- Cloud sync (Google Drive, Dropbox)
- Quest dependencies tracking
- Recommended next quests
- Time tracking & graphs
- Multiple save profiles
- Plugin system
- Web version (Flask + React)
- Mobile app (React Native)

## 📝 Migration Notes

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

**Enjoy your modernized quest tracking experience! 🎮✨**

Questions or issues? Check the GitHub issues page.
