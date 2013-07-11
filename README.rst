Mambo - Content Management system
=================================

`Mambo`_ is a full-featured, award-winning content management system
that can be used for everything from simple websites to complex
corporate applications. It is used all over the world to power
government portals, corporate intranets and extranets, ecommerce sites,
nonprofit outreach, schools, church, and community sites.

This appliance includes all the standard features in `TurnKey Core`_,
and on top of that:

- Mambo configurations:
   
   - Installed from upstream source code to /var/www/mambo

- SSL support out of the box.
- `PHPMyAdmin`_ administration frontend for MySQL (listening on port
  12322 - uses SSL).
- Postfix MTA (bound to localhost) to allow sending of email (e.g.,
  password recovery).
- Webmin modules for configuring Apache2, PHP, MySQL and Postfix.

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH, MySQL, phpMyAdmin: username **root**
-  Mambo: username **admin**


.. _Mambo: http://mambo-foundation.org/
.. _TurnKey Core: http://www.turnkeylinux.org/core
.. _PHPMyAdmin: http://www.phpmyadmin.net
