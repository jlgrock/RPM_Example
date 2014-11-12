%define _topdir %(echo $PWD)/
%define version 1.0

Summary:		My Name
Name:			myapp
Version:		%{version}
Release:		1
URL:			https://github.com/JIATFS/pegasus
Vendor:			VendorName
Packager:		Justin Grant <jlgrock@gmail.com>
License:		MIT
BuildArch:		noarch
BuildRoot:      my/path/%{name}-%{version}-%{release}
Requires:       redhat-release

%description
My Description

###############################################################################
%prep
###############################################################################
rm -rf $RPM_BUILD_ROOT

###############################################################################
%files
###############################################################################REMARK_SH.sql
%defattr(-,root,root)
/myfile.bla