#!/usr/bin/python

# Copyright 2016 Lawrence Kesteloot
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#    http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Given a list of utterances with possibilities, generates the various
# actual utterances. For example:
#
#     [what is|what's] [on|in] {ListName} [list|]
#
# Would generate the eight possible utterances:
#
#     what is on {ListName}
#     what is on {ListName} list
#     what is in {ListName}
#     ...
#
# Run with:
#
#     python expand_utterances.py < sample_utterance_patterns.txt > sample_utterances.txt
#

import sys

# Generates all combinations of the segment, writing each line
# to the file stream "out". The "words" list accumulates the
# words on each line. Pass in an empty list to get it started.
def generate(out, segments, words):
    if not segments:
        # End of line. Remove empty words and join with a space.
        out.write(" ".join(filter(None, words)) + "\n")
    else:
        # Try every option in the first segment, and recurse.
        for option in segments[0]:
            generate(out, segments[1:], words + [option])

# Process a line of input, generating the output to the file stream
# "out".
def process_line(out, line):
    # The segments in this line. Each segment is a list of options.
    segments = []

    # Parse the segments. Plain text is a segment with a single option.
    # This loop must always start with a stripped line.
    while line:
        i = line.find("[")
        if i == -1:
            # No more options on list. Add the remaining text.
            segments.append([line])
            line = ""
        elif i == 0:
            # Starts with options.
            j = line.find("]")
            if j == -1:
                sys.stderr.write("Close brace not found.\n")
                sys.exit(1)
            segments.append(line[i + 1:j].split("|"))
            line = line[j + 1:].strip()
        else:
            # Starts with plain text.
            segments.append([line[:i].strip()])
            line = line[i:].strip()

    # Generate the combinations.
    generate(out, segments, [])

def main():
    # Read each line from standard input.
    for line in sys.stdin.readlines():
        line = line.strip()

        # Strip comments and blank lines.
        if line and not line.startswith("#"):
            process_line(sys.stdout, line)

if __name__ == "__main__":
    main()
