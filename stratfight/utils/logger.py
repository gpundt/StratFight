from datetime import datetime

def log(message: str, *, prefix: str = "", end: str = "\n", use_time: bool = True):
    """Centralized logging function."""
    timestamp = f"[{datetime.now().strftime('%H:%M:%S')}] " if use_time else ""
    print(f"{timestamp}{prefix}{message}", end=end)