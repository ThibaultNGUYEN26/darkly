# Local File Inclusion (LFI) Vulnerability

## Discovery Process

1. Identify pages that load content dynamically using URL parameters
2. Notice a `page` parameter in the URL that might be vulnerable
3. Attempt to exploit Local File Inclusion (LFI) vulnerability

## Vulnerability Details

- **Issue**: The application does not properly sanitize file path inputs
- **Attack vector**: Directory traversal using `../` sequences
- **Target file**: `/etc/passwd` (common Unix/Linux system file)

## Exploitation

1. Test different directory traversal depths to locate `/etc/passwd`:
   - Try `?page=../etc/passwd`
   - Try `?page=../../etc/passwd`
   - Try `?page=../../../etc/passwd`
   - Continue until finding the correct depth

2. Create a Python script to automate the testing process
3. The script tests increasing depths until the flag is found
4. Successfully obtained the flag when the correct path depth was reached
