#!/usr/bin/env python3
import base64, time, os

# Banner
def banner():
    os.system("clear")
    print("\033[1;32m" + "="*40)
    print("     🔐 HACKER CHAT BY S4TYAM ")
    print("     tinyurl.com/S4TYAM ")
    print("="*40 + "\033[0m")

# Encode
def encode():
    msg = input("\n\033[1;34mENTER MESSAGE: \033[0m")
    print("\nEncoding Message...")
    time.sleep(2)
    encoded = base64.b32encode(msg.encode()).decode()
    print(f"\n\033[1;32mMESSAGE ENCODED = {encoded}\033[0m")
    input("\nPress ENTER to go back...")
    menu()

# Decode
def decode():
    code = input("\n\033[1;34mENTER CODE: \033[0m")
    try:
        decoded = base64.b32decode(code).decode()
        print(f"\n\033[1;32mMESSAGE DECODED = {decoded}\033[0m")
    except Exception:
        print("\n\033[1;31mINVALID CODE!\033[0m")
    input("\nPress ENTER to go back...")
    menu()

# Menu
def menu():
    banner()
    print("[1] CODE (ENCODE MESSAGE)")
    print("[2] DECODE")
    print("[3] QUIT\n")
    choice = input("Choose option: ")
    if choice == "1":
        encode()
    elif choice == "2":
        decode()
    elif choice == "3":
        print("\n\033[1;31mExiting... Goodbye!\033[0m")
        exit()
    else:
        menu()

if __name__ == "__main__":
    menu()
