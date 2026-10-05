#!/usr/bin/env python3
"""Compare the log sources of the Sigma taxonomy with the rules of the SigmaHQ repository.

Usage: check-taxonomy.py <path-to-sigma-checkout>

Every log source used by a rule of the rules repository has to be documented by a page of the
`specification/appendix-taxonomy` directory, and the name of a page has to be built from the
attributes of the `logsource` block it holds. The pages that document a log source no rule uses are
reported, they are not an error: the taxonomy accepts log sources that the rules don't use yet.
"""
import collections
import glob
import os
import re
import sys

import yaml

PAGES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..",
                     "specification", "appendix-taxonomy")
AXES = ("product", "category", "service")


def key_of(attributes):
    return tuple(sorted((k, str(v)) for k, v in attributes.items() if k in AXES))


def page_name(key):
    attributes = dict(key)
    if "product" in attributes:
        value = attributes.get("category") or attributes.get("service")
        return f"{attributes['product']}_{value}.md" if value else f"{attributes['product']}.md"
    if "category" in attributes and "service" in attributes:
        return f"{attributes['category']}_{attributes['service']}.md"
    return f"{attributes.get('category') or attributes.get('service')}.md"


def read_pages():
    pages = {}
    for path in sorted(glob.glob(os.path.join(PAGES, "*.md"))):
        name = os.path.basename(path)
        if name == "template.md":
            continue
        content = open(path, encoding="utf-8").read()
        block = re.search(r"```yaml\nlogsource:\n((?:    .*\n)+)```", content)
        if not block:
            print(f"error: {name} has no logsource block")
            continue
        key = key_of(yaml.safe_load(f"logsource:\n{block.group(1)}")["logsource"])
        if key in pages:
            print(f"error: {key} is documented by {pages[key]} and by {name}")
        pages[key] = name
        expected = page_name(key)
        if expected != name:
            print(f"error: {name} should be named {expected}")
    return pages


def read_rules(checkout):
    used = collections.defaultdict(list)
    for path in sorted(glob.glob(os.path.join(checkout, "rules", "**", "*.yml"), recursive=True)):
        try:
            rule = yaml.safe_load(open(path, encoding="utf-8"))
        except Exception as error:  # noqa: BLE001
            print(f"error: {path} is not valid YAML: {error}")
            continue
        if not isinstance(rule, dict) or not isinstance(rule.get("logsource"), dict):
            continue
        used[key_of(rule["logsource"])].append(os.path.relpath(path, checkout))
    return used


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    pages, used = read_pages(), read_rules(sys.argv[1])
    errors = 0
    for key in sorted(used):
        if key not in pages:
            attributes = ", ".join(f"{k}: {v}" for k, v in key)
            print(f"error: no page documents '{attributes}', used by {len(used[key])} rules, "
                  f"for example {used[key][0]}")
            errors += 1
    for key in sorted(pages):
        if key not in used:
            attributes = ", ".join(f"{k}: {v}" for k, v in key)
            print(f"warning: {pages[key]} documents '{attributes}', no rule of the repository uses it")
    print(f"{len(pages)} pages, {len(used)} log sources used by the rules, {errors} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())