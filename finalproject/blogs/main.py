import cv2
import mediapipe as mp
import numpy as np
from django.http import HttpResponse


mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
def ttt(request):
    return HttpResponse("Yowww")

#ลงไป คือคำนวณองศาของแต่ละส่วน
def calculate_angle(a, b, c):
    a = np.array(a)  # First
    b = np.array(b)  # Mid
    c = np.array(c)  # End

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return int(angle)


def calculate_angler(d, e, f):
    d = np.array(d)  # First
    e = np.array(e)  # Mid
    f = np.array(f)  # End

    radians2 = np.arctan2(f[1] - e[1], f[0] - e[0]) - np.arctan2(d[1] - e[1], d[0] - e[0])
    angler = np.abs(radians2 * 180.0 / np.pi)

    if angler > 180.0:
        angler = 360 - angler

    return int(angler)

def calculate_anglekneeleft(a, b, c):
    a = np.array(a)  # First
    b = np.array(b)  # Mid
    c = np.array(c)  # End

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    anglekneeleft = np.abs(radians * 180.0 / np.pi)

    if anglekneeleft > 180.0:
        anglekneeleft = 360 - anglekneeleft

    return int(anglekneeleft)

def calculate_anglekneeright(a, b, c):
    a = np.array(a)  # First
    b = np.array(b)  # Mid
    c = np.array(c)  # End

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    anglekneeright = np.abs(radians * 180.0 / np.pi)

    if anglekneeright > 180.0:
        anglekneeright = 360 - anglekneeright

    return int(anglekneeright)

def calculate_anglehip(a, b, c):
    a = np.array(a)  # First
    b = np.array(b)  # Mid
    c = np.array(c)  # End

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    anglehip = np.abs(radians * 180.0 / np.pi)

    if anglehip > 180.0:
        anglehip = 360 - anglehip

    return int(anglehip)

def calculate_anglehipr(a, b, c):
    a = np.array(a)  # First
    b = np.array(b)  # Mid
    c = np.array(c)  # End

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    anglehipr = np.abs(radians * 180.0 / np.pi)

    if anglehipr > 180.0:
        anglehipr = 360 - anglehipr

    return int(anglehipr)


