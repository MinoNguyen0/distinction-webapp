from flask import Flask, jsonify
from datetime import datetime
import platform

app = Flask(__name__)

@app.route('/')
def home():
    return f'''
    <html>
    <head>
        <title>Distinction Web App - SWE40006</title>
        <style>
            body {{ font-family: Arial, sans-serif; max-width: 600px; margin: 60px auto; padding: 0 20px; }}
            h1 {{ color: #2c3e50; }}
            .card {{ background: #f4f6f8; border-radius: 8px; padding: 20px; margin-top: 20px; }}
            a {{ color: #2980b9; }}
        </style>
    </head>
    <body>
        <h1>SWE40006 - Distinction Task 4.3</h1>
        <p>This page is served from a Docker container deployed to a public host.</p>
        <div class="card">
            <p><strong>Server time:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            <p><strong>Python version:</strong> {platform.python_version()}</p>
        </div>
        <p>Try the <a href="/about">/about</a> page or <a href="/api/status">/api/status</a> endpoint.</p>
    </body>
    </html>
    '''

@app.route('/about')
def about():
    return '''
    <h1>About this app</h1>
    <p>A simple Flask application containerized with Docker and deployed publicly
    for SWE40006 Software Deployment and Evolution, Task 4.3 (Distinction).</p>
    <p><a href="/">Back home</a></p>
    '''

@app.route('/api/status')
def status():
    return jsonify({
        'status': 'ok',
        'timestamp': datetime.now().isoformat(),
        'service': 'distinction-webapp'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 