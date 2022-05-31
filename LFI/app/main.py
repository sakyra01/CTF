from flask import Flask, render_template, request
import os
import time

app = Flask(__name__)


@app.route("/")
def index():
    filename = request.args.get('file') # принимаемый запрос от клиента

    if filename is None:
        filename = "file.txt"
    filename = "files/" + filename
    if os.path.exists(filename) and os.path.isfile(filename):
        with open(filename, 'r') as f:
            content = f.read()
            create = str(time.ctime(os.path.getmtime(filename)))
            filename = f.name.split('/')[-1]
            file = {
                "filename": f"File name {filename}",
                "create": f"Create data {create}",
                "file": content
            }
    else:
        file = {
            "filename": f'File "{filename.split("/")[-1] }" not found',
        }
    return render_template('index.html', file=file)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)