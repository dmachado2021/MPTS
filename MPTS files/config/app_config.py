"""
MPTS Application Configuration
"""

from pathlib import Path

# Application
APP_NAME = "MPTS - Manufacturing Production Tracking System"

# Window
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
START_MAXIMIZED = True

# Database
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATABASE_PATH = PROJECT_ROOT / "database" / "mpts.db"

# Folders
BACKUP_FOLDER = PROJECT_ROOT / "backups"
REPORT_FOLDER = PROJECT_ROOT / "reports"