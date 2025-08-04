#!/usr/bin/perl
use strict;
use warnings;

my @colorscheme;
my @syntax;
my @language;
my @formatter;
my @linter;
my @spell;
my @search;
my @manager;
my @runner;
my @cursor;
my @selection;
my @snippet_abbrev;
my @git_integration;
my @markdown_doc_tools;
my @time_tracker;
my @wiki_notes;
my @ui_enhancement;
my @uncategorized;

while (<STDIN>) {
	my $line1 = <STDIN>;
	if (!defined($line1)) {
		last;
	}
	chomp($line1);

	my $line2 = <STDIN>;
	if (!defined($line2)) {
		last;
	}
	chomp($line2);

    next unless $line1 =~ /^\* \[(.*?)\]\((.*?)\) : (.+)$/;

    my ($title, $url, $desc, $info) = ($1, $2, $3, $4);
    my $line = "* [$title]($url) : $desc";
    my $eval = "$title: : $desc";

    my $found = 0;
    if ($eval =~ /(color|scheme|theme)/i) {
        push @colorscheme, $line;
        push @colorscheme, $line2;
        $found = 1;
    }
    if ($eval =~ /(syntax)/i) {
        push @syntax, $line;
        push @syntax, $line2;
        $found = 1;
    }
    if ($eval =~ /(lang)/i) {
        push @language, $line;
        push @language, $line2;
        $found = 1;
    }
    if ($eval =~ /(format|fmt)/i) {
        push @formatter, $line;
        push @formatter, $line2;
        $found = 1;
    }
    if ($eval =~ /(lint)/i) {
        push @linter, $line;
        push @linter, $line2;
        $found = 1;
    }
    if ($eval =~ /(spell)/i) {
        push @spell, $line;
        push @spell, $line2;
        $found = 1;
    }
    if ($eval =~ /(search)/i) {
        push @search, $line;
        push @search, $line2;
        $found = 1;
    }
    if ($eval =~ /(manager)/i) {
        push @manager, $line;
        push @manager, $line2;
        $found = 1;
    }
    if ($eval =~ /(run|exec)/i) {
        push @runner, $line;
        push @runner, $line2;
        $found = 1;
    }
    if ($eval =~ /(cursor)/i) {
        push @cursor, $line;
        push @cursor, $line2;
        $found = 1;
    }
    if ($eval =~ /(select)/i) {
        push @selection, $line;
        push @selection, $line2;
        $found = 1;
    }
    if ($eval =~ /(snippet|abbrev|macro)/i) {
        push @snippet_abbrev, $line;
        push @snippet_abbrev, $line2;
        $found = 1;
    }
    if ($eval =~ /(git|blame|status)/i) {
        push @git_integration, $line;
        push @git_integration, $line2;
        $found = 1;
    }
    if ($eval =~ /(markdown|pandoc|preview)/i) {
        push @markdown_doc_tools, $line;
        push @markdown_doc_tools, $line2;
        $found = 1;
    }
    if ($eval =~ /(time|tracker)/i) {
        push @time_tracker, $line;
        push @time_tracker, $line2;
        $found = 1;
    }
    if ($eval =~ /(wiki|journal)/i) {
        push @wiki_notes, $line;
        push @wiki_notes, $line2;
        $found = 1;
    }
    if ($eval =~ /(statusline|tooltip|resize|tab)/i) {
        push @ui_enhancement, $line;
        push @ui_enhancement, $line2;
        $found = 1;
    }

    if (!$found) {
        push @uncategorized, $line;
        push @uncategorized, $line2;
    }
}

sub print_section {
    my ($title, $entries) = @_;
    return unless @$entries;
    print "### $title\n\n";
    print "$_\n" for @$entries;
    print "\n";
}

print_section("Color Scheme", \@colorscheme);
print_section("Syntax", \@syntax);
print_section("Language", \@language);
print_section("Formatter", \@formatter);
print_section("Linter", \@linter);
print_section("Spell Checker", \@spell);
print_section("Search", \@search);
print_section("File Manager", \@manager);
print_section("Runner / Executor", \@runner);
print_section("Cursor", \@cursor);
print_section("Selection", \@selection);
print_section("Snippet / Abbrev", \@snippet_abbrev);
print_section("Git Integration", \@git_integration);
print_section("Markdown / Doc Tools", \@markdown_doc_tools);
print_section("Time / Tracker", \@time_tracker);
print_section("Wiki / Notes", \@wiki_notes);
print_section("UI Enhancement", \@ui_enhancement);
print_section("Uncategorized", \@uncategorized);
