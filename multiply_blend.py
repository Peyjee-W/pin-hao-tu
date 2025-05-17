from PIL import Image, ImageOps
import numpy as np
import os

# 设置图片文件夹路径
folder_name = 'output'  # 替换为你的图片文件夹名称
folder_path = os.path.join(os.getcwd(), folder_name)

# 支持的图片格式
valid_extensions = ['.png', '.jpg', '.jpeg']
image_files = [os.path.join(folder_path, f)
               for f in os.listdir(folder_path)
               if os.path.splitext(f)[1].lower() in valid_extensions]

if not image_files:
    raise ValueError(f'文件夹 "{folder_name}" 中没有有效图片文件。')

# 打开第一张图像
base_img = Image.open(image_files[0]).convert('RGBA')
target_size = base_img.size
base_np = np.asarray(base_img).astype(np.float32) / 255.0

# 初始化两个融合图像
add_result = np.copy(base_np)
multiply_result = np.copy(base_np)

# 融合其余图像
for img_path in image_files[1:]:
    overlay = Image.open(img_path).convert('RGBA').resize(target_size, Image.Resampling.LANCZOS)
    overlay_np = np.asarray(overlay).astype(np.float32) / 255.0

    add_result += overlay_np  # 线性减淡
    multiply_result *= overlay_np  # 正片叠底

# 限制范围 [0,1]
add_result = np.clip(add_result, 0, 1)
multiply_result = np.clip(multiply_result, 0, 1)

# 转换为 uint8 并保存图像
def save_and_invert(np_array, filename_base):
    img_uint8 = (np_array * 255).astype(np.uint8)
    img = Image.fromarray(img_uint8, mode='RGBA')
    img.save(f'{filename_base}.png')

    # 转为 RGB 再反转颜色
    inverted = ImageOps.invert(img.convert('RGB'))
    inverted.save(f'{filename_base}_inverted.png')

# 保存结果
save_and_invert(add_result, 'blended_add')
save_and_invert(multiply_result, 'blended_multiply')

print("✅ 所有图像已保存：")
print(" - blended_add.png")
print(" - blended_add_inverted.png")
print(" - blended_multiply.png")
print(" - blended_multiply_inverted.png")
