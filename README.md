# PD-LRRK2-AF3：LRRK2 × 乙酰胆碱受体 计算筛选脚手架  
# PD-LRRK2-AF3: Computational Screening Scaffold for LRRK2 × Acetylcholine Receptor Interactions

---

## 📌 项目简介 | Project Overview
**中文**  
本项目面向帕金森病（PD）研究，利用 AlphaFold3 API（如可用）、AlphaFold2-Multimer 或 ESMFold + 对接，对 **LRRK2** 与 **乙酰胆碱受体（nAChR/mAChR）** 的潜在复合物进行计算筛选，输出接口特征、候选排名与自动化报告，为湿实验（如共免、点突变、功能学）提供候选清单。  

**English**  
This project targets Parkinson's disease (PD) research, using AlphaFold3 API (if available), AlphaFold2-Multimer, or ESMFold + docking to computationally screen potential complexes between **LRRK2** and **acetylcholine receptors** (nAChR/mAChR). It outputs interface features, ranked candidates, and automated reports to support wet-lab experiments such as co-IP, mutagenesis, and functional assays.

---

## 📂 目录结构 | Directory Structure
```
.  
├─ README.md                 # 项目说明 | Project documentation  
├─ LICENSE                   # 许可证 | License (MIT by default)  
├─ .gitignore                # 忽略规则 | Ignore rules for large/intermediate files  
├─ environment.yml           # Conda/Mamba 环境配置 | Conda/Mamba environment definition  
├─ config/  
│  ├─ config.yaml            # 全局配置 | Global config (backends, tokens, params)  
│  └─ receptors.csv          # 受体清单 | Receptor list  
├─ data/  
│  ├─ sequences/             # 序列 | Sequences  
│  ├─ msa/                   # MSA 缓存 | MSA cache  
│  └─ structures_raw/        # 原始结构 | Raw predicted structures  
├─ results/  
│  ├─ complexes/             # 复合物结构 | Complex structures  
│  ├─ docking/               # 对接结果 | Docking results  
│  ├─ metrics/               # 指标 | Metrics  
│  └─ reports/               # 报告 | Reports  
├─ scripts/  
│  ├─ 01_fetch_sequences.py      # 获取序列 | Fetch sequences  
│  ├─ 02_domain_extract.py       # 域切片 | Domain extraction  
│  ├─ 03_build_msa.py            # 构建 MSA | Build MSA  
│  ├─ 04_predict_complex.py      # 结构预测 | Complex prediction  
│  ├─ 05_dock_refine.py          # 对接精修 | Dock/refine  
│  ├─ 06_interface_analysis.py   # 接口分析 | Interface analysis  
│  ├─ 07_rank_and_select.py      # 排名筛选 | Ranking  
│  └─ 08_make_report.py          # 生成报告 | Report generation  
├─ workflow/  
│  ├─ Snakefile                  # 主入口 | Main entry  
│  └─ rules/                     # Snakemake 规则 | Snakemake rules  
└─ notebooks/  
   ├─ 00_exploration.ipynb       # 探索 | Exploration  
   └─ 10_visualize_interfaces.ipynb # 可视化 | Visualization  
```

---

## ⚙️ 环境与依赖 | Environment & Dependencies
**中文**  
推荐使用 **Mambaforge/Miniconda** 创建环境，GPU 建议 ≥12 GB 显存以运行 AF2-Multimer。  
```bash
mamba env create -f environment.yml
conda activate pd-lrrk2
```

**English**  
Use **Mambaforge/Miniconda** to create the environment. For AF2-Multimer, ≥12 GB VRAM is recommended.  
```bash
mamba env create -f environment.yml
conda activate pd-lrrk2
```

---

## 🚀 运行步骤 | How to Run
**中文**
1. 编辑 `config/receptors.csv` 和 `config/config.yaml`  
2. 运行 Snakemake 工作流：  
```bash
snakemake -s workflow/Snakefile -j 8 --use-conda
```
3. 查看 `results/reports/final_report.html`

**English**  
1. Edit `config/receptors.csv` and `config/config.yaml`  
2. Run the Snakemake workflow:  
```bash
snakemake -s workflow/Snakefile -j 8 --use-conda
```
3. Open `results/reports/final_report.html`

---

## 📊 输出结果 | Outputs
- **中文**：  
  - 复合物结构：`results/complexes/`  
  - 接口指标：`results/metrics/summary.csv`  
  - 报告文件：`results/reports/final_report.html`  

- **English**:  
  - Complex structures: `results/complexes/`  
  - Interface metrics: `results/metrics/summary.csv`  
  - Report: `results/reports/final_report.html`

---

## ❗ 常见问题 | Troubleshooting
**中文**
- `conda/mamba: command not found` → 当前环境无 Conda，请本地或可联网平台运行  
- AF3 API 调用失败 → 检查 token、API 地址和配额

**English**
- `conda/mamba: command not found` → No Conda in environment; run locally or on a networked platform  
- AF3 API call failed → Check token, API URL, and quota

---

## 📅 路线图 | Roadmap
- [ ] ColabFold 批量接口 | ColabFold batch API  
- [ ] 能量计算适配 | Energy estimation support  
- [ ] Docker/Singularity 镜像 | Containerization  
- [ ] 保守位点自动注释 | Conservation site annotation  

---

## 📜 许可 | License
MIT License (see `LICENSE`)
