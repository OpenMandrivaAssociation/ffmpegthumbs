Name:		ffmpegthumbs
Summary:	Video thumbnail generator for KDE4 file managers
Epoch:		3
Version:	4.10.2
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		https://projects.kde.org/projects/kde/kdemultimedia/ffmpegthumbs
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(libavcodec)
BuildRequires:	pkgconfig(libavformat)
BuildRequires:	pkgconfig(libswscale)

%description
FFmpegThumbs is a video thumbnails implementation for KDE4 based on
FFmpegThumbnailer.

This thumbnailer uses FFmpeg to decode frames from the video files,
so supported video formats depend on the configuration flags of ffmpeg.

This thumbnailer was designed to be as fast and lightweight as possible.

%files
%{_kde_libdir}/kde4/ffmpegthumbs.so
%{_kde_services}/ffmpegthumbs.desktop

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.0-1
- New version 4.10.0

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.1-1
- New version 4.9.1

* Tue Aug 14 2012 Andrey Bondrov <abondrov@mandriva.org> 3:4.9.0-1
- New version 4.9.0

* Thu Jul 12 2012 Andrey Bondrov <abondrov@mandriva.org> 3:4.8.97-1
+ Revision: 808955
- imported package ffmpegthumbs

* Tue Jul 10 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.8.97-1
- Follow upstream and move ffmpegthumbs from kdemultimedia4 to own package
