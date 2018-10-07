Summary: A tool for generating SELinux security policies for containers
Name: udica
Version: 0.0.4
Release: 1%{?dist}
Source0: https://github.com/containers/udica/archive/v%{version}.tar.gz
License: GPLv3+
BuildArch: noarch
Url: https://github.com/containers/udica
BuildRequires: python3 python3-devel python3-setuptools
Requires: python3 python3-libsemanage python3-libselinux

%description
Tool for generating SELinux security profiles for containers. The whole concept is based on "block inheritence" feature inside CIL intermediate language supported by SELinux userspace. The tool creates a policy which combines rules inherited from specified CIL blocks(templates) and rules discovered by inspection of container JSON file, which contains mountpoints and ports definitions.

%prep
%setup

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --single-version-externally-managed --root=$RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_mandir}/man8
install -m 0644 udica/man/man8/udica.8 %{buildroot}%{_mandir}/man8/udica.8

%files
%license LICENSE
%{_mandir}/man8/udica.8*
%{_bindir}/udica
%dir %{_datadir}/udica
%{_datadir}/udica/templates/*
%dir %{python3_sitelib}/udica-*
%{python3_sitelib}/udica-*
%dir %{python3_sitelib}/udica
%{python3_sitelib}/udica/*


%changelog
* Mon Oct 08 2018 Lukas Vrabec <lvrabec@redhat.com> - 0.0.4-1
- Add manpages
- Add support for communicating with libvirt daemon
- Add support for communicating with X server.
- Add support for read/write to the controlling terminal

* Sun Oct 07 2018 Lukas Vrabec <lvrabec@redhat.com> - 0.0.3-1
- Remove required parameters -i or -j and added support for reading json file from stdin.
- Remove "-n" or "--name" parameter. Name of the container will be required for this tool

* Tue Sep 25 2018 Lukas Vrabec <lvrabec@redhat.com> - 0.0.2-1
- Use subprocess.Popen instead of subprocess.run for inspecting to support also python2

* Thu Sep 20 2018 Lukas Vrabec <lvrabec@redhat.com> - 0.0.1-3
- Update readme and setup.py files after migration to github

* Sun Sep 16 2018 Lukas Vrabec <lvrabec@redhat.com> - 0.0.1-2
- Update LICENSE
- Improve %files section

* Sun Sep 16 2018 Lukas Vrabec <lvrabec@redhat.com> - 0.0.1-1
- Initial build
