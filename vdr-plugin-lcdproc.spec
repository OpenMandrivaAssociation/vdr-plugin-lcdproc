
%define plugin	lcdproc
%define name	vdr-plugin-%plugin
%define version	0.0.10.jw7
%define rel	1

Summary:	VDR plugin: Output to LCD modules that are supported by LCDproc
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://projects.vdr-developer.org/projects/show/plg-lcdproc
Source:		http://projects.vdr-developer.org/attachments/download/86/vdr-%plugin-0.0.10-jw7.tgz
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi
%define Werror_cflags %nil

%description


%prep
%setup -q -n %plugin-0.0.10-jw7

%vdr_plugin_prep
chmod 0644 README*

%vdr_plugin_params_begin %plugin
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY


