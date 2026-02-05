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

## Why Does This Happen?

1. **Insufficient input validation**: The application doesn't sanitize file path inputs
2. **Direct file inclusion**: User input is directly used to construct file paths
3. **No path restriction**: No checks to ensure files are within allowed directories
4. **Directory traversal allowed**: The `../` sequence isn't filtered or blocked

## How to Prevent It

1. **Use a whitelist**: Only allow specific, pre-defined file names or pages
2. **Avoid direct file paths**: Use indirect references (IDs) that map to safe file paths
3. **Sanitize inputs**: Remove or block `../`, `..\\`, and other traversal sequences
4. **Use absolute paths**: Construct file paths from a safe base directory only
5. **Implement access controls**: Restrict file system access to only necessary directories
