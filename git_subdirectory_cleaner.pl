#!/usr/bin/env perl

###
# Utility to clean .git folders out of sub directories, ignores the current directory
#  Useful for cleaning 'sub-repos' out of your directory structure
#
# Created by Dee J. Mann Feb 2024
# All Rights Reserved
###
# To use:
# On Linux systems: 
#  Setup:
#    1) Place file in root git repo directory
#    2) Make executable with: chmod +x clean_dirs.pl
#  To Execute:
#    ./clean_dirs.pl
#  NOTE:
#    This will only work from the same directory the perl script lives in.
#    This may be very dangerous if added to the $PATH.
#    It is safer to just place it in the base directory repo.
###

use File::Find;
use File::Path qw(rmtree);
use strict;

my $version = 0.01;
my $author = "Dee J. Mann";
my $dir = '.';

my $dir_count = 0;

sub display_welcome {
    # Output script info
    printf("Clean Dirs: Version: $version\n");
    printf("Created By: $author Feb 2024\n");
    printf("All Rights Reserved\n")
}

sub process_dirs {

    # If the name is .git and it is a directory
    if($_ eq '.git' and -d $_) {

        # Get the full path of the directory
        my $path = $File::Find::name;

        # If the path is not the same as the current directory
        if($path ne "$dir/.git") {

            # Let the user know we found a dir
            printf("Found and removed $path\n");

            # Remove the directory and all its contents
            rmtree($_) or warn "Failed to remove $_: $!";

            # Skip further processing of this directory
            $File::Find::prune = 1;
            # Append to the count
            $dir_count += 1;
        }
    }
}

display_welcome();
find(\&process_dirs, $dir);
my $dir_str = "directories";
if($dir_count == 1) {$dir_str = "directory"}
printf("All done! Removed $dir_count $dir_str.\n");