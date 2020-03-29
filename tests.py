import unittest
import os, contextlib
import json
from main import *


def silentErrorLog(func):
    def makeRedirection(*args, **kwargs):
        with open(os.devnull, "w") as devnull:
            with contextlib.redirect_stderr(devnull):
                func(*args, **kwargs)

    return makeRedirection


def getTestFile(func):
    def loadTests(*args, **kwargs):
        filename = kwargs["filename"]
        with open(f"./tests/{filename}.json", "r") as testFile:
            kwargs["tests"] = json.load(testFile)
            del kwargs["filename"]
            func(*args, **kwargs)

    return loadTests


class TestService(unittest.TestCase):
    def assertEqual(self, case, expected):
        with open(os.devnull, "w") as devnull:
            with contextlib.redirect_stdout(devnull):
                super().assertEqual(main(case), expected)

    def runAll(self):
        self.runFormattingTests(filename="formatting")

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


TestService().runAll()
