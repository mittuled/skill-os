# Scenario: Secure Code Review of Node.js API

Review the following Express.js endpoint for security vulnerabilities:

```javascript
app.post('/api/users/search', (req, res) => {
  const query = `SELECT * FROM users WHERE name LIKE '%${req.body.name}%'`;
  db.query(query, (err, results) => {
    res.json(results);
  });
});

app.get('/api/file', (req, res) => {
  const filePath = req.query.path;
  res.sendFile(filePath);
});

app.post('/api/login', (req, res) => {
  const user = db.findUser(req.body.username);
  if (user && user.password === req.body.password) {
    const token = jwt.sign({ id: user.id, role: user.role }, 'mysecret');
    res.json({ token });
  }
});
```
