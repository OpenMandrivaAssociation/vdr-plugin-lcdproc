
%define plugin	lcdproc
%define name	vdr-plugin-%plugin
%define oversion 0.0.10-jw7
%define version %(echo %oversion | tr -- - .)
%define rel	2

Summary:	VDR plugin: Output to LCD modules that are supported by LCDproc
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL+
URL:		https://projects.vdr-developer.org/projects/show/plg-lcdproc
Source:		http://projects.vdr-developer.org/attachments/download/86/vdr-%plugin-%oversion.tgz
Patch0:		lcdproc-str-fmt.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
Output VDR status to LCD modules that are supported by the LCDproc
project.

%prep
%setup -q -n %plugin-%oversion
%patch0 -p1

%vdr_plugin_prep
chmod 0644 README*

%vdr_plugin_params_begin %plugin
# LCDproc host (default=localhost)
var=LCD_HOST
param="-h LCD_HOST"
# LCDproc port (default=13666)
var=LCD_PORT
param="-p LCD_PORT"
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


