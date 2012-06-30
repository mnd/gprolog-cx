Summary: GNU Prolog is a free Prolog compiler with constraint solving over Finite Domains
Name: @NAME@
Version: @VERSION@
Release: 1
License: GPL
Group: Development/Languages
Source: ftp://gprolog.univ-paris1.fr/pub/gprolog/@PKG_NAME@.tar.gz
URL: http://www.gprolog.org/
Packager: Daniel Diaz <Daniel.Diaz@univ-paris1.fr>
Vendor: Daniel Diaz (University of Paris 1 & INRIA Rocquencourt)
Prefix: @PREFIX@
Buildroot: @BUILD_ROOT@

%description 

   GNU Prolog is a native Prolog compiler with constraint solving over finite
   domains (FD) developed by Daniel Diaz (http://loco.inria.fr/~diaz).

   GNU Prolog is a very efficient native compiler producing (small) stand-alone
   executables. GNU-Prolog also offers a classical top-level+debugger.

   GNU Prolog conforms to the ISO standard for Prolog but also includes a lot 
   of extensions (global variables, DCG, sockets, OS interface,...).

   GNU Prolog also includes a powerful constraint solver over finite domains 
   with many predefined constraints+heuristics.

   More information can be found at http://www.gnu.org/software/prolog
   or better at http://www.gprolog.org.


%prep
@REAL@ %setup
@LINK@ rm -rf $RPM_BUILD_DIR/@PKG_NAME@
@LINK@ ln -s @ROOT_DIR@ $RPM_BUILD_DIR/@PKG_NAME@

%build
@LINK@ cd $RPM_BUILD_DIR/@PKG_NAME@
cd src
./configure --with-install-dir=$RPM_BUILD_ROOT/@PKG_DIR@ \
            --without-links-dir --without-examples-dir \
            --with-doc-dir=$RPM_BUILD_ROOT/@DOC_DIR@
@REAL@ make

%install
@LINK@ cd $RPM_BUILD_DIR/@PKG_NAME@
rm -rf $RPM_BUILD_ROOT
cd src
make install-strip
mkdir $RPM_BUILD_ROOT/@BIN_DIR@
cd $RPM_BUILD_ROOT/@PKG_DIR@/bin
for i in *; do
	ln -s @SRC_LNK@/$i $RPM_BUILD_ROOT/@BIN_DIR@/$i
done
cd $RPM_BUILD_DIR/@PKG_NAME@
cp README COPYING ChangeLog NEWS $RPM_BUILD_ROOT/@DOC_DIR@

%clean
@REAL@ rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc @DOC_DIR@/*
@BIN_DIR@/*
@PKG_DIR@*

%changelog
* Tue Jul 25 2000 Daniel Diaz <Daniel.Diaz@inria.fr>
- initial specfile
