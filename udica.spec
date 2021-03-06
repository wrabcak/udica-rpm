Summary: A tool for generating SELinux security policies for containers
Name: udica
Version: 0.1.1
Release: 2%{?dist}
Source0: https://github.com/containers/udica/archive/v%{version}.tar.gz
License: GPLv3+
BuildArch: noarch
Url: https://github.com/containers/udica
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires: python3 python3-devel python3-setuptools
Requires: python3 python3-libsemanage python3-libselinux
%else
BuildRequires: python2 python2-devel python2-setuptools
Requires: python2 libsemanage-python libselinux-python
%endif

%description
Tool for generating SELinux security profiles for containers based on
inspection of container JSON file.

%prep
%setup -q

%build
%if 0%{?fedora} || 0%{?rhel} > 7
%{__python3} setup.py build
%else
%{__python2} setup.py build
%endif

%install
install --directory %%{buildroot}%{_datadir}/udica/templates

%if 0%{?fedora} || 0%{?rhel} > 7
%{__python3} setup.py install --single-version-externally-managed --root=%{buildroot}
%else
%{__python2} setup.py install --single-version-externally-managed --root=%{buildroot}
%endif

install --directory %{buildroot}%{_mandir}/man8
install -m 0644 udica/man/man8/udica.8 %{buildroot}%{_mandir}/man8/udica.8

%files
%{_mandir}/man8/udica.8*
%{_bindir}/udica
%dir %{_datadir}/udica
%dir %{_datadir}/udica/templates
%{_datadir}/udica/templates/*

%if 0%{?fedora} || 0%{?rhel} > 7
%license LICENSE
%{python3_sitelib}/udica/
%{python3_sitelib}/udica-*.egg-info
%else
%{_datarootdir}/licenses/udica/LICENSE
%{python2_sitelib}/udica/
%{python2_sitelib}/udica-*.egg-info
%endif

%changelog
* Tue Oct 23 2018 Lukas Vrabec <lvrabec@redhat.com> - 0.1.1-2
- Fix small issues in spec file like improve description and change files section.

* Mon Oct 22 2018 Lukas Vrabec <lvrabec@redhat.com> - 0.1.1-1
- Add proper shebang to all source files
- Add License to all source files

* Sat Oct 13 2018 Lukas Vrabec <lvrabec@redhat.com> - 0.1.0-1
- Add support for docker containers

* Mon Oct 08 2018 Lukas Vrabec <lvrabec@redhat.com> - 0.0.5-1
- Update x_container template based on testing container related to Nvidia Cuda operations

* Mon Oct 08 2018 Lukas Vrabec <lvrabec@redhat.com> - 0.0.4-2
- Build udica on Red Hat Enterprise Linux 7 with python version 2

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
- Improve %%files section

* Sun Sep 16 2018 Lukas Vrabec <lvrabec@redhat.com> - 0.0.1-1
- Initial build
