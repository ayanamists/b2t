# Copyright 2022 ayanamists
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import re

target = ["eclipse", "antlr", "chart", "jython"]

with open("/home/ayanamists/repo/pascal/frontend/bytecodeToTIR/data/data.txt") as f:
    lines = f.readlines()
    count = 0
    same = []
    real_same = 0
    for i in lines:
        if i.startswith("merge"):
            count = count + 1
        if "equiv: true, duplicate: false" in i:
            same.append(i)
            new = re.search(r'newOp: (\[.*?\])', i).group(1)
            old = re.search(r'old: (\[.*\])', i).group(1)
            if new == old:
                real_same += 1

    print(f"total: {count}, same: {len(same)}, real_same: {real_same}")
