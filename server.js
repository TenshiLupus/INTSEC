const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const crypto = require('crypto');

const app = express();
const port = 3002;
const host = "localhost";

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
  next();
});

app.options('*', (req, res) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
  res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept, Authorization');
  res.sendStatus(200);
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.message);
  res.status(500).json({ error: 'Internal Server Error' });
});

// Hashing API
app.post('/hash/:type', (req, res) => {
  const { type } = req.params;
  const { text } = req.body;

  const allowedHashes = ['md5', 'sha1', 'sha256'];
  if (!allowedHashes.includes(type)) {
    return res.status(400).json({ error: "Invalid hash type. Use 'md5', 'sha1', or 'sha256'." });
  }

  try {
    const hash = crypto.createHash(type).update(text, 'utf8').digest('hex');
    res.json({ hash });
  } catch (err) {
    res.status(500).json({ error: 'Error generating hash' });
  }
});

// DES Encryption/Decryption (for legacy compatibility, not recommended for secure systems)
app.post('/encrypt/des', (req, res) => {
  const { text, key } = req.body;
  try {
    const cipher = crypto.createCipheriv('des-ecb', Buffer.from(key, 'hex'), null);
    const encrypted = Buffer.concat([cipher.update(text, 'utf8'), cipher.final()]).toString('base64');
    res.json({ encrypted });
  } catch (err) {
    res.status(500).json({ error: 'Error encrypting data' });
  }
});

app.post('/decrypt/des', (req, res) => {
  const { text, key } = req.body;
  try {
    const decipher = crypto.createDecipheriv('des-ecb', Buffer.from(key, 'hex'), null);
    const decrypted = Buffer.concat([decipher.update(Buffer.from(text, 'base64')), decipher.final()]).toString('utf8');
    res.json({ decrypted });
  } catch (err) {
    res.status(500).json({ error: 'Error decrypting data' });
  }
});

// AES Encryption/Decryption
app.post('/encrypt/aes', (req, res) => {
  const { text, key } = req.body;
  try {
    const iv = crypto.randomBytes(16);
    const cipher = crypto.createCipheriv('aes-256-cbc', crypto.createHash('sha256').update(key).digest(), iv);
    const encrypted = Buffer.concat([cipher.update(text, 'utf8'), cipher.final()]).toString('base64');
    res.json({ encrypted, iv: iv.toString('hex') });
  } catch (err) {
    res.status(500).json({ error: 'Error encrypting data' });
  }
});

app.post('/decrypt/aes', (req, res) => {
  const { text, key, iv } = req.body;
  try {
    const decipher = crypto.createDecipheriv(
      'aes-256-cbc',
      crypto.createHash('sha256').update(key).digest(),
      Buffer.from(iv, 'hex')
    );
    const decrypted = Buffer.concat([decipher.update(Buffer.from(text, 'base64')), decipher.final()]).toString('utf8');
    res.json({ decrypted });
  } catch (err) {
    res.status(500).json({ error: 'Error decrypting data' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Crypto API running at http://${host}:${port}`);
});
