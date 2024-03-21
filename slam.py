import cv2

cap = cv2.VideoCapture("./test_countryroad.mp4")

if not cap.isOpened():
    print("Cannot open Video.")

while True:
    pass