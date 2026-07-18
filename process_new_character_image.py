import os
import base64
from PIL import Image

src_img_path = r"C:\Users\dell\.gemini\antigravity-ide\brain\0bf6792b-241e-40d0-9aad-789d44307a42\media__1784415691271.jpg"
out_dir = r"C:\Users\dell\.gemini\antigravity-ide\scratch\github-profile"

os.makedirs(out_dir, exist_ok=True)

img = Image.open(src_img_path).convert("RGBA")
width, height = img.size

print(f"New character image size: {width}x{height}")

# Target width 440px
target_w = 440
target_h = int(height * (target_w / width))
img_resized = img.resize((target_w, target_h), Image.Resampling.LANCZOS)

# Remove white background
datas = list(img_resized.getdata())
new_data = []

for item in datas:
    if item[0] > 238 and item[1] > 238 and item[2] > 238:
        new_data.append((0, 0, 0, 0))
    elif item[0] > 218 and item[1] > 218 and item[2] > 218:
        avg = (item[0] + item[1] + item[2]) / 3.0
        alpha = int((255 - avg) * (255.0 / 37.0))
        new_data.append((item[0], item[1], item[2], max(0, min(255, alpha))))
    else:
        new_data.append(item)

img_resized.putdata(new_data)

# Quantize RGBA using FASTOCTREE to keep PNG file size compact (~80-110 KB)
img_opt = img_resized.quantize(colors=128, method=Image.Quantize.FASTOCTREE)

bg_removed_path = os.path.join(out_dir, "character_nobg_aldtor.png")
img_opt.save(bg_removed_path, format="PNG", optimize=True)

with open(bg_removed_path, "rb") as f:
    char_nobg_b64 = base64.b64encode(f.read()).decode('utf-8')

char_uri = f"data:image/png;base64,{char_nobg_b64}"
with open(os.path.join(out_dir, "char_nobg_b64.txt"), "w") as f:
    f.write(char_uri)

print(f"Processed new ALDTOR character image! PNG size: {os.path.getsize(bg_removed_path)/1024:.1f} KB, Base64 len: {len(char_uri)}")
