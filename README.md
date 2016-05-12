
# Alexa Utterances Processor

The Amazon Alexa service requires skill developers to submit
a list of utterances that are valid queries from users. They
look like this (the first word is the name of the intent):

    WhatIsOnListIntent what is on the {ListName} list
    WhatIsOnListIntent what is on the {ListName}
    WhatIsOnListIntent what is on {ListName} list
    WhatIsOnListIntent what is on {ListName}
    WhatIsOnListIntent what is in the {ListName} list
    WhatIsOnListIntent what is in the {ListName}
    WhatIsOnListIntent what is in {ListName} list
    WhatIsOnListIntent what is in {ListName}

Writing these is tedious and error-prone because of the
combinatorial explosion of possible phrases. The
`expand_utterances.py` script in this repo reads a
pattern file from standard input and generates the
above utterance list. Square brackets surround
a set of options, which are separated by a bar.
For example, the above eight lines would be generated
by the following pattern:

    WhatIsOnListIntent what is [on|in] [the|] {ListName} [list|]

Note that an empty option is valid and represents an
optional phrase.

Test with the sample file:

    python expand_utterances.py < sample_utterances_patterns.txt

# License

Copyright 2016 Lawrence Kesteloot

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
