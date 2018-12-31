import argparse


parser = argparse.ArgumentParser(description='This script is ')

# Test or not args
parser.add_argument('-t', '--test', default=False, type=bool, help='Test or not')
# The coordinate args
parser.add_argument('-lt_x', '--left_top_x', default=0, type=int, help='Left-top x-coordinate')
parser.add_argument('-lt_y', '--left_top_y', default=0, type=int, help='Left-top y-coordinate')
parser.add_argument('-rl_x', '--right_lower_x', default=0, type=int, help='Left-lower x-coordinate')
parser.add_argument('-rl_y', '--right_lower_y', default=0, type=int, help='Left-lower y-coordinate')

args = parser.parse_args()