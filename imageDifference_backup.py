import cv2
import numpy as np
from firebase import firebase
import time
#change the website in the bracket down below
cap = cv2.VideoCapture('https://192.168.0.102:8080/video')


dim_120 = (120, 120)   #around 1 board

dim_130 = (130, 130)

# read the image as gray, and set it as template for all characters
# for character F, normal and cropped with different sizes(75x75;90x90;100x100)
template_F = cv2.imread('F_copy.jpg', cv2.IMREAD_GRAYSCALE)
template_F_crop = cv2.imread('crop_F.jpg', cv2.IMREAD_GRAYSCALE)
#cap = cv2.VideoCapture('https://192.168.0.102:8080/video')
#cap = cv2.VideoCapture('https://192.168.1.38:8080/video')
cap = cv2.VideoCapture(0)
resized_F120 = cv2.resize(template_F, dim_120, interpolation=cv2.INTER_AREA)
resized_F120_crop = cv2.resize(template_F_crop, dim_120, interpolation=cv2.INTER_AREA)

resized_F130 = cv2.resize(template_F, dim_130, interpolation=cv2.INTER_AREA)
resized_F130_crop = cv2.resize(template_F_crop, dim_130, interpolation=cv2.INTER_AREA)

# for character B
template_B = cv2.imread('B_copy.jpg', cv2.IMREAD_GRAYSCALE)
template_B_crop = cv2.imread('crop_B.jpg', cv2.IMREAD_GRAYSCALE)

resized_B120 = cv2.resize(template_B, dim_120, interpolation=cv2.INTER_AREA)
resized_B120_crop = cv2.resize(template_B_crop, dim_120, interpolation=cv2.INTER_AREA)

resized_B130 = cv2.resize(template_B, dim_130, interpolation=cv2.INTER_AREA)
resized_B130_crop = cv2.resize(template_B_crop, dim_130, interpolation=cv2.INTER_AREA)

# for character L
template_L = cv2.imread('L_copy.jpg', cv2.IMREAD_GRAYSCALE)
template_L_crop = cv2.imread('crop_L.jpg', cv2.IMREAD_GRAYSCALE)

resized_L120 = cv2.resize(template_L, dim_120, interpolation=cv2.INTER_AREA)
resized_L120_crop = cv2.resize(template_L_crop, dim_120, interpolation=cv2.INTER_AREA)

resized_L130 = cv2.resize(template_L, dim_130, interpolation=cv2.INTER_AREA)
resized_L130_crop = cv2.resize(template_L_crop, dim_130, interpolation=cv2.INTER_AREA)

# for character R
template_R = cv2.imread('R_copy.jpg', cv2.IMREAD_GRAYSCALE)
template_R_crop = cv2.imread('crop_R.jpg', cv2.IMREAD_GRAYSCALE)

resized_R120 = cv2.resize(template_R, dim_120, interpolation=cv2.INTER_AREA)
resized_R120_crop = cv2.resize(template_R_crop, dim_120, interpolation=cv2.INTER_AREA)

resized_R130 = cv2.resize(template_R, dim_130, interpolation=cv2.INTER_AREA)
resized_R130_crop = cv2.resize(template_R_crop, dim_130, interpolation=cv2.INTER_AREA)

# for character S
template_S = cv2.imread('S_copy.jpg', cv2.IMREAD_GRAYSCALE)
template_S_crop = cv2.imread('crop_S.jpg', cv2.IMREAD_GRAYSCALE)

resized_S120 = cv2.resize(template_S, dim_120, interpolation=cv2.INTER_AREA)
resized_S120_crop = cv2.resize(template_S_crop, dim_120, interpolation=cv2.INTER_AREA)

resized_S130 = cv2.resize(template_S, dim_130, interpolation=cv2.INTER_AREA)
resized_S130_crop = cv2.resize(template_S_crop, dim_130, interpolation=cv2.INTER_AREA)

