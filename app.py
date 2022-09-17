import re
from rich.console import Console
from rich.table import Table
from collections import Counter
# from check import checkIdentifier

# converted .sol to .txt which contains only one function.
file_name = 'test.txt'

# should contain all the identifiers contained in the above function
identifier_list = ['test', '_spender', '_value', 'success', 'allowance']

# List of assignment operators
assignment_list = [" = ", "+=", "*=", "-=", "%=", "/="]

# List of comparison opeartors
comparison_list = ["==", "!=", " > ", " < ", ">=", "<="]

# List of keywords
reserve_words = ["pragma", "library", "contract", "is", "function",
                 "event", "emit", "modifier", "return ", "public",
                 "private", "const", "external", "internal",
                 "payable", "assert",
                 "require", "throw", "import", "as", "indexed",
                 "pure", "view", "memory", "storage", "calldata",
                 "abstract", "after", "alias", "apply",
                 "auto", "case", "catch", "copyof", "default",
                 "define", "final", "immutable", "implements", "in",
                 "inline", "let", "macro", "match",
                 "mutable", "null", "of", "override", "partial",
                 "promise", "reference", "relocatable", "sealed",
                 "sizeof", "static", "supports", "switch", "try",
                 "typedef", "typeof", "unchecked"]

# List of operators that is not in assignment and comparison operators
operators_list = [" + ", " - ", "*", "/", "%", "++", "--", "&&", "||", "!",
                  " & ", " | ", "^", "~", "<<", ">>"]

# list of data typess
data_types = ['address', 'bool', 'string', 'var', 'int', 'int8',
              'int16', 'int24', 'int32', 'int40', 'int48',
              'int56', 'int64', 'int72', 'int80', 'int88', 'int96',
              'int104',
              'int112', 'int120', 'int128', 'int136', 'int144',
              'int152', 'int160', 'int168', 'int176', 'int184',
              'int192', 'int200', 'int208', 'int216', 'int224',
              'int232', 'int240', 'int248',
              'int256', 'uint', 'uint8', 'uint16', 'uint24',
              'uint32', 'uint40', 'uint48', 'uint56', 'uint64',
              'uint72', 'uint80', 'uint88', 'uint96', 'uint104',
              'uint112', 'uint120',
              'uint128', 'uint136', 'uint144', 'uint152',
              'uint160', 'uint168', 'uint176', 'uint184', 'uint192',
              'uint200',
              'uint208', 'uint216', 'uint224', 'uint232',
              'uint240', 'uint248', 'uint256', 'byte', 'bytes',
              'bytes1', 'bytes2',
              'bytes3', 'bytes4', 'bytes5', 'bytes6', 'bytes7',
              'bytes8', 'bytes9', 'bytes10', 'bytes11', 'bytes12',
              'bytes13',
              'bytes14', 'bytes15', 'bytes16', 'bytes17',
              'bytes18', 'bytes19', 'bytes20', 'bytes21', 'bytes22',
              'bytes23',
              'bytes24', 'bytes25', 'bytes26', 'bytes27',
              'bytes28', 'bytes29', 'bytes30', 'bytes31', 'bytes32']

# List of special characters
sp_list = [" = ", "+=", "*=", "-=", "%=", "/=", "==", "!=", ">", "<",
           ">=", "<=", "~", "!", "#", "$", "%", "^", " & ",
           "*", "(", ")",
           " _", " + ", ",", " / ", " | ", " - ", " = ", " < ", " > ", " ? ", "{",
           "}", "[", "]", ":", ";", '\t', '\n', " ", '',
           '*/', '/*', ]

# List of conditional statements
condition_list = ["if", "else"]
loop_list = ["for", "while"]
parenthesis_list = ["(", ")"]
alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
             "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ]

# List of comments
comments_list = ["//", "/*"]
console = Console()
table = Table(show_header=True, title=file_name, header_style="white")
table.add_column("ID", width=12)
table.add_column("Metric")
table.add_column("Avg")
table.add_column("Max")
characters = []
numbers = []
count_code = 0
count_alphabet = 0
count_blank = 0
isAssignment = False
count_tab = 0
count_specialChar = 0

res = []
identifier_occurance = 4
identifer_length_max = 0
identifierLength = 0
identifiers_average = 0
identifiers_max = 0
occurance_identifier_average = 0
count_condition = 0
count_datatypes = 0
count_keywords = 0
count_line = 0
count_comma = 0
count_operators = 0
count_paranthesis = 0
count_comparison = 0
count_assignment = 0
count_comment = 0
count_numbers = 0
count_loop = 0
count_period = 0
max_alphabet = 0
identifiers = []
count_line_length = 0
count_line_length_max = 0


with open(file_name) as file:
    count_blank = sum(1 for line in file if len(line.strip()) == 0)
file.close()


