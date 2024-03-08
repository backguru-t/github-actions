import os
import argparse
import requests

# open_ai_model = os.environ.get("INPUT_OPENAI_MODEL", "gpt-3.5-turbo")
# max_prompt_tokens = int(os.environ.get("INPUT_MAX_TOKENS", "1000"))
# model_temperature = float(os.environ.get("INPUT_TEMPERATURE", "0.6"))

arg_parser = argparse.ArgumentParser(description="PR reviewer for a pull request with chatgpt")
arg_parser.add_argument("--pr_number", type=int, required=True, help="The pull request number")
arg_parser.add_argument("--github_api_url", type=str, required=True, help="The github api url to use")
arg_parser.add_argument("--github_token", type=str, required=True, help="The github token to use")
arg_parser.add_argument("--openai_api_key", type=str, required=True, help="The openai api key to use")
arg_parser.add_argument("--github_reposiotry", type=str, required=True, help="The github repository to use")
arg_parser.add_argument("--max_prompt_tokens", type=int, required=False, default=1000, help="The maximum number of tokens to use in the prompt")
arg_parser.add_argument("--openai_model", type=str, required=False, default="gpt-3.5-turbo", help="The openai model to use")

args = arg_parser.parse_args()

pr_number = args.pr_number
openai_model = args.openai_model
github_token = args.github_token
openai_api_key = args.openai_api_key
max_prompt_tokens = args.max_prompt_tokens
github_api_url = args.github_api_url
github_repository = args.github_reposiotry

print(f"PR id: {pr_number}, OPENAI_MODEL: {openai_model}, MAX_PROMPT_TOKENS: {max_prompt_tokens}, GIHUB_API_URL: {github_api_url}, REPO: {github_repository}")

authorization_header = {"Accept": "application/vnd.github.v3+json", "Authorization": f"token {github_token}"}
pull_request_url = f"{github_api_url}/repos/{github_repository}/pulls/{pr_number}"

pull_request_result = requests.get(
    pull_request_url,
    headers=authorization_header,
)

if pull_request_result.status_code != requests.codes.ok:
    print(
        "Request to get pull request data failed: "
        + str(pull_request_result.status_code)
    )
    exit(1)
