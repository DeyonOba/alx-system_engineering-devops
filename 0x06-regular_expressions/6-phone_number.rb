#!/usr/bin/env ruby
# Use regular expression to match an input from the terminal

puts ARGV[0].scan(/\b\d{10}\b/).join