with open(file_name) as file:
    for line in file:
        if len(line.strip()) != 0:
            count_line_length += len(line.strip())
            if len(line.strip()) > count_line_length_max:
                count_line_length_max = len(line.strip())


file.close()


with open(file_name) as file:

    text = file.read()
    count_line = text.count('\n')
    results = Counter(text)
    count_space = text.count(' ')
    count_comma = text.count(',')
    count_period = text.count('.')
    count_tab = text.count('    ')
    count_space = count_space-(4*count_tab)

# count assignments
for assignment in assignment_list:
    count_assignment += text.count(assignment)


# count operators
for operator in operators_list:
    count_operators += text.count(operator)


# count comparisons
for comparison in comparison_list:
    count_comparison += text.count(comparison)
# print("comparison", count_comparison)


# count conditionals
for condition in condition_list:
    count_condition += text.count(condition)


# print(identifier_list)
identifiers_average = round(len(identifier_list)/count_line, 4)
identifiers_max = len(identifier_list)
occurance_identifier_average = round(identifier_occurance/count_line, 4)

if len(identifier_list) == 0:
    print('Please enter the identifier names in list')
else:
    for identifier in identifier_list:
        if(len(identifier) > identifer_length_max):
            identifer_length_max = len(identifier)
            identifierLength += len(identifier)
    (round(identifierLength/count_line, 4))
    res.append(identifer_length_max)
    res.append(identifiers_average)
    res.append(identifiers_max)
    res.append(occurance_identifier_average)
    res.append(identifier_occurance)


# count comments
for comment in comments_list:
    count_comment += text.count(comment)


# count reserve
for keywords in reserve_words:
    count_keywords += text.count(keywords)
# print("reserve", count_reserve)


# count loops
for loop in loop_list:
    count_loop += text.count(loop)

# count numbers
for digit in text:
    if re.search('[0-9]', str(digit)):
        match = re.search('[0-9]', str(digit))
        numbers.append(match.group())

count_numbers = len(numbers)

# count parenthesis
for parenthesis in parenthesis_list:
    count_paranthesis += text.count(parenthesis)

# Identifer length
for datatype in data_types:
    identifiers.append(datatype)
    count_datatypes += text.count(datatype)


# count special char
for specialChar in sp_list:
    count_specialChar += text.count(specialChar)

count_line += 1

for items in results.items():

    if re.search('[a-zA-Z]', str(items)):
        match = re.search('[a-zA-Z]', str(items))
        characters.append(match.group())


for char in characters:
    if results.get(str(char)) > max_alphabet:
        max_alphabet = results.get(str(char))
    count_alphabet += results.get(str(char))


# add values to table
table.add_row(
    "1", "Assignment", str(
        round(count_assignment/count_line, 4)), str(count_assignment),
)
table.add_row(
    "2", "Blank Line", str(round(count_blank/count_line, 4)), str(count_blank),
)
table.add_row(
    "3", "Commas", str(round(count_comma/count_line, 4)), str(count_comma),
)
table.add_row(
    "4", "Comments", str(
        'Nil'), str("Nil"),
)
table.add_row(
    "5", "Comparisons", str(
        round(count_comparison/count_line, 4)), str(count_comparison),
)
table.add_row(
    "6", "Conditionals", str(
         round(count_condition/count_line, 4)), str(count_condition),
)
table.add_row(
    "7", "Identifier Length", str(
        round(identifierLength/count_line, 4)), str(identifer_length_max),
)

table.add_row(
    "8", "Intendation", str(
         round(count_tab/count_line, 4)), str(count_tab),
)
table.add_row(
    "9", "Keywords", str(
         round(count_keywords/count_line, 4)), str(count_keywords),
)
table.add_row(
    "10", "Line Length", str(
        round(count_line_length/count_line, 4)), str(count_line_length_max)),

table.add_row(
    "11", "Loops", str(
        round(count_loop/count_line, 4)), str(count_loop),
)
table.add_row(
    "12", "N. of identifiers", str(
        identifiers_average), str(identifiers_max),
)
table.add_row(
    "13", "N. of numbers", str(
        round(count_numbers/count_line, 4)), str(count_numbers),
)
table.add_row(
    "14", "Operators", str(
        round(count_operators/count_line, 4)), str(count_operators),
)
table.add_row(
    "15", "Parenthesis", str(
        round(count_paranthesis/count_line, 4)), str(count_paranthesis),
)
table.add_row(
    "16", "Period", str(
        round(count_period/count_line, 4)), str(count_period),
)
table.add_row(
    "17", "Spaces", str(
        round(count_space/count_line, 4)), str(count_space),
)
table.add_row(
    "18", "Occurance of any character", str(
        round(count_alphabet/count_line, 4)), str(max_alphabet),
)
table.add_row(
    "19", "Occurance of Identifier", str(
        occurance_identifier_average), str(identifier_occurance),
)
console.print(table)
# print(results)
# print(count_line)
