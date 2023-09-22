import cv2
import mediapipe as mp
cam=cv2.VideoCapture(0)#may have multiple cameras just want the first one
face_mesh=mp.solutions.face_mesh.FaceMesh()

while True:
    _,frame=cam.read()
    #just to detect face 
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output=face_mesh.process(rgb_frame)
    
    #creates lots of points
    landmark_points=output.multi_face_landmarks
    print(landmark_points)
    cv2.imshow("eye controlled mouse",frame)
    cv2.waitKey(1)