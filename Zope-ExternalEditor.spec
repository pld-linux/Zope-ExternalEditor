%include	/usr/lib/rpm/macros.python

%define		zope_subname	ExternalEditor

Summary:	ExternalEditor is a Zope product - is a new way to integrate Zope more seamlessly with client-side tools.
Summary(pl):	ExternalEditor jest dodatkiem do Zope - umo¿liwiaj±cy now± integracje z Zope od strony narzêdzi klienta.
Name:		Zope-%{zope_subname}
Version:	0.7
Release:	1
License:	GNU
Group:		Development/Tools
Source0:	http://zope.org/Members/Caseman/%{zope_subname}/%{version}/zopeedit-%{version}-src.tgz
# Source0-md5:	87fe890a7f7c2506db16142bc4789b38
URL:		http://sourceforge.net/projects/collective
%pyrequires_eq	python-modules
Requires:	Zope
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	product_dir	/usr/lib/zope/Products
%define		src_dir_name	zopeedit-%{version}-src

%description
ExternalEditor is a Zope product - is a new way to integrate Zope more
seamlessly with client-side tools.

%description -l pl
ExternalEditor jest dodatkiem do Zope - umo¿liwiaj±cy now± integracje
z Zope od strony narzêdzi klienta.

%prep
%setup -q -n %{src_dir_name}

%build
mkdir docs
mv -f README.txt CHANGES.txt INSTALL* docs/

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}
install -d $RPM_BUILD_ROOT%{_mandir}/man1
mv -f man/* $RPM_BUILD_ROOT%{_mandir}/man1
rm -rf man/
cp -af * $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

%py_comp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}
%py_ocomp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;
rm -rf $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}/docs

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%preun

%postun
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%files
%defattr(644,root,root,755)
%doc docs/*
%dir %{product_dir}/%{zope_subname}
%{_mandir}/man1/*
%{product_dir}/%{zope_subname}/Plugins
%{product_dir}/%{zope_subname}/setup*
%{product_dir}/%{zope_subname}/*.txt
%attr (755,root,root) %{product_dir}/%{zope_subname}/zopeedit*
