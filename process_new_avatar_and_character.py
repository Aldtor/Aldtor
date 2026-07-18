import os
import base64
from PIL import Image

brain_dir = r"C:\Users\dell\.gemini\antigravity-ide\brain\0bf6792b-241e-40d0-9aad-789d44307a42"
out_dir = r"C:\Users\dell\.gemini\antigravity-ide\scratch\github-profile"

os.makedirs(out_dir, exist_ok=True)

# 1. PROCESS CHARACTER FULL BODY IMAGE (No Hair Cut!)
src_char_path = os.path.join(brain_dir, "media__1784412632318.jpg")
img_char = Image.open(src_char_path).convert("RGBA")
width, height = img_char.size

# Add top padding so hair is never cut off
padded_h = height + 40
img_padded = Image.new("RGBA", (width, padded_h), (255, 255, 255, 255))
img_padded.paste(img_char, (0, 40))

# Resize to target width 440
target_w = 440
target_h = int(padded_h * (target_w / width))
img_resized = img_padded.resize((target_w, target_h), Image.Resampling.LANCZOS)

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

# Quantize RGBA using FASTOCTREE to keep PNG file size ~80-100 KB
img_opt = img_resized.quantize(colors=128, method=Image.Quantize.FASTOCTREE)

bg_removed_path = os.path.join(out_dir, "character_full_nobg.png")
img_opt.save(bg_removed_path, format="PNG", optimize=True)

with open(bg_removed_path, "rb") as f:
    char_nobg_b64 = base64.b64encode(f.read()).decode('utf-8')

char_uri = f"data:image/png;base64,{char_nobg_b64}"
with open(os.path.join(out_dir, "char_nobg_b64.txt"), "w") as f:
    f.write(char_uri)

print(f"Full body character processed! Size: {os.path.getsize(bg_removed_path)/1024:.1f} KB")


# 2. PROCESS NEW ATTACHED ID CARD AVATAR IMAGE (media__1784415271576.png)
src_avatar_path = os.path.join(brain_dir, "media__1784415271576.png")
img_avatar = Image.open(src_avatar_path).convert("RGB")
w_a, h_a = img_avatar.size

# Square crop
side = min(w_a, h_a)
crop_box = ((w_a - side) // 2, (h_a - side) // 2, (w_a + side) // 2, (h_a + side) // 2)
avatar_cropped = img_avatar.crop(crop_box)

# Resize to 160x160
avatar_resized = avatar_cropped.resize((160, 160), Image.Resampling.LANCZOS)
opt_avatar_path = os.path.join(out_dir, "id_card_avatar.jpg")
avatar_resized.save(opt_avatar_path, format="JPEG", quality=88, optimize=True)

with open(opt_avatar_path, "rb") as f:
    avatar_b64 = base64.b64encode(f.read()).decode('utf-8')

avatar_uri = f"data:image/jpeg;base64,{avatar_b64}"
with open(os.path.join(out_dir, "face_b64.txt"), "w") as f:
    f.write(avatar_uri)

print(f"New ID card avatar processed! Size: {os.path.getsize(opt_avatar_path)/1024:.1f} KB")
