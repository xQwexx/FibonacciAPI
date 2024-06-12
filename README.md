
API:

Set up environment:
    python3 -m venv .venv 
    install -r requirements.txt

Activate: 
    . .venv/bin/activate


Setup database:
flask --app api init-db

Run server:
flask --app api run --debug

Run test:
python -m pytest
