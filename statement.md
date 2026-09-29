# Statement of Work & Problem Definition

## Project Title
**Automated Teller Machine (ATM) System with NumPy Transaction Analytics**

---

## 1. Problem Statement
Traditional banking systems require manual teller interactions for basic financial operations such as balance inquiries, cash deposits, and cash withdrawals. In modern banking infrastructure, Automated Teller Machines (ATMs) provide 24/7 self-service convenience to banking customers. However, standard educational software implementations of ATM systems often lack analytical reporting capabilities. 

This project addresses the need for a secure, user-friendly, and analytical terminal-based ATM software system. It provides basic transaction capabilities (deposit, withdrawal, balance inquiry) while integrating real-time transaction analysis powered by numerical computing tools (NumPy) to compute statistical metrics such as transaction counts, net totals, peak transaction amounts, and average transaction values.

---

## 2. Project Scope
The scope of the **ATM System with NumPy Transaction Analytics** includes:
* **User Authentication:** Secure PIN verification mechanism to validate customer identity before granting access to account menu options.
* **Account Balance Management:** Real-time balance retrieval and display.
* **Deposit Management:** Cash deposit processing with dynamic balance calculation, transaction history logging, and minimum deposit threshold enforcement (Minimum: ₹100).
* **Withdrawal Management:** Cash withdrawal processing with minimum withdrawal limits (Minimum: ₹100), automated insufficient balance checks, and balance updating.
* **Transaction Analytics:** Analytical reporting using Python's `numpy` library to aggregate and compute metrics across transaction histories (Count, Net Amount, Max, Min, Mean).
* **Session Lifecycle:** Clean session navigation and exit functionality timestamped using Python's `datetime` module.

*Out of Scope for current version:* Hardware integration (card reader, cash dispenser), multi-account database persistence, and network/bank server network communication.

---

## 3. Target Users
* **Banking Customers:** Individuals seeking quick, terminal-based self-service banking operations (deposits, withdrawals, balance checks).
* **Financial Auditors & Account Holders:** Users who require immediate, session-based statistical summaries of their financial transactions.
* **Academic & Software Evaluators:** Instructors and reviewers evaluating Python console applications, control flows, and NumPy array operations.

---

## 4. High-Level Features
1. **Secure PIN Authentication:** Validates user credentials against configured authentication parameters prior to granting system access.
2. **Interactive Menu Interface:** Modular command-line navigation menu allowing seamless selection of banking operations.
3. **Real-Time Balance Tracker:** Immediate updates to account balance following financial transactions.
4. **Conditional Deposit & Withdrawal Logic:** Input validation enforcing minimum transaction limits (₹100) and preventing overdrafts/insufficient balance errors.
5. **NumPy Transaction Analytics:** Array-based computation of statistical insights across logged transaction history vectors.
6. **Timestamped Session Logging:** Capture of system execution timestamps using native `datetime` libraries.
