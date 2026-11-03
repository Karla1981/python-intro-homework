prog_language_list_1 = ["Python", "R", "Javascript"]
prog_language_list_2 = ["Java", "C++", "Python"]

# The union (all languages from both lists, no duplicates)
new_list = list(set(prog_language_list_1) | set( prog_language_list_2))
print(new_list)

# The intersection (languages in both lists)
# conver the list to sets before using the intersection method
languages_in_both = set(prog_language_list_1).intersection(set(prog_language_list_2))
print(languages_in_both)

# The difference (languages only in the first list)
# convert to sets first
languages_only_on_first_list = set(prog_language_list_1).difference(set(prog_language_list_2))
print(languages_only_on_first_list)
