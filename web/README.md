# DocGen Web Interface

Web UI for monitoring and controlling documentation generation.

## Quick Start

```bash
./run.sh
```

This starts both servers:
- **Frontend**: http://localhost:5173 (Vite + React)
- **Backend**: http://localhost:8000 (FastAPI)
- **API Docs**: http://localhost:8000/docs (Swagger UI - interactive API documentation)

Press `Ctrl+C` to stop.

## Architecture

```
web/
├── backend/
│   └── main.py          # FastAPI server
├── frontend/            # React + TypeScript + Vite
│   ├── src/
│   └── package.json
├── run.sh               # Start both servers
└── kill_stuck_jobs.sh   # Cleanup helper
```

## Manual Setup

**Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/config` | GET | Get current configuration |
| `/config` | POST | Update configuration |
| `/jobs` | GET | List documentation jobs |
| `/jobs` | POST | Start new job |
| `/jobs/{id}` | GET | Get job status |
| `/repos` | GET | List processed repositories |

See http://localhost:8000/docs for full API documentation.
