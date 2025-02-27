A rainbow table attack is a method used by hackers to crack password hashes. 
Here's a simplified explanation:

Hashes:
Instead of storing passwords in plain text, systems often store them as "hashes." 
A hash is a one-way function that turns a password into a string of characters.
Rainbow Tables:
A rainbow table is a pre-computed table containing many possible passwords and 
their corresponding hashes.
Hackers use these tables to quickly look up a stolen hash and find the original 
password.
How it works:
If a hacker obtains a database of password hashes, they can compare those hashes 
to the ones in a rainbow table.
If a match is found, the hacker can easily recover the corresponding password.
In this project, we gave you a file that contains username and hash user's password
and want from you to return back password.

Note that the passwords range from 1000 to 9999.
use hashlib library in Python standard library to decoding hashed password.
notice that from simplicity we know that use sha256 for hashing the password.
Note: we just want you to create a function for doing that, so don't worry about 
input and output file.

example for csv file:

danial,99b057c8e3461b97f8d6c461338cf664bc84706b9cc2812daaebf210ea1b9974
elham,85432a9890aa5071733459b423ab2aff9f085f56ddfdb26c8fae0c2a04dce84c

output task:

danial,5104
elham,9770

