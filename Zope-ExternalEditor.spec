%include	/usr/lib/rpm/macros.python
%define		zope_subname	ExternalEditor
Summary:	A Zope product integrating Zope more seamlessly with client-side tools
Summary(pl):	Dodatek do Zope lepiej intergruj±cy Zope z narzêdziami od strony klienta
Name:		Zope-%{zope_subname}
Version:	0.7.2
Release:	1
License:	ZPL 2.0
Group:		Development/Tools
Source0:	http://zope.org/Members/Caseman/%{zope_subname}/%{version}/%{zope_subname}-%{version}-src.tgz
# Source0-md5:	4f1b1540b8afe1088c312a0d543095d5
URL:		http://sourceforge.net/projects/collective/
BuildRequires:	python >= 2.2
%pyrequires_eq	python-modules
Requires:	Zope
Requires(post,postun):  /usr/sbin/installzopeproduct
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExternalEditor is a Zope product, a new way to integrate Zope more seamlessly
with client-side tools. 
This package is supposed to be installed on Zope server, there is a zopeedit
tool for clients.

%description -l pl
ExternalEditor jest dodatkiem do Zope, umo¿liwiaj±cym w nowy, bardziej
przezroczysty sposób integrowaæ Zope z narzêdziami od strony klienta.
Ten pakiet powinien byæ zainstalowany na serwerze Zope. Od strony klienta
dostêp do niego zapewnia pakiet zopeedit.

%prep
%setup -q -n %{zope_subname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d $RPM_BUILD_ROOT%{_mandir}/man1

cp -af {Plugins,*.py,*.gif,*.dtml,version.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -af man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# rm $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname} 
	if [ -f /var/lock/subsys/zope ]; then
		/etc/rc.d/init.d/zope restart >&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc CHANGES.txt INSTALL-UNIX.txt README.txt
%{_mandir}/man1/*
%{_datadir}/%{name}
