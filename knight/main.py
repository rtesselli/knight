from knight.parse import parse_input
from knight.logic import solve
from knight.output import output_solutions


def main():
    statements = parse_input()
    results = solve(statements)
    output_solutions(results)


# echo "Input to my program" | python main.py
if __name__ == '__main__':
    main()
