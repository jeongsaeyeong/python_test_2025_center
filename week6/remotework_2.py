"""
응용 프로그래밍 - 출장 업무 지원 프로그램
    2. IP 확인 및 QR 코드로 회의 정보 공유
"""

import socket
import requests
import qrcode

# 1) 내부 및 외부 IP 확인 함수
def get_ip_info():
    print("IP 정보 확인 중...")
    try:
        # 내부 IP 확인
        internal_ip = socket.gethostbyname(socket.gethostname())
        
        # 외부 IP 확인
        external_ip = requests.get('https://api64.ipify.org?format=json').json()["ip"]
        
        print(f"내부 IP 주소: {internal_ip}")
        print(f"외부 IP 주소: {external_ip}")
    except Exception as e:
        print(f"IP 정보를 확인하는 중 오류 발생: {e}")

# 2) QR 코드 생성 함수
def generate_qr_code(url, data):
    print("QR 코드 생성 중...")
    try:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)
        
        img = qr.make_image(fill='black', back_color='white')
        img.save(f'{data}.png')
        print(f"QR 코드가 '{data}.png'으로 저장되었습니다.")
    except Exception as e:
        print(f"QR 코드를 생성하는 중 오류 발생: {e}")

if __name__ == "__main__":
    get_ip_info()
    generate_qr_code("https://yukingx.github.io/", "QR_meeting")