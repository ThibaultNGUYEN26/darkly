# Admin User Vulnerability

## Discovery Process

1. Navigate to `/robots.txt`
2. Found reference to `/whatever`
3. Access `/whatever` and find `README.md`
4. Discovered credentials in README:
   ```
   root:437394baff5aa33daa618be47b75cb49
   ```

## Hash Cracking

- **Hash found**: `437394baff5aa33daa618be47b75cb49`
- **Hash type**: MD5
- **Tool used**: [CrackStation](https://crackstation.net/)
- **Cracked password**: `qwerty123@`

## Exploitation

1. Navigate to `/admin`
2. Login with discovered credentials:
   - **Username**: `root`
   - **Password**: `qwerty123@`
3. Successfully obtained the flag

## Why Does This Happen?

1. **Information disclosure**: Sensitive files (README, robots.txt) expose internal directories and credentials
2. **Weak password storage**: Password stored as MD5 hash which is easily crackable
3. **Publicly accessible credentials**: Admin credentials stored in plain text files accessible via web
4. **Poor file management**: Sensitive files left in web-accessible directories

## How to Prevent It

1. **Secure robots.txt**: Don't list sensitive directories in robots.txt - use proper access controls instead
2. **Remove sensitive files**: Never store credentials in web-accessible locations
3. **Use strong password hashing**: Replace MD5 with bcrypt, Argon2, or scrypt
4. **Implement proper access controls**: Restrict access to admin areas and sensitive files
5. **Regular security audits**: Scan for exposed sensitive files and misconfigurations
