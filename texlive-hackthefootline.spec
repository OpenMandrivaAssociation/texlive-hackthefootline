Name:		texlive-hackthefootline
Version:	46494
Release:	1
Summary:	Footline selection and configuration for LaTeX beamer's standard themes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hackthefootline
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hackthefootline.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hackthefootline.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is taking over, defining and redefining different
footlines. Configuration is provided via using key-value
syntax. It depends on the pgfkeys used for providing the
configuration keys. Optional features require the following
LaTeX packages: appendixnumberbeamer, calc, etoolbox, and
numprint.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/hackthefootline
%doc %{_texmfdistdir}/doc/latex/hackthefootline

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