# for firebase
fb = firebase.FirebaseApplication('https://ai-camera-5f64e.firebaseio.com/', None)

x = 0
while True:
    _, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.rectangle(gray_frame, (220, 200), (380, 350), (255, 255, 255), 5)

    result_F1 = cv2.matchTemplate(gray_frame, resized_F120, cv2.TM_CCOEFF_NORMED)
    loc_F1 = np.where(result_F1 >= 0.7)
    result_F2 = cv2.matchTemplate(gray_frame, resized_F120_crop, cv2.TM_CCOEFF_NORMED)
    loc_F2 = np.where(result_F2 >= 0.7)
    result_F3 = cv2.matchTemplate(gray_frame, resized_F130, cv2.TM_CCOEFF_NORMED)
    loc_F3 = np.where(result_F3 >= 0.7)
    result_F4 = cv2.matchTemplate(gray_frame, resized_F130_crop, cv2.TM_CCOEFF_NORMED)
    loc_F4 = np.where(result_F4 >= 0.7)

    result_B1 = cv2.matchTemplate(gray_frame, resized_B120, cv2.TM_CCOEFF_NORMED)
    loc_B1 = np.where(result_B1 >= 0.65)
    result_B2 = cv2.matchTemplate(gray_frame, resized_B120_crop, cv2.TM_CCOEFF_NORMED)
    loc_B2 = np.where(result_B2 >= 0.65)
    result_B3 = cv2.matchTemplate(gray_frame, resized_B130, cv2.TM_CCOEFF_NORMED)
    loc_B3 = np.where(result_B3 >= 0.7)
    result_B4 = cv2.matchTemplate(gray_frame, resized_B130_crop, cv2.TM_CCOEFF_NORMED)
    loc_B4 = np.where(result_B4 >= 0.65)

    result_L1 = cv2.matchTemplate(gray_frame, resized_L120, cv2.TM_CCOEFF_NORMED)
    loc_L1 = np.where(result_L1 >= 0.8)
    result_L2 = cv2.matchTemplate(gray_frame, resized_L120_crop, cv2.TM_CCOEFF_NORMED)
    loc_L2 = np.where(result_L2 >= 0.8)
    result_L3 = cv2.matchTemplate(gray_frame, resized_L130, cv2.TM_CCOEFF_NORMED)
    loc_L3 = np.where(result_L3 >= 0.8)
    result_L4 = cv2.matchTemplate(gray_frame, resized_L130_crop, cv2.TM_CCOEFF_NORMED)
    loc_L4 = np.where(result_L4 >= 0.8)

    result_R1 = cv2.matchTemplate(gray_frame, resized_R120, cv2.TM_CCOEFF_NORMED)
    loc_R1 = np.where(result_R1 >= 0.65)
    result_R2 = cv2.matchTemplate(gray_frame, resized_R120_crop, cv2.TM_CCOEFF_NORMED)
    loc_R2 = np.where(result_R2 >= 0.65)
    result_R3 = cv2.matchTemplate(gray_frame, resized_R130, cv2.TM_CCOEFF_NORMED)
    loc_R3 = np.where(result_R3 >= 0.65)
    result_R4 = cv2.matchTemplate(gray_frame, resized_R130_crop, cv2.TM_CCOEFF_NORMED)
    loc_R4 = np.where(result_R4 >= 0.65)

    result_S1 = cv2.matchTemplate(gray_frame, resized_S120, cv2.TM_CCOEFF_NORMED)
    loc_S1 = np.where(result_S1 >= 0.6)
    result_S2 = cv2.matchTemplate(gray_frame, resized_S120_crop, cv2.TM_CCOEFF_NORMED)
    loc_S2 = np.where(result_S2 >= 0.6)
    result_S3 = cv2.matchTemplate(gray_frame, resized_S130, cv2.TM_CCOEFF_NORMED)
    loc_S3 = np.where(result_S3 >= 0.6)
    result_S4 = cv2.matchTemplate(gray_frame, resized_S130_crop, cv2.TM_CCOEFF_NORMED)
    loc_S4 = np.where(result_S4 >= 0.6)

    for pt in zip(*loc_F1[::-1]):  # F100
        if x != 'F':
            fb.put('Recognized_letter', 'character', 'F')
        x = 'F'
    """for pt in zip(*loc_F2[::-1]):  # F100_crop
        if x != 'F':
            fb.put('Recognized_letter', 'character', 'F')
        x = 'F'
    """
    for pt in zip(*loc_F3[::-1]):  # F100
        if x != 'F':
            fb.put('Recognized_letter', 'character', 'F')
        x = 'F'
    """for pt in zip(*loc_F4[::-1]):  # F90_crop
        if x != 'F':
            fb.put('Recognized_letter', 'character', 'F')
        x = 'F'
    """
    for pt in zip(*loc_B1[::-1]):
        if x != 'B':
            fb.put('Recognized_letter', 'character', 'B')
        x = 'B'
    for pt in zip(*loc_B2[::-1]):
        if x != 'B':
            fb.put('Recognized_letter', 'character', 'B')
        x = 'B'
    for pt in zip(*loc_B3[::-1]):
        if x != 'B':
            fb.put('Recognized_letter', 'character', 'B')
        x = 'B'
    for pt in zip(*loc_B4[::-1]):
        if x != 'B':
            fb.put('Recognized_letter', 'character', 'B')
        x = 'B'

    for pt in zip(*loc_L1[::-1]):
        if x != 'L':
            fb.put('Recognized_letter', 'character', 'L')
        x = 'L'
    for pt in zip(*loc_L2[::-1]):
        if x != 'L':
            fb.put('Recognized_letter', 'character', 'L')
        x = 'L'
    for pt in zip(*loc_L3[::-1]):
        if x != 'L':
            fb.put('Recognized_letter', 'character', 'L')
        x = 'L'
    for pt in zip(*loc_L4[::-1]):
        if x != 'L':
            fb.put('Recognized_letter', 'character', 'L')
        x = 'L'

    for pt in zip(*loc_R1[::-1]):
        if x != 'R':
            fb.put('Recognized_letter', 'character', 'R')
        x = 'R'
    for pt in zip(*loc_R2[::-1]):
        if x != 'R':
            fb.put('Recognized_letter', 'character', 'R')
        x = 'R'
    for pt in zip(*loc_R3[::-1]):
        if x != 'R':
            fb.put('Recognized_letter', 'character', 'R')
        x = 'R'
    for pt in zip(*loc_R4[::-1]):
        if x != 'R':
            fb.put('Recognized_letter', 'character', 'R')
        x = 'R'

    for pt in zip(*loc_S1[::-1]):
        if x != 'S':
            fb.put('Recognized_letter', 'character', 'S')
        x = 'S'
    for pt in zip(*loc_S2[::-1]):
        if x != 'S':
            fb.put('Recognized_letter', 'character', 'S')
        x = 'S'
    for pt in zip(*loc_S3[::-1]):
        if x != 'S':
            fb.put('Recognized_letter', 'character', 'S')
        x = 'S'
    for pt in zip(*loc_S4[::-1]):
        if x != 'S':
            fb.put('Recognized_letter', 'character', 'S')
        x = 'S'

    print(x)
    cv2.imshow("Frame", gray_frame)
    cv2.imshow("F", resized_F130_crop)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()

"""
firebase = firebase.FirebaseApplication('https://ai-camera-5f64e.firebaseio.com/', None)

result = firebase.put('Recognized_letter', 'character', 'F')
#result = firebase.get('Recognized_letter/character', '')
print(result)

fb = firebase.FirebaseApplication("https://ai-camera-5f64e.firebaseio.com/", None)

data = {
    'character':''
}

#result = fb.put('Recognized_letter', 'character', 'S')
result = fb.get('Recognized_letter/character', '')
print(result)

"""
