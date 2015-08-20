#!/usr/bin/python
"""Set Mambo admin password and email

Option:
    --pass=     unless provided, will ask interactively
    --email=    unless provided, will ask interactively

"""

import sys
import getopt
import inithooks_cache
import hashlib

from dialog_wrapper import Dialog
from mysqlconf import MySQL
from executil import system

def usage(s=None):
    if s:
        print >> sys.stderr, "Error:", s
    print >> sys.stderr, "Syntax: %s [options]" % sys.argv[0]
    print >> sys.stderr, __doc__
    sys.exit(1)

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass=', 'email='])
    except getopt.GetoptError, e:
        usage(e)

    password = ""
    email = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            password = val
        elif opt == '--email':
            email = val

    if not password:
        d = Dialog('TurnKey Linux - First boot configuration')
        password = d.get_password(
            "Mambo Password",
            "Enter new password for the Mambo 'admin' account.")

    if not email:
        if 'd' not in locals():
            d = Dialog('TurnKey Linux - First boot configuration')

        email = d.get_email(
            "Mambo Email",
            "Enter email address for the Mambo 'admin' account.",
            "admin@example.com")

    inithooks_cache.write('APP_EMAIL', email)

    hash = hashlib.md5(password).hexdigest()

    m = MySQL()
    m.execute('UPDATE mambo.users SET password=\"%s\" WHERE username=\"admin\";' % hash)
    m.execute('UPDATE mambo.users SET email=\"%s\" WHERE username=\"admin\";' % email)

    config = "/var/www/mambo/configuration.php"
    system("sed -i \"s|mailfrom =.*|mailfrom = '%s';|\" %s" % (email, config))


if __name__ == "__main__":
    main()

