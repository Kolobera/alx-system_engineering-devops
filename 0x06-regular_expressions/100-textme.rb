#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(\S*)\]\s\[to:(\+?\w*)\]\s\[flags:(\S*)\]/).join(',')
