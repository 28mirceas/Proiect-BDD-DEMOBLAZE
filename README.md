# BDD Demoblaze Project – Test Automation with Behave & Selenium
![CI](https://github.com/28mirceas/BDD-Demoblaze-Automation-Testing/actions/workflows/behave-tests.yml/badge.svg)

## About the Project

This project was developed as part of my QA Automation portfolio to demonstrate practical experience in building a maintainable UI automation framework using Python, Selenium WebDriver, Behave (BDD), and the Page Object Model (POM).

## Description

This project represents an automated UI test suite developed using Behavior-Driven Development (BDD) with Behave and Selenium WebDriver, following the Page Object Model (POM) design pattern.

The framework automates core user journeys of the Demoblaze e-commerce application, including authentication, product navigation, cart management, and order placement.

The project is structured to be maintainable, scalable, and suitable for real-world QA Automation practices.

---

## Technologies Used

Python 3.13

Behave – BDD Framework

Selenium WebDriver

Page Object Model (POM)

Chrome WebDriver

Gherkin Syntax

---

## Installation

### 1. Clone the project

```bash
git clone https://github.com/28mirceas/BDD-Demoblaze-Automation-Testing.git
cd BDD-Demoblaze-Automation-Testing
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Install ChromeDriver

Make sure ChromeDriver is installed and compatible with your Chrome browser version.

Driver configuration can be adjusted in:

```bash
browser.py
```

---

## Running the Tests

Run all tests:

```bash
behave
```

Run tests with verbose output:

```bash
behave -v
```

Run a specific feature:

```bash
behave features/login.feature
```

Run a specific scenario group:

```bash
behave --tags=login
```

```bash
behave --tags=negativeLogin
```

```bash
behave --tags=addProductToCart
```

```bash
behave --tags=deleteProductFromCart
```

```bash
behave --tags=placeAnOrder
```

---

## Included Test Scenarios

### Login

• Login with valid credentials

• Login with invalid password

### Categories

• Open product details page

• Add product to cart

### Shopping Cart

• Delete product from cart

• Verify product removal

### Order Placement

• Add product to cart

• Complete purchase form

• Place order successfully

• Verify successful purchase confirmation

---

## Project Structure

```bash
BDD-Demoblaze-Project/
│ 
│ behave.ini
│ browser.py
│ README.md
│ requirements.txt
│ environment.py
│
├── features/
│   │ cart.feature
│   │ categories.feature
│   │ login.feature
│   
│
├── pages/
│   │ base_page.py
│   │ cart_page.py
│   │ categories_page.py
│   │ login_page.py
│
└── steps/
    │ cart_steps.py
    │ categories_steps.py
    │ login_steps.py
```

---

## Page Object Model

All pages are implemented using the Page Object Model pattern.

Each page object contains:

• element locators

• page-specific actions

• reusable methods

Implemented Page Objects:

• login_page.py

• categories_page.py

• cart_page.py

• base_page.py

---

## Behave Hooks

The project uses Behave hooks defined in:

```bash
features/environment.py
```

Implemented hooks:

• before_scenario

• after_scenario

These hooks are responsible for:

• browser initialization

• browser cleanup

• automatic login for tagged scenarios

• shopping cart cleanup before execution

---

## Framework Features

• Explicit Waits

• JavaScript Alert Handling

• Dynamic Locators

• Parameterized BDD Scenarios

• Shopping Cart Cleanup

• Reusable Page Objects

• End-to-End Purchase Flow

• Data Isolation Between Tests

---

## Test Coverage

The framework covers the following business flows:

✓ User Authentication

✓ Product Navigation

✓ Product Details Validation

✓ Add Product to Cart

✓ Delete Product from Cart

✓ Purchase Order Submission

✓ Purchase Confirmation Validation

---

## Author

Mircea Sava

QA Automation Portfolio Project

---

## License

[MIT](https://choosealicense.com/licenses/mit/)
