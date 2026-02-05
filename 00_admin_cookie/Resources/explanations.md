# Admin Cookie Vulnerability

## Discovery Process

1. Inspect browser cookies
2. Found cookie with name `I_am_admin` and value `b326b5062b2f0e69046810717534cb09`
3. Recognized the value as an MD5 hash (32 hexadecimal characters)

## Cookie Details

- **Name**: `I_am_admin`
- **Value**: `b326b5062b2f0e69046810717534cb09`

## MD5 Hash Analysis

- **Hash found**: `b326b5062b2f0e69046810717534cb09`
- **Hash type**: MD5
- **Tool used**: [CrackStation](https://crackstation.net/)
- **Decrypted value**: `false`
- **Encrypted `true`**: `b326b5062b2f0e69046810717534cb09`

| Action | Input | Output |
|--------|-------|--------|
| Decrypt | `b326b5062b2f0e69046810717534cb09` | `false` |
| Encrypt | `true` | `b326b5062b2f0e69046810717534cb09` |

## Exploitation

1. Replace cookie value with MD5 hash of `true`
2. Set `I_am_admin` cookie to `b326b5062b2f0e69046810717534cb09`
3. Refresh the page
4. Successfully obtained the flag

## Why Does This Happen?

1. **Client-side authentication**: The application stores admin status in a cookie that users can modify
2. **Weak hashing**: MD5 is an old, broken algorithm that can be easily cracked
3. **Predictable values**: Using simple words like "true" and "false" makes it trivial to guess
4. **No server-side verification**: The server blindly trusts the cookie value without validation

## How to Prevent It

1. **Never store authentication state in cookies**: Use server-side sessions instead
2. **Use strong cryptography**: Replace MD5 with bcrypt, Argon2, or scrypt for passwords
3. **Implement secure session management**: Store user roles on the server, not in cookies
4. **Use secure cookie attributes**: Set `httpOnly`, `secure`, and `sameSite` flags
5. **Always validate on the server**: Never trust client-provided data, always verify permissions server-side
