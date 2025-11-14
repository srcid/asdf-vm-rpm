Name:           asdf
Version:        0.18.0
Release:        1%{?dist}
Summary:        A tool to manage multiple runtimes
License:        MIT
URL:            https://github.com/asdf-vm/asdf
Source0:        %{url}/releases/download/v%{version}/%{name}-v%{version}-linux-amd64.tar.gz 
ExclusiveArch:  x86_64
Requires:       git bash

%global debug_package %{nil}
%global _missing_build_ids_terminate_build 0

%description
asdf is a CLI tool that can manage multiple runtime versions of languages
and tools such as Ruby, Node.js, Elixir, Python, etc. It is extendable via
plugins and integrates well into shells like Bash, Zsh, and Fish.

%prep
%setup -c -T
tar zxf %{SOURCE0}

%build
# Nothing to build - it's pre-compiled

%install
mkdir -p %{buildroot}/usr/bin/
cp -a asdf %{buildroot}/usr/bin/

%files
/usr/bin/asdf
# update from testing workflow
