# Automated Teller Machine (ATM) System with NumPy Transaction Analytics

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Library](https://img.shields.io/badge/NumPy-1.20%2B-green.svg)
![Course](https://img.shields.io/badge/VITyarthi-Build%20Your%20Own%20Project-orange.svg)

A terminal-based Automated Teller Machine (ATM) software application built with Python and NumPy, featuring secure user authentication, deposit/withdrawal workflows, balance checks, and real-time statistical analytics on transaction history.

---

## 📌 Project Overview
This project delivers a functional simulation of an ATM system designed for console interactions. Beyond fundamental banking operations (PIN authentication, balance inquiries, cash deposits, and cash withdrawals), the system integrates statistical data analysis using the **NumPy** library. Users can view statistical breakdowns of their session transactions, including total transaction count, net flow, peak transaction value, minimum transaction value, and average transaction size.

---

## ✨ Features
* 🔒 **PIN Authentication:** Validates user authorization (`PIN: 6267`) before granting access to account operations.
* 💳 **Balance Checking:** Instantly displays current account balance.
* 💵 **Deposit Funds:** Enables cash deposits with minimum limit validation (Minimum ₹100) and instant account updates.
* 🏧 **Withdraw Cash:** Facilitates cash withdrawals with minimum limit checks (Minimum ₹100) and automated overdraft protection (insufficient balance detection).
* 📊 **Transaction Analytics (NumPy):** Converts transaction logs into 1D NumPy arrays to compute:
  * Total number of transactions
  * Net transaction sum
  * Largest transaction value
  * Smallest transaction value
  * Average transaction value
* ⏱️ **Timestamping:** Captures transaction execution time using Python's `datetime` module.

---

## 🛠️ Technologies & Tools
* **Programming Language:** Python 3.x
* **Core Libraries:**
  * `numpy`: Array creation, mathematical aggregations (`sum`, `max`, `min`, `mean`).
  * `datetime`: System date and time tracking.
* **Development Environment:** VS Code / Terminal / Any standard Python IDE.
* **Version Control:** Git & GitHub.

---

## 📂 Repository Structure
```text
├── statement.md              # Project Problem Statement, Scope, Target Audience
├── README.md                 # Project Overview & Setup Instructions
├── atm_system.py             # Main Python Source Code Implementation
└── ATM_System_Project_Report.pdf  # Comprehensive Project Submission Report
```

---

## ⚙️ Installation & Running Guide

### Prerequisites
* Python 3.8 or higher installed on your system.
* `pip` package manager.

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/atm-vityarthi-project.git
cd atm-vityarthi-project
```

### Step 2: Install Dependencies
Install NumPy using pip:
```bash
pip install numpy
```

### Step 3: Execute the Project
Run the main script:
```bash
python atm_system.py
```

---

## 🧪 Instructions for Testing & Sample Outputs

### Default System Parameters
* **Default Account Balance:** ₹1,00,000
* **Default System PIN:** `6267`
* **Minimum Deposit/Withdrawal Amount:** ₹100

### Test Cases

#### Test Case 1: Successful Authentication & Balance Inquiry
* **Action:** Enter PIN `6267`, select menu option `1`.
* **Expected Output:**
  ```text
  hello customer
  your balance is:- 100000
  ```

#### Test Case 2: Cash Deposit (Above ₹100)
* **Action:** Select option `2`, enter deposit amount `500`.
* **Expected Output:**
  ```text
  miminum deposit amount is 100
  enter deposit amount:- 500
  Amount deposit sucesssfully
  account balance is:- 100500.0
  ```

#### Test Case 3: Cash Withdrawal with Insufficient Balance Protection
* **Action:** Select option `3`, enter withdrawal amount `200000`.
* **Expected Output:**
  ```text
  minimum withdraw amount is 100Rs
  enter withdraw amount:- 200000
  insufficient balance
  ```

#### Test Case 4: NumPy Transaction Analytics
* **Action:** Perform deposit of `500` and withdrawal of `200`, then select option `4`.
* **Expected Output:**
  ```text
  transaction analysis
  total transaction : 2
  total transaction amount: 300.0
  largest transaction : 500.0
  Smallest transaction : -200.0
  Average tramsaction : 150.0
  ```

---

## 📜 Academic Compliance
This repository is created in compliance with the **VITyarthi Build Your Own Project (BYOP)** guidelines for flipped course evaluations.
