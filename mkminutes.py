#!/usr/bin/python3.6
import argparse
from string import Template
import config

# Set up command line arguments
parser = argparse.ArgumentParser(description="Create a minute.tex file.")
parser.add_argument(
    "-d, --date",
    dest="minute_date",
    action="store",
    default="2018-01-01",
    help="Date of the minute to be generated",
)

parser.add_argument(
    "-t, --target",
    dest="path",
    action="store",
    default="./",
    help="The path of the folder the .tex file should b saved to. (Defaults to './')",
)

args = parser.parse_args()

# Process some config
mems = sorted(config.MEMBERS, key=str.lower)
wiimb = ""
for mem in mems:
    wiimb += "\subsection{" + mem + "}\n\n\n"

# Define the replacement dictionary
d = {
    "members": ", ".join(mems),
    "secretary": config.SECRETARY,
    "chairman": config.CHAIRMAN,
    "date": args.minute_date,
    "APList": None,
    "wiimb":wiimb,
}

# Process the dictionary
template = open("template.txt")

src = Template(template.read())

result = src.safe_substitute(d)

with open(f"{args.path}Notulen-{args.minute_date}.tex", "w") as file:
    file.write(result)
    print(f"Created {args.path}Notulen-{args.minute_date}.tex")
