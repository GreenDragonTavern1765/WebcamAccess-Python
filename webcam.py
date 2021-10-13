import cv2

vid_capture = cv2.VideoCapture(0)
vid_cod = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter("~/home/thaldrin/Videos/camVideo.mp4", vid_cod, 20.0, (640, 480))
while True:
    ret, frame = vid_capture.read()
    cv2.imshow("My cam video", frame)
    output.write(frame)
    if cv2.waitKey(1) and ord('q'):
        break
vid_capture.release()
output.release()
cv2.destroyAllWindows()