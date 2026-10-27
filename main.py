#!/usr/bin/env python

import functools
import secrets
import string

import click

alphabets = {
    "digits": string.digits,
    "ascii_letters": string.ascii_letters,
    "punctuation": string.punctuation,
    "ascii_uppercase": string.ascii_uppercase,
    "ascii_lowercase": string.ascii_lowercase,
    "simple": string.ascii_letters + string.digits,
    "django": "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)",  # length of 50
}


@click.command()
@click.option("-c", "--count", default=1)
@click.option("-l", "--length", default=16)
@click.option(
    "-a",
    "--alphabet",
    type=click.Choice(alphabets.keys()),
    multiple=True,
    default=("digits", "ascii_letters", "punctuation"),
)
def generate_string(length, count, alphabet):
    choices = "".join([alphabets[a] for a in alphabet])

    for _ in range(count):
        click.echo("".join([secrets.choice(choices) for _ in range(length)]))


if __name__ == "__main__":
    generate_string()