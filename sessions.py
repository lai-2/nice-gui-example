import uuid
from collections import Counter
from datetime import datetime
from nicegui import ui, app
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request

app.add_middleware(SessionMiddleware, secret_key='abcd')

counter = Counter()
start = datetime.now().strftime('%H:%M, %d %B %Y')

@ui.page('/session_demo')
def session_demo(request: Request):
    if 'id' not in request.session:
        request.session['id'] = str(uuid.uuid4())
    
    counter[request.session['id']] += 1
    ui.label(f'{len(counter)} unique views ({sum(counter.values())} overall) since {start}')


ui.link('visit session demo', session_demo)
ui.run()