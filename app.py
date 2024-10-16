from flask import Flask, render_template, request, send_file
from scanner.scanner import scan_network
from flask_weasyprint import HTML
import io

app = Flask(__name__)

devices = []
last_scanned = None

@app.route('/')
def index():
    global devices, last_scanned
    ip_range = "192.168.0.1/24"
    devices = scan_network(ip_range)
    return render_template('index.html', devices=devices, search_query='')

@app.route('/search', methods=['GET'])
def search():
    global devices
    query = request.args.get('query', '').lower()
    
    filtered_devices = [
        device for device in devices 
        if query in device['ip'].lower() or query in device['mac'].lower() or query in device['name'].lower()
    ]

    return render_template('index.html', devices=filtered_devices, search_query=query)

@app.route('/export/pdf')
def export_pdf():
    ip_range = "192.168.0.1/24"
    devices = scan_network(ip_range)
    html = render_template('devices_pdf.html', devices=devices)

    pdf = HTML(string=html).write_pdf()
    

    return send_file(io.BytesIO(pdf), as_attachment=True, download_name='devices_report.pdf')

if __name__ == '__main__':
    app.run(debug=True)
