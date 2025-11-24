import cv2
import sys

print("File: ", sys.argv[1:])
print("Showing file...")
img = cv2.imread(sys.argv[1])
cv2.imshow("Window", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
print("Finished")