#รับค่ามาจาก view.py
def AnalysVideo(change, content): # ชื่อวิดีโอ, pathวิดีโอ
    cap = cv2.VideoCapture(content)
    print(content)
    counter = 0
    stage = None
    #เช็คแบบรวม
    checkdeadliftfontred = 0
    checkdeadliftrightred = 0

    checkbenchpresstopred = 0
    checkbenchpressleftred = 0

    checklatpulldownbackred = 0
    checklatpulldownrightred = 0

    checkdeadliftfontgreen = 0
    checkdeadliftrightgreen = 0

    checkbenchpresstopgreen = 0
    checkbenchpressleftgreen = 0

    checklatpulldownbackgreen = 0
    checklatpulldownrightgreen = 0


    #เก็บแบบละเอียดทุกจุดที่ใช้วิเคราะห์

    sumarmrightred = 0
    sumarmrightgreen = 0
    sumarmleftred = 0
    sumarmleftgreen = 0


    sumarmleftred1 = 0
    sumarmleftgreen1 = 0


    sumarmleftred2 = 0
    sumarmleftgreen2 = 0
    sumarmrightred2 = 0
    sumarmrightgreen2 = 0

    sumkneeleftred2 = 0
    sumkneeleftgreen2 = 0
    sumkneerightred2 = 0
    sumkneerightgreen2 = 0


    sumarmrightred3 = 0
    sumkneerightred3 = 0

    sumarmrightgreen3 = 0
    sumkneerightgreen3 = 0

    sumhiprightred3 = 0
    sumhiprightgreen3 = 0


    sumarmrightred4 = 0
    sumarmrightgreen4 = 0
    sumarmleftred4 = 0
    sumarmleftgreen4 = 0


    sumarmrightred5 = 0
    sumarmrightgreen5 = 0
    sumhiprightred5 = 0
    sumhiprightgreen5 = 0

    average1 = 0
    average1_2 = 0
    average2 = 0
    average2_2 = 0
    average3 = 0
    average3_2 = 0

    averagebp1 = 0
    averagebp2 = 0
    averagebp3 = 0

    averagedl1 = 0
    averagedl2 = 0
    averagedl3 = 0
    averagedl4 = 0
    averagedl5 = 0
    averagedl6 = 0
    averagedl7 = 0

    averagelpd1 = 0
    averagelpd2 = 0
    averagelpd3 = 0
    averagelpd4 = 0

    ## Setup mediapipe instance
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            print("1")
            ret, frame = cap.read()
            if change == 'deadlift2_2':
                frame = cv2.resize(frame, (1080, 780))
            if change == 'deadlift_1':
                frame = cv2.resize(frame, (1080, 780))
            if change == 'benchpress2_wrong':
                frame = cv2.resize(frame, (1080, 780))
            if change == 'benchpress_wrong':
                frame = cv2.resize(frame, (1080, 780))
            if change == 'latpulldown':
                frame = cv2.resize(frame, (1080, 780))
            if change == 'latpulldown2_wrong':
                frame = cv2.resize(frame, (1080, 780))
            # Recolor image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            # Make detection
            results = pose.process(image)

            # Recolor back to BGR
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Extract landmarks
            try:
                landmarks = results.pose_landmarks.landmark

                # Get coordinates
                #LEFT
                shoulderl = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                            landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                elbowl = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                wristl = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

                kneel = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
                hipl = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                anklel = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]

                #RIGHT
                shoulderr = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                elbowr = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                wristr = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

                kneer = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                        landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
                hipr = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                        landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                ankler = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                        landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]
                if change == 'benchpress2_wrong': 
                    angler = calculate_angler(shoulderr, elbowr, wristr) #คำนวณองศา
                    cv2.putText(image, str(angler), #แสดงตัวเลขแบบเรียลไทม
                                tuple(np.multiply(elbowr, [1080, 780]).astype("int")),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA
                                )
                    # Calculate angle
                    angle = calculate_angle(shoulderl, elbowl, wristl)

                    # Visualize angle
                    cv2.putText(image, str(angle),
                                tuple(np.multiply(elbowl, [1080, 780]).astype(int)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA
                                )
                if change == 'benchpress_wrong':
                    angler = calculate_angler(shoulderr, elbowr, wristr)
                    cv2.putText(image, str(angler),
                                tuple(np.multiply(elbowr, [1280, 780]).astype("int")),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA
                                )
                    # Calculate angle
                    angle = calculate_angle(shoulderl, elbowl, wristl)

                    # Visualize angle
                    cv2.putText(image, str(angle),
                                tuple(np.multiply(elbowl, [1080, 780]).astype(int)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA
                                )

                if change == 'deadlift2_2':
                    angler = calculate_angler(shoulderr, elbowr, wristr)
                    cv2.putText(image, str(angler),
                                tuple(np.multiply(elbowr, [1080, 780]).astype("int")),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA
                                )
                    # Calculate angle
                    angle = calculate_angle(shoulderl, elbowl, wristl)

                    # Visualize angle
                    cv2.putText(image, str(angle),
                                tuple(np.multiply(elbowl, [1080, 780]).astype(int)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA
                                )
                    anglekneeleft = calculate_anglekneeleft(hipl, kneel, anklel)

                    cv2.putText(image, str(anglekneeleft),
                                tuple(np.multiply(kneel, [1080, 780]).astype("int")),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA
                                )

                    anglehip = calculate_anglehip(shoulderl, hipl, kneel)
                    cv2.putText(image, str(anglehip),
                                tuple(np.multiply(hipl, [1080, 780]).astype("int")),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA
                                )
                    anglekneeright = calculate_anglekneeright(hipr, kneer, ankler)

                    cv2.putText(image, str(anglekneeright),
                                tuple(np.multiply(kneer, [1080, 780]).astype("int")),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA
                                )

                    anglehipr = calculate_anglehip(shoulderr, hipr, kneer)
                    cv2.putText(image, str(anglehipr),
                                tuple(np.multiply(hipr, [1080, 780]).astype("int")),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA
                                )

                if change == 'deadlift_1':
                    angle = calculate_angle(shoulderl, elbowl, wristl) #คำนวณองศา

                    # Visualize angle
                    cv2.putText(image, str(angle), #ตัวเลขที่แสดงแบบเรียลทาม
                                tuple(np.multiply(elbowl, [1080, 780]).astype(int)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA
                                )

                    anglekneeleft = calculate_anglekneeleft(hipl, kneel, anklel)
                    cv2.putText(image, str(anglekneeleft),
                                tuple(np.multiply(kneel, [1080, 780]).astype("int")),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA
                                )

                    anglehip = calculate_anglehip(shoulderl, hipl, kneel)
                    cv2.putText(image, str(anglehip),
                                tuple(np.multiply(hipl, [1080, 780]).astype("int")),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA
                                )

                if change == 'latpulldown':
                    angler = calculate_angler(shoulderr, elbowr, wristr)
                    cv2.putText(image, str(angler),
                                tuple(np.multiply(elbowr, [1080, 780]).astype("int")),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA
                                )
                    angle = calculate_angler(shoulderl, elbowl, wristl)
                    cv2.putText(image, str(angle),
                                tuple(np.multiply(elbowl, [1080, 780]).astype("int")),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA
                                )

                if change == 'latpulldown2_wrong':
                    # Calculate angle
                    angler = calculate_angler(shoulderr, elbowr, wristr)
                    # Visualize angle
                    cv2.putText(image, str(angler),
                                tuple(np.multiply(elbowr, [1080, 780]).astype("int")),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA
                                )
                    anglehipr = calculate_anglehip(shoulderr, hipr, kneer)
                    cv2.putText(image, str(anglehipr),
                                tuple(np.multiply(hipr, [1080, 780]).astype("int")),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA
                                )

                # if angler < 70:
                #     stage = "Error"
                #     print(stage)
                # else:
                #     if angle < 80:
                #         stage = "down"
                #         print(stage)
                # if angle > 170 and stage == 'down':
                #     stage = "up"
                #     counter += 1
                #     print(counter)
                #     print(stage)
                # if stage == 'Error':
                #     print("ผิดๆ")


            except:
                pass
            if change == 'benchpress2_wrong': #คำนวณถูก-ผิด
                if angler > 170 and angle > 170: #การยกแขน ถ้ายกสุดจะถือว่าถูกต้อง ขึ้นสีเขียว
                    stage = "Error"
                    checkbenchpresstopgreen += 1
                    sumarmrightgreen += 1
                    sumarmleftgreen += 1
                    cv2.rectangle(image, (0, 0), (225, 73), (0, 255, 0), -1)
                    # print(stage)
                elif angler > 95 and angle > 95:  # การเอาแขนลงอยากมากต้องตั้งฉาก ถ้าไม่ถึงตั้งฉากจะถือว่าผิด ขึ้นสีแดง
                    stage = "Error"
                    sumarmrightred += 1
                    sumarmleftred += 1
                    checkbenchpresstopred += 1
                    cv2.rectangle(image, (0, 0), (225, 73), (0, 0, 255), -1)
                    # print(stage)
                elif angler < 50 and angle < 50: # การเอาแขนลงต่ำสุด ถ้าต่ำเกินไปจะถือว่าผิด ขึ้นสีแดง
                    stage = "Error"
                    sumarmrightred += 1
                    sumarmleftred += 1
                    checkbenchpresstopred += 1
                    cv2.rectangle(image, (0, 0), (225, 73), (0, 0, 255), -1)
                    # print(stage)
                else:
                    cv2.rectangle(image, (0, 0), (225, 73), (0, 255, 0), -1) #ถ้าไม่เข้าเงื่อนไขใดๆ จะถือว่าถูก ขึ้นสีเขียว
                    checkbenchpresstopgreen += 1
                    sumarmrightgreen += 1
                    sumarmleftgreen += 1
            if change == 'benchpress_wrong':
                if angle > 170: #การยกแขน ถ้ายกสุดจะถือว่าถูกต้อง ขึ้นสีเขียว
                    stage = "Error"
                    checkbenchpressleftgreen += 1
                    sumarmleftgreen1 += 1
                    cv2.rectangle(image, (0, 0), (225, 73), (0, 255, 0), -1)
                    # print(stage)
                elif angle > 95:  # การเอาแขนลงอยากมากต้องตั้งฉาก ถ้าไม่ถึงตั้งฉากจะถือว่าผิด ขึ้นสีแดง
                    stage = "Error"
                    checkbenchpressleftred += 1
                    sumarmleftred1 += 1
                    cv2.rectangle(image, (0, 0), (225, 73), (0, 0, 255), -1)
                    # print(stage)
                elif angle < 20: # การเอาแขนลงต่ำสุด ถ้าต่ำเกินไปจะถือว่าผิด ขึ้นสีแดง
                    stage = "Error"
                    checkbenchpressleftred += 1
                    sumarmleftred1 += 1
                    cv2.rectangle(image, (0, 0), (225, 73), (0, 0, 255), -1)
                    # print(stage)
                else:
                    cv2.rectangle(image, (0, 0), (225, 73), (0, 255, 0), -1) #ถ้าไม่เข้าเงื่อนไขใดๆ จะถือว่าถูก ขึ้นสีเขียว
                    checkbenchpressleftgreen += 1
                    sumarmleftgreen1 += 1


            if change == 'deadlift2_2':
                if angler < 170 and angle < 170:  # การยืดแขน ถ้าแขนงอจนต่ำกว่า 170 องศา จะถือว่าผิด ขึ้นสีแดง
                    stage = "Error"
                    checkdeadliftfontred +=1
                    sumarmleftred2 += 1
                    sumarmrightred2 += 1
                    cv2.rectangle(image, (0, 0), (225, 73), (0, 0, 255), -1)
                    # print(stage)
                elif anglekneeleft < 150 and anglekneeright < 150:  # ถ้างอขาเกิน 170 องศาจะถือว่าผิด ขึ้นสีแดง
                    stage = "Error"
                    checkdeadliftfontred += 1
                    sumkneeleftred2 += 1
                    sumkneerightred2 += 1
                    cv2.rectangle(image, (0, 0), (225, 73), (0, 0, 255), -1)
                    # print(stage)
                else:
                    cv2.rectangle(image, (0, 0), (225, 73), (0, 255, 0), -1)  # ถ้าไม่เข้าเงื่อนไขใดๆ จะถือว่าถูก ขึ้นสีเขียว
                    checkdeadliftfontgreen += 1
                    sumarmrightgreen2 += 1
                    sumarmleftgreen2 += 1
                    sumkneeleftgreen2 += 1
                    sumkneerightgreen2 += 1


            if change == 'deadlift_1':
                if angle < 160:  # การยืดแขน ถ้าแขนงอจนต่ำกว่า 170 องศา จะถือว่าผิด ขึ้นสีแดง
                    stage = "Error"
                    checkdeadliftrightred += 1
                    sumarmrightred3 += 1
                    cv2.rectangle(image, (0, 0), (225, 73), (0, 0, 255), -1)
                    # print(stage)
                elif anglekneeleft > 140:  # ถ้างอน้อยกว่า 160 องศาจะถือว่าผิด ขึ้นสีแดง
                    stage = "Error"
                    sumkneerightgreen3 += 1
                    checkdeadliftrightgreen += 1
                    cv2.rectangle(image, (0, 0), (225, 73), (0, 255, 0), -1)

                    # print(stage)
                elif anglekneeleft < 140:  # ถ้างอขาเกิน 170 องศาจะถือว่าผิด ขึ้นสีแดง
                    stage = "Error"
                    checkdeadliftrightred += 1
                    sumkneerightred3 += 1
                    cv2.rectangle(image, (0, 0), (225, 73), (0, 0, 255), -1)
                elif anglehip > 100:
                    cv2.rectangle(image, (0, 0), (225, 73), (0, 0, 255), -1)
                    checkdeadliftrightred += 1
                    sumhiprightred3 += 1
                else:
                    cv2.rectangle(image, (0, 0), (225, 73), (0, 255, 0), -1)  # ถ้าไม่เข้าเงื่อนไขใดๆ จะถือว่าถูก ขึ้นสีเขียว
                    checkdeadliftrightgreen += 1
                    sumarmrightgreen3 += 1
                    sumkneerightgreen3 += 1
                    sumhiprightgreen3 += 1

            if change == 'latpulldown':
                if angler > 170 and angle > 170:  # การยกแขน ถ้ายกสุดจะถือว่าถูกต้อง ขึ้นสีเขียว
                    stage = "Error"
                    checklatpulldownbackgreen += 1
                    sumarmrightgreen4 += 1
                    sumarmleftgreen4 += 1
                    cv2.rectangle(image, (0, 0), (225, 73), (0, 255, 0), -1)
                    # print(stage)
                elif angler > 50 and angle > 50:  # การเอาแขนลงอยากมากต้องตั้งฉาก ถ้าไม่ถึงตั้งฉากจะถือว่าผิด ขึ้นสีแดง
                    stage = "Error"
                    checklatpulldownbackred += 1
                    sumarmrightred4 += 1
                    sumarmleftred4 += 1
                    cv2.rectangle(image, (0, 0), (225, 73), (0, 0, 255), -1)
                    # print(stage)
                elif angler < 40 and angle < 40:  # การเอาแขนลงต่ำสุด ถ้าต่ำเกินไปจะถือว่าผิด ขึ้นสีแดง
                    stage = "Error"
                    checklatpulldownbackred += 1
                    sumarmrightred4 += 1
                    sumarmleftred4 += 1
                    cv2.rectangle(image, (0, 0), (225, 73), (0, 0, 255), -1)
                    # print(stage)
                else:
                    cv2.rectangle(image, (0, 0), (225, 73), (0, 255, 0),
                                -1)  # ถ้าไม่เข้าเงื่อนไขใดๆ จะถือว่าถูก ขึ้นสีเขียว
                    checklatpulldownbackgreen += 1
                    sumarmrightgreen4 += 1
                    sumarmleftgreen4 += 1

            if change == 'latpulldown2_wrong':
                if angler > 170:  # การยกแขน ถ้ายกสุดจะถือว่าถูกต้อง ขึ้นสีเขียว
                    stage = "Error"
                    checklatpulldownrightgreen += 1
                    sumarmrightgreen5 = 0
                    cv2.rectangle(image, (0, 0), (225, 73), (0, 255, 0), -1)
                    # print(stage)
                elif angler > 20:  # การเอาแขนลงอยากมากต้องตั้งฉาก ถ้าไม่ถึงตั้งฉากจะถือว่าผิด ขึ้นสีแดง
                    stage = "Error"
                    checklatpulldownrightred += 1
                    sumarmrightred5 = 0
                    cv2.rectangle(image, (0, 0), (225, 73), (0, 0, 255), -1)
                    # print(stage)
                elif angler < 10:  # การงอแขน ถ้าแขนงอจนต่ำกว่า 50 องศา จะถือว่าผิด ขึ้นสีแดง
                    stage = "Error"
                    checklatpulldownrightred += 1
                    sumarmrightred5 = 0
                    cv2.rectangle(image, (0, 0), (225, 73), (0, 0, 255), -1)
                    # print(stage)
                elif anglehipr > 160:
                    cv2.rectangle(image, (0, 0), (225, 73), (0, 0, 255), -1)
                    checklatpulldownrightred += 1
                    sumhiprightred5 = 0
                elif anglehipr > 145:
                    cv2.rectangle(image, (0, 0), (225, 73), (0, 0, 255), -1)
                    checklatpulldownrightred += 1
                    sumhiprightred5 = 0
                else:
                    cv2.rectangle(image, (0, 0), (225, 73), (0, 255, 0), -1)  # ถ้าไม่เข้าเงื่อนไขใดๆ จะถือว่าถูก ขึ้นสีเขียว
                    checklatpulldownrightgreen += 1
                    sumarmrightgreen5 = 0
                    sumhiprightgreen5 = 0


                # if anglekneeleft > 170 and anglekneeright > 170:  # ถ้างอขาเกิน 170 องศาจะถือว่าผิด ขึ้นสีแดง
                #     stage = "Error"
                #     cv2.rectangle(image, (360, 0), (225, 73), (0, 0, 255), -1)
                #     # print(stage)
                # else:
                #     cv2.rectangle(image, (0, 0), (225, 73), (0, 255, 0), -1)  # ถ้าไม่เข้าเงื่อนไขใดๆ จะถือว่าถูก ขึ้นสีเขียว

                    # elif anglehip < 80 and anglehipr < 80:  # การเอาแขนลงต่ำสุด ถ้าต่ำเกินไปจะถือว่าผิด ขึ้นสีแดง
                    #     stage = "Error"
                    #     cv2.rectangle(image, (0, 0), (225, 73), (0, 0, 255), -1)
                    #     # print(stage)
                    # else:
                    #     cv2.rectangle(image, (0, 0), (225, 73), (0, 255, 0), -1)  # ถ้าไม่เข้าเงื่อนไขใดๆ จะถือว่าถูก ขึ้นสีเขียว


                # if angle > 95 and stage == 'down':
                #     stage = "up"
                #     counter += 1
                #     cv2.rectangle(image, (0, 0), (225, 73), (0, 255, 0), -1)
                #     print(counter)

            # Render detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                    mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                    mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                    )
            
            cv2.imshow('Project', image) #สร้างหน้าต่างวิเคราะห์

            # out = cv2.VideoWriter('output.avi', 50, 20.0, (640, 480))

            # while (cap.isOpened()):
            #     ret, frame = cap.read()
            #     if ret == True:
            #         frame = cv2.flip(frame, 60)
            #
            #         # write the flipped frame
            #         out.write(frame)
            #     if cv2.waitKey(10) & 0xFF == ord('q'):
            #         break
            #     else:
            #         break
            if cv2.waitKey(10) & 0xFF == ord('q'):
                # print(sumarmrightgreen4, sumarmrightred4)
                if change == 'deadlift2_2':
                    averagedl1 = (sumarmleftgreen2 / (sumarmleftgreen2 + sumarmleftred2))*100
                    averagedl2 = (sumarmrightgreen2 / (sumarmrightgreen2 + sumarmrightred2)) * 100
                    averagedl3 = (sumkneeleftgreen2 / (sumkneeleftgreen2 + sumkneeleftred2)) * 100
                    averagedl4 = (sumkneerightgreen2 / (sumkneerightgreen2 + sumkneerightred2)) * 100
                    average1 = (checkdeadliftfontgreen / (
                            checkdeadliftfontgreen + checkdeadliftfontred)) * 100  # ค่าเฉลี่ยรวมdeadliftด้านหน้า
                    print(average1)
                    # print(averagedl1,averagedl2,averagedl3,averagedl4)
                elif change == 'deadlift_1':
                    # averagedl5 = (sumarmrightgreen3 / (sumarmrightgreen3 + sumarmrightred3)) * 100
                    # averagedl6 = (sumkneerightgreen3 / (sumkneerightgreen3 + sumkneerightred3)) * 100
                    # averagedl7 = (sumhiprightgreen3 / (sumhiprightgreen3 + sumhiprightred3)) * 100
                    average2 = (checkdeadliftrightgreen / (checkdeadliftrightgreen+checkdeadliftrightred))*100 # ค่าเฉลี่ยรวมdeadliftด้านขวา
                    print(average2)
                elif change == 'benchpress2_wrong':
                    # averagebp1 = (sumarmrightgreen / (sumarmrightgreen + sumarmrightred))*100
                    # averagebp2 = (sumarmleftgreen / (sumarmleftgreen + sumarmleftred))*100
                    average3 = (checkbenchpresstopgreen / (checkbenchpresstopgreen+checkbenchpresstopred))*100 # ค่าเฉลี่ยรวมbenchpressด้านบน
                    print(average3)
                elif change == 'benchpress_wrong':
                    # averagebp3 = (sumarmleftgreen1 / (sumarmleftgreen1 + sumarmleftred1))*100
                    average4 = (checkbenchpressleftgreen / (checkbenchpressleftgreen+checkbenchpressleftred))*100 # ค่าเฉลี่ยรวมbenchpressด้านซ้าย
                    print(average4)
                elif change == 'latpulldown':
                    # averagelpd1 = (sumarmrightgreen4 / (sumarmrightgreen4 + sumarmrightred4)) * 100
                    # averagelpd2 = (sumarmleftgreen4 / (sumarmleftgreen4 + sumarmleftred4)) * 100
                    average5 = (checklatpulldownbackgreen / (checklatpulldownbackgreen+checklatpulldownbackred))*100 # ค่าเฉลี่ยรวมlatpulldownด้านหลัง
                    print(average5)
                elif change == 'latpulldown2_wrong':
                    # averagelpd3 = (sumarmrightgreen5 / (sumarmrightgreen5 + sumarmrightred5)) * 100
                    # averagelpd4 = (sumhiprightgreen5 / (sumhiprightgreen5 + sumhiprightred5)) * 100
                    average6 = (checklatpulldownrightgreen / (checklatpulldownrightgreen+checklatpulldownrightred))*100 # ค่าเฉลี่ยรวมlatpulldownด้านขวา
                    print(average6)
                # print(averagedl1)
                # print(averagedl2)
                # print(averagedl3)
                # print(averagedl4)
                # print(averagedl5)
                # print(averagedl6)
                # print(averagedl7)
                # print(averagebp1)
                # print(averagebp2)
                # print(averagebp3)
                # print(averagelpd1)
                # print(averagelpd2)
                # print(averagelpd3)
                # print(averagelpd4)


                break

        cap.release()
        cv2.destroyAllWindows()