import threading
import cv2
import os
from deepface import DeepFace

# Disable oneDNN optimizations if needed
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
face_match = False

Face_img = cv2.imread("Face.jpg")

def check_face(frame):
    global face_match
    try:
        if DeepFace.verify(frame, Face_img.copy())['verified']:
            face_match = True
        else:
            face_match = False
    except Exception as e:
        print(f"Error in face verification: {e}")
        face_match = False

while True:
    ret, frame = cap.read()

    if ret:
        if counter % 30 == 0:  # Fix modulus operator logic
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except Exception as e:
                print(f"Error starting thread: {e}")
        counter += 1

        if face_match:
            cv2.putText(frame, "MATCH", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        else:
            cv2.putText(frame, "NO MATCH", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.imshow("Video", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
