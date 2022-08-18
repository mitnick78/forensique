#!/usr/bin/env python3
# coding:utf8

from ast import arg
import PyPDF2
import argparse
import re


def get_pdf_meta(file_name):
    pdf_file = PyPDF2.PdfFileReader(open(file_name, 'rb'))
    doc_info = pdf_file.getDocumentInfo()
    for info in doc_info:
        print("[+] " + info + " " + doc_info[info])


def get_strings(file_name):
    with open(file_name, "rb") as file:
        content = file.read()
    _re = re.compile("[\S\s]{4,}")
    for match in _re.finditer(content.decode("utf8", "backslashreplace")):
        print(match.group())


def decode_hex(string, decodeString):
    try:
        response = bytes.fromhex(string).decode(decodeString)
        print("--------INFORMATION----------")
        print(response)
        print("--------INFORMATION----------")
    except UnicodeDecodeError as err:
        print(err)


parser = argparse.ArgumentParser(description="Outil de forensique")
parser.add_argument("-pdf", dest="pdf",
                    help="Chemin du fichier PDF", required=False)
parser.add_argument("-str", dest="str",
                    help="Chemin du fichier auquel nous pouvons récuper les strings", required=False)

parser.add_argument("-fromHex", dest="fromHex",
                    help="", required=False)
parser.add_argument("-pattern", dest="pattern",
                    help="Ajouter un argument de decode (UTF8,UTF16...)", required=False)

args = parser.parse_args()

if args.pdf:
    get_pdf_meta(args.pdf)
if args.str:
    get_strings(args.str)
if args.pattern and args.fromHex:
    decode_hex(args.fromHex, args.pattern)
