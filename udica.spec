
%define PYTHONVER 3.7

Summary: A tool for generating SELinux security policies for containers
Name: udica
Version: 0.0.1
Release: 3%{?dist}
Source0: https://github.com/wrabcak/udica/archive/master.tar.gz
License: GPLv3+
Group: Development/Libraries
BuildArch: noarch
Vendor: Lukas Vrabec <lvrabec@redhat.com>
Url: https://github.com/wrabcak/udica
BuildRequires: python3 >= %{PYTHONVER} python3-devel python3-setuptools python3-libsemanage python3-libselinux
Requires: python3 >= %{PYTHONVER} python3-libsemanage python3-libselinux

%description
Tool for generating SELinux security profiles for containers. The whole concept is based on "block inheritence" feature inside CIL intermediate language supported by SELinux userspace. The tool creates a policy which combines rules inherited from specified CIL blocks(templates) and rules discovered by inspection of container JSON file, which contains mountpoints and ports definitions.

%prep
%setup -n udica-master

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%license LICENSE
%{_bindir}/udica
%dir %{_datadir}/udica
%dir %{_datadir}/udica/templates
%{_datadir}/udica/templates/*
%dir %{python3_sitelib}/udica-0.0.1-py3.7.egg-info
%{python3_sitelib}/udica-0.0.1-py3.7.egg-info/*
%dir %{python3_sitelib}/udica
%{python3_sitelib}/udica/*

%changelog
* Thu Sep 20 2018 Lukas Vrabec <lvrabec@redhat.com> - 0.0.1-3
- Update readme and setup.py files after migration to github

* Sun Sep 16 2018 Lukas Vrabec <lvrabec@redhat.com> - 0.0.1-2
- Update LICENSE
- Improve %files section

* Sun Sep 16 2018 Lukas Vrabec <lvrabec@redhat.com> - 0.0.1-1
- Initial build
