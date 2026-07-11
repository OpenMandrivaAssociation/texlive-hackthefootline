%global tl_name hackthefootline
%global tl_revision 46494

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Footline selection and configuration for LaTeX beamers standard themes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/hackthefootline
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hackthefootline.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hackthefootline.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is taking over, defining and redefining different
footlines. Configuration is provided via using key-value syntax. It
depends on the pgfkeys used for providing the configuration keys.
Optional features require the following LaTeX packages:
appendixnumberbeamer, calc, etoolbox, and numprint.

