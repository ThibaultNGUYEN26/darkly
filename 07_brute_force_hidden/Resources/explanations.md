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
