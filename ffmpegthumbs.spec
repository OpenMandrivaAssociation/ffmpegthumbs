%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Video thumbnail generator for KDE4 file managers
Name:		ffmpegthumbs
Version:	24.02.0
Release:	3
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		https://projects.kde.org/projects/kde/kdemultimedia/ffmpegthumbs
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
#Patch0:		ffmpegthumbs-21.12.1-ffmpeg-5.0.patch
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(libavcodec)
BuildRequires:	pkgconfig(libavformat)
BuildRequires:	pkgconfig(libswscale)
BuildRequires:	pkgconfig(taglib)

%description
FFmpegThumbs is a video thumbnails implementation for KDE4 based on
FFmpegThumbnailer.

This thumbnailer uses FFmpeg to decode frames from the video files,
so supported video formats depend on the configuration flags of ffmpeg.

This thumbnailer was designed to be as fast and lightweight as possible.

%files 
#-f %{name}.lang
%{_qt5_plugindir}/kf5/thumbcreator/ffmpegthumbs.so
%{_datadir}/config.kcfg/ffmpegthumbnailersettings5.kcfg
%{_datadir}/metainfo/org.kde.ffmpegthumbs.metainfo.xml
%{_datadir}/qlogging-categories5/ffmpegthumbs.categories

#------------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
#find_lang %{name}
