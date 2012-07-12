Name:		ffmpegthumbs
Summary:	Video thumbnail generator for KDE4 file managers
Epoch:		3
Version:	4.8.97
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		https://projects.kde.org/projects/kde/kdemultimedia/ffmpegthumbs
Source:		ftp://ftp.kde.org/pub/kde/unstable/%{version}/src/%{name}-%{version}.tar.xz
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

