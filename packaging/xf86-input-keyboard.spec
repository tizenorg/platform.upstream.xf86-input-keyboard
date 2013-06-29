Name:           xf86-input-keyboard
Version:        1.6.1
Release:        0
License:        GPL-2.0+
Summary:        Keyboard input driver for the Xorg X server
Url:            http://xorg.freedesktop.org/
Group:          System/X11/Servers/XF86_4
Source0:        http://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.bz2
Source1001: 	xf86-input-keyboard.manifest
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(inputproto)
BuildRequires:  pkgconfig(resourceproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xorg-server) >= 1.4
BuildRequires:  pkgconfig(xproto)
Requires:       udev
Requires:       xkeyboard-config >= 1.5

%description
kbd is an Xorg input driver for keyboards. The driver supports the
standard OS-provided keyboard interface, but these are currently only
available to this driver module for Linux, BSD, and Solaris.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%configure
make %{?_smp_mflags}

%install
%make_install


%remove_docs

%post
# re-plug the input devices
udevadm trigger --subsystem-match=input --action=change
exit 0

%postun
# re-plug the input devices
udevadm trigger --subsystem-match=input --action=change
exit 0

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%doc COPYING
%dir %{_libdir}/xorg/modules/input
%{_libdir}/xorg/modules/input/kbd_drv.so

%changelog
