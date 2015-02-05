password.py
===========
password.py is a keyboard layout and prefix password generator for better
passwords.

Why?
====
Secure passwords are all the rage these days. Actually remembering passwords is
far less in vogue, and password resets are common and expected.

The more you, as a user, reset your passwords, the less likely you will
construct a strong password the next time. So the solution is obvious: Stop
forgetting your passwords. There's already the option of using a password
manager, but if that gets compromised you're going to be in a complete mess.

A possible solution
===================
Pattern-based passwords are becoming a thing. Instead of remembering a series
of different passwords, remember a single strong password to use as a prefix
to another password based off a secret (constant) string and the name of the
website or service. Additionally, scramble the secret string and service name
by applying a transformation to each character before typing it.

This is the approach taken by the [qwertycard](http://qwertycards.com/), sold by Tream Tech Ltd.:
Each card contains a strong prefix password, as well as a mapping between the
letters in your own strings and random typeable letters on the keyboard. See
their website for an example of this.

A dirty implementation
======================
Hot on the heels of the qwertycard comes password.py. password.py generates
both this random mapping and the strong prefix password for you, but doesn't
give you the cool-looking card (or guaranteed randomness, or indeed any sort of
guarantee) that a qwertycard provides.

Additionally, if you provide password.py a layout, prefix password, secret
and service name, it will output the sequence of characters you have to type
in order to produce the password for that service.

Example usage
=============

    > ./password.py
    Layout: QWERTYUIOPASDFGHJKLZXCVBNM
            8:<blw%zxOtn*4/Z@# iT"geKo
    Base phrase: ek 6NUmU
    Keep these safe and don't lose them!
    Use your layout like this:
      ./password.py '8:<blw%zxOtn*4/Z@# iT"geKo' 'ek 6NUmU' <secret> <sitename>

Usage notes
===========
When run without parameters, password.py will output a layout and base phrase.
The base phrase is a prefix you should put in front of every password you
create.
The layout returned is a map between the characters on the keyboard and the
characters in the layout.

For instance, if the layout is

    8:<blw%zxOtn*4/Z@# iT"geKo

then the mapping will look like

    QWERTYUIOPASDFGHJKLZXCVBNM
    8:<blw%zxOtn*4/Z@# iT"geKo

When typing your secret and site name, use the mapping. For instance, instead
of typing 'moteki', you would type 'oxl<#z' instead, because 'M' maps to 'O',
'O' maps to 'x' and so on. Note that the keys in the mapping are not case-
sensitive, but the characters they map to are. Let's hope you don't use a site
with only digits in the site name.

When you design your passwords, think up a common secret word that will be used
across all passwords.
If this word is 'moteki', and your base phrase is 'ek 6NUmU', then all your
passwords will begin with

    ek 6NUmUoxl<#z

Then the end of the password is the name of the site or service you're
generating the password for. For example, if generating a password for
www.shazbot.co.uk, the site name is 'shazbot'. You suffix the mapped version
of the site name to the prefix password. 'shazbot' remapped under our layout
reads as 'nZtiexl', so our final password for www.shazbot.co.uk will read as

    ek 6NUmUoxl<#znZtiexl

For the lazy and those who live dangerously
===========================================
Supposing you don't want to go through the tedious business of doing this
character mapping for the secret and site name yourself, password.py will
do this for you.

    > /password.py '8:<blw%zxOtn*4/Z@# iT"geKo' 'ek 6NUmU' moteki shazbot
    Your password is: ek 6NUmUoxl<#znZtiexl

Provide password.py the generated mapping, base phrase, your secret and site
name and it will produce the password for you. Not super recommended, but
probably easier to use until you've memorised the mapping and base phrase.

Caveats
=======
Some websites disallow special characters or have limits on password length.
Usually this is a sign of something very, very wrong with how they handle
passwords, so be careful when interacting with these sites. If forced to
use one, you can remove characters and truncate your password as necessary,
but this will obviously compromise security.

Disclaimer
==========
password.py doesn't pretend to be even the tiniest bit secure: The string and
mapping generation isn't special, using the built-in Python random library.
If you're serious about security, you'll want something else. If you use
password.py, you use it at your own risk. If you want something with real
security, qwertycards claims to have true randomness in their cards.

In other words, there's NO WARRANTY. You can see the license for more info.
I don't even know what 'crypto' or 'security' are, I just live here.

Also, if you have a non-QWERTY layout or commonly switch layouts, you might
have trouble using password.py passwords. As long as you have the mapping
and base phrase however, you should be okay if you give it some thinking.