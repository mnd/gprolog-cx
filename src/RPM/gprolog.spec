Summary: GNU Prolog is a free Prolog compiler with constraint solving over Finite Domains
Name: gprolog
Version: 1.3.2
Release: 1
License: GPL
Group: Development/Languages
Source: ftp://gprolog.univ-paris1.fr/pub/gprolog/gprolog-1.3.2.tar.gz
URL: http://www.gprolog.org/
Packager: Daniel Diaz <Daniel.Diaz@univ-paris1.fr>
Vendor: Daniel Diaz (University of Paris 1 & INRIA Rocquencourt)
Prefix: /usr
Buildroot: /var/tmp/gprolog-build-rpm

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
%setup

%build
cd src
./configure --with-install-dir=$RPM_BUILD_ROOT//usr/lib/gprolog-1.3.2 \
            --without-links-dir --without-examples-dir \
            --with-doc-dir=$RPM_BUILD_ROOT//usr/doc/gprolog-1.3.2
make

%install
rm -rf $RPM_BUILD_ROOT
cd src
make install-strip
mkdir $RPM_BUILD_ROOT//usr/bin
cd $RPM_BUILD_ROOT//usr/lib/gprolog-1.3.2/bin
for i in *; do
	ln -s ../lib/gprolog-1.3.2/bin/$i $RPM_BUILD_ROOT//usr/bin/$i
done
cd $RPM_BUILD_DIR/gprolog-1.3.2
cp README COPYING ChangeLog NEWS $RPM_BUILD_ROOT//usr/doc/gprolog-1.3.2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc /usr/doc/gprolog-1.3.2/*
/usr/bin/*
/usr/lib/gprolog-1.3.2*

%changelog
* Tue Jul 25 2000 Daniel Diaz <Daniel.Diaz@inria.fr>
- initial specfile
