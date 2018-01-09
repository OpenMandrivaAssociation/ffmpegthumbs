%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Video thumbnail generator for KDE4 file managers
Name:		ffmpegthumbs
Epoch:		3
Version:	17.12.1
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		https://projects.kde.org/projects/kde/kdemultimedia/ffmpegthumbs
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	pkgconfig(Qt5Gui)
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
%{_qt5_plugindir}/ffmpegthumbs.so
%{_datadir}/kservices5/ffmpegthumbs.desktop

#------------------------------------------------------------------------------

%prep
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
