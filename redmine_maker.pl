#!/usr/bin/env perl

use DateTime;
use DateTime::TimeZone;
use DateTime::Format::Strptime;
use Date::Calc qw( Date_to_Days );

my $csvfile = "./WorkLog2015/Work\ Log-Daily\ Breakdown.csv";
my $htmlout = "WorkLog2015.txt";
my $dt;
open INPUT, $csvfile or die "Can't open csv file!";
open HTMOUT, ">./$htmlout" or die "Can't open html out!";

print HTMOUT "|_.Date|_.Morning|_.Afternoon|_.Notes|\n";
# print HTMOUT "|_.Date|_.Morning|_.Afternoon|_.Notes|_.Planned Focus|\n";
while(<INPUT>) {

  chomp;
  s/\r/|/g;
  # s/,/|/g;
  my @entries = split(',', $_);
  my $parser = DateTime::Format::Strptime->new(
    pattern => '%m/%d/%Y',
    on_error => 'undef',
  );
  $dt = $parser->parse_datetime($entries[0]) or $dt="wookie";
  if ($dt ne "wookie") {
    my $now  = DateTime->now();
    my $then = DateTime->now()->subtract( days => 7 );
    $lower = Date_to_Days($then->year(),$then->month(),$then->day());
    $upper = Date_to_Days($now->year(),$now->month(),$now->day());
    $date  = Date_to_Days($dt->year(),$dt->month(),$dt->day());
    if (($date >= $lower) && ($date <= $upper)) {
      print HTMOUT "|";
      print HTMOUT $parser->format_datetime($dt);
      for ($i=1; $i<scalar @entries; $i++) {
        print HTMOUT "|".$entries[$i]
      }
      print HTMOUT "\n";
    }
  }

}

close (INPUT);
close (HTMOUT);
