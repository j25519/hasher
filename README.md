# Hasher

Type any random shit and generate a SHA256 hash for it.

~~Maybe I'll add other hashing options to this as well.~~ Have added a choice of SHA256, SHA384, SHA512, SHA3-256, blake2b, blake2s. Still defaults to SHA256 if you don't specify a hash.

## Help flag output

```bash
usage: hasher.py [-h] [-a ALGORITHM] [text]

Hasher v0.0.2: Quickly get cryptographic hashes from strings.

positional arguments:
  text                  String to hash (will prompt for a string if not specified)

options:
  -h, --help            show this help message and exit
  -a ALGORITHM, --algorithm ALGORITHM
                        Hashing algorithm to use (default: sha256)

Supported algorithms: sha256 (default), sha384, sha512, sha3_256, blake2b, blake2s.
```