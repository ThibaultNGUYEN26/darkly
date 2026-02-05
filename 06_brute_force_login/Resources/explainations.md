# Brute Force Login Vulnerability

## Discovery Process

1. Click on **Sign in** button
2. Analyze the login request structure:
```
http://10.13.200.245/index.php?page=signin&password={password}&Login=Login
```
3. Notice that the request works with any random password (returns a response)
4. Discovered that no username is required for the request

## Vulnerability Details

- **Issue**: Login endpoint lacks rate limiting and account lockout mechanisms
- **Attack vector**: Password can be brute-forced using dictionary attacks
- **Weakness**: No username validation required

## Exploitation

1. Download a list of known/common passwords (password dictionary)
2. Iterate through the password list, testing each one:
```bash
http://10.13.200.245/index.php?page=signin&password={password}&Login=Login
```
3. Search for the keyword `flag` in each response
4. When `flag` appears in the response, the correct password is found
5. Successfully found the password: `shadow`
6. Successfully obtained the flag

## Why Does This Happen?

1. **No rate limiting**: The server allows unlimited login attempts without delays or blocks
2. **Missing account lockout**: No mechanism to lock accounts after failed attempts
3. **No CAPTCHA**: No challenge-response test to prevent automated attacks
4. **Weak password**: Using common dictionary words makes brute force attacks trivial

## How to Prevent It

1. **Implement rate limiting**: Limit login attempts per IP address and per account
2. **Add account lockout**: Temporarily lock accounts after a threshold of failed attempts
3. **Use CAPTCHA**: Implement CAPTCHA after several failed login attempts
4. **Enforce strong passwords**: Require complex passwords that resist dictionary attacks
5. **Add delays**: Introduce progressive delays after each failed attempt
