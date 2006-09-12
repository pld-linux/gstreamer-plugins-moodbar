%define         gst_major_ver   0.10
%define         gstlibdir       %{_libdir}/gstreamer-%{gst_major_ver}

Summary:	Moodbar plugin for gstreamer
Summary(pl):	Wtyczka do gstreamera generuj±ca Moodbar
Name:		gstreamer-plugins-moodbar
Version:	0.1.1
Release:	0.5
License:	GPL v2
Group:		Libraries
Source0:	http://pwsp.net/~qbob/moodbar-%{version}.tar.gz
# Source0-md5:	82d5114a71f1bb28a0845624914cbc4b
URL:		http://amarok.kde.org/wiki/Moodbar
BuildRequires:	gstreamer-devel >= %{gst_major_ver}
BuildRequires:	rpmbuild(macros) >= 1.194
Requires:	gstreamer-plugins-base >= %{gst_major_ver}
Requires:	gstreamer-plugins-good >= %{gst_major_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Moodbar is an algorithm for creating a colorful visual
representation of the contents of an audio file, giving an idea of its
"mood" (this is a rather fanciful term for the simple analysis it
actually does). The Moodbar was invented by Gavin Wood and Simon
O'Keefe for inclusion in the Amarok music player.

This package contains a GStreamer plugin with elements that are used
in the moodbar analysis, and an application that actually does the
analysis.

%description -l pl
Moodbar to algorytm tworzenia kolorowej reprezentacji zawarto¶ci
plików audio mówi±cej o nastroju danego utworu (to jest raczej
dziwaczne okre¶lenie prostej analizy któr± dokonuje). Moodbar zosta³
wymy¶lony przez Gavina Wooda i Simona O'Keefee'a do zastosowania dla
odtwarzacza Amarok.

Ten pakiet zawiera wtyczkê dla systemu GStreamer oraz aplikacjê, która
dokonuje tej analizy.

%package devel
Summary:	Header files for Moodbar library
Summary(pl):	Pliki nag³ówkowe biblioteki Moodbar
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Moodbar library.

%description devel -l pl
Pliki nag³ówkowe biblioteki Moodbar.

%package static
Summary:	Static Moodbar library
Summary(pl):	Statyczna biblioteka Moodbar
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Moodbar library.

%description static -l pl
Statyczna biblioteka Moodbar.

%prep
%setup -q -n moodbar-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%banner %{name} -e << EOF
 *******************************************************
 *                                                     *
 *  NOTE:                                              *
 *  You must install suitable gstreamer-* packages     *
 *  to work with different audio file formats.         *
 *                                                     *
 *******************************************************

EOF

%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/moodbar
%attr(755,root,root) %{gstlibdir}/libmoodbar.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libmoodbar.so
%{gstlibdir}/libmoodbar.la

%files static
%defattr(644,root,root,755)
%{gstlibdir}/libmoodbar.a
