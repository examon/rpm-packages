Name:           fedora-gooey-karma
Version:        1
Release:        5
Summary:        fedora-easy-karma like tool with GUI and some more features

Group:          Development/Tools
License:        MIT
URL:            https://github.com/examon/fedora-gooey-karma

#VCS: git://github.com/examon/fedora-gooey-karma.git
Source0:        fedora-gooey-karma.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       python-fedora
Requires:       fedora-cert
Requires:       yum
Requires:       bodhi-client
Requires:       python-pyside


%description
fedora-gooey-karma provides similar functionality to the fedora-easy-karma via GUI. It also provides some extra info like: yum info, bodhi info, test cases, bugs.

%prep
%setup -q -n fedora-gooey-karma

%build

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/fedora-gooey-karma
/usr/share/fedora-gooey-karma

%changelog
* Thu Apr 25 2013 Tomas Meszaros <exo@tty.sk> - 1-5
- added Fedora 19 support

* Sun Apr 21 2013 Tomas Meszaros <exo@tty.sk> - 1-4
- fixed exception invalid raising on checking karmaCheckBox

* Thu Mar 07 2013 Tomas Meszaros <exo@tty.sk> - 1-3
- fixed __serch_pkg()

* Thu Mar 07 2013 Tomas Meszaros <exo@tty.sk> - 1-2
- updated load_installed() so installed packages are loading now much faster

* Mon Mar 04 2013 Tomas Meszaros <exo@tty.sk> - 1-1
- initial spec for Fedora
