Summary: Tifinagh TTF font(s)
Name: fonts-ttf-tifinagh
Version: 1.0
Release: %mkrel 3
License: Free use and distribution
Group: System/Fonts/True type
Source0: http://pages.infinit.net/hapax/polices/hapaxber.ttf.bz2
Source1: http://pages.infinit.net/hapax/polices/inventaire-des-oeils.pdf.bz2
URL: http://cooptel.qc.ca/%7Epandries/propo_tifinagh.pdf
BuildArch:	noarch
BuildRequires:	freetype-tools
Requires(post): fontconfig
Requires(postun): fontconfig

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
[ -x %_bindir/fc-cache ] && %{_bindir}/fc-cache 

%postun
# 0 means a real uninstall
if [ "$1" = "0" ]; then
  [ -x %_bindir/fc-cache ] && %{_bindir}/fc-cache 
fi

%clean
rm -fr %buildroot

%files
%defattr(0644,root,root,0755)
%doc %{name}-%{version}/README* %{name}-%{version}/*.pdf
%dir %_datadir/fonts/TTF/
%dir %_datadir/fonts/TTF/tifinagh
%_datadir/fonts/TTF/tifinagh/*.ttf



