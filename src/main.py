import sys

from config import Config
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()

    try:
        # Load values from `config.yaml`
        cfg = Config()

        exit_code = 0
        # Iterate over all API Clients
        for client in cfg.clients:
            if client.disabled:
                print(
                    f"Skipping '{client.type}' model '{client.model}'. Test disabled."
                )
            else:
                print(f"Testing '{client.type}' model '{client.model}'")

                # Iterate over all test cases
                for case in cfg.cases:
                    print(f'Test Case "{case.name}":')
                    response = client.request(case.prompt)

                    # Testing Expected cases
                    has_match = False
                    for case_test in case.expected:
                        if case_test.validate(response):
                            has_match = True
                    if not has_match:
                        print("FAILED: No match to the expected substring")
                        exit_code += 1

                    # Testing Forbidden cases
                    has_match = False
                    for case_test in case.forbidden:
                        if case_test.validate(response):
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
