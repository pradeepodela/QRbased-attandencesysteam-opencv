from pyzbar.pyzbar import decode
import numpy as np
import cv2
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)

authorised = []


classmates = {
    "11111":"pradeep",
    "11112":"vishnu",
    "11113":"rahul",
    "11114":"jagu",
    "11115":"chotobheem"

}

while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))

    for barcode in decode(img):
        ###GETTING THE DATA######
        my_data = barcode.data.decode('utf-8')

        ##### GETTING THE POINTS#####
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))

        ######PRINTING THE DATA####
        pts2 = barcode.rect

        if my_data in classmates:
            pnt = classmates.get(my_data)
            print(my_data, pnt, "authorised")
            cv2.putText(img, "authorised", (pts2[0], pts2[1]), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 128, 0), 2)
            ####### PLOTING THE POLYGEN####
            cv2.polylines(img, [pts], True, (0, 0, 0), 3)
        else:
            print(my_data, "un-authorised")
            cv2.putText(img, "un-authorised", (pts2[0], pts2[1]), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255), 2)
            ####### PLOTING THE POLYGEN####
            cv2.polylines(img, [pts], True, (0,0,0), 3)


    cv2.imshow("Result", img)

    cv2.waitKey(1)



