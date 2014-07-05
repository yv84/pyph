import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


from proxy.run import run


def main():
    run(BASE_DIR)

if __name__ == '__main__':
    main()
