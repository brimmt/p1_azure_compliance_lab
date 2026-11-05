![Python CI](https://github.com/brimmt/p1_azure_compliance_lab/actions/workflows/ci.yml/badge.svg)



# Project 1 — Azure Compliance Lab
**Project Status: Completed (V1)**

A personal engineering project and the first in my Engineering Boot Camp series, focused on strengthening my software engineering skills through hands-on development and learning how different technologies and systems work together.

Built with Python, Terraform, Streamlit, and the Azure SDK to evaluate Azure resources against a custom security baseline.

## Technologies
- Python / Azure SDK
- Terraform / Microsoft Azure
- Streamlit / openpyxl
- GitHub Actions / pytest / Ruff

## Features
- Azure resource discovery and configuration validation
- Seven custom compliance rules covering tags and storage security
- PASS/FAIL findings with remediation guidance
- Interactive Streamlit dashboard
- Excel report generation and downloads
- Automated CI checks with GitHub Actions

## Getting Started

```bash
git clone https://github.com/brimmt/p1_azure_compliance_lab.git
cd p1_azure_compliance_lab
pip install -r requirements.txt
az login
streamlit run streamlit_logic.py
```

*Requires an Azure subscription and locally configured environment variables.*

## Developer Retrospective

**What I Learned:** Azure SDK integration, Terraform provisioning, Python modular development, Excel automation, Streamlit session state, Git workflows, and CI/CD fundamentals.

**Challenges:** Debugging Python logic, understanding Azure resource properties, managing data between modules, and learning Streamlit.

**Future Enhancements:** AI-assisted remediation, multi-model evaluation, expanded compliance rules, and dashboard improvements.

---

**Project Status: Completed (V1)**

---
