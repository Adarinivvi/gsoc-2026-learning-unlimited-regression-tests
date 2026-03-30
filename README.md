# GSoC 2026: Regression Tests Expansion for Learning Unlimited

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/Django-4.2-green.svg)](https://www.djangoproject.com/)

## 🎯 Project Overview

This repository contains my **Google Summer of Code 2026** proposal for **Learning Unlimited** focused on expanding test coverage for the ESP website.

### Mission
Building a robust, well-tested codebase that enables Learning Unlimited chapters to run educational programs reliably.

### Goals
- 📊 Increase code coverage metrics across legacy modules
- 🧪 Create comprehensive unit tests for critical components
- 🤖 Fix failing Selenium browser tests
- 📝 Document testing patterns for future contributors
- 🔄 Integrate tests with GitHub Actions CI/CD

---

## 📁 Repository Structure
├── docs/ 
├── examples/ 
├── scripts/ 
└── .github/

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- Git
- Virtual environment tool (venv or conda)

### Setup

```bash
# Clone the repository
git clone https://github.com/your-username/gsoc-2026-learning-unlimited-regression-tests.git
cd gsoc-2026-learning-unlimited-regression-tests

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run example tests
pytest examples/
```

🛠️ Technologies Used
Python 3.9+ - Core language

Django - Web framework

pytest - Testing framework

Selenium - Browser automation

GitHub Actions - CI/CD

Codecov - Coverage tracking


🙏 Acknowledgments

Miles Calabresi - Primary Mentor

Will Gearty - Secondary Mentor

Learning Unlimited for the opportunity

Google Summer of Code for the program
