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
