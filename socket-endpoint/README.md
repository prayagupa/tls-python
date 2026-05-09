# Certificate Setup

## Generate a self-signed certificate

### 1. Generate a private key

```bash
openssl genrsa -out restapi.key 2048
```

Generates a **2048-bit RSA private key** and writes it to `restapi.key`.  
This key is used to sign the certificate and decrypt incoming TLS connections.

---

### 2. Create a Certificate Signing Request (CSR)

```bash
openssl req -new -key restapi.key -out restapi.csr \
  -subj "/C=US/ST=WA/L=SEA/O=upadhyay/OU=engineering/CN=localhost/emailAddress=upadhyay@upadhyay.com"
```

Creates a **CSR** using the private key. The `-subj` flag supplies the
Distinguished Name (DN) fields inline, avoiding interactive prompts.

#### `-subj` field reference

| Field | Short form | Example value | Description |
|---|---|---|---|
| Country | `C` | `US` | 2-letter ISO 3166 country code |
| State / Province | `ST` | `WA` | State or province name |
| Locality | `L` | `SEA` | City or locality name |
| Organization | `O` | `upadhyay` | Legal name of the organization |
| Organizational Unit | `OU` | `engineering` | Department or team within the org |
| Common Name | `CN` | `localhost` | **Hostname** the cert is issued for — must match the server address clients connect to |
| Email Address | `emailAddress` | `upadhyay@upadhyay.com` | Contact email for the cert owner |

> ⚠️ `CN` must match the hostname used by clients. For local testing use `localhost`.

---

### 3. Self-sign the certificate

```bash
openssl x509 -req -days 3650 -in restapi.csr -signkey restapi.key -out restapi.crt
```

Signs the CSR with the same private key, producing a **self-signed X.509 certificate** valid for 3650 days (10 years).  
Because there is no CA involved, clients must explicitly trust this certificate by loading it as their CA bundle.

---

## Verify the generated files

```bash
ls -l conf/
.rw-r--r--@ 1.4k upadhyay  8 May 21:53  restapi.crt
.rw-r--r--@ 1.1k upadhyay  8 May 21:53  restapi.csr
.rw-r--r--@ 1.7k upadhyay  8 May 21:53  restapi.key
```

---

## References

- [Python `ssl` module docs](https://docs.python.org/3/library/ssl.html)
- [openssl-req man page](https://www.openssl.org/docs/man1.1.1/man1/req.html)
- [openssl-x509 man page](https://www.openssl.org/docs/man1.1.1/man1/x509.html)
