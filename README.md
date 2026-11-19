<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:0f766e&height=170&section=header&text=Python%20Import%20Time%20Tree&fontColor=ffffff&fontSize=34" alt="Python Import Time Tree banner"/></p>
<p align="center"><img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=19&duration=2800&pause=900&center=true&vCenter=true&width=620&lines=Understand%20slow%20Python%20imports%3BVisualize%20self%20and%20cumulative%20time%3BDependency-free%20CLI" alt="Typing title"/></p>
<p align="center"><img src="https://img.shields.io/github/license/CyberLoop-dev/python-importtime-tree?style=flat-square" alt="License"/> <img src="https://img.shields.io/github/languages/top/CyberLoop-dev/python-importtime-tree?style=flat-square" alt="Language"/> <img src="https://img.shields.io/github/stars/CyberLoop-dev/python-importtime-tree?style=flat-square" alt="Stars"/> <img src="https://img.shields.io/github/last-commit/CyberLoop-dev/python-importtime-tree?style=flat-square" alt="Last commit"/></p>
<p align="center"><img src="assets/mark.svg" width="520" alt="Python Import Time Tree illustration"/></p>

## 🧭 Overview
Python Import Time Tree parses output from CPython's `-X importtime` option and presents nested imports with self and cumulative timings. It does not import or execute the target application.

## ✨ Features
- 🌳 Reconstruct nested import depth from CPython output
- ⏱️ Show self-time and cumulative-time values in microseconds
- 📦 Export parsed rows as JSON for further analysis
- 🔒 Parse an existing log file; never execute the target code

## 🖥️ Demo
No hosted demo is provided. Run the tool locally using the quick-start command.

## 🚀 Quick Start
Requires Python 3.10 or newer.

```bash
python main.py importtime.log
```

Run the test suite with:

```bash
python -m unittest discover -s tests -v
```

## 🧰 Tech Stack
- Python standard library
- `argparse` CLI and `unittest`
- Read-only inspection by default

## 🗂️ Folder Structure
```text
.
├── .github/workflows/ci.yml
├── assets/mark.svg
├── tests/test_main.py
├── main.py
├── pyproject.toml
└── README.md
```

## 🗺️ Roadmap
- [ ] Add more edge-case fixtures
- [ ] Improve machine-readable output
- [ ] Keep the core workflow dependency-free

## 🤝 Contributing
Issues and focused pull requests are welcome. Add regression tests for parser and reporting changes.

## 📄 License
MIT License. See [LICENSE](LICENSE).

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f766e,100:0f172a&height=100&section=footer" alt="Animated wave footer"/></p>
