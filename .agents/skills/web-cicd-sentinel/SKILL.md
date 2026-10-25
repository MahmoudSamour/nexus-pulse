---
name: web-cicd-sentinel
description: Runbook for executing web integrity tests and validating GitHub Pages CI/CD deployment readiness under Tariq.
---

# 💻 Web CI/CD Sentinel Runbook (Tariq)

Use this skill before committing or pushing changes to the `nexus-pulse` repository.

## 1. Run Web Integrity & Standards Tests
```bash
python3 -m unittest tests/test_web_integrity.py
```

## 2. Check Static Assets & GitHub Pages Pre-requisites
```bash
test -f index.html && test -f .nojekyll && echo "✅ Web hub distribution ready."
```
