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
