const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const crypto = require('crypto');

const app = express();
const port = 3002;
const host = "localhost";

// Middleware to parse request body
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

// Hashing APIs
app.post('/hash/:type', (req, res) => {
  const { type } = req.params;
  const { text } = req.body;
  const allowedHashes = ['md5', 'sha1'];

  if (!allowedHashes.includes(type)) {
    return res.status(400).send({ error: "Invalid hash type. Use \"md5\" or \"sha1\"." });
  }

  try {
    const hash = crypto.createHash(type).update(text).digest('hex');
    res.json({ hash });
  } catch (error) {
    res.status(500).send({ error: error.message });
  }
});
// AES Encryption API
app.post('/encrypt/aes', (req, res) => {
  const { text, key } = req.body;

  // Ensure the key is exactly 32 bytes for AES-256
  if (key.length !== 32) {
    return res.status(400).json({ error: 'Invalid key length. AES-256 requires a 32-byte key.' });
  }

  const iv = Buffer.alloc(16, 0); // Initialization vector (16 bytes for AES-256-CBC)

  try {
    const cipher = crypto.createCipheriv('aes-256-cbc', Buffer.from(key, 'utf-8'), iv);
    let encrypted = cipher.update(text, 'utf8', 'base64');
    encrypted += cipher.final('base64');
    res.json({ encrypted });
  } catch (error) {
    res.status(500).send({ error: `Encryption failed: ${error.message}` });
  }
});

// AES Decryption API
app.post('/decrypt/aes', (req, res) => {
  const { text, key } = req.body;

  // Ensure the key is exactly 32 bytes for AES-256
  if (key.length !== 32) {
    return res.status(400).json({ error: 'Invalid key length. AES-256 requires a 32-byte key.' });
  }

  const iv = Buffer.alloc(16, 0); // Initialization vector (16 bytes for AES-256-CBC)

  try {
    const decipher = crypto.createDecipheriv('aes-256-cbc', Buffer.from(key, 'utf-8'), iv);
    let decrypted = decipher.update(text, 'base64', 'utf8');
    decrypted += decipher.final('utf8');
    res.json({ decrypted });
  } catch (error) {
    res.status(500).send({ error: `Decryption failed: ${error.message}` });
  }
});

// DES Encryption API
app.post('/encrypt/des', (req, res) => {
  try {
    const { text, key } = req.body;

    // Ensure the key is exactly 8 bytes (56 bits)
    if (key.length !== 8) {
      return res.status(400).send({ error: "Invalid key length for DES. Use an 8-byte key." });
    }

    // ECB mode does not use an IV
    const cipher = crypto.createCipheriv('des-ecb', Buffer.from(key, 'utf8'), null);
    let encrypted = cipher.update(text, 'utf8', 'base64');
    encrypted += cipher.final('base64');

    res.json({ encrypted });
  } catch (error) {
    res.status(500).json({ error: `Encryption failed: ${error.message}` });
  }
});

// DES Decryption API
app.post('/decrypt/des', (req, res) => {
  try {
    const { text, key } = req.body;

    // Ensure the key is exactly 8 bytes (56 bits)
    if (key.length !== 8) {
      return res.status(400).send({ error: "Invalid key length for DES. Use an 8-byte key." });
    }

    // ECB mode does not use an IV
    const decipher = crypto.createDecipheriv('des-ecb', Buffer.from(key, 'utf8'), null);
    let decrypted = decipher.update(text, 'base64', 'utf8');
    decrypted += decipher.final('utf8');

    res.send({ decrypted });
  } catch (error) {
    res.status(500).send({ error: `Decryption failed: ${error.message}` });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Crypto API running at http://${host}:${port}`);
});
