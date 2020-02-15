import cv2

if __name__ == '__main__':
    window = cv2.namedWindow('webcam')
    capture = cv2.VideoCapture()
    capture.open(0)

    if capture.isOpened:
        print('capture is opened')
        runFlag = True

        while runFlag:
            status, img = capture.read()
            cv2.imshow('webcam', img)

            if cv2.waitKey(16) & 0xFF == ord('q'):
                runFlag = False

    else:
        print('capture can\'t be opened')

    capture.release()
    cv2.destroyAllWindows()
