#!/bin/bash
# Kill stuck DocGen analysis jobs

echo "🔍 Finding DocGen processes..."

# Find all Python processes running main.py
PIDS=$(ps aux | grep "[p]ython.*main.py" | awk '{print $2}')

if [ -z "$PIDS" ]; then
    echo "✅ No DocGen processes found"
    exit 0
fi

echo "Found processes:"
ps aux | grep "[p]ython.*main.py" | grep -v grep

echo ""
read -p "Kill these processes? (y/N) " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    for PID in $PIDS; do
        echo "Killing process group for PID $PID..."
        # Kill the entire process group
        kill -TERM -$PID 2>/dev/null || kill -TERM $PID 2>/dev/null
        sleep 1
        # Force kill if still running
        kill -KILL -$PID 2>/dev/null || kill -KILL $PID 2>/dev/null
    done
    echo "✅ Done"
else
    echo "Cancelled"
fi

