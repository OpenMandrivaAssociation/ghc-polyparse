%global debug_package %{nil}
%define module polyparse

Summary:	A variety of alternative parser combinator libraries for Haskell
Name:		ghc-%{module}
Version:	1.8
Release:	3
License:	LGPLv2.1+
Group:		Development/Other
Url:		http://hackage.haskell.org/package/%{module}
Source0:	http://hackage.haskell.org/packages/archive/%{module}/%{version}/%{module}-%{version}.tar.gz
Source10:	%{name}.rpmlintrc
BuildRequires:	ghc-devel
BuildRequires:	haddock
BuildRequires:	haskell-macros
BuildRequires:	haskell(text)
Requires(post,preun):	ghc
Requires(pre):	haskell(text)
Obsoletes:	haskell-%{module} < 1.8-2

%description
A variety of alternative parser combinator libraries, including the original
HuttonMeijer set. The Poly sets have features like good error reporting,
arbitrary token type, running state, lazy parsing, and so on. Finally,
Text.Parse is a proposed replacement for the standard Read class, for better
deserialisation of Haskell values from Strings.

%files
%{_docdir}/%{module}-%{version}
%{_libdir}/%{module}-%{version}
%{_cabal_rpm_deps_dir}
%{_cabal_haddoc_files}

#----------------------------------------------------------------------------

%prep
%setup -q -n %{module}-%{version}

%build
%_cabal_build

%install
%_cabal_install
%_cabal_rpm_gen_deps
%_cabal_scriptlets

%check
%_cabal_check

