import re

def insert_docker_username_into_yml_file(username, yml_file_path):
    """Used from a shell script"""
    with open(yml_file_path, encoding='utf-8', mode="r+") as f:
        yml_file = f.read()
        f.seek(0)
        new_line = f"image: {username}/"
        new_yml_file = re.sub(r"(image: )(.*/*)(.*)",
                              r"image: {}/\2".format(username),
                              yml_file)
        f.write(new_yml_file)
        f.truncate()


def test_self():
    mock_yml_file = """
        version: 1.0
        provider:
            name: openfaas
            gateway: http://127.0.0.1:8080
        functions:
            function_name_1:
                lang: language
                handler: ./wherever
                image: this_should_be_prefixed_after:latest
            function_name_2:
                lang: language2
                handler: ./wherever2
                image: 2this_should_be_prefixed_after2:latest"""
    mock_new_yml_file = """
        version: 1.0
        provider:
            name: openfaas
            gateway: http://127.0.0.1:8080
        functions:
            function_name_1:
                lang: language
                handler: ./wherever
                image: kodiakcrypto/this_should_be_prefixed_after:latest
            function_name_2:
                lang: language2
                handler: ./wherever2
                image: kodiakcrypto/2this_should_be_prefixed_after2:latest"""

    # Goal is to splice this in
    username = 'kodiakcrypto'
    new_line = f"image: {username}/"
    new_yml_file = re.sub("image: (.*)", 
                         new_line + r"\1", 
                         mock_yml_file)
    print(new_yml_file)
    assert new_yml_file == mock_new_yml_file

import sys
if __name__ == "__main__":
    # this is so we can call it from a shell script
    insert_docker_username_into_yml_file(sys.argv[1], sys.argv[2])
