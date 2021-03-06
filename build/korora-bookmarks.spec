Name:           korora-bookmarks
Version:        20
Release:        0.1
Summary:        Korora bookmarks
Group:          Applications/Internet
License:        GFDL
URL:            http://kororaa.org/
# I had to strip the embedded icons out of the bookmarks file, because they are not 
# distributable under the GFDL. See https://bugzilla.redhat.com/show_bug.cgi?id=433471
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Provides:       system-bookmarks
Obsoletes:      fedora-bookmarks
Provides:       fedora-bookmarks
Obsoletes:      kororaa-bookmarks
Provides:       kororaa-bookmarks

%description
This package contains the default bookmarks for Korora.

%prep
%setup -q

%build
# We are nihilists, Lebowski.  We believe in nassing.

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/bookmarks
install -p -m 644 default-bookmarks.html $RPM_BUILD_ROOT%{_datadir}/bookmarks

%clean
%{__rm} -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%dir %{_datadir}/bookmarks
%{_datadir}/bookmarks/default-bookmarks.html

%changelog
* Sat Oct 26 2013 Chris Smart <csmart@kororaproject.org> 20.0.1
- Updated build for Korora 20.

* Wed Feb 13 2013 Chris Smart <csmart@kororaproject.org> 18.0.1
- Updated build for Kororaa 18.

* Mon May 21 2012 Chris Smart <chris@kororaa.org> 17.0.1
- Updated build for Kororaa 17.

* Thu Nov 10 2011 Chris Smart <chris@kororaa.org> 16.0.1
- Updated build for Kororaa 16.

* Sun Sep 04 2011 Chris Smart <chris@kororaa.org> 15.0.2
- Add Replaces fedora-bookmarks.

* Sun Jul 10 2011 Chris Smart <chris@kororaa.org> 15.0.1
- Update f15.

* Mon Mar 28 2011 Chris Smart <chris@kororaa.org> 14-1
- Port from fedora-bookmarks.

