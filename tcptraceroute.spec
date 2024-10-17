%define prel beta7

Summary:	Traceroute implementation using TCP packets
Name:		tcptraceroute
Version:	1.5
Release:	0.%{prel}.6
License:	GPLv2+
Group:		Networking/Other
Url:		https://michael.toren.net/code/tcptraceroute/
Source:		http://michael.toren.net/code/tcptraceroute/%{name}-%{version}%{prel}.tar.gz
BuildRequires:	libnet-devel
BuildRequires:	libpcap-devel

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

%files
%defattr(644,root,root,755)
%doc %{_datadir}/doc/tcptraceroute/*
%attr(755,root,bin) %{_sbindir}/tcptraceroute
%{_mandir}/man1/tcptraceroute.1*

#----------------------------------------------------------------------------

%prep
%setup -qn %{name}-%{version}%{prel}

%build
%configure2_5x \
	--bindir=%{_sbindir}

%make

%install
%makeinstall_std

