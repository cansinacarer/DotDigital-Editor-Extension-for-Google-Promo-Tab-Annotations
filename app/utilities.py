import requests

import base64
import json

from app.config import API_USER, API_PASSWORD


def read_file(file_path):
    with open(file_path, "r") as file:
        contents = file.read()
    return contents


def escape_html(file_path):
    contents = read_file(file_path)
    return json.dumps(contents)


def build_payload(
    block_key,
    group_name,
    group_icon,
    block_name,
    block_icon,
    block_desc,
    block_inputs,
    template,
    author="Cansin Acarer",
):
    return {
        "key": block_key,
        "contactIdentifier": "account",
        "json": {
            "listing": {
                "scope": ["email"],
                "author": author,
                "group": {"name": group_name, "icon": group_icon},
                "name": block_name,
                "icon": block_icon,
                "description": block_desc,
            },
            "parameters": {"interactive": [input for input in block_inputs]},
            "template": template,
        },
    }


def update_block(
    block_key,
    group_name,
    group_icon,
    block_name,
    block_icon,
    block_desc,
    block_inputs,
    template,
    author="Cansin Acarer",
    extension_key="promo_annotations",
):
    payload = build_payload(
        block_key=block_key,
        group_name=group_name,
        group_icon=group_icon,
        block_name=block_name,
        block_icon=block_icon,
        block_desc=block_desc,
        block_inputs=block_inputs,
        template=template,
        author=author,
    )
    response = get_api_response(
        endpoint=f"/contacts/transactional-data/editor_extensions_{extension_key}",
        payload=payload,
    )
    if response.status_code == 201:
        print(f'{block_name} is uploaded successfully.')
    else:
        print(f'There has been an error while uploading the {block_name} block.')


def auth_header():
    credentials = f"{API_USER}:{API_PASSWORD}"
    encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")

    return f"Basic {encoded_credentials}"


def get_api_response(endpoint, payload, type="post"):
    base_url = "https://r2-api.dotdigital.com/v2"
    url = base_url + endpoint

    if type == "post":
        headers = {"Content-Type": "application/json", "Authorization": auth_header()}
        return requests.post(url, headers=headers, json=payload)

    if type == "get":
        print("not supported yet")
