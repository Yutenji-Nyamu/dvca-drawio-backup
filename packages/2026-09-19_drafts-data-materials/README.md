# Draw.io 分类备份 · 2026-09-19

来源：ICLR27/drawio 顶层当前文件。每个 ZIP 保留原文件名，内容与源文件 SHA-256 一致。全部 ZIP 通过 CRC 和解压哈希检查；全部 Draw.io 通过 XML 解析，页名列于 manifest.json。

## 分类

- `01_paper_drafts/`：8 份。
- `02_plot_data/`：3 份。
- `03_drawio_materials/`：5 份。
- `04_drawing_guides/`：5 份。

论文草稿为 8 份 dvca 图；画图数据为 3 份 Excel；素材为头图素材、主图素材、实验素材、ODPR 素材和 Turn Switch 选帧，共 5 份 Draw.io。Turn Switch 选帧按用途归入素材，原文件保持原样。

按文件分别压缩，方便单独恢复和避免单个归档过大。素材包含当前 Draw.io 内嵌图像。视频原件、图片目录、资料目录中的历史产物和 .bak 文件保持在本地原位置；本次清单覆盖顶层全部当前 Draw.io、Excel 和 Markdown。以前 Git 快照继续保留。

## 文件清单

| 类别 | 文件 | 源大小 bytes | 压缩大小 bytes |
|---|---|---:|---:|
| 04_drawing_guides | Codex_drawio画图要点.md | 11994 | 6154 |
| 01_paper_drafts | dvca bc 0915.drawio | 26215506 | 11625663 |
| 01_paper_drafts | dvca curve comp&abl 0917.drawio | 10324925 | 4664841 |
| 02_plot_data | dvca curve raw data.xlsx | 23195 | 21480 |
| 03_drawio_materials | dvca exp material.drawio | 91507200 | 69276809 |
| 01_paper_drafts | dvca exp scene 0916.drawio | 52810226 | 39509386 |
| 01_paper_drafts | dvca head 0912.drawio | 71308587 | 52002179 |
| 01_paper_drafts | dvca main 0914.drawio | 32283550 | 15487573 |
| 01_paper_drafts | dvca pcode 0915.drawio | 3300828 | 661255 |
| 01_paper_drafts | dvca real chart 0916.drawio | 6554788 | 2936700 |
| 02_plot_data | dvca real chart data.xlsx | 11332 | 10154 |
| 01_paper_drafts | dvca real sample chart 0916.drawio | 6395574 | 2907624 |
| 02_plot_data | dvca real sample chart data.xlsx | 21327 | 18079 |
| 03_drawio_materials | ODPR_Fig1_素材.drawio | 932176 | 491504 |
| 03_drawio_materials | turn_switch_world_选帧_0915.drawio | 386328 | 291080 |
| 03_drawio_materials | 主图素材.drawio | 15449356 | 9054650 |
| 03_drawio_materials | 头图素材.drawio | 144441181 | 107662763 |
| 04_drawing_guides | 本轮检查与风格讨论.md | 7249 | 4248 |
| 04_drawing_guides | 精修七_逐项修改.md | 3327 | 2006 |
| 04_drawing_guides | 精修五_逐条批注与处理.md | 18607 | 8969 |
| 04_drawing_guides | 精修六_逐条批注与处理.md | 4475 | 2473 |

头图素材压缩后约 103 MiB，归档分成 3 个小于 GitHub 单文件限制的分片。下载整个分类目录后，在目录运行 python restore_split.py，即可重组并自动核对 SHA-256，再解压生成的 ZIP。
