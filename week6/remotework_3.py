"""
응용 프로그래밍 - 출장 업무 지원 프로그램
    3. 회의록 음성 변환
"""

import pyttsx3

# 텍스트를 음성으로 변환하는 함수
def text_to_speech(text):
    print("텍스트를 음성으로 변환 중...")
    try:
        engine = pyttsx3.init() # pyttsx3 엔진 초기화
        engine.say(text)
        engine.runAndWait()
        print(f"텍스트 '{text}'가 음성으로 출력되었습니다.")
    except Exception as e:
        print(f"텍스트 음성 변환 중 오류 발생: {e}")

if __name__ == "__main__":
    text = input("음성으로 변환할 텍스트를 입력하세요: ")
    text_to_speech(text)