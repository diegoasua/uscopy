import argparse
import os
import shutil
import time
from fnmatch import fnmatch
from glob import glob
from math import floor
from pathlib import Path
from random import randint

# parse options
parser = argparse.ArgumentParser(description="Crawl files according to some pattern")
parser.add_argument(
    "pattern", metavar="-p", type=str, help="Unix style-like pattern to be queried"
)
parser.add_argument(
    "source",
    metavar="-s",
    type=str,
    help="Where to look for files that match the pattern",
)
parser.add_argument(
    "destination", metavar="-d", type=str, help="where to accumulate found files"
)
parser.add_argument(
    "dice", type=int, metavar="-D", help="a chosen file every dice", default=1
)
parser.add_argument(
    "omit",
    metavar="-o",
    type=str,
    help="unix style-like patterns as a space delimited string",
)

args = parser.parse_args()
omit = args.omit.split(" ")

if os.path.isabs(args.source):
    source = args.source
else:
    source = Path(os.path.abspath(".")) / args.source

if os.path.isabs(args.destination):
    destination = args.destination
else:
    destination = Path(os.path.abspath(".")) / args.destination

# move data
matches = glob(str(source / "**/" / args.pattern), recursive=True)
total_matches = len(matches)
print(f"found {total_matches} files matching pattern \nCleaning and moving...")
print("\n")
log_time = time.time_ns()
for i_match, match in enumerate(matches):
    for omit_i in omit:
        if fnmatch(match, omit_i):
            fnmatched = True
            break
    # if matched an omit keyword then jump to the next match
    if fnmatched:
        fnmatched = False
        continue
    is_chosen = bool(floor(randint(1, args.dice) / args.dice))
    if not is_chosen:
        continue
    shutil.copy2(match, destination)
    current = time.time_ns()
    # progress every 5 seconds
    if (current - log_time) / 10e-9 > 5:
        log_time = current
        print(
            f"Progress...: {int(i_match / total_matches * 100)}%", end="\r", flush=True
        )
