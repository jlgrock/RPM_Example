RPM_Example
===========

My first go at creating a simple RPM bundle

To build, use the command `rpmbuild -v -bb --clean SPECS/myTemplate.spec`


To check if it worked, you can see that everything bundled using the following command:
`rpm2cpio nameOfMyApp.rpm | cpio -idmv`

Also, you can install it!
`rpm -i nameOfMyApp.rpm`

Then, just check the installed RPMs:
`rpm -q nameOfMyApp` (or `rpm -qa | grep package-name`)

At which point, you can uninstall it with:
`rpm -e nameOfMyApp`