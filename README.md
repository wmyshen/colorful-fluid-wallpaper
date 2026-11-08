# 彩色流体壁纸 · Colorful Fluid Wallpaper

一个适合 Intel 核显尝试的轻量交互式网页动态壁纸。鼠标经过时注入不同颜色的墨水，空闲时缓慢自动流动。

基于 [Pavel Dobryakov 的 WebGL Fluid Simulation](https://github.com/PavelDoGreat/WebGL-Fluid-Simulation) 修改，保留 MIT 许可和原作者版权声明。不是从零实现的流体引擎。

## 效果与轻量设置

- 全色相随机配色，包括蓝紫、青绿、金橙和玫红。
- 鼠标移动互动，无需按住；空闲时自动生成缓慢流动。
- 帧率上限 30 FPS；模拟精度 64，染料精度 512，输出长边上限约 1280。
- 关闭 Bloom 和 Sunrays；保留明暗效果。
- 页面隐藏时停止模拟，并支持 Lively 的暂停事件。
- 壁纸运行不需要联网，不采集音频，无声音。

这些设置降低渲染负担，但不代表零占用。实际流畅度、发热和耗电取决于硬件、驱动和同时运行的程序。已通过 JavaScript 语法检查和 Lively 加载检查，尚未完成画面及长期性能验证。

## 先在浏览器预览

下载仓库并解压，使用支持 WebGL 的现代浏览器打开 `index.html`。移动鼠标查看彩色流体。按 `P` 暂停/继续，空格生成几团随机墨水。

## 在 Windows 中设为动态壁纸

1. 从 [Lively 官方仓库](https://github.com/lively-community/lively) 安装 Lively Wallpaper。
2. 运行 `python package.py`，生成 `dist/colorful-fluid-wallpaper.zip`。仅用 Python 标准库，无需安装额外依赖。
3. 在 Lively 点击“添加壁纸”→“选择一个文件”，选择生成的 ZIP。
4. 在壁纸库点击“彩色流体 · 核显轻量版”应用到桌面。
5. 建议关闭“开机自启动”，并在“性能”中设置全屏应用和省电模式时暂停。

项目不会自动安装软件、修改系统设置或开启自启动。上述设置由使用者在 Lively 中选择。

## 恢复原壁纸

从系统托盘的 Lively 图标选择“退出”，即可关闭动态壁纸并显示 Windows 原来的背景。也可先在 Lively 中关闭正在运行的壁纸。

如需重新指定背景，打开 Windows“设置 → 个性化 → 背景”选择原图片。此项目不修改、删除或覆盖原壁纸图片，也不需要改注册表或替换系统文件。

## 修改颜色和性能

`fluid.js` 的 `generateColor()` 使用 HSV 色相生成颜色。当前 `Math.random()` 覆盖整个色环；蓝紫配色可以改为 `0.53 + Math.random() * 0.24`。

文件顶部 `config` 可调整 `SIM_RESOLUTION`、`DYE_RESOLUTION`、`CURL` 等参数。帧率限制位于 `update()` 中的 `1000 / 30`；输出分辨率限制位于 `scaleByPixelRatio()` 中。

## 文件与许可

- `index.html`：全屏画布页面。
- `fluid.js`：WebGL 流体引擎和轻量、多彩、自动流动修改。
- `LDR_LLL1_0.png`：上游渲染资源。
- `LivelyInfo.json`：Lively 导入元数据。
- `package.py`：生成可导入的壁纸包。
- `LICENSE`：MIT 许可，原引擎版权归 Pavel Dobryakov。

本仓库不包含 Lively 安装包、第三方运行库、浏览器个人资料或设备壁纸备份。
