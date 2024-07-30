import cv2
from pyzbar.pyzbar import decode

def read_qr_code(image_path):
    img = cv2.imread(image_path)
    decoded_objects = decode(img)

    if not decoded_objects:
        print("No QR codes found")
        return

    for obj in decoded_objects:
        print(f"Type: {obj.type}")
        print(f"Data: {obj.data.decode('utf-8')}")
        points = obj.polygon
        if len(points) > 4:
            hull = cv2.convexHull(points)
            points = hull
        points = [(point.x, point.y) for point in points]
        n = len(points)
        for j in range(0, n):
            cv2.line(img, points[j, points(j + 1) % n], (0, 255, 0), 3)

    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = "path_to_your_image.png"
    read_qr_code(image_path)