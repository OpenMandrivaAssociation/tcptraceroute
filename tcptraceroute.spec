%define prel	beta7

Name:           tcptraceroute
Summary:        Tcptraceroute is a traceroute implementation using TCP packets 
Version:	1.5
Release:	%mkrel 0.%{prel}.2
Source:		http://michael.toren.net/code/tcptraceroute/%{name}-%{version}%{prel}.tar.gz
URL:		http://michael.toren.net/code/tcptraceroute/
Group:		Networking/Other
License:	GPL
BuildRequires:	libpcap-devel 		>= 0.9.5
%ifarch x86_64
BuildRequires:	lib64net1.1.2-devel
%endif
%ifarch i586
BuildRequires:	libnet1.1.2-devel
%endif

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

			      

