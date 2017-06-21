
```bash
openssl genrsa -out restapi.key 2048
openssl req -new -key restapi.key -out restapi.csr
openssl x509 -req -days 365 -in restapi.csr -signkey restapi.key -out restapi.crt
```

```
ls -l 
19052408 -rw-r--r--  1 as18  NORD\Domain Users  1314 Jun 19 21:53 restapi.crt
19052403 -rw-r--r--  1 as18  NORD\Domain Users  1127 Jun 19 21:52 restapi.csr
19052343 -rw-r--r--  1 as18  NORD\Domain Users  1675 Jun 19 21:51 restapi.key
```
https://docs.python.org/2/library/ssl.html
