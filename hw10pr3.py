# coding: utf-8
#
# the top line, above, is important --
# it ensures that Python will be able to use this file,
# even if you paste in text with Unicode characters
# (beyond ASCII)
# for an more expansive example of such a file, see
#    http://www.cl.cam.ac.uk/~mgk25/ucs/examples/UTF-8-demo.txt
#
# OK! Now we're ready for hw10pr3.py ...
#
#
# Name: Waverly Wang
#
#

# function #1
#
import random
def createDictionary(filename):
    """accepts a strin gwhich is the name of a text file 
    containing some sample text. It should
    return a dictionary whose
    keys are words encountered in the text file and
    whose entri
    es are a list of words that may legally follow the key
    word. Note that you should determine  away to keep track of frequency o finformation
    """
    pass
    f = open(filename)
    text = f.read()
    f.close()

    LoW = text.split() 
    
    pw = '$'
    d = {}
    for nw in LoW:
        if pw not in d:
            d[pw] = [nw]
        else:
            d[pw] += [nw]
        pw = nw
        if nw[-1] in '.!?': # then check for whether that new pw ends in                        # punctuation -- if it _does_ then set pw = '$'
            pw = '$'
    return d
    



# function #2
#
def generateText(d, N):
    """generates n number of words from d directiry"""
    pass
    pw = random.choice(d['$'])
    print(pw)
    for i in range(0, N): 
        nw = random.choice(d[pw])
        print(nw)
        pw = nw
        if nw[-1] in '.!?':
            pw = '$'
     #first choose words that follow $ radomly
    #second word will be randomly chosen among the list of words that followc firsr word
    #if seees a ?!. it should choose a random words from amon those that follow $



#
# Your 500-or-so-word CS essay (paste into these triple-quoted strings below):
#
"""
Harry Potter and the Chamber of Secrets. J.K Rowling

Even
aside
from
the
Slytherin
team,
had
been
spying
on
the
Slytherin
team,
had
seen
for
regular
training
sessions,
however,
was
why
Harry
was
not
dampened,
which
was
no
more
than
seven
greenish
blurs,
shooting
through
the
speed
of
bullets
thundered
on
the
flower
beds
turned
into
muddy
streams,
and
Ones.
They
reported
that
the
castle
windows
for
regular
training
sessions,
however,
was
no
more
than
seven
greenish
blurs,
shooting
through
the
flower
beds
turned
into
muddy
streams,
and
splattered
with
mud.
Even
aside
from
the
skin
and
splattered
with
mud.
Raindrops
the
size
of
garden
sheds.
They
reported
that
the
rain
and
Ones.
Raindrops
the
size
of
garden
sheds.
Even
aside
from
the
lake
rose,
the
speed
of
those
new
Nimbus
Two
Thousand
and
splattered
with
mud.
They
reported
that
the
flower
beds
turned
into
muddy
streams,
and
splattered
with
mud.
Fred
and
George,
who
had
been
a
few
days
before
Halloween,
returning
to
the
skin
and
Ones.
They
reported
that
the
air
like
missiles.
Even
aside
from
the
flower
beds
turned
into
muddy
streams,
and
wind
it
hadn't
been
a
few
days
on
the
castle
windows
for
themselves
the
Slytherin
team
was
not
dampened,
which
was
no
more
than
seven
greenish
blurs,
shooting
through
the
Slytherin
team,
had
been
a
few
days
on
the
flower
beds
turned
into
muddy
streams,
and
Ones.
Oliver
Wood's
enthusiasm
for
days
before
Halloween,
returning
to
be
found,
late
one
stormy
Saturday
afternoon
a
happy
practice
session.
Raindrops
the
Slytherin
team
was
to
the
Slytherin
team
was
to
Gryffindor
Tower,
drenched
to
be
found,
late
one
stormy
Saturday
afternoon
a
few
days
on
the
castle
windows
for
days
before
Halloween,
returning
to
the
flower
beds
turned
into
muddy
streams,
and
George,
who
had
seen
for
themselves
the
size
of
those
new
Nimbus
Two
Thousand
and
Ones.
Oliver
Wood's
enthusiasm
for
themselves
the
speed
of
bullets
thundered
on
the
flower
beds
turned
into
muddy
streams,
and
George,
who
had
been
a
few
days
before
Halloween,
returning
to
Gryffindor
Tower,
drenched
to
the
rain
and
Ones.
Raindrops the speed of garden sheds. 
Oliver
Wood's
enthusiasm
for
days
before
Halloween,
returning
to
the
lake
rose,
the
flower
beds
turned
into
muddy
streams,
and
wind
it
hadn't
been
a
few
days
before
Halloween,
returning
to
Gryffindor
Tower,
drenched
to
Gryffindor
Tower,
drenched
to
be
found,
late
one
stormy
Saturday
afternoon
a
happy
practice
session.
Raindrops
the
air
like
missiles.
Oliver
Wood's
enthusiasm
for
days
on
the
flower
beds
turned
into
muddy
streams,
and
George,
who
had
seen
for
themselves
the
flower
beds
turned
into
muddy
streams,
and
Ones.
Oliver
Wood's
enthusiasm
for
regular
training
sessions,
however,
was
why
Harry
was
no
more
than
seven
greenish
blurs,
shooting
through
the
air
like
missiles.
Fred
and
wind
it
hadn't
been
a
few
days
before
Halloween,
returning
to
the
rain
and
Ones.
Oliver
Wood's
enthusiasm
for
days
on
the
Slytherin
team,
had
seen
for
regular
training
sessions,
however,
was
why
Harry
was
why
Harry
was
no
more
than
seven
greenish
blurs,

"""
#
#
