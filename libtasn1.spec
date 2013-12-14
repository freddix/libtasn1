Summary:	ASN.1 library used in GNUTLS
Name:		libtasn1
Version:	3.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnu.org/gnu/libtasn1/%{name}-%{version}.tar.gz
# Source0-md5:	21ec021c534b0f30b2834ce233c70f15
Patch0:		%{name}-ar.patch
URL:		http://www.gnu.org/software/gnutls/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library 'libasn1' developed for ASN1 (Abstract Syntax Notation One)
structures management. The main features of this library are:
- on line ASN1 structure management that doesn't require any C code
  file generation.
- off line ASN1 structure management with C code file generation
  containing an array.
- DER (Distinguish Encoding Rules) encoding
- no limits for INTEGER and ENUMERATED values

%package devel
Summary:	Header files etc to develop libtasn1 applications
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files etc to develop libtasn1 applications.

%package apidocs
Summary:	libtasn1 API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libtasn1 API documentation.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4 -I gl/m4 -I lib/glm4
%{__automake}
%{__autoheader}
%{__autoconf}

%configure \
	--disable-silent-rules	\
	--disable-static	\
	--enable-shared		\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS doc/*.html
%attr(755,root,root) %{_bindir}/asn1*
%attr(755,root,root) %ghost %{_libdir}/libtasn1.so.6
%attr(755,root,root) %{_libdir}/libtasn1.so.*.*.*
%{_mandir}/man1/asn1*.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtasn1.so
%{_libdir}/libtasn1.la
%{_includedir}/*.h
%{_pkgconfigdir}/libtasn1.pc
%{_infodir}/*.info*
%{_mandir}/man3/*.3*

%if 0
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}
%endif

