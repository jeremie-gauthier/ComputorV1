from computor import app
import sys

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc == 2:
        ret = app.run(sys.argv[1])
        if ret["status"] == "Error":
            sys.exit("[*] Exit")
    else:
        print("[-] Arguments error", file=sys.stderr)
        sys.exit("[*] Exit")
