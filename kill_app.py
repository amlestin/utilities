import os
import sys

if len(sys.argv) < 2:
    app = "vim"
else:
    app = sys.argv[1]

os.system(f"killall -9 {app}")
