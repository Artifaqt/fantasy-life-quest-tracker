"""
Progress Tracker for Fantasy Life Quest Tracker
Calculates and caches Life progress data
"""

import time
from .constants import RANK_ORDER


class ProgressTracker:
    """Calculates and caches Life progress data"""

    def __init__(self, database):
        self.db = database
        self.cache = {}
        self.cache_timestamp = None

    def get_life_progress(self, life_name):
        """Get progress for specific Life with caching"""
        # Check cache (valid for 1 second)
        if self.cache_timestamp and (time.time() - self.cache_timestamp < 1):
            if life_name in self.cache:
                return self.cache[life_name]

        # Calculate progress
        progress = self._calculate_life_progress(life_name)

        # Cache result
        self.cache[life_name] = progress
        self.cache_timestamp = time.time()

        return progress

    def _calculate_life_progress(self, life_name):
        """Calculate completion progress for a Life"""
        cursor = self.db.conn.cursor()

        # Get total and completed quests for this Life
        cursor.execute('''
            SELECT
                COUNT(*) as total,
                SUM(CASE WHEN status >= 2 THEN 1 ELSE 0 END) as completed
            FROM quests
            WHERE life = ?
        ''', (life_name,))

        result = cursor.fetchone()
        total = result['total'] if result else 0
        completed = result['completed'] if result and result['completed'] else 0
        percentage = (completed / total * 100) if total > 0 else 0

        # Get rank breakdown
        cursor.execute('''
            SELECT
                rank,
                COUNT(*) as total,
                SUM(CASE WHEN status >= 2 THEN 1 ELSE 0 END) as completed
            FROM quests
            WHERE life = ?
            GROUP BY rank
        ''', (life_name,))

        rank_progress = []
        rank_data = cursor.fetchall()

        # Sort ranks by RANK_ORDER
        for rank_name in RANK_ORDER:
            for row in rank_data:
                if row['rank'] == rank_name:
                    rank_progress.append({
                        'rank': row['rank'],
                        'total': row['total'],
                        'completed': row['completed'] if row['completed'] else 0
                    })
                    break

        return {
            'total': total,
            'completed': completed,
            'percentage': percentage,
            'ranks': rank_progress
        }

    def get_all_progress(self):
        """Get progress for all Lives"""
        from .constants import LIVES

        all_progress = {}
        for life_name, _ in LIVES:
            all_progress[life_name] = self.get_life_progress(life_name)

        return all_progress

    def invalidate_cache(self):
        """Clear cache when quest status changes"""
        self.cache.clear()
        self.cache_timestamp = None
