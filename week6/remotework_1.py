"""
응용 프로그래밍 - 출장 업무 지원 프로그램
    1. 출장용으로 지급된 컴퓨터 상태 체크
"""

import platform
import os
import psutil
import datetime

# 1) 운영 체제 정보
print("Operating System:", platform.system())
print("OS Version:", platform.version())
print("Processor:", platform.processor())
print("Machine:", platform.machine())

# 2) 현재 디렉터리와 환경 변수 확인
print("Current Directory:", os.getcwd()) # current working directory
print("Environment Variables: os.environ")

# 3) CPU 정보
print("CPU Count (Logical):", psutil.cpu_count(logical=True))
print("CPU Usage (%):", psutil.cpu_percent(interval=1))

# 3) 메모리 정보
memory_info = psutil.virtual_memory()
print("Total Memory (GB):", memory_info.total / (1024 ** 3))
print("Memory Usage (%):", memory_info.percent)

# 3) 디스크 정보
disk_info = psutil.disk_usage('/')
print("Total Disk Space (GB):", disk_info.total / (1024 ** 3))
print("Disk Usage (%):", disk_info.percent)

# 4) 네트워크 정보
net_io = psutil.net_io_counters()
print("Bytes Sent:", net_io.bytes_sent)
print("Bytes Received:", net_io.bytes_recv)

