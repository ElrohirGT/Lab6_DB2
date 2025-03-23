#!/usr/bin/env bash

set -euxo pipefail

# import subprocess
#
# for i in range(100):
#     subprocess.run(["python", "./gen.py", ">", "output.js"])
#     subprocess.run(
#         [
#             "mongosh",
#             "mongodb+srv://admin:galand0nis@freecluster.0iqxl.mongodb.net/Lab6",
#             "--eval",
#             "'load(\"output.js\")'",
#         ]
#     )

for i in {1..100}; do
	echo "Iteration " "$i"
	python ./gen.py >./output.js
	mongosh mongodb+srv://admin:galand0nis@freecluster.0iqxl.mongodb.net/Lab6 --eval 'load("output.js")'
done
