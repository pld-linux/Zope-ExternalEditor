%include	/usr/lib/rpm/macros.python
%define		zope_subname	ExternalEditor
Summary:	ExternalEditor - a Zope product integrating Zope more seamlessly with client-side tools
Summary(pl):	ExternalEditor - dodatek do Zope lepiej intergruj±cy Zope z narzêdziami od strony klienta
Name:		Zope-%{zope_subname}
Version:	0.7
Release:	5
License:	ZPL 2.0
Group:		Development/Tools
Source0:	http://zope.org/Members/Caseman/%{zope_subname}/%{version}/%{zope_subname}-%{version}.tgz
# Source0-md5:	1dac15db90bb3c320955c114f2053963
URL:		http://sourceforge.net/projects/collective/
BuildRequires:	python >= 2.2
%pyrequires_eq	python-modules
Requires:	Zope
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	product_dir	/usr/lib/zope/Products

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
install -d $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

install -m 644 {*.py,*.gif,*.dtml,README.txt} $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

%py_comp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}
%py_ocomp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

# rm $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}/*.py

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
%{product_dir}/%{zope_subname}
