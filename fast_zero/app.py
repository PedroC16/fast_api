from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>Olar bebe</title>
        </head>
        <body>
            <h1>Olá mundo 🤪</h1>
        </body>
    </html>
"""
