import json
import argparse
from enum import Enum

from organization_fuzzer import OrganizationFuzzer
from user_fuzzer import UserFuzzer
from sample_fuzzer import SampleFuzzer
from excursion_fuzzer import ExcursionFuzzer
from http_methods import post_request, get_request

class ObjectType(Enum):
    ORGANIZATION = "organizations"
    USER = "users"
    SAMPLES = "samples"

API_BASE_URL = "http://localhost:8080/api"

def generate_organizations(num):
    fuzzer = OrganizationFuzzer()
    for _ in range(num):
        org = fuzzer.generate()
        print(org)
        response = post_request(f"{API_BASE_URL}/organizations", json.dumps(org))
        print(response.status_code, response.text)
        print("_"*50)

def generate_excursions(num):
    users_response = get_request(f"{API_BASE_URL}/users")
    user_ids = [org["id"] for org in users_response.json()]

    fuzzer = ExcursionFuzzer(user_ids=user_ids)
    for _ in range(num):
        excursion = fuzzer.generate()
        response = post_request(f"{API_BASE_URL}/excursions", json.dumps(excursion))
        print(response.status_code, response.text)

        # try:
        #     excursion_data = response.json()
        #     excursion_id = excursion_data["id"]
        # except (KeyError, ValueError) as e:
        #     print("Failed to extract excursion ID:", e, response.text)
        #     continue

        # for _ in range(4):
        #     user_excursion = fuzzer.generate_user_excursion(excursion_id)
        #     join_response = post_request(
        #         f"http://localhost:8080/api/excursions/join",
        #         json.dumps(user_excursion)
        #     )
        #     print(join_response.status_code, join_response.text)

def generate_users(num):
    orgs_response = get_request(f"{API_BASE_URL}/organizations")
    org_ids = [org["id"] for org in orgs_response.json()]

    fuzzer = UserFuzzer(org_ids)
    for _ in range(num):
        user = fuzzer.generate()
        response = post_request(f"{API_BASE_URL}/users", json.dumps(user))
        print(response.status_code, response.text)

def generate_samples(num):
    users_response = get_request(f"{API_BASE_URL}/users")
    user_ids = [org["id"] for org in users_response.json()]

    organization_response = get_request(f"{API_BASE_URL}/organizations")
    organization_ids = [org["id"] for org in organization_response.json()]

    fuzzer = SampleFuzzer(user_ids, [] ,organization_ids)
    for _ in range(num):
        sample = fuzzer.generate()
        print(sample)
        response = post_request(f"{API_BASE_URL}/samples", json.dumps(sample))
        print(response.status_code, response.text)

def save_all_data():
    orgs = get_request(f"{API_BASE_URL}/organizations").json()
    users = get_request(f"{API_BASE_URL}/users").json()
    samples = get_request(f"{API_BASE_URL}/samples").json()
    excursions = get_request(f"{API_BASE_URL}/excursions").json()

    with open("response.json", "w") as f:
        json.dump({"organizations": orgs, "users": users, "samples":samples, "excursions":excursions}, f, indent=4)

def main():
    parser = argparse.ArgumentParser(description="Generate fake users or organizations.")
    parser.add_argument("type", choices=["users", "organizations", "samples", "excursions"], help="Object type to generate.")
    parser.add_argument("-n", "--number", type=int, default=1, help="Number of objects to generate.")
    args = parser.parse_args()

    if args.type == "organizations":
        generate_organizations(args.number)
    elif args.type == "users":
        generate_users(args.number)
    elif args.type == "samples":
        generate_samples(args.number)
    elif args.type == "excursions":
        generate_excursions(args.number)

    save_all_data()

if __name__ == "__main__":
    main()
