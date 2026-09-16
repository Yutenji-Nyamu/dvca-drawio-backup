# Draw.io 恢复及图表修订后完整快照

时间：2026-09-16T21:21:48.310702+08:00

按用户确认的公开 Git 仓库备份约定，记录同一批 8 份正式 Draw.io 当前版本。全部文件 XML 检查通过。

- 场景图恢复为完整 3 页，保留本轮 9 处最新右移修改。
- 真机图表批注处理版为首页，原页保留，共 2 页。
- real sample chart 在 21:16:45 有用户独立编辑，本快照原样保全其最新版本。
- 其余 5 份与上一现场快照 SHA-256 完全一致。
- 上一损坏现场快照继续保留在 2026-09-16_210942_before-recovery。

| 文件 | 字节 | 页数 | 本轮更新 | SHA-256 |
|---|---:|---:|---|---|
| dvca bc 0915.drawio | 26215506 | 7 | 否 | `f34587facdf8e3cd2cd973712da1c0368e0787a13f1402101a27e2a148f0d6f7` |
| dvca exp scene 0916.drawio | 39555121 | 3 | 是 | `e9b1d55d51c25ada66e3b2848076f0149ef7ed460501ab8aebfb2269e6af3990` |
| dvca head 0912.drawio | 71308587 | 9 | 否 | `7ce6536c569feeff6d0bb3d0bc762e2ebd1500ba37dc2069f40557647d40c77c` |
| dvca main 0914.drawio | 32283550 | 9 | 否 | `04eec8c47062a553059cbb4f6c7b41a8d6b8250c9961ded02186b83e77ac1add` |
| dvca pcode 0915.drawio | 3300828 | 6 | 否 | `077e5e615c9b0965778b249ad9202fdfab4d38272804663d1966f773d03eded3` |
| dvca real chart 0916.drawio | 1743784 | 2 | 是 | `bfd3aca787fc0baa6b41f102543ab46a673d2adc95df8e2ebd778b8ae4741f62` |
| dvca real sample chart 0916.drawio | 165529 | 1 | 是 | `be12e8c2c0591d43fe63a665303d6eda5a2587d9a588c2e65d562ab208dc812c` |
| turn_switch_world_选帧_0915.drawio | 386328 | 1 | 否 | `effba0e00c64bc3e7f434b0664a574199345c30340fb0f8ce9c03bd0af279f37` |

排除素材：ODPR_Fig1_素材.drawio、dvca exp material.drawio、主图素材.drawio、头图素材.drawio

逐项来源时间及完整校验见 manifest.json。
