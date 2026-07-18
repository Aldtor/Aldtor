import os
import base64
from PIL import Image

brain_dir = r"C:\Users\dell\.gemini\antigravity-ide\brain\0bf6792b-241e-40d0-9aad-789d44307a42"
src_img_path = os.path.join(brain_dir, "media__1784412632318.jpg")
out_dir = r"C:\Users\dell\.gemini\antigravity-ide\scratch\github-profile"

os.makedirs(out_dir, exist_ok=True)

img = Image.open(src_img_path).convert("RGBA")
width, height = img.size

target_w = 420
target_h = int(height * (target_w / width))
img_resized = img.resize((target_w, target_h), Image.Resampling.LANCZOS)

# Remove pure/near white background
datas = list(img_resized.getdata())
new_data = []

for item in datas:
    if item[0] > 238 and item[1] > 238 and item[2] > 238:
        new_data.append((0, 0, 0, 0))
    elif item[0] > 220 and item[1] > 220 and item[2] > 220:
        avg = (item[0] + item[1] + item[2]) / 3.0
        alpha = int((255 - avg) * (255.0 / 35.0))
        new_data.append((item[0], item[1], item[2], max(0, min(255, alpha))))
    else:
        new_data.append(item)

img_resized.putdata(new_data)

# Quantize RGBA using FASTOCTREE (method 2) to reduce file size to ~100-140 KB
img_opt = img_resized.quantize(colors=128, method=Image.Quantize.FASTOCTREE)

bg_removed_path = os.path.join(out_dir, "character_nobg.png")
img_opt.save(bg_removed_path, format="PNG", optimize=True)

# Convert to Base64
with open(bg_removed_path, "rb") as f:
    char_nobg_b64 = base64.b64encode(f.read()).decode('utf-8')

char_uri = f"data:image/png;base64,{char_nobg_b64}"

with open(os.path.join(out_dir, "char_nobg_b64.txt"), "w") as f:
    f.write(char_uri)

print(f"Background removed & quantized! PNG size: {os.path.getsize(bg_removed_path)/1024:.1f} KB, Base64 len: {len(char_uri)}")
