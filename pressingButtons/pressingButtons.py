"""
Given a string of digits, return all of the possible non-empty letter combinations that the number could represent. The mapping of digits to letters is the same as you would find on a telephone's buttons, as in the example below:

The resulting array should be sorted lexicographically.

[input] string buttons

A string composed of digits ranging from '2' to '9'.

Guaranteed constraints:

0 ≤ buttons.length ≤ 7.

[output] array.string
"""

def button_to_letters(button):
    letters = { 
        2: ('a', 'b', 'c'), 3: ('d', 'e', 'f'), 4: ('g', 'h', 'i'), 
        5: ('j', 'k', 'l'), 6: ('m', 'n', 'o'), 7: ('p', 'q', 'r', 's'), 
        8: ('t', 'u', 'v'), 9: ('w', 'x', 'y', 'z')}
    return letters[int(button)]

def pressingButtons(buttons):
    if buttons:
        sub_strs = pressingButtons(buttons[1:])
        sub_strs = sub_strs if sub_strs else ['']
        return ['{}{}'.format(my_char, sub_strings) for 
                my_char in button_to_letters(buttons[0])
                for sub_strings in sub_strs]
    else:
        return []

