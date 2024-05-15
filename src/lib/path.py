import os

def path(filename):
    static_dir = os.path.join(os.path.dirname(__file__), "..", "..", "static")
    return os.path.join(static_dir, filename)
