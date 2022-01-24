
# Perl|Python|Go for DevOps

[![License](http://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
## contents

- [comments](#comments)
  - [Shell](#shell)
  - [Perl](#perl)
  - [Python](#python)
  - [Go](#go)
- [echo: printing](#echo-printing)
  - [Shell](#shell-1)
  - [Perl](#perl-1)
  - [Python](#python-1)
  - [Go](#go-1)
- [cat: open and print a file](#cat-open-and-print-a-file)
  - [Shell](#shell-2)
  - [Perl](#perl-2)
  - [Python](#python-2)
  - [Go](#go-2)
- [urls](#urls)
- [license](#license)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## comments

---

### Shell

```bash
# comment
```

### Perl

```perl
#!/usr/bin/env perl
# this is a line comment

=pod
 this is a block comment
=cut

```

### Python

```python
#!/usr/bin/env python
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
#!/usr/bin/env perl
use v5.10;
use strict;
use warnings;

say 'DevOps ', 'is great!';

```

### Python

```python
#!/usr/bin/env python
print('DevOps', 'is great!')

```

### Go

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

## urls

- <https://golangprojectstructure.com/12-powerful-linux-bash-commands-with-go/>
- <https://wiki.python.org/moin/PerlPhrasebook>
- <http://pleac.sourceforge.net/>
- <https://github.com/miguelmota/golang-for-nodejs-developers>

**[⬆ back to top](#contents)**

## license

[MIT](LICENSE)
