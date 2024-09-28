import os
import sys
from dotenv import load_dotenv
from config import Config


if __name__ == "__main__":
    load_dotenv()

    try:
        cfg = Config()
        exit_code = 0
        for client in cfg.clients:
            if client.disabled:
                print(f"Skipping '{client.type}' model '{client.model}'. Test disabled.")
            else:
                print(f"Testing '{client.type}' model '{client.model}'")
                for case in cfg.cases:
                    print(f"Test Case \"{case.name}\":")
                    response = client.request(case.prompt)
                    if case.expected_substrings:
                        has_match = False
                        for substr in case.expected_substrings:
                            if substr.lower() not in response.lower():
                                has_match = True
                        if not has_match:
                            print("FAILED: No match to the expected substring")
                            exit_code += 1

                    if case.forbidden_substrings:
                        has_match = False
                        for substr in case.forbidden_substrings:
                            if substr.lower() not in response.lower():
                                has_match = True
                        if has_match:
                            print("FAILED: Match found in the forbidden substring")
                            exit_code += 1
    except Exception as e:
        print(f"ERROR: {e}")
        exit_code = 99

if exit_code:
    print("Test FAILED!")
else:
    print("Test PASSED!")
sys.exit(exit_code)
