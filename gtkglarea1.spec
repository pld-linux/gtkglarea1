Summary:	GtkGLArea OpenGL widget for GTK+
Summary(pl):	GtkGLArea - kontrolka Gtk+ do prezentacji obiektów OpenGL
Summary(pt_BR):	Um widget OpenGL para a biblioteca GUI GTK+
Summary(ru):	GtkGLArea - ÜÔÏ OpenGL ×ÉÄÖÅÔ ÄÌÑ GTK+
Summary(uk):	GtkGLArea - ÃÅ OpenGL ×¦ÄÖÅÔ ÄÌÑ GTK+
Summary(wa):	GtkGLArea est on ahesse pol toolkit grafike GTK+
Name:		gtkglarea1
%define		tar_name	gtkglarea
Version:	1.2.3
Release:	7
License:	LGPL
Group:		X11/Libraries
Source0:	http://gliv.tuxfamily.org/%{tar_name}-%{version}.tar.gz
# Source0-md5:	31061342e2da718dad549b01e795bb7a
Patch0:		%{name}-m4_fix.patch
URL:		http://www.student.oulu.fi/~jlof/gtkglarea/
BuildRequires:	OpenGL-devel
BuildRequires:	gtk+-devel => 1.2.0
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libgtkglarea5
Obsoletes:	gtkglarea < 1.99
# not added yet because of rpm and poldek problems
#Provides:	gtkglarea = %{version}

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_datadir	/usr/share

%description
Just as GTK+ is build on top of GDK, GtkGLArea is built on top of
gdkgl which is basically wrapper around GLX functions. The widget
itself is derived from GtkDrawinigArea widget and adds only few extra
functions.

%description -l pl
Podobnie jak GTK+ jest zbudowane na GDK, tak i GtkGLArea powsta³o na
bazie gdkgl, który jest wrapperem funkcji GLX. Sam widget pochodzi od
GtkDrawingArea i posiada jedynie kilka dodatkowych funkcji.

%description -l pt_BR
GtkGLArea é um OpenGL widget para GTK+ (the Gimp ToolKit), uma
biblioteca GUI. GtkGLArea é construída em cima do gdkgl. Gdkgl é
basicamente um wrapper de funções GLX. GtkGLArea widget é derivado do
widget GtkDrawingArea e adiciona somente algumas funções.

%description -l ru
ôÁË ÖÅ ËÁË GTK+ ÓÔÒÏÉÔÓÑ ÐÏ×ÅÒÈ GDK, GtkGLArea ÐÏÓÔÒÏÅÎÁ ÐÏ×ÅÒÈ gdkgl,
ËÏÔÏÒÁÑ ÐÏ ÓÕÔÉ ÅÓÔØ ÏÂÅÒÔËÏÊ ×ÏËÒÕÇ ÆÕÎËÃÉÊ GLX. óÁÍ ×ÉÄÖÅÔ ÏÞÅÎØ
ÐÏÈÏÖ ÎÁ ×ÉÄÖÅÔ GtkDrawinigArea É ÄÏÂÁ×ÌÑÅÔ ÔÏÌØËÏ ÔÒÉ ÎÏ×ÙÅ ÆÕÎËÃÉÉ.

%description -l uk
ôÁË ÓÁÍÏ, ÑË GTK+ ÂÕÄÕ¤ÔØÓÑ ÐÏ×ÅÒÈ GDK, GtkGLArea ÐÏÂÕÄÏ×ÁÎÁ ÐÏ×ÅÒÈ
gdkgl, ÑËÁ ÐÏ ÓÕÔ¦ ¤ ÏÂÇÏÒÔËÏÀ ÎÁ×ËÒÕÇ ÆÕÎËÃ¦Ê GLX. óÁÍ ×¦ÄÖÅÔ ÄÕÖÅ
ÓÈÏÖÉÊ ÎÁ ×¦ÄÖÅÔ GtkDrawinigArea ÔÁ ÄÏÄÁ¤ ÌÉÛÅ ÔÒÉ ÎÏ×¦ ÆÕÎËÃ¦§.

%package devel
Summary:	GtkGLArea OpenGL widget for GTK+ - development libs and headers
Summary(pl):	Pliki nag³ówkowe GtkGLArea
Summary(pt_BR):	Bibliotecas e arquivos de inclusão para desenvolvimento de aplicações que usem a biblioteca GtkGLArea
Summary(ru):	GtkGLArea - ÆÁÊÌÙ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ
Summary(uk):	GtkGLArea - ÆÁÊÌÉ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ
Summary(wa):	GtkGLArea est on ahesse po GTK+ - fitchîs *.h èt statikès lîvreyes
Group:		X11/Libraries
Requires:	%{name} = %{version}
Requires:	OpenGL-devel
Requires:	gtk+-devel => 1.2.0
Obsoletes:	gtkglarea-devel < 1.99
Obsoletes:	libgtkglarea5-devel
#Provides:	gtkglarea-devel = %{version}

%description devel
Header files for development using the GtkGLArea widget.

%description devel -l pl
Pliki nag³ówkowe do budowania programów u¿ywaj±cych widgetu GtkGLArea.

%description devel -l pt_BR
Bibliotecas e arquivos de inclusão para desenvolvimento de aplicações
que usem a biblioteca GtkGLArea.

%description devel -l ru
æÁÊÌÙ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ Ó ÉÓÐÏÌØÚÏ×ÁÎÉÅÍ GtkGLArea.

%description devel -l uk
æÁÊÌÉ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ Ú ×ÉËÏÒÉÓÔÁÎÎÑÍ GtkGLArea.

%description devel -l wa
Ci paket chal a dvins les fitchîs *.h eyèt les statikès lîvreyes k' i
gn a mezåjhe po fé des porogrames avou les foncsions di GtkGLArea.

%package static
Summary:	GtkGLArea static libraries
Summary(pl):	Statyczne biblioteki GtkGLArea
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento de aplicações que usem a biblioteca GtkGLArea
Group:		X11/Libraries
Requires:	%{name}-devel = %{version}
Obsoletes:	gtkglarea-static < 1.99
#Provides:	gtkglarea-static = %{version}

%description static
GtkGLArea (OpenGL for GTK+) static libraries.

%description static -l pl
Statyczne biblioteki GtkGLArea (OpenGL dla GTK+).

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento de aplicações que usem a
biblioteca GtkGLArea.

%prep
%setup -q -n gtkglarea-%{version}
%patch0

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog docs/HOWTO.txt docs/gdkgl.txt docs/gtkglarea.txt
%{_includedir}/gtkgl
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
