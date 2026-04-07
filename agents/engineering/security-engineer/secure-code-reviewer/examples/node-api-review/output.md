# Secure Code Review: Node.js API Endpoints

## Finding 1: SQL Injection (CRITICAL)

**Location:** `POST /api/users/search`
**Issue:** User input is directly concatenated into a SQL query string.
**Impact:** Full database compromise — attacker can extract, modify, or delete all data.

**Vulnerable code:**
```javascript
const query = `SELECT * FROM users WHERE name LIKE '%${req.body.name}%'`;
```

**Fixed code:**
```javascript
app.post('/api/users/search', (req, res) => {
  const { name } = req.body;
  if (typeof name !== 'string' || name.length > 100) {
    return res.status(400).json({ error: 'Invalid name parameter' });
  }
  db.query(
    'SELECT id, name, email FROM users WHERE name LIKE $1 LIMIT 50',
    [`%${name}%`],
    (err, results) => {
      if (err) return res.status(500).json({ error: 'Internal error' });
      res.json(results.rows);
    }
  );
});
```

## Finding 2: Path Traversal (CRITICAL)

**Location:** `GET /api/file`
**Issue:** Unsanitized file path allows `../../etc/passwd` style attacks.
**Impact:** Arbitrary file read from the server filesystem.

**Vulnerable code:**
```javascript
const filePath = req.query.path;
res.sendFile(filePath);
```

**Fixed code:**
```javascript
const path = require('path');

const ALLOWED_DIR = path.resolve(__dirname, 'public/uploads');

app.get('/api/file', (req, res) => {
  const requested = path.resolve(ALLOWED_DIR, path.basename(req.query.path));
  if (!requested.startsWith(ALLOWED_DIR)) {
    return res.status(403).json({ error: 'Access denied' });
  }
  res.sendFile(requested);
});
```

## Finding 3: Hardcoded JWT Secret (HIGH)

**Location:** `POST /api/login`
**Issue:** JWT signing key `'mysecret'` is hardcoded. Anyone with source access can forge tokens.
**Impact:** Authentication bypass, privilege escalation.

**Fixed code:**
```javascript
const JWT_SECRET = process.env.JWT_SECRET; // min 256-bit, rotated quarterly
const JWT_EXPIRY = '15m';

app.post('/api/login', async (req, res) => {
  const user = await db.findUser(req.body.username);
  if (!user) return res.status(401).json({ error: 'Invalid credentials' });

  const valid = await bcrypt.compare(req.body.password, user.passwordHash);
  if (!valid) return res.status(401).json({ error: 'Invalid credentials' });

  const token = jwt.sign({ id: user.id, role: user.role }, JWT_SECRET, {
    expiresIn: JWT_EXPIRY,
    algorithm: 'HS256',
  });
  res.json({ token });
});
```

## Finding 4: Plaintext Password Comparison (HIGH)

**Location:** `POST /api/login`
**Issue:** Passwords are compared as plaintext (`user.password === req.body.password`), meaning they are stored unhashed.
**Impact:** Database breach exposes all user passwords in cleartext.
**Fix:** Store bcrypt hashes. Compare with `bcrypt.compare()` as shown above.

## Finding 5: Missing Error Handling (MEDIUM)

**Location:** All endpoints
**Issue:** No error handling on `db.query` callback. Errors leak stack traces to clients.
**Fix:** Return generic error responses. Log details server-side only.

## Summary

| # | Finding | Severity | OWASP Category |
|---|---------|----------|----------------|
| 1 | SQL Injection | Critical | A03:2021 Injection |
| 2 | Path Traversal | Critical | A01:2021 Broken Access Control |
| 3 | Hardcoded JWT Secret | High | A02:2021 Cryptographic Failures |
| 4 | Plaintext Passwords | High | A02:2021 Cryptographic Failures |
| 5 | Missing Error Handling | Medium | A05:2021 Security Misconfiguration |
