#!/usr/bin/env ruby
# Use regular expression to match an input from the terminal

puts ARGV[0].scan(/hb{2,5}n/).join
