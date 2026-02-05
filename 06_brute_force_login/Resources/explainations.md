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
