import cv2
import pandas as pd

img = cv2.imread("pic3.jpg")
img = cv2.resize(img, (1000, 700))


original_img = img.copy()
data = pd.read_csv("colors.csv")

def get_color_name(R, G, B):
    minimum = 100000
    color_name = ""

    for i in range(len(data)):
        distance = (
            abs(R - int(data.loc[i, "R"])) +
            abs(G - int(data.loc[i, "G"])) +
            abs(B - int(data.loc[i, "B"]))
        )

        if distance < minimum:
            minimum = distance
            color_name = data.loc[i, "Name"]

    return color_name

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
         print("You clicked at:", x, y)
         b, g, r = img[y, x]
         print("RGB:", r, g, b)
         color_name = get_color_name(r, g, b)
         print("Color:", color_name)
         cv2.rectangle(img, (20, 20), (450, 120), (255, 255, 255), -1)

         cv2.putText(img, color_name,
                    (40, 60),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 0, 0),
                    2)

         cv2.putText(img,
                    f"RGB: {r}, {g}, {b}",
                    (40, 100),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.4,
                    (0, 0, 0),
                    2)

         cv2.imshow("Color Detection", img)

cv2.namedWindow("Color Detection")

cv2.imshow("Color Detection", img)
cv2.setMouseCallback("Color Detection", mouse_callback)
cv2.waitKey(0)
cv2.destroyAllWindows()



