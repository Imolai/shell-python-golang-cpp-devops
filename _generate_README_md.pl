#!/usr/bin/env perl
use v5.10;
use strict;
use warnings;
use IO::File;
use Carp;
use English qw(-no_match_vars);
use Path::Tiny qw(path);

my $input  = 'README.src.md';
my $ifh    = IO::File->new($input, 'r');
my $output = 'README.md';
my $ofh    = IO::File->new($output, 'w');

say "Generating '$output' from '$input' and sources in 'src/'.";
if (defined $ifh && defined $ofh) {
    foreach my $line ($ifh->getlines) {
        chomp $line;
        if ($line =~ m/^\[\[(.*)\]\]$/xms) {
            if (-e $1) {
                $ofh->print(path($1)->slurp_utf8 . "\n");
            } else {
                croak $line;
            }
        } else {
            $ofh->print($line . "\n");
        }
    }
    undef $ifh;
} else {
    croak "$OS_ERROR: $input OR $output";
}

croak "$CHILD_ERROR: doctoc"
  if system("doctoc --title '## contents' $output") != 0;
