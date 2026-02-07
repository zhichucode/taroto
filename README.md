# ✨ 塔罗牌解读 - Tarot Reading

一个精美的在线塔罗牌解读网站，支持多种牌阵和详细的牌义解读。

![塔罗牌解读](https://img.shields.io/badge/塔罗牌-解读-blue)
![Python](https://img.shields.io/badge/Python-3.12+-green)
![Flask](https://img.shields.io/badge/Flask-3.0.0-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🎴 功能特色

- **完整牌组**：包含78张塔罗牌（22张大阿卡纳 + 56张小阿卡纳）
- **多种牌阵**：支持单张抽牌、三牌阵（过去-现在-未来）、爱情阵
- **智能解读**：自动生成牌面综合解读和详细分析
- **精美设计**：iOS 风格的简洁界面，每张牌都有独特的 SVG 图片
- **正逆位支持**：支持正位和逆位牌的显示和解读
- **响应式设计**：完美适配桌面和移动设备

## 🌐 在线体验

访问 [https://taroto.onrender.com](https://taroto.onrender.com) 体验在线塔罗牌解读。

## 📦 安装部署

### 本地运行

1. 克隆仓库
```bash
git clone https://github.com/zhichucode/taroto.git
cd taroto
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 运行应用
```bash
python app.py
```

4. 访问应用
打开浏览器访问 `http://localhost:8000`

### Render 部署

本项目已部署在 Render，可通过以下步骤重新部署：

1. 将代码推送到 GitHub
2. 登录 [Render](https://render.com)
3. 创建新的 Web Service
4. 连接 GitHub 仓库
5. Render 会自动检测 Flask 应用并部署

## 🎨 牌组说明

### 大阿卡纳（Major Arcana）
愚者、魔术师、女祭司、皇后、皇帝、教皇、恋人、战车、力量、隐士、命运之轮、正义、倒吊人、死神、节制、恶魔、高塔、星星、月亮、太阳、审判、世界

### 小阿卡纳（Minor Arcana）
- **权杖**（Wands - 火元素）：22-35号牌
- **圣杯**（Cups - 水元素）：36-49号牌
- **宝剑**（Swords - 风元素）：50-63号牌
- **星币**（Pentacles - 土元素）：64-77号牌

## 🛠️ 技术栈

- **后端**：Python Flask
- **前端**：HTML, CSS, JavaScript
- **样式**：iOS 风格设计
- **图片**：SVG 矢量图形

## 📁 项目结构

```
taroto/
├── app.py                 # Flask 主应用
├── tarot_cards.py         # 塔罗牌数据模型
├── create_tarot_images.py # 牌面图片生成脚本
├── requirements.txt       # Python 依赖
├── Procfile              # Render 部署配置
├── runtime.txt           # Python 版本
├── templates/
│   └── index.html        # 主页模板
└── static/
    ├── css/
    │   └── style.css     # 样式文件
    ├── js/
    │   └── app.js        # 前端逻辑
    └── images/
        └── cards/        # 塔罗牌图片
            ├── 00.svg
            ├── 01.svg
            └── ...
```

## 🎮 使用方法

1. 选择你想要的牌阵类型
   - **单张抽牌**：快速获得当下的指引
   - **三牌阵**：了解过去、现在、未来的发展脉络
   - **爱情阵**：探索爱情运势和情感状态

2. 点击"开始抽牌"按钮

3. 查看抽到的牌面和详细解读

4. 可以点击"重新抽牌"再次尝试

## 📝 牌义说明

每张牌都有正位和逆位两种状态，分别代表不同的含义：

- **正位**：积极、正面、顺遂的含义
- **逆位**：挑战、阻碍、需要反思的含义

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 🙏 致谢

- 塔罗牌释义参考了传统的韦特塔罗牌体系
- UI 设计灵感来自 Apple iOS 设计语言
- 使用 Flask 框架构建后端服务

## 📮 联系方式

- GitHub: [@zhichucode](https://github.com/zhichucode)
- 项目地址: [https://github.com/zhichucode/taroto](https://github.com/zhichucode/taroto)

---

⚠️ **免责声明**：塔罗牌解读仅供娱乐和参考，不能作为生活决策的唯一依据。请理性对待塔罗牌的指引。

✨ 愿塔罗牌为你带来心灵的平静和智慧！