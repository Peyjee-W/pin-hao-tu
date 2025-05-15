from PIL import Image
import numpy as np
import os

# 设置图片所在子文件夹路径（相对于当前py脚本目录）
folder_name = 'images'  # ✅ 替换为你的图片文件夹名称
folder_path = os.path.join(os.getcwd(), folder_name)

# 获取所有图片文件（支持png/jpg/jpeg格式）
valid_extensions = ['.png', '.jpg', '.jpeg']
image_files = [os.path.join(folder_path, f)
               for f in os.listdir(folder_path)
               if os.path.splitext(f)[1].lower() in valid_extensions]

# 检查是否有图片
if not image_files:
    raise ValueError(f'文件夹 "{folder_name}" 中没有有效图片文件。')

# 打开第一张图并作为初始图像
base_img = Image.open(image_files[0]).convert('RGBA')
result = np.asarray(base_img).astype(np.float32) / 255.0
target_size = base_img.size

# 正片叠底叠加剩余图像
for img_path in image_files[1:]:
    overlay = Image.open(img_path).convert('RGBA')
    overlay = overlay.resize(target_size, Image.Resampling.LANCZOS)
    overlay_np = np.asarray(overlay).astype(np.float32) / 255.0
    result *= overlay_np

# 转换为uint8并保存
result = (result * 255).astype(np.uint8)
output_image = Image.fromarray(result, mode='RGBA')
output_image.save('blended_result.png')
output_image.show()
