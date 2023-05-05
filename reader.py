import os
import re


SECTION_PREFIX = "processing times :"
SECTION_SUFFIX = "number of jobs, ..."


def read_file(file_name: str):
    def parse_batch(text):
        return [parse_tasks(x) for x in text.split("\n") if x.strip()]

    def parse_tasks(line):
        return [int(x) for x in line.strip().split()]

    file_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "./instances", file_name)
    )

    pattern = SECTION_PREFIX + r"([\d\s]+)" + SECTION_SUFFIX

    with open(file_path) as f:
        content = f.read() + "\n" + SECTION_SUFFIX
        return [parse_batch(x) for x in re.findall(pattern, content)]


def read_sample_batch():
    return read_file("tai20_5.txt")[0]


if __name__ == "__main__":
    read_file("tai20_5.txt")
