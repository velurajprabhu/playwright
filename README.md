# 🧪 Playwright Python Automation Framework
---

## ⚙️ Prerequisites

* Python **3.10+**
* pip
* Node.js (for Playwright browsers)

---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository

```
git clone https://github.com/velurajprabhu/playwright.git
cd project-root
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Install Playwright Browsers

```
playwright install
```

---

## 🧪 Running Tests

### ▶️ Run All Tests

```
behave
```

---

### 🎯 Run Specific Tag

```
behave --tags=@login
```

---

### 📊 Run with Allure Reporting

```
behave -f allure_behave.formatter:AllureFormatter -o reports/
```

---

## 📊 View Allure Report (Local)

```
allure serve reports/
```

---

## 🌐 Live Report

```
https://velurajprabhu.github.io/playwright/builds/tests/
```

---
