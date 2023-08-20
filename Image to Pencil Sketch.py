import cv2

# Load the image
image = cv2.imread("profile.jpg")

# Convert the image to grayscale
grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply an inverted filter to the grayscale image
invert = cv2.bitwise_not(grey_img)

# Apply Gaussian blur to the inverted image
blur = cv2.GaussianBlur(invert, (21, 21), 0)

# Invert the blurred image again
invertedblur = cv2.bitwise_not(blur)

# Create a sketch-like image by dividing the grayscale image by the inverted blurred image
# The scale parameter adjusts the intensity of the division
sketch = cv2.divide(grey_img, invertedblur, scale=256.0)

# Save the resulting sketch image
cv2.imwrite("profile_sketch.png", sketch)

# Display a message indicating the completion of the process
print("Sketch image saved as 'profile_sketch.png'")