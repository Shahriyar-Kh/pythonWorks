from PIL import Image, ImageDraw, ImageFont

# Create a blank image with white background
width, height = 200, 200
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Choose a font and size
font_size = 60
font = ImageFont.truetype("arial.ttf", font_size)

# Define the letters and their positions
letters = "SHK"
positions = [(30, 60), (80, 60), (130, 60)]

# Draw the letters on the image
for letter, pos in zip(letters, positions):
    draw.text(pos, letter, fill="black", font=font)

# Save the icon
image.save("shk_icon.png")

# Show the icon
image.show()
