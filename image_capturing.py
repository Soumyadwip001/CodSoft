import cv2

# Initialize the webcam
cam = cv2.VideoCapture(0)

# Create a window named "Python Webcam Screenshot App"
cv2.namedWindow("Python Webcam Screenshot App")

img_counter = 0

while True:
    ret, frame = cam.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Display the captured frame
    cv2.imshow("Python Webcam Screenshot App", frame)

    k = cv2.waitKey(1)

    if k % 256 == 27:
        # ESC key pressed
        print("Escape hit, closing the app")
        break
    elif k % 256 == 32:
        # SPACE key pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("Screenshot taken")
        img_counter += 1

# Release the webcam and destroy the window
cam.release()
cv2.destroyAllWindows()
