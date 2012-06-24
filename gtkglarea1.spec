Summary:	GtkGLArea OpenGL widget for GTK+
Summary(pl):	GtkGLArea - kontrolka Gtk+ do prezentacji obiekt�w OpenGL
Summary(pt_BR):	Um widget OpenGL para a biblioteca GUI GTK+
Summary(ru):	GtkGLArea - ��� OpenGL ������ ��� GTK+
Summary(uk):	GtkGLArea - �� OpenGL צ���� ��� GTK+
Summary(wa):	GtkGLArea est on ahesse pol toolkit grafike GTK+
Name:		gtkglarea
Version:	1.2.3
Release:	7
License:	LGPL
Group:		X11/Libraries
Source0:	http://www.student.oulu.fi/~jlof/gtkglarea/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-m4_fix.patch
Requires:	OpenGL
BuildRequires:	OpenGL-devel
BuildRequires:	gtk+-devel => 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libgtkglarea5

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix		/usr/X11R6
%define		_datadir	/usr/share

%description
Just as GTK+ is build on top of GDK, GtkGLArea is built on top of
gdkgl which is basically wrapper around GLX functions. The widget
itself is derived from GtkDrawinigArea widget and adds only few extra
functions.

%description -l pl
Podobnie jak GTK+ jest zbudowane na GDK, tak i GtkGLArea powsta�o na
bazie gdkgl, kt�ry jest wrapperem funkcji GLX. Sam widget pochodzi od
GtkDrawingArea i posiada jedynie kilka dodatkowych funkcji.

%description -l pt_BR
GtkGLArea � um OpenGL widget para GTK+ (the Gimp ToolKit), uma
biblioteca GUI. GtkGLArea � constru�da em cima do gdkgl. Gdkgl �
basicamente um wrapper de fun��es GLX. GtkGLArea widget � derivado do
widget GtkDrawingArea e adiciona somente algumas fun��es.

%description -l ru
��� �� ��� GTK+ �������� ������ GDK, GtkGLArea ��������� ������ gdkgl,
������� �� ���� ���� �������� ������ ������� GLX. ��� ������ �����
����� �� ������ GtkDrawinigArea � ��������� ������ ��� ����� �������.

%description -l uk
��� ����, �� GTK+ ���դ���� ������ GDK, GtkGLArea ���������� ������
gdkgl, ��� �� ��Ԧ � ��������� ������� ����æ� GLX. ��� צ���� ����
������ �� צ���� GtkDrawinigArea �� ����� ���� ��� ��צ ����æ�.

%package devel
Summary:	GtkGLArea OpenGL widget for GTK+ - development libs and headers
Summary(pl):	Pliki nag��wkowe GtkGLArea
Summary(pt_BR):	Bibliotecas e arquivos de inclus�o para desenvolvimento de aplica��es que usem a biblioteca GtkGLArea
Summary(ru):	GtkGLArea - ����� ��� ���������� ��������
Summary(uk):	GtkGLArea - ����� ��� �������� �������
Summary(wa):	GtkGLArea est on ahesse po GTK+ - fitch�s *.h �t statik�s l�vreyes
Group:		X11/Libraries
Requires:	%{name} = %{version}
Requires:	OpenGL-devel
Requires:	gtk+-devel => 1.2.0
Obsoletes:	libgtkglarea5-devel

%description devel
Header files for development using the GtkGLArea widget.

%description devel -l pl
Pliki nag��wkowe do budowania program�w u�ywaj�cych widgetu GtkGLArea.

%description devel -l pt_BR
Bibliotecas e arquivos de inclus�o para desenvolvimento de aplica��es
que usem a biblioteca GtkGLArea.

%description devel -l ru
����� ��� ���������� �������� � �������������� GtkGLArea.

%description devel -l uk
����� ��� �������� ������� � ������������� GtkGLArea.

%description devel -l wa
Ci paket chal a dvins les fitch�s *.h ey�t les statik�s l�vreyes k' i
gn a mez�jhe po f� des porogrames avou les foncsions di GtkGLArea.

%package static
Summary:	GtkGLArea static libraries
Summary(pl):	Statyczne biblioteki GtkGLArea
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento de aplica��es que usem a biblioteca GtkGLArea
Group:		X11/Libraries
Requires:	%{name}-devel = %{version}

%description static
GtkGLArea (OpenGL for GTK+) static libraries.

%description static -l pl
Statyczne biblioteki GtkGLArea (OpenGL dla GTK+).

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento de aplica��es que usem a
biblioteca GtkGLArea.

%prep
%setup -q
%patch0

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

gzip -9nf AUTHORS ChangeLog NEWS README docs/HOWTO.txt docs/gdkgl.txt \
	docs/gtkglarea.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *gz docs/*.gz
%{_includedir}/gtkgl
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
