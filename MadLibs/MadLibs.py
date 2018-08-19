name1 = raw_input('\nEnter a name')
name2 = raw_input('\nEnter a name')
place1 = raw_input('\nEnter a place')
place2 = raw_input('\nEnter a place')
place3 = raw_input('\nEnter a place')
year1 = raw_input('\nEnter a year')
noun1 = raw_input('\nEnter a noun')
noun2 = raw_input('\nEnter a noun')
noun3 = raw_input('\nEnter a noun')
pluralnoun1 = raw_input('\nEnter a plural noun')
pluralnoun2 = raw_input('\nEnter a plural noun')
pluralnoun3 = raw_input('\nEnter a plural noun')
pluralnoun4 = raw_input('\nEnter a plural noun')
adjective1 = raw_input('\nEnter a adjective')
adjective2 = raw_input('\nEnter a adjective')
pluralprofession1 = raw_input('\nEnter a plural profession')

madlib = "\nAlbert Einstein, the son of %s and %s,\n\
was born in %s in %s. In 1902, he had a job\n\
as assistant %s in the Swiss patent office and attended\n\
the University of %s. There he began studying atoms, molecules,\n\
and %s. He developed the theory of\n\
%s relativity, which expanded the phenomena of sub-atomic\n\
%s and %s magnetism. In 1921,\n\
he won the Nobel prize for %s and was director of\n\
theoretical physics at the Kaiser Wilhelm %s in Berlin.\n\
In 1933, when Hitler became Chancellor of %s,\n\
Einstein came to America to take a post at Princeton Institute for\n\
%s, where his theories helped America devise the first\n\
atomic %s. There is no question about it: Einstein was\n\
one of the most brilliant %s of our time."

formattedinput = (name1, name2, place1, year1, noun1, place2, pluralnoun1, adjective1, pluralnoun2, adjective2,
               pluralnoun3, noun2, place3, pluralnoun4, noun3, pluralprofession1)

print (madlib % formattedinput)
