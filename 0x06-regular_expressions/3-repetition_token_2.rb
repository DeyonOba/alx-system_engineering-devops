#!/usr/bin/env ruby
# Use regular expression to match an input from the terminal

puts ARGV[0].scan(/hbt{1,4}n/).join
