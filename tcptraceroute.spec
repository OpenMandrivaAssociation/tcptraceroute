%define prel	beta7

Name:           tcptraceroute
Summary:        Traceroute implementation using TCP packets 
Version:	1.5
Release:	%mkrel 0.%{prel}.5
Source:		http://michael.toren.net/code/tcptraceroute/%{name}-%{version}%{prel}.tar.gz
URL:		http://michael.toren.net/code/tcptraceroute/
Group:		Networking/Other
License:	GPL
BuildRequires:	libpcap-devel >= 0.9.5
BuildRequires:	net-devel >= 1.1.3
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The more traditional traceroute(8) sends out either UDP or ICMP ECHO
packets with a TTL of one, and increments the TTL until the destination
has been reached. By printing the gateways that generate ICMP time
exceeded messages along the way, it is able to determine the path packets
are taking to reach the destination. 

The problem is that with the widespread use of firewalls on the modern
Internet, many of the packets that traceroute(8) sends out end up being
filtered, making it impossible to completely trace the path to the
destination. However, in many cases, these firewalls will permit inbound
TCP packets to specific ports that hosts sitting behind the firewall are
listening for connections on. By sending out TCP SYN packets instead of
UDP or ICMP ECHO packets, tcptraceroute is able to bypass the most common
firewall filters. 

%prep 

%setup -qn %{name}-%{version}%{prel}

%build

%configure2_5x \
    --bindir=%{_sbindir}

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files 
%defattr(644,root,root,755) 
%doc %{_datadir}/doc/tcptraceroute/*
%attr(755,root,bin) %{_sbindir}/tcptraceroute
%{_mandir}/man1/tcptraceroute.1*

			      



%changelog
* Sun Apr 03 2011 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 1.5-0.beta7.5mdv2011.0
+ Revision: 650091
- Rebuild

* Thu Jun 04 2009 Oden Eriksson <oeriksson@mandriva.com> 1.5-0.beta7.4mdv2010.0
+ Revision: 382702
- rebuilt against libnet 1.1.3

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 1.5-0.beta7.3mdv2009.1
+ Revision: 298418
- rebuilt against libpcap-1.0.0

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 1.5-0.beta7.2mdv2008.1
+ Revision: 170575
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Sep 04 2007 Oden Eriksson <oeriksson@mandriva.com> 1.5-0.beta7.2mdv2008.0
+ Revision: 79143
- rebuild


* Wed Jan 17 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.5-0.beta7.1mdv2007.0
+ Revision: 109797
- Import tcptraceroute

