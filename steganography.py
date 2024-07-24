import cv2
import string
import os

# Creating dictionaries for encoding and decoding
d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

# Load the image
x = cv2.imread("1.jpg")

# Get image dimensions
rows, cols, _ = x.shape
print(rows, cols)

# User input for the key and the text to hide
key = input("Enter key to edit (Security Key): ")
text = input("Enter text to hide: ")

# Initialize variables
kl = 0
z = 0  # Plane (0 for Blue, 1 for Green, 2 for Red)
n = 0  # Row
m = 0  # Column

# Embed the text into the image
for char in text:
    x[n, m, z] = d[char] ^ d[key[kl]]
    n = (n + 1) % rows
    m = (m + 1) % cols
    z = (z + 1) % 3  # Cycle through color planes
    kl = (kl + 1) % len(key)

# Save the encrypted image
cv2.imwrite("encrypted_img.jpg", x)
os.startfile("encrypted_img.jpg")
print("Data Hiding in Image completed successfully.")

# User input to extract data from the image
ch = int(input("\nEnter 1 to extract data from Image: "))

if ch == 1:
    key1 = input("\n\nRe-enter key to extract text: ")
    decrypt = ""

    # Initialize variables for extraction
    kl = 0
    z = 0  # Plane (0 for Blue, 1 for Green, 2 for Red)
    n = 0  # Row
    m = 0  # Column

    if key == key1:
        for i in range(len(text)):
            decrypt += c[x[n, m, z] ^ d[key[kl]]]
            n = (n + 1) % rows
            m = (m + 1) % cols
            z = (z + 1) % 3  # Cycle through color planes
            kl = (kl + 1) % len(key)
        print("Encrypted text was: ", decrypt)
    else:
        print("Key doesn't match.")
else:
    print("Thank you. EXITING.")
