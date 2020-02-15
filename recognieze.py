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
            grayScale = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            blue, green, red = cv2.split(img)

            edgeDet = cv2.Canny(img, 100, 200)
            status, mask = cv2.threshold(grayScale, 100, 200, 0)
            # imgAnd = cv2.bitwise_and(img, img, mask=mask)

            contour, hierarchy = cv2.findContours(edgeDet, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            cv2.drawContours(img, contour, -1, (0, 255, 0), 3)
            cv2.imshow('webcam', img)
            cv2.imshow('mask', mask)
            # cv2.imshow('blue', blue)
            cv2.imshow('edgeDet', edgeDet)

            if cv2.waitKey(16) & 0xFF == ord('q'):
                runFlag = False

    else:
        print('capture can\'t be opened')

    capture.release()
    cv2.destroyAllWindows()
