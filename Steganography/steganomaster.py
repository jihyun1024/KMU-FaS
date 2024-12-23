import os
from PIL import Image


startFlag = '(#*CEVAP*#)'
endFlag = '(#*BUREK*#)'
passwordStartFlag = '[!$'
passwordEndFlag = '$!]'


# 픽셀의 RGB로부터 아스키코드표의 정수 값을 한 자리씩 받아 아스키코드 문자로 리턴
def decode_pixel(pixel):
    red, green, blue = pixel
    character_ascii = ((red % 10) * 100) + ((green % 10) * 10) + (blue % 10)
    return chr(character_ascii)


# 이미지에서 메시지가 은닉되어 있는지, 패스워드가 있는지 탐색
# 패스워드를 따로 설정한 경우, 패스워드가 맞는지 체크
def check(image, password):
    read_password = False
    encoded_password = ''
    message = ''
    char_counter = 1
    width, height = image.size

    for i in range(width):
        for j in range(height):
            pixel = image.getpixel((i, j))
            character = decode_pixel(pixel)
            message += character

            if char_counter == len(startFlag) and message != startFlag:
                return '[Error] Photo is not encoded'
            if read_password:
                encoded_password += character
                if encoded_password.endswith(passwordEndFlag):
                    encoded_password = encoded_password.replace(passwordEndFlag, '')
                    if encoded_password == password:
                        return '[Status] Password Matched'
                    else:
                        return '[Error] Wrong password'
                    
            if char_counter == len(startFlag) + len(password):
                if message.endswith(passwordStartFlag):
                    read_password = True
                else:
                    return '[Status] Photo is encoded'
                
            char_counter += 1
    
    return None


# parameter로 받은 이미지에서 은닉된 메시지를 반환
def decode_message(image, password):
    decoded_status = check(image, password)
    if (decoded_status == '[Error] Wrong password'):
        return '[Error] Incorrect password'
    
    # 처음 메시지를 저장할 변수는 비어 있음 (나중에 하나씩 더할 것)
    message = ''
    char_counter = 1

    # skip_length: 메시지를 디코딩할 때 건너뛰어야 하는 문자의 수
    if password:
        skip_length = len(startFlag) + len(passwordStartFlag) + len(password) + len(passwordEndFlag)
    else:
        skip_length = len(startFlag)

    width, height = image.size

    for i in range(width):
        for j in range(height):
            pixel = image.getpixel((i, j))
            character = decode_pixel(pixel)
            if char_counter > skip_length:
                message += character
            if message.endswith(endFlag):
                return message.replace(endFlag, '')
            char_counter += 1
    
    # 반복문을 돌렸는데도 아무것도 안 나온 경우
    return '[Error] No message found'


if __name__ == '__main__':
    # 파일 경로 입력 + 작업 디렉토리 변경
    filepath = input('Enter file path: ')
    os.chdir(filepath)

    # 파일 이름 입력 with png 확장자
    filename = input('Enter image name with .png: ')
    path = os.getcwd() + '/' + filename

    # 패스워드 입력
    password = input('Enter password to decode: ')
    image = Image.open(path)
    print(decode_message(image, password))