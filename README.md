# Selenium WebDriver Basics

A small, single-script Selenium WebDriver example demonstrating fundamental
browser-automation concepts: element location, explicit waits, dropdown
handling and assertions.

> Personal practice / portfolio project, not connected to any employer's
> systems or confidential data. It uses the same public
> [XYZ Bank demo](https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login)
> sandbox as the companion Cypress project, to demonstrate basic Selenium
> WebDriver fundamentals alongside the Cypress automation framework.

## Why this exists

This repo intentionally stays "basic" -- a single script, no page-object
framework -- to show working knowledge of Selenium WebDriver locators and
browser automation fundamentals, distinct from the fuller Cypress POM
framework in
[`cypress-portfolio-automation`](https://github.com/tanzeelashaik02-cell/cypress-portfolio-automation).

## What it does

1. Opens the banking demo and navigates to **Customer Login**.
2. Selects a customer from the dropdown (`Select` class usage).
3. Logs in and waits for the account dashboard to load.
4. Asserts the welcome banner and account summary are visible.

## Run it

```bash
pip install -r requirements.txt
python test_customer_login_basic.py
```

Requires a local Chrome browser. Selenium 4's built-in Selenium Manager
downloads a matching chromedriver automatically.
