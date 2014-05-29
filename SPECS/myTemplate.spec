#######################################################################################
#
# This file attempts to include all of the common directives and macros that one might 
# use to create a simple spec file.  This keeps the documentation of this code local.  
# Please do further documentation research for more information about any of this 
# though, as this was not meant to be complete, but rather a good starting template.
# Anything that is not used should be removed from this file or commented out.
#
# Please note that Directives (in the Prep and Files sections) and Sections that are used
# for building (Prep, Build, Install, Files, Clean, Changelog) and 
# Packaging (Pre, Post, Preun, Postun, Trigerrin, Triggerun, TriggerPostun, Verify) all
# start with a percent sign.
#
#######################################################################################



#######################################################################################
#
# Variables
#
########################################################################################
# Define variables that can be used in later sections.  There are a number of global 
# variables that can be accessed as well, which you can look up 
# at http://fedoraproject.org/wiki/Packaging:RPMMacros or check /usr/lib/rpm/macros for 
# all of them (specific to each distribution).

%define name bla
%define version 1.0
%define longname %{name}-%{version}
%define dir %{_initddir}/${longname}

#######################################################################################
#
# The Preamble
#
#######################################################################################
# The preamble contains information that will be displayed when users request 
# information about the package. This would include a description of the package's 
# function, the version number of the software, and so on. Also contained in the
# preamble are lines identifying sources, patches, and even an icon to be used if the 
# package is manipulated by graphical interface.

# Product name and version.  Use "Serial" instead of "Version" if the version is not clear
Summary: MyApp
Name: myapp
Version: %{version}
Release: 1
# Serial: 23

# Information about the author/distribution
Source: git://github.com/jlgrock/myapp
URL: http://www.myapp.com
Distribution: MadeUp Linux
Vendor: My Company
License: Government Open Source

# This is the graphics file (often GIF) that contains an icon for this package 
# (used by graphical package-management tools).
Icon: bla.xpm

# The group that this will be categorized with.  If not provided, the default is "Applications/System"
Group: Applications/Sound      

# Name and email address of person who packaged the product
Packager: Justin Grant <jgrant@gmail.com>

# Description/Summary of the product
Summary:  Installs Postgres and a bunch of useful extensions

%description
Installs Postgres and a bunch of useful extensions

# This is a URL for the source files for the software. The filename part is used by 
# the build process, and the rest of the URL is for informational purposes. Note that
# Source is the same as Source0 (the 0 is optional).
Source: bla.tar.gz
Source1: bla2.tar.gz
Source2: bla3.tar.gz

# These entries denote the filenames of the patch files used during the build process. 
# Patch is the same as Patch0.
Patch: bla.patch
Patch1: bla1.pach
Patch2: bla.testsuite.patch

BuildRequires: libtool, someothertool

# The architecture (x86 vs x64 vs whatever)
BuildArch:      noarch

