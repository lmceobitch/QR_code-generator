# QR-terminal

small python script, give it a link and it spits out the qr code straight in the terminal, no files saved.

## what you need

- python3
- qrcode

## Install

```
pip install -r requirements.txt --break-system-packages
```

## How to run

```
python3 qr_terminal.py
```

it asks for a link and gives you the qr code right in the console.

## example

```
$ python3 qr_terminal.py
=== QR Code Generator (terminal) ===

Enter the link (ex: https://google.com): https://google.com

(qr code here)

```

## does the qr code expire?

no, it's a static qr generated locally, it doesn't expire. it'll always work as long as the link behind it is still valid.
