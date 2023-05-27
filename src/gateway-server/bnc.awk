BEGIN{
  print "http {"
  print "\tserver {"
};
{
  if ($1 != "") {
  print "\t\tlocation " $1 " {"
  print "\t\t\trewrite ^" $1 "(.*)$ /$1 break;"
  print "\t\t\tproxy_pass " $2 ";"
  print "\t\t}"
  }
};
END {
  print "\t}"
  print  "}"
  print "events {"
  print "}"
}
