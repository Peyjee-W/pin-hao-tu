## 📌 README.md：拼好图（Multiply Blend Images）

# 拼好图 🖼️（Multiply Blend Images）

一个使用 Python 实现的图像融合工具，支持将指定文件夹下的多张图片采用正片叠底（Multiply Blend）模式叠加生成一张融合图像。适用于图像合成、图像效果测试、数字艺术等应用场景。

---

## 🧩 功能介绍

- ✅ 支持自动读取文件夹中的所有图片
- ✅ 多张图像自动按尺寸统一处理
- ✅ 使用正片叠底（Multiply）算法融合
- ✅ 支持 PNG、JPG、JPEG 等主流格式
- ✅ 生成融合结果图 `blended_result.png`

---

## 📂 项目结构

```

拼好图/
├── images/                # 存放待融合图片的文件夹
│   ├── image1.png
│   ├── image2.jpg
│   └── ...
├── multiply\_blend.py      # 主程序脚本
├── blended\_result.png     # 输出结果图像（运行后生成）
└── README.md              # 项目说明文档

````

---

## 🚀 使用方法

### 1. 克隆项目

```bash
git clone https://github.com/Peyjee-W/pin-hao-tu.git
cd pin-hao-tu
````

### 2. 安装依赖

确保你已安装 Python 3.6+，并使用如下命令安装依赖库：

```bash
pip install pillow numpy
```

### 3. 准备图片

将你要融合的所有图片放入项目根目录下的 `images/` 文件夹。

> ⚠️ 所有图片尺寸将被自动统一为第一张图片的尺寸。

### 4. 运行脚本

```bash
python multiply_blend.py
```

运行后将生成 `blended_result.png`，并自动展示图像。

---

## 🧠 正片叠底算法简介

正片叠底（Multiply Blend Mode）是一种图像混合方式，其核心计算方式如下：

```
Result = Image1 × Image2
```

对每个像素的每个通道（R, G, B）在 0\~1 区间内相乘，得到更暗的融合效果，广泛用于 Photoshop 和图像编辑中。

---

## 📷 示例效果

| 原图1                    | 原图2                    | 叠加效果（正片叠底）              |
| ---------------------- | ---------------------- | ----------------------- |
| ![](images/image1.jpg) | ![](images/image2.jpg) | ![](blended_result.png) |

> 请用你自己的图片替换 `images/` 文件夹中的示例图片。

---

## 💡 TODO

* [ ] 支持更多混合模式（如叠加、滤色、柔光等）
* [ ] 添加图像尺寸自动裁剪功能
* [ ] 支持 GUI 拖拽选择图片（未来版本）

---

## 📄 License

MIT License © 2025 \[Peyjee-W]

---

## 🤝 贡献者

欢迎提 Issue 或 Pull Request 改进本项目！

```

---

