# Examples

This folder contains quick examples for using the SDK and backend.

1) Health check

Start the backend:

```bash
cd backend
python -m venv venv
# On Windows (cmd.exe)
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Run SDK CLI (from project root):

```bash
cd sdk
npm install
npx ts-node src/index.ts
```
