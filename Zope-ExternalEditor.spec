%include	/usr/lib/rpm/macros.python
%define		zope_subname	ExternalEditor
Summary:	ExternalEditor - a Zope product integrating Zope more seamlessly with client-side tools
Summary(pl):	ExternalEditor - dodatek do Zope lepiej intergruj±cy Zope z narzêdziami od strony klienta
Name:		Zope-%{zope_subname}
Version:	0.7
Release:	2
License:	ZPL 2.0
Group:		Development/Tools
Source0:	http://zope.org/Members/Caseman/%{zope_subname}/%{version}/zopeedit-%{version}-src.tgz
# Source0-md5:	87fe890a7f7c2506db16142bc4789b38
URL:		http://sourceforge.net/projects/collective/
BuildRequires:	python >= 2.2
%pyrequires_eq	python-modules
Requires:	Zope
Requires:	python-tkinter
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	product_dir	/usr/lib/zope/Products
%define		src_dir_name	zopeedit-%{version}-src

%description
ExternalEditor is a Zope product, a new way to integrate Zope more
seamlessly with client-side tools.

%description -l pl
ExternalEditor jest dodatkiem do Zope, umo¿liwiaj±cym w nowy, bardziej
przezroczysty sposób integrowaæ Zope z narzêdziami od strony klienta.

%prep
%setup -q -n %{src_dir_name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{product_dir}/%{zope_subname},%{_mandir}/man1}

install man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -af {Plugins,*.py} $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

%py_comp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}
%py_ocomp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%files
%defattr(644,root,root,755)
%doc CHANGES.txt INSTALL-UNIX.txt LICENSE.txt README.txt
%dir %{product_dir}/%{zope_subname}
%{product_dir}/%{zope_subname}/Plugins
%{product_dir}/%{zope_subname}/setup*
%attr(755,root,root) %{product_dir}/%{zope_subname}/zopeedit*
%{_mandir}/man1/*
