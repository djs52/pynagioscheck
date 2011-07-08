%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python-nagioscheck
Version:        0.1.2
Release:        1%{?dist}
Summary:        A Python framework for Nagios plug-in developers

Group:          Development/Languages
License:        BSD
URL:            https://github.com/saj/pynagioscheck
Source0:        nagioscheck-0.1.2.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-setuptools

%description


%prep
%setup -q -n nagioscheck-0.1.2
%{__rm} -rf *.egg-info
%{__sed} -i 's,^#!.*env python.*$,#!/usr/bin/python,' \
    setup.py


%build


%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --root %{buildroot}

 
%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc
%{python_sitelib}/*


%changelog
* Fri Jul 01 2011 Saj Goonatilleke <sg@redu.cx> - 0.1.2-1
- Initial release.
