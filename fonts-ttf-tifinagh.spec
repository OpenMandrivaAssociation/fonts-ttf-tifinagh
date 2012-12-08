Summary: Tifinagh TTF font(s)
Name: fonts-ttf-tifinagh
Version: 1.0
Release: %mkrel 12
License: Free use and distribution
Group: System/Fonts/True type
Source0: http://pages.infinit.net/hapax/polices/hapaxber.ttf.bz2
Source1: http://pages.infinit.net/hapax/polices/inventaire-des-oeils.pdf.bz2
URL: http://cooptel.qc.ca/%7Epandries/propo_tifinagh.pdf
BuildArch:	noarch
BuildRequires: fontconfig
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildRequires:	freetype-tools

%description
This package contains fonts for the Tifinagh script,
as encoded in unicode.

%prep
#%setup -c 

rm -rf %{name}-%{version}
mkdir %{name}-%{version}
cd %{name}-%{version}

%build
cd %{name}-%{version}
bzcat %{SOURCE0} > hapaxber.ttf
bzcat %{SOURCE1} > inventaire-des-oeils.pdf

cat << EOF > README.txt
The "Hapax Berbère" font was used as the reference font for
the proposal of inclusion of tifinagh script into Unicode BMP;
its autor, Patrick Andries hapax(at)iquebec.com, kindly released
as freely usable and distributable.

The PDF file inventaire-des-oeils.pdf gives the list of all the glyphs
in the font (there are various glyph variants and ligatures on private
use area too)
EOF

%install
cd %{name}-%{version}
rm -rf %buildroot
install -d %buildroot/%_datadir/fonts/TTF/tifinagh

for i in `find . -name "*.ttf"` ; do
install -m 644 $i %buildroot/%_datadir/fonts/TTF/tifinagh
done

%post
touch %{_datadir}/fonts/TTF

%clean
rm -fr %buildroot

%files
%defattr(0644,root,root,0755)
%doc %{name}-%{version}/README* %{name}-%{version}/*.pdf
%dir %_datadir/fonts/TTF/
%dir %_datadir/fonts/TTF/tifinagh
%_datadir/fonts/TTF/tifinagh/*.ttf





%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.0-10mdv2011.0
+ Revision: 675430
- br fontconfig for fc-query used in new rpm-setup-build

* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.0-9
+ Revision: 675190
- rebuild for new rpm-setup

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0-8
+ Revision: 664339
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-7mdv2011.0
+ Revision: 605205
- rebuild

* Wed Jan 20 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0-6mdv2010.1
+ Revision: 494158
- fc-cache is now called by an rpm filetrigger

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0-5mdv2009.1
+ Revision: 351135
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0-4mdv2009.0
+ Revision: 220956
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.0-3mdv2008.1
+ Revision: 125156
- kill re-definition of %%buildroot on Pixel's request


* Fri Aug 04 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-04 23:12:24 (52896)
- Normalize fonts with new paths

* Fri Aug 04 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-04 21:09:34 (52813)
- import fonts-ttf-tifinagh-1.0-2mdk

* Wed Feb 08 2006 Frederic Crozat <fcrozat@mandriva.com> 1.0-2mdk
- Don't package fontconfig cache file
- Fix prereq
- touch parent directory to workaround rpm changing directory last modification
  time (breaking fontconfig cache consistency detection)

* Tue Aug 10 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 1.0-1mdk
- Initial rpm package

