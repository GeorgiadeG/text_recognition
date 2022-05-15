import cv2
from PIL import Image
from pytesseract import pytesseract


def tesseract():
    path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    image_path = r'image.jpg'
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(Image.open(image_path))
    print(text[:-1])


if __name__ == '__main__':
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    while True:
        ret, image = camera.read()
        cv2.imshow('Text detection', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite('image.jpg', image)
            break
    camera.release()
    cv2.destroyAllWindows()
    tesseract()
