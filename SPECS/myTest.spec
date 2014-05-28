#
# The Preamble
#
# The preamble contains information that will be displayed when users request information about the package. 
# This would include a description of the package's function, the version number of the software, and so on. 
# Also contained in the preamble are lines identifying sources, patches, and even an icon to be used if the 
# package is manipulated by graphical interface.

# Product name and version.  Use "Serial" instead of "Version" if the version is not clear
Summary: MyApp
Name: myapp
Version: 1.0
Release: 1
# Serial: 23

# Information about the author/distribution
Source: git://github.com/jlgrock/myapp
URL: http://www.myapp.com
Distribution: MadeUp Linux
Vendor: My Company
Packager: Justin Grant <jgrant@justinleegrant.com>
Copyright: GPL
Group: Applications/Sound

# Description/Summary of the product
Summary:  The one-line description of my app

%description
This is my app and what it does...

Provides: mail-reader
Requires: playmidi = 2.3
Requires: bla >= 0.3
Conflicts: playmidi =S 4
%setup

#
# The Prep Section
#
# The prep section is where the actual work of building a package starts. As the name implies, this section is 
# where the necessary preparations are made prior to the actual building of the software. In general, if 
# anything needs to be done to the sources prior to building the software, it needs to happen in the prep 
# section. Usually, this boils down to unpacking the sources.
# 
# The contents of this section are an ordinary shell script. However, RPM does provide two macros to make 
# life easier. One macro can unpack a compressed tar file and cd into the source directory. The other macro 
# easily applies patches to the unpacked sources.
%prep


#
# The Build Section
#
# Like the prep section, the build section consists of a shell script. As you might guess, this section is 
# used to perform whatever commands are required to actually compile the sources. This section could consist 
# of a single make command, or be more complex if the build process requires it. Since most software is built 
# today using make, there are no macros available in this section.
%build

#
# The Install Section
# 
# Also containing a shell script, the install section is used to perform the commands required to actually 
# install the software. If the software's author added an install target in the makefile, this section might 
# only consist of a make install command. Otherwise, you'll need to add the usual assortment of cp, mv, or 
# install commands to get the job done.
%install



#
# Install and Uninstall Scripts
#
# While the previous sections contained either information required by RPM to build the package, or the 
# actual commands to do the deed, this section is different. It consists of scripts that will be run, on 
# the user's system, when the package is actually installed or removed. RPM can execute a script:
# * Prior to the package being installed.
# * After the package has been installed.
# * Prior to the package being erased.
# * After the package has been erased.
#
# One example of when this capability would be required is when a package contains shared libraries. In 
# this case, ldconfig would need to be run after the package is installed or erased. As another example, if 
# a package contains a shell, the file /etc/shells would need to be updated appropriately when the package 
# was installed or erased.




#
# The Verify Script
#
# This is another script that is executed on the user's system. It is executed when RPM verifies the package's 
# proper installation. While RPM does most of the work verifying packages, this script can be used to verify 
# aspects of the package that are beyond RPM's capabilities.




#
# The Clean Section
#
# Another script that can be present is a script that can clean things up after the build. This script is 
# rarely used, since RPM normally does a good job of clean-up in most build environments.
%clean



#
# The File List
#
# The last section consists of a list of files that will comprise the package. Additionally, a number of macros 
# can be used to control file attributes when installed, as well as to denote which files are documentation, 
# and which contain configuration information. The file list is very important — if it is missing, no package will 
# be built.
%files
%doc README
/usr/local/bin/cdp
/usr/local/bin/cdplay
/usr/local/man/man1/cdp.1

