import sys
from .runner import TestService

if __name__ == "__main__":
    runner = TestService()
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            if arg.lower() in ("format", "formatting"):
                runner.runFormattingTests(filename="formatting")
            elif arg.lower() in ("result", "results"):
                runner.runResultTests(filename="results")
            elif arg.lower() in ("-h", "--help"):
                print(
                    """The following tests are available:
                    \r- format
                    \r- result

                    \re.g.: py -m computor.tests [test.name ...]
                    \rYou can run all of them by omitting <test.name>"""
                )
            else:
                print(f"[-] Unrecognized arg '{arg}'\n[*] Skipped", file=sys.stderr)
    else:
        runner.runAll()
