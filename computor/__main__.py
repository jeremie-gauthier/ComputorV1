from computor import app
import sys

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc > 1 and argc < 4:
        entry = sys.argv[1]
        if argc == 3 and sys.argv[2].startswith("-"):
            verbose = "v" in sys.argv[2]
            ret = app.run(entry, opt_verbose=verbose)
        else:
            ret = app.run(entry)
        if ret["status"] == "Error":
            sys.exit("[*] Exit")
    else:
        print("[-] Arguments error", file=sys.stderr)
        sys.exit("[*] Exit")
