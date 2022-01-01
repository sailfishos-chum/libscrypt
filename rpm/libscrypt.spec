Name:           libscrypt
Version:        1.21
Release:        1%{?dist}
Summary:        Library that implements the secure password hashing function "scrypt"
License:        BSD
URL:            http://www.lolware.net/libscrypt.html
Source:         %{name}-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make

%description
This is a library that implements the secure password hashing function "scrypt".

Custom:
  Repo: https://github.com/technion/libscrypt

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

Custom:
  Repo: https://github.com/technion/libscrypt

%prep
%setup -q -n %{name}-%{version}/libscrypt

%build
export CFLAGS="$CFLAGS -fPIC"
make %{?_smp_mflags}

%install
make install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir}

find $RPM_BUILD_ROOT -name '*.*a' -exec rm -f {} ';'

%post -n libscrypt -p /sbin/ldconfig

%postun -n libscrypt -p /sbin/ldconfig

%files
%license LICENSE
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%doc README.md


%changelog
* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 14 2020 Denis Fateyev <denis@fateyev.com> - 1.21-14
- Temporarily disable failing test suite

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 28 2019 Denis Fateyev <denis@fateyev.com> - 1.21-10
- Spec cleanup from deprecated items

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Denis Fateyev <denis@fateyev.com> - 1.21-1
- Update to 1.21 release
- Spec modernize and cleanup

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Dec 1 2014 Joshua Small <technion@lolware.net> 1.20-1
- Bugfixes involving large N, failure return values

* Tue May 6 2014 Joshua Small <technion@lolware.net> 1.19-1
- Code improvements, courtesy of Coverity

* Tue Mar 11 2014 Joshua Small <technion@lolware.net> 1.18-1
- Documentation corrections 

* Sun Feb 02 2014 Joshua Small <technion@lolware.net> 1.15-1
- More portable b64 libraries implemented.

* Tue Sep 24 2013 Dan Horák <dan[at]danny.cz> - 1.14-2
- big endian fix

* Thu Sep 12 2013 Joshua Small <technion@lolware.net> - 1.14-1
- Fixed length bug reported by shawjef3

* Fri Aug 02 2013 Joshua Small <technion@lolware.net> - 1.13-1
- Initial version of the library
