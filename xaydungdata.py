import numpy as np
import cv2
import time
label = "KHONGCOSANPHAM"
cap = cv2.VideoCapture(0)
i=0
while(True):
    i+=1
    ret, frame = cap.read()
    if not ret:
        continue
    frame = cv2.resize(frame, dsize=None,fx=0.3,fy=0.3)

    cv2.imshow('frame',frame)

    # Lưu dữ liệu
    if i>=60 and i<=100:
        print("Số ảnh capture = ",i-60)
        # Tạo thư mục nếu chưa có
        if not os.path.exists('data/validation/' + str(label)):
            os.mkdir('data/valitation/' + str(label))
        cv2.imwrite('data/validation/' + str(label) + "/" + str(i) + ".png",frame)

    if cv2.waitKey(1) & 0xFF == ord('Q'):

        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()