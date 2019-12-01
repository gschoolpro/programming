import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    img = np.full((210,425,3),128,dtype=np.uint8)

    cv2.rectangle(img,(30,60),(220,160),(255,0,0))
    cv2.line(img,(30,100),(300,100),(0,255,0))

    cv2.imwrite("sample.png",img)
    plt.imshow(img)
    plt.show()
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        pass
