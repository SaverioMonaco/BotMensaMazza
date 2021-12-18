#!./perl

use strict;

use POSIX qw(strftime);

# PER TROVARE IL TOKEN DEVI DECRIPTARE token.gpg COL COMANDO
# gpg token.gpg
# LA PASSWORD PER DECRIPTARE È IL NOME DEL CONO STRADALE
# (TUTTO MINUSCOLO, TUTTO UNITO)
my $bot_token  = 'INSERT_TOKEN';
my $bot_chatID = '-1001604234843';

# The URLs where to take all the informations.
# The first value after menu/ tells the day (in UNIX time)
# The other two are useless
# The last one is 3 for pranzo, 5 for cena
my @url = map { 'https://donmazza.serenissimacloud.it/menu/' . time . "/0/0/$_" } (3, 5);
my @html = map { join ' ', `curl $_` } @url;
my @dishes = map {
  my %results;
  $_ =~ m/<!-- INIZIO Piatti del giorno.*<!-- FINE Piatti del giorno/s;
  my $day_dishes = $&;
  while ($day_dishes =~ m/cbp-item[ \t]+cbp-l-grid-masonry-projects[ \t]+dt_([124]).*?cbp-l-grid-masonry-projects-title">(.*?)<\/div>/sg) {
    push @{$results{$1}}, $2;
  }
  \%results;
} @html;

my @meals = ('Pranzo', 'Cena');
my %types = ('1' => 'Primi', '2' => 'Secondi', '4' => 'Contorni');

my $message = 'Menù del giorno: ' . strftime("%d/%m/%y", localtime) . "\n";

while (my ($m, $meal) = each @meals) {
  $message .= "\n*$meal*\n";
  foreach my $t ('1', '2', '4') {
      $message .= "  *$types{$t}*\n";
      foreach (@{$dishes[$m]{$t}}) {
        $message .= "    $_\n";
      }
  }
}

$message =~ s/([\W])/"%" . uc(sprintf("%2.2x",ord($1)))/eg;
print `curl "https://api.telegram.org/bot$bot_token/sendMessage?chat_id=$bot_chatID&parse_mode=Markdown&text=$message"`;
