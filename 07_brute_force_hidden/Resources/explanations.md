# Brute Force Hidden Directories Vulnerability

## Discovery Process

1. Navigate to `/robots.txt`
2. Found reference to `/.hidden` directory
3. Discovered that `/.hidden` contains a README file
4. Identified that the directory has multiple subdirectories, each containing README files

## Vulnerability Details

- **Issue**: Hidden directory structure exposed through robots.txt
- **Attack vector**: Recursive directory crawling to access all hidden content
- **Scale**: Multiple nested subdirectories with README files

## Exploitation

1. Create a Python script to recursively crawl all subdirectories
2. Read every README file in the directory structure
3. Save all README contents to `output.log`
4. Search through the output log to find the flag among the content
5. Successfully obtained the flag

## Why Does This Happen?

1. **Information disclosure via robots.txt**: Sensitive directories are listed in publicly accessible robots.txt
2. **Directory listing enabled**: Web server allows browsing of directory contents
3. **No access controls**: Hidden directories are accessible without authentication
4. **Security through obscurity**: Relying on "hidden" paths instead of proper access controls

## How to Prevent It

1. **Don't list sensitive paths in robots.txt**: Use proper authentication instead of obscurity
2. **Disable directory listing**: Configure web server to prevent directory browsing
3. **Implement authentication**: Require login credentials to access sensitive areas
4. **Use proper access controls**: Set file permissions and use .htaccess or server configs
5. **Remove sensitive files**: Don't store sensitive data in web-accessible directories
