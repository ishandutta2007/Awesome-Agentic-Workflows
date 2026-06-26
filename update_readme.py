import os
import re

base_dir = r"C:\Users\ishan\Documents\Projects\Awesome-Agentic-Workflows"

# 1. Create assets dir and SVG
assets_dir = os.path.join(base_dir, "assets")
os.makedirs(assets_dir, exist_ok=True)
svg_content = """<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#8A2BE2;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#4B0082;stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="800" height="200" fill="url(#grad1)" rx="15" />
  <text x="400" y="90" fill="white" font-family="Arial, sans-serif" font-size="40" font-weight="bold" text-anchor="middle" dominant-baseline="middle">Awesome Agentic Workflows 🤖</text>
  <text x="400" y="140" fill="#E6E6FA" font-family="Arial, sans-serif" font-size="20" text-anchor="middle" dominant-baseline="middle">Master the Future of Autonomous AI</text>
</svg>"""

with open(os.path.join(assets_dir, "banner.svg"), "w", encoding="utf-8") as f:
    f.write(svg_content)

# 2. Update README.md
readme_path = os.path.join(base_dir, "README.md")
with open(readme_path, "r", encoding="utf-8") as f:
    readme_content = f.read()

# Badges and Banner at top
top_content = """<div align="center">
  <img src="assets/banner.svg" alt="Awesome Agentic Workflows Banner" width="800" />
</div>

<div align="center">
  <a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>
  <a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>
</div>

# ✨ Awesome-Agentic-Workflows ✨

**Keywords**: *Agentic Workflows, AI Agents, LLM Orchestration, Autonomous Systems, Multi-Agent Systems, GenAI*

## 🤖 The Agentic Workflows Map"""

readme_content = readme_content.replace("# Awesome-Agentic-Workflows\n## 🤖 The Agentic Workflows Map", top_content)

# Add Star History
star_history_text = """
## 🌟 Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007/Awesome-Agentic-Workflows&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Agentic-Workflows&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Agentic-Workflows&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Agentic-Workflows&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"""

# Append star history if not already there
if "Star History" not in readme_content:
    readme_content += "\n" + star_history_text

# Replace chartrepos with chart?repos
readme_content = readme_content.replace("chartrepos", "chart?repos")

# Replace awesome link
readme_content = readme_content.replace("https://github.com/sindresorhus/awesome", "https://github.com/ishandutta2007/Awesome-Awesome-Awesome")

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme_content)

print("Updates successful.")
