#!/usr/bin/python3.6
import argparse
from datetime import datetime
from string import Template
import config
import os.path

template_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "template.txt")

# Set up command line arguments
parser = argparse.ArgumentParser(description="Create a minute.tex file.")
parser.add_argument(
    "-d, --date",
    dest="minute_date",
    action="store",
    default=datetime.today().strftime('%Y-%m-%d'),
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
    wiimb += "\subsection{" + mem + "}\n\subsubsection{Wat heb je gedaan?}\n\subsubsection{Waar ben je mee bezig?\n\subsubsection{Welke problemen heb je?}\n\n\n"

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
with open(template_path) as template:
    src = Template(template.read())

    result = src.safe_substitute(d)

    with open(f"{args.path}Notulen-{args.minute_date}.tex", "w") as file:
        file.write(result)
        print(f"Created {args.path}Notulen-{args.minute_date}.tex")
