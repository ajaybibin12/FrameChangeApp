import cv2
import os

# Define allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'webp', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    """
    Check if the file has an allowed extension.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def processImage(filename, operation):
    """
    Process the image based on the selected operation.
    Operations include converting to grayscale, PNG, WebP, and JPG formats.
    """
    # Load the image from the uploads folder
    img = cv2.imread(os.path.join('uploads', filename))
    
    # Perform the operation
    match operation:
        case "cgray":
            # Convert image to grayscale
            imgProcessed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            newFilename = f"uploads/{filename.split('.')[0]}_gray.png"
            cv2.imwrite(newFilename, imgProcessed)
            return newFilename
        case "cwebp":
            # Convert image to WebP format
            newFilename = f"uploads/{filename.split('.')[0]}.webp"
            cv2.imwrite(newFilename, img)
            return newFilename
        case "cjpg":
            # Convert image to JPG format
            newFilename = f"uploads/{filename.split('.')[0]}.jpg"
            cv2.imwrite(newFilename, img)
            return newFilename
        case "cpng":
            # Convert image to PNG format
            newFilename = f"uploads/{filename.split('.')[0]}.png"
            cv2.imwrite(newFilename, img)
            return newFilename
        case "rotate":
            # Rotate image
            rows, cols, _ = img.shape
            M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
            imgProcessed = cv2.warpAffine(img, M, (cols, rows))
            newFilename = f"uploads/{filename.split('.')[0]}_rotated.jpg"
            cv2.imwrite(newFilename, imgProcessed)
            return newFilename
        case _:
            # If the operation is not recognized, return None or raise an error
            return None
