Name:           fedora-gooey-karma
Version:        1
Release:        2
Summary:        Fedora Gooey Karma

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
Fedora Gooey Karma

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
* Thu Mar 07 2013 Tomas Meszaros <exo@tty.sk> - 1-2
- updated load_installed() so installed packages are loading now much faster

* Mon Mar 04 2013 Tomas Meszaros <exo@tty.sk> - 1-1
- initial spec for Fedora
