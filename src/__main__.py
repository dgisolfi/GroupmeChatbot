#!/usr/bin/python3

from src.server import server

def main():
    server.run(port=5525, debug=True, threaded=True)

if __name__ == "__main__":
    main()