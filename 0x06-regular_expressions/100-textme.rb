#!/usr/bin/env ruby
# Script outputs: [SENDER], [RECEIVER], [FLAGS]
# Sender phone number or name (including country if present)
# receiver phone number or name (including country if present)
# flags used

puts ARGV[0].scan(/(?<=from:|to:|flags:)[^\]]*/).join(',')
