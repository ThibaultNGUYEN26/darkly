# XSS Feedback Form Vulnerability

## Discovery Process

1. Click on the **Feedback** page
2. Observe the feedback form with input fields
3. Identify that form inputs might be vulnerable to XSS

## Vulnerability Details

- **Issue**: Input fields do not properly sanitize user input
- **Attack vector**: Script injection through form fields
- **Vulnerable field**: Name field

## Exploitation

1. Navigate to the feedback form
2. Enter a script tag in the name field:
```html
script
```
3. Submit the form
4. Successfully obtained the flag
