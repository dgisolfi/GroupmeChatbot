#!/usr/bin/python3

from GroupmeChatbot.server import server

def main():
    server.run(host='0.0.0.0', port=5525, debug=False, threaded=True)

if __name__ == "__main__":
    main()