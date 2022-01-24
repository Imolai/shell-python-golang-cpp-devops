
# Perl|Python|Go for DevOps

[![License](http://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## contents

Use `doctoc` to generate it.

## comments

---

### Shell

```bash
# comment
```

### Perl

```perl
# this is a line comment

=pod
 this is a block comment
=cut
```

### Python

```python
# this is a line comment

'''
this is a block comment
'''
```

### Go

```go
package main

func main() {
	// this is a line comment

	/*
	   this is a block comment
	*/
}
```

**[⬆ back to top](#contents)**

## echo: printing

---

### Shell

```bash
echo "DevOps" "is great!"
```

### Perl

```perl
use v5.26;
use strict;
use warnings;

say 'DevOps ', 'is great!';
```

### Python

```python
```

### Go

```go
package main

import (
	"fmt"
	"os"
)

func main() {
	fmt.Println("DevOps ", "is great!")
}
```

**[⬆ back to top](#contents)**

## cat: open and print a file

---

### Shell

```bash
cat test.txt
```

### Perl

```perl
#!/usr/bin/env perl
use strict;
use warnings;
use IO::File;
use Carp;
use English qw(-no_match_vars);

my $filename = 'test.txt';
my $fh       = IO::File->new($filename, 'r');
if (defined $fh) {
    my @lines = $fh->getlines;
    undef $fh;
    print @lines;
} else {
    croak "$OS_ERROR: 'test.txt'";
}
```

### Python

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

### Go

```go
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	filename := "test.txt"

	readFile, err := os.Open(filename)
	if err != nil {
		fmt.Println(err)
	}
	defer readFile.Close()

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)

	for fileScanner.Scan() {
		fmt.Println(fileScanner.Text())
	}
}
```

**[⬆ back to top](#contents)**

## urls

- <https://golangprojectstructure.com/12-powerful-linux-bash-commands-with-go/>
- <https://wiki.python.org/moin/PerlPhrasebook>
- <http://pleac.sourceforge.net/>
- <https://github.com/miguelmota/golang-for-nodejs-developers>

**[⬆ back to top](#contents)**

## license

[MIT](LICENSE)
