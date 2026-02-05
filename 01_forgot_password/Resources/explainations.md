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

## Why Does This Happen?

1. **Client-side controls**: The application relies on hidden HTML fields that users can easily modify
2. **No server-side validation**: The server accepts whatever email is submitted without checking who requested it
3. **Trust in client data**: The application assumes users can't or won't modify hidden fields
4. **Lack of authentication**: No verification that the person requesting the reset owns the email account

## How to Prevent It

1. **Never use hidden fields for security**: Hidden fields are not secure and can be easily modified
2. **Implement proper authentication flow**: Users should enter their email in a visible field, not rely on pre-filled values
3. **Validate on the server**: Always verify user identity before processing password resets
4. **Use secure tokens**: Generate unique, time-limited tokens and send them only to the verified email
5. **Add rate limiting**: Prevent abuse by limiting password reset requests per IP/account
