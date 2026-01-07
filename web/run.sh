#!/bin/bash
# DocGen Web - Start both backend and frontend servers

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}  📚 DocGen Web Interface${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Check for required commands
check_command() {
    if ! command -v "$1" &> /dev/null; then
        echo -e "${RED}Error: $1 is not installed${NC}"
        exit 1
    fi
}

check_command python3
check_command pip3
check_command node
check_command npm

# Main project setup (for running analysis)
echo -e "${YELLOW}▶ Setting up main project...${NC}"
PROJECT_ROOT="$SCRIPT_DIR/.."

# Check if project venv exists, create if not
if [ ! -d "$PROJECT_ROOT/venv" ] && [ ! -d "$PROJECT_ROOT/.venv" ]; then
    echo -e "  Creating project virtual environment..."
    python3 -m venv "$PROJECT_ROOT/venv"
fi

# Determine which venv to use
if [ -d "$PROJECT_ROOT/venv" ]; then
    PROJECT_VENV="$PROJECT_ROOT/venv"
elif [ -d "$PROJECT_ROOT/.venv" ]; then
    PROJECT_VENV="$PROJECT_ROOT/.venv"
fi

# Install project dependencies
if [ -n "$PROJECT_VENV" ]; then
    echo -e "  Installing project dependencies..."
    source "$PROJECT_VENV/bin/activate"
    pip install -q -r "$PROJECT_ROOT/requirements.txt"
    deactivate
fi

echo -e "${GREEN}  ✓ Main project ready${NC}"

# Backend setup
echo -e "${YELLOW}▶ Setting up backend...${NC}"
cd "$SCRIPT_DIR/backend"

# Check if venv exists, create if not
if [ ! -d "venv" ]; then
    echo -e "  Creating virtual environment..."
    python3 -m venv venv
fi

# Activate venv
source venv/bin/activate

# Install/upgrade dependencies
echo -e "  Installing Python dependencies..."
pip install -q -r requirements.txt

echo -e "${GREEN}  ✓ Backend ready${NC}"

# Frontend setup
echo -e "${YELLOW}▶ Setting up frontend...${NC}"
cd "$SCRIPT_DIR/frontend"

# Install npm dependencies if node_modules doesn't exist or package.json changed
if [ ! -d "node_modules" ] || [ "package.json" -nt "node_modules" ]; then
    echo -e "  Installing npm dependencies..."
    npm install --silent
fi

echo -e "${GREEN}  ✓ Frontend ready${NC}"
echo ""

# Function to cleanup on exit
cleanup() {
    echo ""
    echo -e "${YELLOW}Shutting down servers...${NC}"
    kill $BACKEND_PID 2>/dev/null || true
    kill $FRONTEND_PID 2>/dev/null || true
    exit 0
}

trap cleanup SIGINT SIGTERM

# Start backend
echo -e "${BLUE}▶ Starting backend server...${NC}"
cd "$SCRIPT_DIR/backend"
source venv/bin/activate
python main.py &
BACKEND_PID=$!

# Wait a moment for backend to start
sleep 2

# Start frontend
echo -e "${BLUE}▶ Starting frontend dev server...${NC}"
cd "$SCRIPT_DIR/frontend"
npm run dev &
FRONTEND_PID=$!

# Wait a moment for frontend to start
sleep 3

echo ""
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}  🚀 DocGen Web is running!${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "  Frontend: ${BLUE}http://localhost:5173${NC}"
echo -e "  Backend:  ${BLUE}http://localhost:8000${NC}"
echo -e "  API Docs: ${BLUE}http://localhost:8000/docs${NC}"
echo ""
echo -e "  Press ${YELLOW}Ctrl+C${NC} to stop both servers"
echo ""

# Wait for both processes
wait $BACKEND_PID $FRONTEND_PID
