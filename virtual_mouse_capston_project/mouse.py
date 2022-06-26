from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import mediapipe as mp
import pyautogui
import mouse
from pynput.mouse import Button, Controller

mouse1 = Controller()
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
            frame, results = self.detectHandsLandmarks(frame, hands_videos, display=False)

            # Check if the hands landmarks in the frame are detected.
            if results.multi_hand_landmarks:
                frame, fingers_statuses, count = self.countFingers(frame, results,display=False)
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
                elif (cc2[0] == 1 and cc2[1] == 0 and yy[0] ==False and yy[1] == True and yy[2] == False and yy[3] == False and yy[4] == False):
                    pyautogui.moveTo(1250, 1)
                    mouse1.click(Button.left, 2)


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

#class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1054, 633)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(720, 60, 171, 221))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(500, 120, 291, 111))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(520, 300, 211, 111))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(120, 300, 171, 111))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(40, 120, 391, 111))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(230, 480, 341, 111))
        self.label_8.setObjectName("label_8")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(290, 90, 171, 181))
        self.label_5.setObjectName("label_5")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(500, 440, 161, 201))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(720, 290, 171, 191))
        self.label_10.setObjectName("label_10")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(290, 290, 181, 181))
        self.label_4.setObjectName("label_4")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(360, -40, 661, 151))
        self.label_11.setObjectName("label_11")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(850, 540, 101, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.start_camera)

    def start_camera(self):
        #self.obj1 = hand_detect()
        self.main()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Virtual Mouse"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/newPrefix6/up.png\"/></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Cursor Up Shift </span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Right Shift</span></p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Left Shift </span></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Cursor Right Shift </span></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Cursor Down Shift </span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/newPrefix1/right_shif.png\"/></p></body></html>"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/newPrefix3/down.png\"/></p></body></html>"))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/newPrefix23/right_click.png\"/></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/newPrefixlc/left.png\"/></p></body></html>"))
        self.label_11.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; color:#ff0000;\">Virtual Mouse Gestures</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Start Gesture"))

import down_rc
import gesture_rc
import leftc_rc
import ls_rc
import up_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui= hand_detect()
    #ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