# the name of the directory in which you'd like the software to install. If, for example,
# you specify a build root of /tmp/foo, and the software you're packaging installs a file
# bar in /usr/bin, you'll find bar residing in /tmp/foo/usr/bin after the build.
#
# This option instructs RPM to place files in a temporary directory during the install step. This 
# is very useful when building packages for a distribution.
#
# Also, you can refer to this using the environment variable RPM_BUILD_ROOT
BuildRoot: %{_tmppath/%{name}-%{version}-%{release}-root-

# What the package provides (other than it's own name, which is provided by default)
Provides: mail-reader

# The list of items that the package requires.  If programs require shared libs or
# interpreters, it is detected automatically.
Requires: playmidi = 2.3
Requires: bla >= 0.3
Requires(post): /sbin/bla
Requires(preun): /sbin/bla

# Lists the conflicts that the package has.  This is used by RPM to prevent two conflicting
# packages from being installed on the same machine.
Conflicts: playmidi =S 4

# This lists packages that are obsoleted by this package. This is a more specific version 
# of the Conflicts field.
Obsoletes:


#######################################################################################
#
# The Prep Section
#
#######################################################################################
# The prep section is the first section of the build process, where the actual work 
# of building a package starts. As the name implies, this section is where the 
# necessary preparations are made prior to the actual building of the software. 
# In general, if anything needs to be done to the sources prior to building the
# software, it needs to happen in the prep section. Usually, this boils down to
# unpacking the sources.
# 
# It is the responsibility of the %prep script to:
# * Create the top-level build directory.
# * Unpack the original sources into the build directory.
# * Apply patches to the sources, if necessary.
# * Perform any other actions required to get the sources in a ready-to-build state.
#
# The contents of this section are an ordinary shell script. However, RPM does provide
# two macros to make life easier. One macro (%setup) can unpack a compressed tar file 
# and cd into the source directory. The other macro (%patch) easily applies patches to 
# the unpacked sources.
#
# The %setup has several parameters that it can take:
# * -n <name> - The name of the build directory
# * -c - Create the directory (and change to it) before unpacking
# * -D - Do not delete the top level directory before Unpacking sources
# * -b <n> - Unpack the nth source before changing the directory
# * -a <n> - Unpack the nth source after changing the directory
# * -q - Run quietly with Minimal Output
# * -T - Disable the unpacking of archives
#
# The %prep has several parameters that it can take:
# * -p <n> - Strip n leading slashes and directories from patch filenames
# * -b <name> - set the backup file extension to <name>
# * -E - Remove empty output files

%prep

%setup

%patch

#######################################################################################
#
# The Build Section
#
#######################################################################################
# The second section in the build process.  Like the prep section, the build 
# section consists of a shell script. As you might guess, this section is used to
# perform whatever commands are required to actually compile the sources. This 
# section could consist of a single make command, or be more complex if the build
# process requires it. Since most software is built today using make, there are no
# macros available in this section.
%build

#######################################################################################
#
# The Install Section
# 
#######################################################################################
# The third section in the build process.  Also containing a shell script, the install section is used to perform the commands
# required to actually install the software. If the software's author added an install
# target in the makefile, this section might only consist of a make install command. 
# Otherwise, you'll need to add the usual assortment of cp, mv, or install commands 
# to get the job done.
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


#######################################################################################
#
# Install and Uninstall Scripts
#
#######################################################################################
# While the previous sections contained either information required by RPM to build the
# package, or the actual commands to do the deed, this section is different. It consists
# of scripts that will be run, on the user's system, when the package is actually installed
# or removed. RPM can execute a script:
# * Prior to the package being installed. (%Pre)
# * After the package has been installed. (%Post)
# * Prior to the package being erased. (%PreUn)
# * After the package has been erased. (%PostUn)
#
# One example of when this capability would be required is when a package contains shared
# libraries. In this case, ldconfig would need to be run after the package is installed or
# erased. As another example, if a package contains a shell, the file /etc/shells would
# need to be updated appropriately when the package was installed or erased.
%Install

%Pre
if [ -f /some/file ]
then
    echo "/some/file exists, it shouldn't"
    exit -1
fi
if [ -z "${$VAR}" ]
then
	echo "VAR is not set at all"
fi

if [ -z "$VAR" -a "${VAR+xxx}" = "xxx" ]
then
	echo "VAR is set but empty"
fi

%Post
%PreUn
%PostUn



#######################################################################################
#
# The Verify Directive
#
#######################################################################################
# This is another script that is executed on the user's system. It is executed when RPM
# verifies the package's proper installation. While RPM does most of the work verifying
# packages, this script can be used to verify aspects of the package that are beyond
# RPM's capabilities.  This is executed when you do a "rpm -V".
#
# By default, this directive macro follows the following format:
# %verify(mode md5 size maj min symlink mtime) <file>
# or
# %verify(not owner group) <file>
%verify(mode md5 size maj min symlink 456789) /foo/bar


#######################################################################################
#
# The Clean Directive
#
#######################################################################################
# Another script that can be present is a script that can clean things up after the build. This script is 
# rarely used, since RPM normally does a good job of clean-up in most build environments.  So much so that
# some of the implementations ignore this section entirely.
%clean
rm -rf $RPM_BUILD_ROOT


#######################################################################################
#
# The Attribute Directive
#
#######################################################################################
# The %attr directive is used to permit RPM to directly control a file's permissions and ownership. It is
# normally used when non-root users build packages.  Format = "%attr(<mode>, <user>, <group>) file".  To set
# the default attr for all files, use the %defattr, format = "%defattr(<file mode>, <user>, <group>, <dir mode>)".
# Attributes that do not need to be set can be replaced with a dash.

%defattr(-, root, root, -)
%attr(644, root, root) /usr/local/bin/abc.def

#######################################################################################
# 
# The Documentation Directive
# 
#######################################################################################
# %doc will define where your documentation is for inclusion.  Use %doc for individual
# files and %docdir for directories.
# 

%doc README LICENSE bla.txt
%docdir /usr/local/docs

#######################################################################################
#
# Configure Directive
#
#######################################################################################
# Similar to the %doc directive, the %config directive marks a file as configuration.
# The only restriction is that this directive can only take one parameter.
#
%config /etc/yp.conf
%config /etc/rc.d/init.d/*

#######################################################################################
#
# The Files Section
#
#######################################################################################
# The last section consists of a list of files (full path!) that will comprise the package. Additionally, a 
# number of macros can be used to control file attributes when installed, as well as to denote which files 
# are documentation, and which contain configuration information. The file list is very important — if it
# is missing, no package will be built.
#
# The %dir allows you to package only the directory itself, and ignores the files contained within it.  Prefix 
# allows you to tell all files in the %files list what to prefix with. (e.g. "/local" becomes "/usr/local")

Prefix: /usr
%files
/local/bin/cdp
/local/bin/cdplay
/local/man/man1/cdp.1
%dir /usr/bla

#
# Change Log
# 
# Edit to describe the last change you have made to the package. Fill it in with the date, your name and email address, 
# the version and release of the package, and a short description of what has changed in the package in the following format:
# * date Packager's Name <packager's_email> version-revision
# - Summary of changes
%changelog

* 5/13/2014 Justin Grant <jlgrock@gmail.com> 0.8.18.1-0.2
- Updated to fix spelling mistake

* 5/12/2014 Justin Grant <jlgrock@gmail.com> 0.8.18.1-0.1
- Initial RPM Release
