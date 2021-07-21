import requests
from datetime import datetime

class Network:
    url = "http://192.168.1.99/ipnc/"

    def send_message(self, command):
        response = requests.post(self.url, headers={
            'Content-Type': "text/plain"
        }, json={
            'header': {
                'version': 101,
                'seq': 0,
                'peer_type': 4001,
                'local_version': 0,
                'peer_id': 'ffffffffffffffff0000000000000001',
                'session_id': '61333639643236302D653935372D3131',
                'tt': datetime.now().strftime("%Y%m%d%H%M%S"),
                'cc': '61a3e9b2a540a0f261d986ce4fea9fefdc4c6087'},
            'body': {
                'cmd': 1027,
                'channel': 0,
                'control': command,
                'pan_speed': 5,
                'tilt_speed': 50,
                'zoom_speed': 30
            }
        })
