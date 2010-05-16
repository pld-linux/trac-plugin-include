%define		trac_ver	0.11
%define		plugin		include
Summary:	Include external resources in a wiki page
Name:		trac-plugin-%{plugin}
Version:	2.1
Release:	0.1
License:	BSD
Group:		Applications/WWW
# Source0Download: http://trac-hacks.org/changeset/latest/includemacro?old_path=/&filename=includemacro&format=zip
Source0:	%{plugin}macro.zip
# Source0-md5:	9f706e733d205d4467ce6534772cb505
URL:		http://trac-hacks.org/wiki/IncludeMacro
BuildRequires:	python-devel
BuildRequires:	unzip
Requires:	trac >= %{trac_ver}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This macro lets you include various things.

Currently supported sources:
- HTTP - http: and https:
- FTP - ftp:
- Wiki pages - wiki:
- Repository files - source:

The default source is wiki if only a source path is given.

An optional second argument sets the output MIME type, though in most
cases the default will be correct.

%prep
%setup -q -n %{plugin}macro

%build
cd %{trac_ver}
%{__python} setup.py build
%{__python} setup.py egg_info

%install
rm -rf $RPM_BUILD_ROOT
cd %{trac_ver}
%{__python} setup.py install \
	--single-version-externally-managed \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "$1" = "1" ]; then
	%banner -e %{name} <<-'EOF'
	To enable the %{plugin} plugin, add to conf/trac.ini:

	[components]
	%{plugin}macro.* = enabled
EOF
fi

%files
%defattr(644,root,root,755)
%doc %{trac_ver}/README
%{py_sitescriptdir}/%{plugin}macro
%{py_sitescriptdir}/*-*.egg-info
