#!/usr/bin/env ruby
# Regular expression that matches School

def match_school(input)
  regex = /School/
  if match_data = input.match(regex)
    puts match_data[0]
  else
    puts ''
  end
end

if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <input>"
  exit 1
end

match_school(ARGV[0])
