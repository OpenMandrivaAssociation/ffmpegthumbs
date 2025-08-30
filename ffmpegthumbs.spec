#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Video thumbnail generator for KDE4 file managers
Name:		ffmpegthumbs
Version:	25.08.0
Release:	%{?git:0.%{git}.}2
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		https://projects.kde.org/projects/kde/kdemultimedia/ffmpegthumbs
%if 0%{?git:1}
Source0:	https://invent.kde.org/multimedia/ffmpegthumbs/-/archive/%{gitbranch}/ffmpegthumbs-%{gitbranchd}.tar.bz2#/ffmpegthumbs-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/ffmpegthumbs-%{version}.tar.xz
%endif
#Patch0:		ffmpegthumbs-21.12.1-ffmpeg-6.0.patch
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(libavcodec)
BuildRequires:	pkgconfig(libavformat)
BuildRequires:	pkgconfig(libswscale)
BuildRequires:	pkgconfig(taglib)

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildOption:	-DQT_MAJOR_VERSION=6

%rename plasma6-ffmpegthumbs

%patchlist
ffmpegthumbs-ffmpeg-8.0.patch

%description
FFmpegThumbs is a video thumbnails implementation for KDE based on
FFmpegThumbnailer.

This thumbnailer uses FFmpeg to decode frames from the video files,
so supported video formats depend on the configuration flags of ffmpeg.

This thumbnailer was designed to be as fast and lightweight as possible.

%files 
#-f %{name}.lang
%{_qtdir}/plugins/kf6/thumbcreator/ffmpegthumbs.so
%{_datadir}/metainfo/org.kde.ffmpegthumbs.metainfo.xml
%{_datadir}/qlogging-categories6/ffmpegthumbs.categories
%{_datadir}/config.kcfg/ffmpegthumbnailersettings5.kcfg
