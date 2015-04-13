#!/usr/bin/env perl

use FileHandle;
use File::Slurp;
use Data::Dumper;

my %objs;
while ($line = <STDIN>) {
    chomp $line;
#    ($desig, $range,$numimp,$improb,$vinf,$H,$diam_km,$palermocum,$palermomax,$torino) = split /,/, $line;
    ($desig, @foo) = split /,/, $line;
    $torino = 0 if $torino eq '(*)';

    # If desig contains "(", it's numbered.  If not, it's a 
    # standard MPC YEAR-SUFFIX desig.
    if ($desig =~ /\(/) {
        if ($desig =~ /^(\d+)\s+/) {
            $desig = $1;
        }
        else {
            print STDERR "Weird desig: $desig\n";
        }
    }
    else {
        $desig =~ s/\s+//g; # strip all spaces
    }
    $objs{$desig} = [ @foo ];
}

#print Dumper(\%objs);

# Now loop through all files, adding diam_km and palermoc.
for $fn (@ARGV) {
    @lines = read_file(@ARGV);
    chomp @lines;
    $fh = new FileHandle ">new/$fn" or die "can't create new/$fn";
    $diam_km = $objs{$desig}->[5];
    $palermoc = $objs{$desig}->[6];
    $_ .= " $diam_km $palermoc\n" foreach @lines;
    print $fh @lines;
    $fh->close;
    print STDERR "Done $fn.\n";
}

__DATA__
Desig,Year Range,Potential Impacts,Impact Prob,Vinf,H,Diam,Palermoc,Palermom,Torino
2015 FL290,2082-2085,2,2.7e-06,10.85,22.0,0.130,-4.30,-4.36,0
2015 FQ332,2082-2089,6,5.1e-05,7.06,25.2,0.030,-4.70,-4.99,0
2015 DA54,2107-2107,1,4.7e-08,23.13,20.8,0.230,-5.27,-5.27,0
2015 FG120,2062-2103,4,6.9e-07,8.42,23.2,0.079,-5.39,-5.53,0
2015 FN36,2100-2113,3,9.5e-07,22.04,23.9,0.057,-5.47,-5.60,0
2015 EO,2050-2077,8,6.7e-06,14.24,26.6,0.016,-5.91,-6.14,0
2015 FE35,2096-2096,1,1.2e-09,25.21,19.3,0.460,-6.03,-6.03,0
2015 DD54,2114-2114,1,2.1e-06,6.70,25.4,0.028,-6.35,-6.35,0
2015 ET,2076-2114,10,3.7e-06,11.65,26.7,0.016,-6.42,-6.98,0
