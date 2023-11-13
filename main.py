from chain import Chain


def main():
    chain = Chain(18)
    while True:
        data = input("Add something to the chain: ")
        chain.add_to_pool(data)
        chain.mine()


if __name__ == "__main__":
    main()
