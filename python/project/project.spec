%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           MODIFY-PROJECT-NAME
Version:        2.0
Release:        %{?dist}
Summary:        MODIFY-PROJECT-SUMMARY-ONE-LINER

Group:          Development/Libraries
License:        Apache License 2.0
URL:            http://MODIFY-GIT-URL-PATH
Source0:        http://MODIFY-URL-TO-CODE
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
Requires:       python >= 2.5, python-simplejson >= 2.0.7
BuildRequires:  python-setuptools


%description
This library provides MODIFY-DESCRIPTION


%prep
%setup -q


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
chmod a-x README
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README.rst CHANGES COPYING LICENSE 
# For noarch packages: sitelib
%{python_sitelib}/*


%changelog
* Sat Oct 1 2014 clairvoyant <clairvoyant@MODIFY.org> - 0.5-1
- Initial package.
