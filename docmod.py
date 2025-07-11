import ast
import os
import pathlib
from collections import defaultdict
from dataclasses import dataclass


class DocstringData:
    """Container for the collection of docstring data extracted from
    some entity.
    """

    def __init__(self) -> None:
        self.name: str = ""
        self.cls: ast.ClassDef | None = None
        self.methods: dict[str, str] = {}
        # attributes: dict[str, str] = {}


def extract_docstrings(path: pathlib.Path) -> DocstringData:
    if not path.exists():
        raise ValueError("invalid source code path supplied.")

    source = path.read_text()
    tree = ast.parse(source)
    data = DocstringData()

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            data.name = node.name  # [node.name]ast.get_docstring(node)
            data.cls = node

        if isinstance(node, ast.FunctionDef):
            data.methods[node.name] = ast.get_docstring(node) or ""

    try:
        __IPYTHON__
        for k, v in data.methods.items():
            v = v.replace("\n", "\n\t")
            data.cls.__doc__ += f"\n\n{k}\n\t{v}"

    except:
        ...

    return data


if __name__ == "__main__":
    p = pathlib.Path("/Users/chris/code/docmod/testables.py")
    data = extract_docstrings(p)

    # for k, v in data.methods.items():
    #     print(k)
    #     print(f"\t{v}")

    print(data.cls.__doc__)
