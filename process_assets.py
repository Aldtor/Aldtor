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

# Resize character image to fit 460x660 box perfectly while compressing file size
# Scale down to 460px width
target_w = 460
target_h = int(height * (target_w / width))
img_resized = img.resize((target_w, target_h), Image.Resampling.LANCZOS)

# Save as optimized JPEG with quality=82 for super crisp look and tiny file size (~60-80 KB)
opt_char_path = os.path.join(out_dir, "character_opt.jpg")
img_resized.save(opt_char_path, format="JPEG", quality=82, optimize=True)

# Also process face crop for lanyard avatar
box = (int(width * 0.38), int(height * 0.07), int(width * 0.60), int(height * 0.28))
face_crop = img.crop(box)

w_c, h_c = face_crop.size
side = max(w_c, h_c)
square_face = Image.new("RGB", (side, side), (255, 255, 255))
offset = ((side - w_c) // 2, (side - h_c) // 2)
square_face.paste(face_crop, offset)

# Resize square face to 160x160
face_resized = square_face.resize((160, 160), Image.Resampling.LANCZOS)
opt_face_path = os.path.join(out_dir, "face_opt.jpg")
face_resized.save(opt_face_path, format="JPEG", quality=85, optimize=True)

# Convert both optimized images to base64 data URIs
with open(opt_char_path, "rb") as f:
    char_b64 = base64.b64encode(f.read()).decode('utf-8')

with open(opt_face_path, "rb") as f:
    face_b64 = base64.b64encode(f.read()).decode('utf-8')

char_uri = f"data:image/jpeg;base64,{char_b64}"
face_uri = f"data:image/jpeg;base64,{face_b64}"

with open(os.path.join(out_dir, "char_b64.txt"), "w") as f:
    f.write(char_uri)

with open(os.path.join(out_dir, "face_b64.txt"), "w") as f:
    f.write(face_uri)

print(f"Compressed char_b64 len={len(char_uri)} (~{len(char_uri)/1024:.1f} KB)")
print(f"Compressed face_b64 len={len(face_uri)} (~{len(face_uri)/1024:.1f} KB)")
