import sys

from clients import import_client
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    # Pre-requisite: `ollama run llama2
    client = import_client("openai")
    con = client(
        {
            "model": "gpt-4o-mini",
            "type": "openai",
            "max_tokens": 100,
            "temperature": 0.0,
            "system_prompt": "You are Spock from Vulcan, an AI assistant.",
        }
    )
    print(con.request("Hello. Please introduce yourself. Are you human?"))

    sys.exit(0)

#     try:
#         # Load values from `config.yaml`
#         cfg = Config()
#
#         exit_code = 0
#         # Iterate over all API Clients
#         for client in cfg.clients:
#             if client.disabled:
#                 print(
#                     f"Skipping '{client.type}' model '{client.model}'. Test disabled."
#                 )
#             else:
#                 print(f"Testing '{client.type}' model '{client.model}'")
#
#                 # Iterate over all test cases
#                 for case in cfg.cases:
#                     print(f'Test Case "{case.name}": ')
#                     response = client.request(case.prompt)
#
#                     # Testing Expected cases
#                     has_match = False
#                     for test_def in case.expected:
#                         if test_def.validate(response):
#                             has_match = True
#                     if not has_match:
#                         print(f"FAILED: expected test {test_def.type}")
#                         exit_code += 1
#
#                     # Testing Forbidden cases
#                     has_match = False
#                     for test_def in case.forbidden:
#                         if test_def.validate(response):
#                             has_match = True
#                     if has_match:
#                         print(f"FAILED: forbidden test {test_def.type}")
#                         exit_code += 1
#
#     except Exception as e:
#         print(f"ERROR: {e}")
#         exit_code = 99
#
# if exit_code:
#     print("Test FAILED!")
# else:
#     print("Test PASSED!")
# sys.exit(exit_code)
