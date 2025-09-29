from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# === Step 1: Load image ===
image_path = r"D:\User\Downloads\MRI.jpg"
original_image = Image.open(image_path)
image = original_image.copy()
draw = ImageDraw.Draw(image)

# Load font
try:
    font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 22)
except:
    font = ImageFont.load_default()

# List to store clicked coordinates
coords = []

# Function to cover old text and write new text
def cover_and_write_text(draw, x, y, new_text, font):
    # Adjust rectangle to cover any date format
    text_width, text_height = draw.textsize("00-Sep-0000", font=font)
    draw.rectangle([x-5, y-5, x + text_width + 5, y + text_height + 5], fill="white")
    draw.text((x, y), new_text, fill="black", font=font)

# === Step 2: Show image and let user click ===
img = mpimg.imread(image_path)
fig, ax = plt.subplots()
ax.imshow(img)
ax.set_title("Click on the old date (close window after clicking)")

def onclick(event):
    if event.xdata and event.ydata:
        x, y = int(event.xdata), int(event.ydata)
        coords.append((x, y))
        print(f"✅ Clicked coordinates: {x}, {y}")
        # Ask user for new date
        new_date = input(f"Enter new date for position ({x},{y}): ")
        cover_and_write_text(draw, x, y, new_date, font)

cid = fig.canvas.mpl_connect("button_press_event", onclick)
plt.show()  # Wait for clicks

# === Step 3: Save modified image ===
output_filename = r"D:\User\Downloads\MRI_modified_interactive.jpg"
image.save(output_filename)

# Show before/after comparison
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 12))
ax1.imshow(original_image); ax1.axis("off"); ax1.set_title("Original")
ax2.imshow(image); ax2.axis("off"); ax2.set_title("Modified")
plt.show()

print("✅ Image saved as:", output_filename)
