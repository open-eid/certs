Name: esteidcerts
Version: 3.3
Release: 1%{?dist}
Summary: Estonian ID card certificates
Group: System Environment/Libraries
License: LGPLv2+
URL: http://www.ria.ee		
Source0: esteidcerts.tar.gz
BuildRoot: %{_tmppath}/-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArchitectures: noarch

%description
Estonian ID card root, intermediate and OCSP certificates

%package devel
Summary: Estonian ID card test certificates
Group: System Environment/Libraries

%description devel
Estonian ID card test root, intermediate and OCSP certificates

%prep
%setup -q -n %{name}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
cp -r %{_builddir}/esteidcerts/* %{buildroot}

%files
%defattr(-,root,root,-)
%doc
%exclude %{_usr}/share/esteid/certs/TEST*
%{_usr}/share/esteid/certs

%files devel
%defattr(-,root,root,-)
%doc
%{_usr}/share/esteid/certs/TEST*

%changelog
* Fri Aug 13 2010 RIA <info@ria.ee> 1.0-1
- first build no changes
