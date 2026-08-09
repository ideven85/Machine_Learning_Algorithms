def encoding_decoding(s):
    amount = "₹50"

    print(amount.encode("UTF-16"))

    print("UTF 8", amount.encode("UTF-8"), type(amount.encode("UTF-8")))

    amount_decoded = amount.encode("UTF-8")
    print(amount_decoded.decode("UTF-8"), type(amount_decoded.decode("UTF-8")))


def main():
    encoding_decoding("₹50")


if __name__ == "__main__":
    main()
