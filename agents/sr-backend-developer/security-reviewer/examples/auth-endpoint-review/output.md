# Security Review: Authentication Endpoints

**Scope:** `/api/auth/register`, `/api/auth/login`, `/api/auth/refresh`
**Date:** 2024-03-15
**Reviewer:** Security Review Agent

## Findings

### 1. Password Hashing Configuration (HIGH)

**Current:** bcrypt with default rounds (10)
**Recommendation:** Increase to 12 rounds minimum. Consider migrating to Argon2id.

```typescript
// Before
const hash = await bcrypt.hash(password, 10);

// After
const hash = await bcrypt.hash(password, 12);

// Preferred: Argon2id
import argon2 from 'argon2';
const hash = await argon2.hash(password, {
  type: argon2.argon2id,
  memoryCost: 65536,
  timeCost: 3,
  parallelism: 4,
});
```

### 2. JWT Token Lifetime (MEDIUM)

**Current:** Access token expires in 24 hours
**Recommendation:** Reduce to 15 minutes. Use refresh tokens for session continuity.

```typescript
const accessToken = jwt.sign(payload, ACCESS_SECRET, { expiresIn: '15m' });
const refreshToken = jwt.sign({ id: user.id }, REFRESH_SECRET, { expiresIn: '7d' });
```

### 3. Missing Rate Limiting on Login (HIGH)

**Current:** No rate limiting on `/api/auth/login`
**Recommendation:** Add per-IP and per-account rate limiting.

```typescript
import rateLimit from 'express-rate-limit';

const loginLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 5,
  keyGenerator: (req) => req.body.email || req.ip,
  message: { error: 'Too many login attempts. Try again in 15 minutes.' },
});

app.post('/api/auth/login', loginLimiter, loginHandler);
```

### 4. Refresh Token Not Stored Server-Side (HIGH)

**Current:** Refresh tokens are stateless JWTs with no server-side tracking
**Risk:** Cannot revoke compromised refresh tokens
**Recommendation:** Store refresh token hashes in the database. Implement token rotation.

```typescript
// On login: store refresh token hash
await db.query(
  'INSERT INTO refresh_tokens (user_id, token_hash, expires_at) VALUES ($1, $2, $3)',
  [user.id, sha256(refreshToken), expiresAt]
);

// On refresh: validate against DB, rotate token
await db.query('DELETE FROM refresh_tokens WHERE token_hash = $1', [sha256(oldToken)]);
```

### 5. Missing Account Lockout (MEDIUM)

**Current:** No lockout after failed attempts
**Recommendation:** Lock account after 5 consecutive failures. Require email verification to unlock.

### 6. Registration Endpoint Leaks User Existence (LOW)

**Current:** Returns "Email already registered" on duplicate
**Recommendation:** Return generic message. Send email to existing users informing them of the attempt.

```typescript
// Always return the same response
res.json({ message: 'If this email is valid, you will receive a confirmation.' });
```

## Summary

| # | Finding | Severity | Status |
|---|---------|----------|--------|
| 1 | Weak bcrypt rounds | High | Fix required |
| 2 | Long-lived access tokens | Medium | Fix required |
| 3 | No login rate limiting | High | Fix required |
| 4 | Stateless refresh tokens | High | Fix required |
| 5 | No account lockout | Medium | Recommended |
| 6 | User enumeration | Low | Recommended |
