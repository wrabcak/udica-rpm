Summary: A tool for generating SELinux security policies for containers
Name: udica
Version: 0.0.2
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

%files
%license LICENSE
%{_bindir}/udica
%dir %{_datadir}/udica
%{_datadir}/udica/templates/*
%dir %{python3_sitelib}/udica-*
%{python3_sitelib}/udica-*
%dir %{python3_sitelib}/udica
%{python3_sitelib}/udica/*

%changelog
* Tue Sep 25 2018 Lukas Vrabec <lvrabec@redhat.com> - 0.0.2-1
- Use subprocess.Popen instead of subprocess.run for inspecting to support also python2

* Thu Sep 20 2018 Lukas Vrabec <lvrabec@redhat.com> - 0.0.1-3
- Update readme and setup.py files after migration to github

* Sun Sep 16 2018 Lukas Vrabec <lvrabec@redhat.com> - 0.0.1-2
- Update LICENSE
- Improve %files section

* Sun Sep 16 2018 Lukas Vrabec <lvrabec@redhat.com> - 0.0.1-1
- Initial build
