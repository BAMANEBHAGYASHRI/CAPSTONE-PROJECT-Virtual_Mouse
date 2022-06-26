import cv2
import time
import numpy as np
import mediapipe as mp
from gui1 import *
import pyautogui
import mouse

camera_video = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5)
hands_videos = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils
mp=35
mp1=30
mp2=mp1
class hand_detect:
    def detectHandsLandmarks(self, image, hands, draw=True, display=True):
        output_image = image.copy()
        imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
        if results.multi_hand_landmarks and draw:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image=output_image, landmark_list=hand_landmarks,
                                          connections=mp_hands.HAND_CONNECTIONS,

                                          landmark_drawing_spec=mp_drawing.DrawingSpec(color=(255, 255, 255),
                                                                                       thickness=2, circle_radius=2),
                                          connection_drawing_spec=mp_drawing.DrawingSpec(color=(255, 0, 0),
                                                                                      thickness=2, circle_radius=2))

        return output_image, results

    def countFingers(self, image, results,  draw=True, display=True):
        height, width, _ = image.shape
        output_image = image.copy()


        count = {'RIGHT': 0, 'LEFT': 0}

        # Store the indexes of the tips landmarks of each finger of a hand in a list.
        fingers_tips_ids = [mp_hands.HandLandmark.INDEX_FINGER_TIP, mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
                            mp_hands.HandLandmark.RING_FINGER_TIP, mp_hands.HandLandmark.PINKY_TIP]

        fingers_statuses = {'RIGHT_THUMB': False, 'RIGHT_INDEX': False, 'RIGHT_MIDDLE': False, 'RIGHT_RING': False,
                            'RIGHT_PINKY': False, 'LEFT_THUMB': False, 'LEFT_INDEX': False, 'LEFT_MIDDLE': False,
                            'LEFT_RING': False, 'LEFT_PINKY': False}

        for hand_index, hand_info in enumerate(results.multi_handedness):
            hand_label = hand_info.classification[0].label


            hand_landmarks = results.multi_hand_landmarks[hand_index] #ladnmark recheck from hand

            for tip_index in fingers_tips_ids:

                # Retrieve the label (i.e., index, middle, etc.) of the finger on which we are iterating upon.
                finger_name = tip_index.name.split("_")[0]

                if (hand_landmarks.landmark[tip_index].y < hand_landmarks.landmark[tip_index-2].y):
                    fingers_statuses[hand_label.upper() + "_" + finger_name] = True

                    # Increment the count of the fingers up of the hand by 1.
                    count[hand_label.upper()] += 1

            # Retrieve the y-coordinates of the tip and mcp landmarks of the thumb of the hand.
            thumb_tip_x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x
            thumb_mcp_x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP - 2].x

            # Check if the thumb is up by comparing the hand label and the x-coordinates of the retrieved landmarks.
            if (hand_label == 'Right' and (thumb_tip_x < thumb_mcp_x)) or (
                    hand_label == 'Left' and (thumb_tip_x > thumb_mcp_x)):
                # Update the status of the thumb in the dictionary to true.
                fingers_statuses[hand_label.upper() + "_THUMB"] = True

                # Increment the count of the fingers up of the hand by 1.
                count[hand_label.upper()] += 1
        if draw:
            mp=35
            xx = list(fingers_statuses.keys())
            yy = list(fingers_statuses.values())
            cc2 = list(count.values())
            if (cc2[0] >= 0 and cc2[1] == 0 and xx[1] == 'RIGHT_INDEX' and xx[2] == 'RIGHT_MIDDLE' and yy[0] == False and yy[1] == True and yy[2] == True and yy[3] == False and yy[4] == False):
                pyautogui.moveTo(mp, 25)
                mp = mp + 20
                print(mp)
        if draw:
            cv2.putText(output_image, " Total Fingers: ", (10, 25), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
            cv2.putText(output_image, str(sum(count.values())), (width // 2 - 150, 140), cv2.FONT_HERSHEY_SIMPLEX,
                        5, (0, 0, 255),10, 10)
        return output_image, fingers_statuses, count
    def main(self):
        global mp,mp1,mp2,mp3, mp4
        cv2.namedWindow('Fingers Counter', cv2.WINDOW_NORMAL)
        while camera_video.isOpened():
            ok, frame = camera_video.read()
            if not ok:
                continue

            frame = cv2.flip(frame, 1)
            frame, results = obj1.detectHandsLandmarks(frame, hands_videos, display=False)

            # Check if the hands landmarks in the frame are detected.
            if results.multi_hand_landmarks:
                frame, fingers_statuses, count = obj1.countFingers(frame, results,display=False)
                xx = list(fingers_statuses.keys())
                yy = list(fingers_statuses.values())
                cc2 = list(count.values())
                #print(cc2, xx,yy)
                if (cc2[0] >= 0 and cc2[1] == 0 and xx[1] == 'RIGHT_INDEX' and xx[2] == 'RIGHT_MIDDLE' and yy[0] == False and yy[1] == True and yy[2] == True and yy[3] == False and yy[4] == False):
                    for m in range(mp,mp+20):
                        if(mp< 1700):
                            pyautogui.moveTo(mp,mp1)
                            mp = mp + 20
                            print(mp)

                elif (cc2[0] == 3 and cc2[1] == 0 and xx[0] == 'RIGHT_THUMB' and xx[1] == 'RIGHT_INDEX' and xx[2] == 'RIGHT_MIDDLE' and yy[0] == True and yy[1] == True and yy[2] == True and yy[3] == False and yy[4] == False):
                    if(mp1<900):
                        for n in range(mp,mp1+mp):
                            pyautogui.moveTo(mp,mp1)
                            mp1 = mp1 + 20
                            print(mp1)
                            break
                elif (cc2[0] == 2 and cc2[1] == 0 and xx[0] == 'RIGHT_THUMB' and xx[1] == 'RIGHT_INDEX' and xx[2] == 'RIGHT_MIDDLE' and yy[0] == False and yy[1] == True and yy[2] == False and yy[3] == False and yy[4] == True):
                    mouse.double_click('left')


                elif (cc2[0] == 2 and cc2[1] == 0 and xx[0] == 'RIGHT_THUMB' and xx[1] == 'RIGHT_INDEX' and xx[2] == 'RIGHT_MIDDLE' and yy[0] == True and yy[1] == True and yy[2] == False and yy[3] == False and yy[4] == False):
                    print(mp, mp1)
                    if(mp> mp1):
                        for o in range(mp, mp1,-25):
                            print(mp, mp1)
                            pyautogui.moveTo(mp,o)
                            mp = mp - 20
                            print(mp)
                            break
                    elif(mp< mp1):
                        for o in range(mp, mp1):
                                #print(mp, mp1 + mp)
                            pyautogui.moveTo(o,mp1)
                            mp1 = mp1 - 20
                            print(mp1)
                            break
                elif (cc2[0] == 5 and cc2[1] == 0 ):
                    print("right click")
                    mouse.click('right')
                elif (cc2[0] == 4 and cc2[1] == 0 ):
                    print("left click")
                    mouse.click('left')


                #print(mp,mp1,mp2)
            cv2.imshow('Fingers Counter', frame)
            k = cv2.waitKey(1) & 0xFF
            if (k == 27):
                break
        camera_video.release()
        cv2.destroyAllWindows()

if (__name__ == "__main__"):

    #obj1 = hand_detect()
    #obj1.main()
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

    
