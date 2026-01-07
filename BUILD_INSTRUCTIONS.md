# Build Instructions - Fantasy Life Quest Tracker

This guide explains how to build a standalone executable of the Fantasy Life Quest Tracker.

## Prerequisites

1. **Python 3.8 or higher** installed
2. **All dependencies** installed:
   ```bash
   pip install -r requirements.txt
   ```
3. **PyInstaller** for building the executable:
   ```bash
   pip install pyinstaller
   ```

## Quick Build

The easiest way to build the executable:

```bash
python build_exe.py
```

This will:
- Create a standalone `.exe` file in the `dist/` folder
- Include all necessary dependencies and data files
- Take 2-5 minutes to complete

## What Gets Included

The build script automatically bundles:

### Python Modules
- `modules/` directory (constants, progress tracker, image manager, etc.)
- All CustomTkinter, Pillow, and openpyxl dependencies

### Data Files
- `FLData.xlsx` - Quest database source
- `currentprogress.txt` - Progress file (if exists)
- `placenames.txt` - Location names
- `imagenames.txt` - Image filename mappings
- `Images/` directory - Location thumbnails and maps (48 GIF files)

### Configuration
- Single-file executable (all dependencies bundled)
- Windowed mode (no console window)
- Custom icon (if `Images/icon.ico` exists)

## Build Output

After building, you'll find:

```
fantasy-life-quest-tracker/
├── build/                          # Temporary build files (can delete)
├── dist/
│   └── FantasyLifeQuestTracker.exe # Your standalone executable!
└── FantasyLifeQuestTracker.spec    # PyInstaller spec file
```

## Testing the Executable

1. Navigate to the `dist/` folder
2. Double-click `FantasyLifeQuestTracker.exe`
3. The app should launch without needing Python installed
4. Verify:
   - Database auto-imports on first run
   - Dark mode toggle works
   - Life filters display correctly
   - Progress bars appear at bottom
   - Wiki links open in browser
   - All images load properly

## Distribution

To share the executable:

1. **Single File Method:**
   - Just share `FantasyLifeQuestTracker.exe` from `dist/`
   - Recipients double-click to run
   - No installation needed!

2. **With Data Files (Recommended):**
   - Create a zip with:
     - `FantasyLifeQuestTracker.exe`
     - `FLData.xlsx`
     - `currentprogress.txt` (optional)
   - This allows users to start fresh or import existing progress

## Advanced: Manual PyInstaller Command

If you need to customize the build:

```bash
pyinstaller FantasyLifeQuestTracker_Modern.py \
  --name=FantasyLifeQuestTracker \
  --onefile \
  --windowed \
  --icon=Images/icon.ico \
  --add-data="modules;modules" \
  --add-data="Images;Images" \
  --add-data="FLData.xlsx;." \
  --add-data="currentprogress.txt;." \
  --add-data="placenames.txt;." \
  --add-data="imagenames.txt;."
```

**Note:** On Windows, use semicolon (`;`) as the path separator. On Linux/Mac, use colon (`:`).

## Troubleshooting

### Build Fails with "Module not found"
```bash
# Reinstall all dependencies
pip install --upgrade -r requirements.txt
pip install --upgrade pyinstaller
```

### Executable is huge (>100MB)
- This is normal! PyInstaller bundles Python interpreter + all dependencies
- Typical size: 80-150MB for CustomTkinter apps

### Executable won't start
1. Check if Windows Defender or antivirus blocked it
2. Run from command prompt to see error messages:
   ```bash
   cd dist
   FantasyLifeQuestTracker.exe
   ```

### Missing images or data files
- Verify files exist in the project root before building
- Check `build_exe.py` for correct file paths
- Rebuild after adding missing files

### "Failed to execute script"
- Usually means a dependency is missing
- Check that all modules in `requirements.txt` are installed
- Try deleting `build/` and `dist/` folders, then rebuild

## GitHub Release

To create a release on GitHub:

1. **Build the executable** (as above)

2. **Create a new release:**
   ```bash
   # Tag the version
   git tag -a v2.0 -m "Modern edition with dark mode and progress tracking"
   git push origin v2.0
   ```

3. **Upload to GitHub:**
   - Go to your repo → Releases → "Create a new release"
   - Choose tag: `v2.0`
   - Title: "Fantasy Life Quest Tracker v2.0 - Modern Edition"
   - Upload `dist/FantasyLifeQuestTracker.exe`
   - Add release notes (see below)

4. **Release Notes Template:**
   ```markdown
   ## Fantasy Life Quest Tracker - Modern Edition

   ### Features
   - Modern dark mode UI with CustomTkinter
   - Enhanced search (Name/Life/NPC/Description/All)
   - 12 Life filter buttons with quest counts
   - Life progress tracking with progress bars
   - Clickable wiki links for each quest
   - Virtual scrolling (view all 1296 quests)
   - Multi-select and bulk operations
   - Quest notes system
   - 10+ keyboard shortcuts
   - SQLite database backend

   ### Download
   - **Windows:** `FantasyLifeQuestTracker.exe` (standalone, no installation)
   - **Source:** Clone repo and run `python FantasyLifeQuestTracker_Modern.py`

   ### Requirements (for standalone exe)
   - Windows 10 or higher
   - No Python installation needed!

   ### First Run
   - Place `FLData.xlsx` in the same folder (or it will auto-import from bundled file)
   - Double-click to run
   - All quests start as "Unobtained"
   ```

## File Size Optimization (Optional)

To reduce executable size:

1. **Use UPX compression:**
   ```bash
   # Install UPX: https://upx.github.io/
   # Add to build_exe.py:
   '--upx-dir=C:/path/to/upx',
   ```

2. **Exclude unused modules:**
   ```bash
   # Add to PyInstaller command:
   --exclude-module=matplotlib
   --exclude-module=numpy
   # (only if you're certain they're not needed)
   ```

## Clean Build

To start fresh:

```bash
# Delete build artifacts
rm -rf build dist *.spec

# Or on Windows:
rmdir /s build dist
del FantasyLifeQuestTracker.spec

# Rebuild
python build_exe.py
```

## Support

If you encounter issues building:
1. Check Python version: `python --version` (should be 3.8+)
2. Check PyInstaller version: `pyinstaller --version` (should be 5.0+)
3. Review error messages in the console
4. Check [PyInstaller documentation](https://pyinstaller.org/)
5. Open an issue on GitHub with build log

---

Happy building!
