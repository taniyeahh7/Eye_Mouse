import cv2
import mediapipe as mp
import pyautogui

cam=cv2.VideoCapture(0)#may have multiple cameras just want the first one
face_mesh=mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)#refine landmarks dfualt value=False
screen_w,screen_h=pyautogui.size()


while True:
    _,frame=cam.read()
    frame=cv2.flip(frame,1)#to flip the image
    #just to detect face 
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output=face_mesh.process(rgb_frame)
    #creates lots of points
    landmark_points=output.multi_face_landmarks
    frame_h,frame_w,_=frame.shape#tells the width height and width
    if landmark_points:
        landmarks=landmark_points[0].landmark
        for id,landmark in enumerate(landmarks[474:478]):#need to define range of index #to get the index also
            #detects one of the eyes
            #going to draw need to get the coordinates
            x=int(landmark.x*frame_w)#has x y and z
            y=int(landmark.y*frame_h)
            cv2.circle(frame,(x,y),3,(0,255,0))#makes all circles for landmarks
            # z=landmark.z
            if id==1:
                screen_x=screen_w/frame_w*x
                screen_y=screen_h/frame_h*y
                pyautogui.moveTo(screen_x,screen_y)
        left=[landmarks[145],landmarks[159]]#there are different      
        #need right ot move and left to click and need any two landmarks
        for landmark in left:
            x=int(landmark.x*frame_w)#has x y and z
            y=int(landmark.y*frame_h)
            cv2.circle(frame,(x,y),3,(0,255,255))
        # print(left[0].y-left[1].y)
        #if very close the eye is closed 
        #0.002 or something means eye closed
        if((left[0].y-left[1].y)):
            # print('click')
            pyautogui.click()
            pyautogui.sleep(1)
    print(landmark_points)
    cv2.imshow("eye controlled mouse",frame)
    cv2.waitKey(1)