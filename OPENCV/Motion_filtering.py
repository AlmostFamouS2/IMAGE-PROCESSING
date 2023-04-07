import cv2 as cv
import time

def all():
    video = cv.VideoCapture('PEOPLE.mp4')
    print(video)
    subtractor = cv.createBackgroundSubtractorMOG2(20, 50)

    while 1:
        ret, frame = video.read()
    
        if ret:  # Se ainda tiver algum frame para renderizar
            mask = subtractor.apply(frame)
            cv.imshow('Mask', mask)
        
            if cv.waitKey(5) == ord('x'):
                break
        else:
            video = cv.VideoCapture('PEOPLE.mp4')  # Restart the whole thing from beginning

        time.sleep(0.09)

    cv.destroyAllWindows()
    video.release()

print('OK')
if __name__ == '__main__':
    all()