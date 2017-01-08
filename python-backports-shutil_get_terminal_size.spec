%global srcname backports.shutil_get_terminal_size
%global fedname backports-shutil_get_terminal_size
%global sum A backport of the get_terminal_size function from Python 3.3's shutil

Name:           python-%{fedname}
Version:        1.0.0
Release:        1
Summary:        %{sum}
Group:		Development/Python 
License:        MIT
URL:            https://github.com/chrippa/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel

%description
A backport of the get_terminal_size function from Python 3.3’s shutil.
Unlike the original version it is written in pure Python rather than C,
so it might be a tiny bit slower.

%package -n python2-%{fedname}
Summary:        %{sum}
Requires:       python2-backports

%description -n python2-%{fedname}
A backport of the get_terminal_size function from Python 3.3’s shutil.
Unlike the original version it is written in pure Python rather than C,
so it might be a tiny bit slower.


%prep
%setup -n %{srcname}-%{version}

%build
%__python2 setup.py build

%install
%__python2 setup.py install --root=%buildroot

# This files are provided by python-backports
rm -f %{buildroot}%{python2_sitelib}/backports/__init__.py*


%files -n python2-%{fedname}
%doc README.rst LICENSE
%{python2_sitelib}/%{srcname}-%{version}-py?.?.egg-info
%{python2_sitelib}/backports/shutil_get_terminal_size

    
%changelog
* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jun 23 2016 Dominika Krejci <dkrejci@redhat.com> - 1.0.0-1
- Initial release

