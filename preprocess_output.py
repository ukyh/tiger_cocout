import os
import sys
import json


INPUT_FILE = sys.argv[1]
OUTPUT_DIR = "./data/candidates/{}".format(
    INPUT_FILE.split("/")[-1].rstrip("json").rstrip(".")
)
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "output_cap.txt")
if not os.path.exists(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)

with open(INPUT_FILE, "rb") as infile:
    indict = json.load(infile)
count = 0
with open(OUTPUT_FILE, "w") as outfile:
    for key in indict["imgToEval"]:
        outfile.write("{}\t{} .\n".format(key, indict["imgToEval"][key]["caption"]))
        count += 1
assert count == 5000

print("Done preprocessing: {}".format(INPUT_FILE))
