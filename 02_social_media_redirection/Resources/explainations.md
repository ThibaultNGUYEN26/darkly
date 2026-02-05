# Social Media Redirection Vulnerability

## Discovery Process

1. Inspect a social media logo on the page
2. Examine the link/redirection URL

## Vulnerability Details

- **Issue**: Social media links can be manipulated to redirect users to malicious sites
- **Example**: Changed Facebook redirection to Google

## Exploitation

1. Modify the social media link redirection URL
2. Change the target URL (e.g., from Facebook to Google)
3. Successfully obtained the flag

## Why Does This Happen?

1. **Open redirect vulnerability**: The application accepts any URL for redirection without validation
2. **Lack of URL whitelist**: No check to ensure links point to legitimate social media sites
3. **User-controllable redirects**: Attackers can modify links to redirect to malicious sites
4. **Trust in link integrity**: The application assumes social media links won't be tampered with

## How to Prevent It

1. **Use a whitelist**: Only allow redirects to approved domains (facebook.com, twitter.com, etc.)
2. **Validate redirect URLs**: Check that URLs match expected patterns before redirecting
3. **Use direct links**: Hardcode social media URLs instead of making them dynamic
4. **Implement URL validation**: Verify protocol (https) and domain before any redirect
5. **Avoid user-controlled redirects**: Don't allow users to specify arbitrary redirect targets
