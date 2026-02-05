# Forgot Password Vulnerability

## Discovery Process

1. Click on **Sign in** button
2. Click on **Forgot password** button
3. Inspect the page and find the hidden input tag:

```html
<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
```

## Vulnerability Details

- **Issue**: Hidden input field contains a sensitive email value
- **Email exposed**: `webmaster@borntosec.com`

## Exploitation

1. Modify the hidden input field value to another email address
2. Submit the password reset form
3. Successfully obtained the flag
