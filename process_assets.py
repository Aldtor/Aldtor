import os
import base64
from PIL import Image

brain_dir = r"C:\Users\dell\.gemini\antigravity-ide\brain\0bf6792b-241e-40d0-9aad-789d44307a42"
src_img_path = os.path.join(brain_dir, "media__1784412632318.jpg")
out_dir = r"C:\Users\dell\.gemini\antigravity-ide\scratch\github-profile"

os.makedirs(out_dir, exist_ok=True)

img = Image.open(src_img_path)
width, height = img.size
print(f"Original image size: {width}x{height}")

# 1. Full character image saved as clean PNG
character_png_path = os.path.join(out_dir, "character.png")
img.save(character_png_path, format="PNG")

# 2. Crop head/face for lanyard avatar
# Head is located roughly around top 5% to 30% vertically, and middle 35% to 65% horizontally
box = (int(width * 0.38), int(height * 0.07), int(width * 0.60), int(height * 0.28))
face_crop = img.crop(box)

# Make face_crop square
w_c, h_c = face_crop.size
side = max(w_c, h_c)
square_face = Image.new("RGBA", (side, side), (255, 255, 255, 0))
offset = ((side - w_c) // 2, (side - h_c) // 2)
square_face.paste(face_crop, offset)

face_png_path = os.path.join(out_dir, "avatar_face.png")
square_face.save(face_png_path, format="PNG")

# Convert both to base64 strings
with open(character_png_path, "rb") as f:
    char_b64 = base64.b64encode(f.read()).decode('utf-8')

with open(face_png_path, "rb") as f:
    face_b64 = base64.b64encode(f.read()).decode('utf-8')

with open(os.path.join(out_dir, "char_b64.txt"), "w") as f:
    f.write(f"data:image/png;base64,{char_b64}")

with open(os.path.join(out_dir, "face_b64.txt"), "w") as f:
    f.write(f"data:image/png;base64,{face_b64}")

print("Assets processed and base64 strings created successfully.")
