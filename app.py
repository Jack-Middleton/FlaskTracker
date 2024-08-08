from flask import Flask, redirect, request
from datetime import datetime

app = Flask(__name__)
log_file_path = 'click_log.txt'

@app.route('/track_click')
def track_click():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ip_address = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    referrer = request.referrer or 'Direct'

    log_entry = f"Timestamp: {timestamp}, IP: {ip_address}, User-Agent: {user_agent}, Referrer: {referrer}\n"

    try:
        with open(log_file_path, 'a') as log_file:
            log_file.write(log_entry)
    except IOError as e:
        return f"Error writing to log file: {e}", 500

    return redirect('https://www.example.com/verification_page')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)