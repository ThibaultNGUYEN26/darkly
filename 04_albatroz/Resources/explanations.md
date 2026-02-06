# Albatroz Vulnerability

## Discovery Process

1. Click on `© BornToSec` link in the footer
2. Found a page displaying an Albatroz image
3. Inspect the image and discovered hidden requirements:
   - `You must come from : "https://www.nsa.gov/".`
   - `Let's use this browser : "ft_bornToSec". It will help you a lot.`

## Vulnerability Details

- **Issue**: Server-side validation based on HTTP headers (User-Agent and Referer)
- **Required User-Agent**: `ft_bornToSec`
- **Required Referer**: `https://www.nsa.gov/`

## Exploitation

1. Use cURL to spoof the required HTTP headers:

```bash
curl \
-H "User-agent: ft_bornToSec" \
-H "Referer: https://www.nsa.gov/" \
"http://10.11.200.35/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f" | grep flag
```

2. Successfully obtained the flag

## Why Does This Happen?

1. **Weak authentication mechanism**: Using HTTP headers (User-Agent, Referer) for access control
2. **Client-controlled headers**: These headers can be easily spoofed by attackers
3. **Security through obscurity**: Relying on "secret" requirements that are visible in HTML
4. **No real authentication**: No verification of user identity, just header checking

## How to Prevent It

1. **Never rely on HTTP headers for security**: User-Agent and Referer can be easily forged
2. **Implement proper authentication**: Use session-based or token-based authentication
3. **Server-side access control**: Verify user permissions on the server, not through headers
4. **Don't expose security requirements**: Avoid putting authentication hints in HTML comments
5. **Use strong authorization mechanisms**: Implement proper role-based access control (RBAC)
