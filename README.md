# randompassword

Generate random passwords from the command line.

## Install

With [uv](https://docs.astral.sh/uv/) installed, run this single command from the project directory:

```sh
uv tool install .
```

## Usage

```sh
randompassword
randompassword --length 32 --count 5
randompassword --length 24 --alphabet simple
```

Passwords default to 16 characters using digits, letters, and punctuation. Repeat
`--alphabet` to combine character sets. Available sets: `digits`, `ascii_letters`,
`punctuation`, `ascii_uppercase`, `ascii_lowercase`, `simple`, and `django`.

Run `randompassword --help` for all options.
