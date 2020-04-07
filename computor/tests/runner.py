import unittest
import os, contextlib
import json
from computor import app


def silentErrorLog(func):
    def makeRedirection(*args, **kwargs):
        with open(os.devnull, "w") as devnull:
            with contextlib.redirect_stderr(devnull):
                func(*args, **kwargs)

    return makeRedirection


def silentOutputLog(func):
    def makeRedirection(*args, **kwargs):
        with open(os.devnull, "w") as devnull:
            with contextlib.redirect_stdout(devnull):
                func(*args, **kwargs)

    return makeRedirection


def getTestFile(func):
    def loadTests(*args, **kwargs):
        filename = kwargs["filename"]
        with open(f"./computor/tests/{filename}.json", "r") as testFile:
            kwargs["tests"] = json.load(testFile)
            del kwargs["filename"]
            func(*args, **kwargs)

    return loadTests


class TestService(unittest.TestCase):
    @silentOutputLog
    def assertEqual(self, case, expected):
        result = app.run(case)
        super().assertEqual(result["status"], expected["status"])
        if result["status"] == "Success":
            if result["solutions"] is None:
                super().assertEqual(result["solutions"], expected["s1"])
            elif len(result["solutions"]) == 2:
                s1, s2 = result["solutions"]
                super().assertEqual(s1, expected["s1"])
                super().assertEqual(s2, expected["s2"])
            else:
                super().assertEqual(result["solutions"][0], expected["s1"])

    def runAll(self):
        self.runFormattingTests(filename="formatting")
        self.runResultTests(filename="results")

    @getTestFile
    @silentErrorLog
    def runFormattingTests(self, tests):
        print("[*] TESTS FORMATTING")
        res = [" "] * len(tests) * 2
        done = 0
        for test in tests:
            print(f"\r[{''.join(res)}]", end="")
            try:
                self.assertEqual(test["case"], test["expected"])
                res[done] = "✔"
            except Exception:
                res[done] = "✖"
            finally:
                done += 2
        print(f"\r[{''.join(res)}]")

    @getTestFile
    @silentErrorLog
    def runResultTests(self, tests):
        print("[*] TESTS RESULTS")
        res = [" "] * len(tests) * 2
        done = 0
        for test in tests:
            print(f"\r[{''.join(res)}]", end="")
            try:
                self.assertEqual(test["case"], test["expected"])
                res[done] = "✔"
            except Exception:
                res[done] = "✖"
            finally:
                done += 2
        print(f"\r[{''.join(res)}]")
