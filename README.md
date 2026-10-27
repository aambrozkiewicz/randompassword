# randompassword

Generate random passwords from the command line.

## Install

With [uv](https://docs.astral.sh/uv/) installed, run this single command from any directory:

```sh
uv tool install git+https://github.com/aambrozkiewicz/randompassword.git
```

## Usage

```sh
randompassword
randompassword --length 32 --count 5
randompassword --length 24 --alphabet simple
```

Passwords default to 16 characters using digits, letters, and punctuation.

Run `randompassword --help` for all options.

## Alphabets

Use `--alphabet` (or `-a`) to choose which characters can appear:

| Alphabet | Characters |
| --- | --- |
| `digits` | Digits: `0123456789` |
| `ascii_letters` | Lowercase `a`–`z` and uppercase `A`–`Z` |
| `punctuation` | ASCII punctuation: <code>!&quot;#$%&amp;'()*+,-./:;&lt;=&gt;?@[&#92;]^_&#96;{&#124;}~</code> |
| `ascii_uppercase` | Uppercase letters: `ABCDEFGHIJKLMNOPQRSTUVWXYZ` |
| `ascii_lowercase` | Lowercase letters: `abcdefghijklmnopqrstuvwxyz` |
| `simple` | Lowercase `a`–`z`, uppercase `A`–`Z`, and digits `0`–`9` |
| `django` | Lowercase `a`–`z`, digits `0`–`9`, and symbols `!@#$%^&*(-_=+)`; intended for generating a Django `SECRET_KEY` |

Repeat `--alphabet` to combine character sets. Specifying an alphabet replaces the
default selection of `digits`, `ascii_letters`, and `punctuation`:

```sh
randompassword --length 24 --alphabet ascii_letters --alphabet digits
```

To generate a 50-character Django secret key:

```sh
randompassword --length 50 --alphabet django
```
