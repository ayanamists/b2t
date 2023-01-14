// Copyright 2022 ayanamists
// 
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
// 
//     http://www.apache.org/licenses/LICENSE-2.0
// 
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

class A {
    public static int f(int a, int b) {
        int sum = 0;
        for (int i = (a > b) ? a + 1 : b + 1; i < a;) {
            sum = sum + i;
        }
        return sum;
    }
}