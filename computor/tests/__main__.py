import sys
from .runner import TestService

synopsis = """The following tests are available:
- format
- result

e.g.: py -m computor.tests [test.name ...]
You can run all of them by omitting <test.name>"""


if __name__ == "__main__":
    runner = TestService()
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            if arg.lower() in ("format", "formatting"):
                runner.runFormattingTests(filename="formatting")
            elif arg.lower() in ("result", "results"):
                runner.runResultTests(filename="results")
            elif arg.lower() in ("-h", "--help"):
                print(synopsis)
            else:
                print(f"[-] Unrecognized arg '{arg}'", file=sys.stderr)
                print("[*] Skipped")
    else:
        runner.runAll()
