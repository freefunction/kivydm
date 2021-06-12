import cv2
import mediapipe as mp
import time



def faced(cap):
    mpFaceDetection = mp.solutions.face_detection
    faceDetection = mpFaceDetection.FaceDetection(0.5)
    mpDraw = mp.solutions.drawing_utils

    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)
    if results.detections:
        for id, detection in enumerate(results.detections):
            #mpDraw.draw_detection(img, detection)
            h, w, c = img.shape
            bboxC = detection.location_data.relative_bounding_box
            bbox = int(bboxC.xmin * w),int(bboxC.ymin * h),\
                       int(bboxC.width * w),int(bboxC.height * h)
            cv2.rectangle(img,bbox, (255, 0, 255), 2)
            cv2.putText(img,f'{int(detection.score[0]*100)}%', (bbox[0], bbox[1]-15), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 2)
            # print(id, detection)
            # print(detection.score)
            #print(detection.location_data.relative_bounding_box)

    #cv2.imshow("Image", img)
    #print(type(img))
    #cv2.waitKey(20)
    return img
