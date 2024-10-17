Name:		texlive-clrstrip
Version:	60363
Release:	2
Summary:	Place contents into a full width colour strip
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/clrstrip
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clrstrip.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clrstrip.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clrstrip.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This lightweight package provides the colorstrip environment,
that places its contents into a full page width colour strip.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/clrstrip
%{_texmfdistdir}/tex/latex/clrstrip
%doc %{_texmfdistdir}/doc/latex/clrstrip

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
