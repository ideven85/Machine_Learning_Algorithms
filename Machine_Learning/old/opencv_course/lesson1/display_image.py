import cv2
import matplotlib.pyplot as plt

cb_img = cv2.imread("images/checkerboard_color.png")
coke_img = cv2.imread("images/coca-cola-logo.png")

# Use matplotlib imshow()
plt.imshow(cb_img)
plt.title("matplotlib imshow")
plt.show()

# Use OpenCV imshow(), display for 8 sec
# window1 = cv2.namedWindow("w1")
# cv2.imshow(window1, cb_img)
# cv2.waitKey(8000)
# cv2.destroyWindow(window1)
#
# # Use OpenCV imshow(), display for 8 sec
# window2 = cv2.namedWindow("w2")
# cv2.imshow(window2, coke_img)
# cv2.waitKey(8000)
# cv2.destroyWindow(window2)

# Use OpenCV imshow(), display until any key is pressed
name = "w3"
cv2.namedWindow(name)
cv2.imshow(name, cb_img)
cv2.waitKey(8000)
cv2.destroyWindow(name)
#
window4 = "w4"
cv2.namedWindow(window4)
#
Alive = True
while Alive:
    # Use OpenCV imshow(), display until 'q' key is pressed
    cv2.imshow(window4, coke_img)
    keypress = cv2.waitKey(1)
    if keypress == ord("q"):
        Alive = False
cv2.destroyWindow(window4)

cv2.destroyAllWindows()
stop = 1
