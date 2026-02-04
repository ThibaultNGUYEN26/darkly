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
