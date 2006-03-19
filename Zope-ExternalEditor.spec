%define		zope_subname	ExternalEditor
Summary:	A Zope product integrating Zope more seamlessly with client-side tools
Summary(pl):	Dodatek do Zope lepiej intergruj±cy Zope z narzêdziami od strony klienta
Name:		Zope-%{zope_subname}
Version:	0.9.1
Release:	1
License:	ZPL 2.0
Group:		Development/Tools
Source0:	http://plope.com/software/ExternalEditor/ExternalEditor-%{version}-src.tgz
# Source0-md5:	6befe8f5af29e8b4e27d9aba0299b57c
URL:		http://plope.com/software/ExternalEditor/
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.268
%pyrequires_eq	python-modules
Requires(post,postun):	/usr/sbin/installzopeproduct
Requires:	Zope
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExternalEditor is a Zope product, a new way to integrate Zope more
seamlessly with client-side tools. This package is supposed to be
installed on Zope server, there is a zopeedit tool for clients.

%description -l pl
ExternalEditor jest dodatkiem do Zope, umo¿liwiaj±cym w nowy, bardziej
przezroczysty sposób integrowaæ Zope z narzêdziami od strony klienta.
Ten pakiet powinien byæ zainstalowany na serwerze Zope. Od strony
klienta dostêp do niego zapewnia pakiet zopeedit.

%prep
%setup -q -n %{zope_subname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
# install -d $RPM_BUILD_ROOT%{_mandir}/man1

cp -af {Plugins,*.py,*.gif,*.dtml,version.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}
# cp -af man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# rm $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
%service -q zope restart

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	%service -q zope restart
fi

%files
%defattr(644,root,root,755)
%doc CHANGES.txt INSTALL-UNIX.txt README.txt
# %%{_mandir}/man1/*
%{_datadir}/%{name}
