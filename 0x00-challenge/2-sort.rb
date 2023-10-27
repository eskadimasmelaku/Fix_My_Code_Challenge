###
#
#  Sort integer arguments

# Extract integers from command-line arguments
numbers = ARGV.select { |arg| arg.match?(/^-?\d+$/) }.map(&:to_i)

# Sort the numbers
sorted_numbers = numbers.sort

# Print the sorted numbers
sorted_numbers.each { |number| puts number }

