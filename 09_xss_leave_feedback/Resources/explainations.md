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

## Why Does This Happen?

1. **No input sanitization**: The application accepts script tags without filtering or encoding
2. **Missing output encoding**: User input is displayed without HTML encoding
3. **Lack of input validation**: No checks for potentially dangerous characters or patterns
4. **Stored XSS risk**: If saved, the script could execute for other users viewing the feedback

## How to Prevent It

1. **Sanitize all inputs**: Remove or encode HTML tags and special characters
2. **Encode outputs**: HTML-encode all user-generated content before displaying
3. **Use Content Security Policy**: Implement CSP headers to restrict script execution
4. **Validate input types**: Ensure inputs match expected formats (name should only contain letters)
5. **Use security frameworks**: Employ frameworks with built-in XSS protection
