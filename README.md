
# Shell|Python|Go|C++ for DevOps

[![License](http://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
## contents

- [comments](#comments)
  - [shell](#shell)
  - [python](#python)
  - [go](#go)
  - [cpp](#cpp)
- [echo: printing](#echo-printing)
  - [shell](#shell-1)
  - [python](#python-1)
  - [go](#go-1)
- [cat: open and print a file](#cat-open-and-print-a-file)
  - [shell](#shell-2)
  - [python](#python-2)
  - [go](#go-2)
- [generating a random number](#generating-a-random-number)
- [urls](#urls)
- [license](#license)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## comments

---

### shell

```bash
#!/bin/bash
# this is a line comment
```

### python

```python
#!/usr/bin/env python
# this is a line comment

'''
this is a block comment
'''
```

### go

```go
package main

func main() {
	// this is a line comment

	/*
	   this is a block comment
	*/
}
```

### cpp

```cpp
int main()
{
        // this is a line comment

        /*
           this is a block comment
        */
        return 0;
}
```

**[⬆ back to top](#contents)**

## echo: printing

---

### shell

```bash
#!/bin/bash
echo "DevOps" "is great!"
```

### python

```python
#!/usr/bin/env python
print('DevOps', 'is great!')
```

### go

```go
package main

import (
	"fmt"
)

func main() {
	fmt.Println("DevOps ", "is great!")
}
```

**[⬆ back to top](#contents)**

## cat: open and print a file

---

### shell

```bash
#!/bin/bash
cat test.txt
```

### python

```python
#!/usr/bin/env python
import sys

filename = "test.txt"
try:
  with open(filename, "r") as fh:
    lines = fh.readlines()
    [print(line, end="") for line in lines]
except IOError as err:
  print(err, file=sys.stderr)
```

### go

```go
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	filename := "test.txt"

	fh, err := os.Open(filename)
	if err != nil {
		fmt.Println(err)
	}
	defer fh.Close()

	scanner := bufio.NewScanner(fh)
	scanner.Split(bufio.ScanLines)
	var lines []string

	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	for _, line := range lines {
		fmt.Println(line)
	}
}
```

**[⬆ back to top](#contents)**

## generating a random number

## urls

- <https://stackoverflow.com/a/1154355/17222624>
- <https://golangprojectstructure.com/12-powerful-linux-bash-commands-with-go/>
- <https://linuxhandbook.com/bash-automation/>
- <https://github.com/miguelmota/golang-for-nodejs-developers>

**[⬆ back to top](#contents)**

## license

[MIT](LICENSE)
