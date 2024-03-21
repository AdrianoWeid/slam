#!/usr/bin/env python3
import cv2
import sdl2
import sdl2.ext
sdl2.ext.init()

W = 1920//2
H = 1080//2

window = sdl2.ext.Window("PySDL2", (W,H))



if __name__ == "__main__":
    cap = cv2.VideoCapture("./test_countryroad.mp4")

    if not cap.isOpened():
        print("Cannot ope Video.")

    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, (540, 380), fx=0, fy=0, interpolation=cv2.INTER_LINEAR)
        if not ret:
            print("Can't receive frame (stream end?). Exiting...")
            break
    
        cv2.imshow("Frame", frame)
    
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()