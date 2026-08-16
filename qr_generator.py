#!/usr/bin/env python3
import qrcode
import sys


def afiseaza_qr_terminal(link: str):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L, border=2)
    qr.add_data(link)
    qr.make(fit=True)
    qr.print_ascii(invert=True)


def main():
    print("=== QR Code Generator (terminal) ===\n")

    link = input("Introdu link-ul (ex: https://google.com): ").strip()

    if not link:
        print("Eroare: nu ai introdus niciun link.")
        sys.exit(1)

    print()
    afiseaza_qr_terminal(link)
    print()


if __name__ == "__main__":
    main()