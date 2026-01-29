---
                {
  "source": "web",
  "label": "docker-packet-filtering-firewalls",
  "url": "https://docs.docker.com/engine/network/packet-filtering-firewalls/",
  "description": "iptables/nftables integration, DOCKER-USER chain; supports netfilter overhead and connectivity issues",
  "license": "Docker docs (see site for license)",
  "collected_at": "2025-12-15T17:15:33.703138+00:00"
}
                ---
                # Docker packet filtering and firewalls

                Packet filtering and firewalls | Docker Docs
{"@context":"https://schema.org","@type":"WebPage","headline":"\"Packet filtering and firewalls\"","description":"\"How Docker works with packet filtering, iptables, and firewalls\"","url":"https:\/\/docs.docker.com\/engine\/network\/packet-filtering-firewalls\/"}function OptanonWrapper(){}(function(e,t,n,s,o){e[s]=e[s]||[],e[s].push({"gtm.start":(new Date).getTime(),event:"gtm.js"});var a=t.getElementsByTagName(n)[0],i=t.createElement(n),r=s!="dataLayer"?"&l="+s:"";i.async=!0,i.src="https://www.googletagmanager.com/gtm.js?id="+o+r,a.parentNode.insertBefore(i,a)})(window,document,"script","dataLayer","GTM-WL2QLG5")(function(e,t,n,s,o,i){e.hj=e.hj||function(){(e.hj.q=e.hj.q||[]).push(arguments)},e._hjSettings={hjid:3169877,hjsv:6},o=t.getElementsByTagName("head")[0],i=t.createElement("script"),i.async=1,i.src=n+e._hjSettings.hjid+s+e._hjSettings.hjsv,o.appendChild(i)})(window,document,"https://static.hotjar.com/c/hotjar-",".js?sv=")window.askAI=function(e="search-page-input"){const t=document.querySelector("#"+e),n=t?t.value.trim():"";n&&window.Kapa?window.Kapa.open({mode:"ai",query:n,submit:!1}):window.Kapa&&window.Kapa.open({mode:"ai"})},document.addEventListener("click",function(e){e.target.closest(".open-kapa-widget")&&(e.preventDefault(),window.askAI("search-page-input"))})(()=>{function t(){let e=localStorage.getItem("theme-preference");return e||(window.matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light")}var e=t();document.firstElementChild.className=e==="dark"?"dark":"light",localStorage.setItem("theme-preference",e)})()
- Get started
- Guides
- Manuals
- Reference
Ask AI
Start typing to search or try
Ask AI.
    window.addEventListener("load", async function () {
      const pagefind = await import("/pagefind/pagefind.js");
      await pagefind.options({
        ranking: {
          termFrequency: 0.2,
          pageLength: 0.75,
          termSaturation: 1.4,
          termSimilarity: 6.0,
        },
      });
      const searchBarInput = document.querySelector("#search-bar-input");
      const searchBarResults = document.querySelector("#search-bar-results");
      const searchDropdown = document.querySelector("#search-bar-dropdown");
      function updateDropdownPosition() {
        const searchBar = document.querySelector("#search-bar");
        if (
          !searchBar ||
          !searchDropdown ||
          searchDropdown.style.display === "none"
        )
          return;
        const rect = searchBar.getBoundingClientRect();
        const dropdownWidth = Math.min(500, window.innerWidth * 0.9);
        const viewportWidth = window.innerWidth;
        let leftPos = rect.left;
        if (leftPos + dropdownWidth > viewportWidth - 20) {
          leftPos = viewportWidth - dropdownWidth - 20;
        }
        if (leftPos < 20) {
          leftPos = 20;
        }
        searchDropdown.style.top = rect.bottom + 8 + "px";
        searchDropdown.style.left = leftPos + "px";
      }
      window.addEventListener("scroll", updateDropdownPosition);
      window.addEventListener("resize", updateDropdownPosition);
      async function search(e) {
        const query = e.target.value;
        if (query === "") {
          searchBarResults.innerHTML = `\n      \u003cdiv\u003e\n        Start typing to search or try\n        \u003cbutton onclick=\u0022askAI(\u0027search-bar-input\u0027)\u0022 class=\u0022link\u0022\u003eAsk AI\u003c\/button\n        \u003e.\n      \u003c\/div\u003e\n      `;
          return;
        }
        const search = await pagefind.debouncedSearch(query);
        if (search === null) {
          return;
        } else {
          const resultsLength = search.results.length;
          const resultsData = await Promise.all(
            search.results.slice(0, 5).map((r) => r.data()),
          );
          const results = resultsData.map((item, index) => ({
            ...item,
            index: index + 1,
          }));
          if (query) {
            searchBarResults.classList.remove("hidden");
          } else {
            searchBarResults.classList.add("hidden");
          }
let resultsHTML = `<div class="p-2 text-gray-400 dark:text-gray-500">${resultsLength} results</div>`;
resultsHTML += results
  .map((item) => {
    let excerpt = item.excerpt;
    if (excerpt.length > 200) {
      excerpt = excerpt.substring(0, 200);
    }
    return `<div class="p-2">
<div class="flex flex-col items-start item">
  <a class="link" style="word-break: break-word; overflow-wrap: anywhere;" href="${item.url}" data-query="${query}" data-index="${item.index}">${item.meta.title}</a>
  <p class="text-black dark:text-white overflow-hidden text-left" style="word-break: break-word; overflow-wrap: anywhere;">â¦${excerpt}â¦</p>
</div>
</div>`;
  })
  .join("");
if (resultsLength > 5) {
  resultsHTML += `<div class="w-fit ml-auto px-4 py-2"><a href="/search/?q=${query}" class="link">Show all results</a></div>`;
}
          searchBarResults.innerHTML = resultsHTML;
        }
      }
      searchBarInput.addEventListener("input", search);
      if (window.heap !== undefined) {
        searchBarResults.addEventListener("click", function (event) {
          if (event.target.tagName === "A" && event.target.closest(".link")) {
            const searchQuery = event.target.getAttribute("data-query");
            const resultIndex = event.target.getAttribute("data-index");
            const url = new URL(event.target.href);
            const properties = {
              docs_search_target_path: url.pathname,
              docs_search_target_title: event.target.textContent,
              docs_search_query_text: searchQuery,
              docs_search_target_index: resultIndex,
              docs_search_source_path: window.location.pathname,
              docs_search_source_title: document.title,
            };
            heap.track("Docs - Search - Click - Result Link", properties);
          }
        });
      }
    });
BackManuals
- Get started
- Guides
- Reference
- Open source
- Docker Engine
- Install
- Ubuntu
- Debian
- RHEL
- Fedora
- Raspberry Pi OS (32-bit / armhf)
- CentOS
- SLES (s390x)
- Binaries
- Post-installation steps
- Storage
- Volumes
- Bind mounts
- tmpfs mounts
- Storage drivers
- Select a storage driver
- BTRFS storage driver
- Device Mapper storage driver (deprecated)
- OverlayFS storage driver
- VFS storage driver
- windowsfilter storage driver
- ZFS storage driver
- containerd image store
- Networking
- Docker with iptables
- Docker with nftables
- Packet filtering and firewalls
- Port publishing and mapping
- Network drivers
- Bridge network driver
- Host network driver
- IPvlan network driver
- Macvlan network driver
- None network driver
- Overlay network driver
- CA certificates
- Legacy container links
-
Containers
- Start containers automatically
- Run multiple processes in a container
- Resource constraints
- Runtime metrics
- Running containers
-
CLI
- Completion
- Proxy configuration
- Filter commands
- Format command and log output
- OpenTelemetry for the Docker CLI
- Daemon
- Start the daemon
- Use IPv6 networking
- Daemon proxy configuration
- Live restore
- Alternative container runtimes
- Collect Docker metrics with Prometheus
- Configure remote access for Docker daemon
- Read the daemon logs
- Troubleshooting the Docker daemon
-
Manage resources
- Docker contexts
- Docker object labels
- Prune unused Docker objects
- Logs and metrics
- Configure logging drivers
- Customize log driver output
-
Logging drivers
- Amazon CloudWatch Logs logging driver
- ETW logging driver
- Fluentd logging driver
- Google Cloud Logging driver
- Graylog Extended Format logging driver
- Journald logging driver
- JSON File logging driver
- Local file logging driver
- Splunk logging driver
- Syslog logging driver
- Use a logging driver plugin
- Use docker logs with remote logging drivers
- Security
- Rootless mode
- Tips
- Troubleshooting
- Antivirus software and Docker
- AppArmor security profiles for Docker
- Content trust in Docker
- Automation with content trust
- Delegations for content trust
- Deploy Notary Server with Compose
- Manage keys for content trust
- Play in a content trust sandbox
- Docker security non-events
- Isolate containers with a user namespace
- Protect the Docker daemon socket
- Seccomp security profiles for Docker
- Verify repository client with certificates
- Swarm mode
- Administer and maintain a swarm of Docker Engines
- Deploy a stack to a swarm
- Deploy services to a swarm
- Getting started with Swarm mode
- Create a swarm
- Add nodes to the swarm
- Deploy a service to the swarm
- Inspect a service on the swarm
- Scale the service in the swarm
- Delete the service running on the swarm
- Apply rolling updates to a service
- Drain a node on the swarm
-
How swarm works
- How nodes work
- How services work
- Manage swarm security with public key infrastructure (PKI)
- Swarm task states
- Join nodes to a swarm
- Lock your swarm to protect its encryption key
- Manage nodes in a swarm
- Manage sensitive data with Docker secrets
- Manage swarm service networks
- Raft consensus in swarm mode
- Run Docker Engine in swarm mode
- Store configuration data using Docker Configs
- Swarm mode key concepts
- Use Swarm mode routing mesh
- Deprecated features
- Docker Engine plugins
- Access authorization plugin
- Docker log driver plugins
- Docker network driver plugins
- Docker Plugin API
- Docker volume plugins
- Plugin Config Version 1 of Plugin V2
- Use Docker Engine plugins
-
Release notes
- Engine v29
- Engine v28
- Engine v27
- Engine v26.1
- Engine v26.0
- Engine v25.0
- Engine v24.0
- Engine v23.0
- Engine v20.10
- Engine v19.03
- Engine v18.09
- Engine v18.06
- Engine v18.05
- Engine v18.04
- Engine v18.03
- Engine v18.02
- Engine v18.01
- Engine v17.12
- Engine v17.11
- Engine v17.10
- Engine v17.09
- Engine v17.07
- Engine v17.06
- Engine v17.05
- Engine v17.04
- Engine v17.03
- Prior releases
- Docker Build
-
Core concepts
- Docker Build Overview
- Dockerfile overview
- Build context
-
Building
- Multi-stage
- Variables
- Secrets
- Multi-platform
- Export binaries
- Container Device Interface (CDI)
- Best practices
- Base images
- Build checks
New
- Builders
- Build drivers
- Docker container driver
- Docker driver
- Kubernetes driver
- Remote driver
- Manage builders
- Bake
- Introduction
- Targets
- Inheritance
- Variables
- Expressions
- Functions
- Matrix targets
- Contexts
- Bake file reference
- Bake standard library functions
- Building with Bake from a Compose file
- Overriding configurations
- Remote Bake file definition
- Cache
- Build cache invalidation
- Build garbage collection
- Cache storage backends
- Amazon S3 cache
- Azure Blob Storage cache
- GitHub Actions cache
- Inline cache
- Local cache
- Registry cache
- Optimize cache usage in builds
- CI
- GitHub Actions
- Annotations
- Attestations
- Build checks
- Build secrets
- Build summary
- BuildKit configuration
- Cache management
- Copy image between registries
- Export to Docker
- Local registry
- Multi-platform image
- Named contexts
- Push to multiple registries
- Reproducible builds
- Share image between jobs
- Tags and labels
- Test before push
- Update Docker Hub description
-
Metadata
- Annotations
- Build attestations
- Image attestation storage
- Provenance attestations
- SBOM attestations
- SLSA definitions
- Exporters
- Image and registry exporters
- Local and tar exporters
- OCI and Docker exporters
- BuildKit
- buildkitd.toml
- Configure BuildKit
- Custom Dockerfile syntax
- Dockerfile release notes
-
Debugging
- OpenTelemetry support
- Build release notes
- Docker Compose
-
Introduction to Compose
- How Compose works
- Why use Compose?
- History and development
- Install
- Plugin
- Standalone (Legacy)
- Uninstall
- Quickstart
-
How-tos
- Specify a project name
- Use lifecycle hooks
- Use service profiles
- Control startup order
- Use environment variables
- Set environment variables
- Environment variables precedence
- Pre-defined environment variables
- Interpolation
- Best practices
- Build dependent images
- Use Compose Watch
- Secrets in Compose
- Networking
- Use multiple Compose files
- Merge
- Extend
- Include
- Enable GPU support
- Use Compose in production
- OCI artifact applications
New
- Use provider services
New
- Compose Bridge
- Usage
- Customize
- Use Model Runner
- Compose SDK
New
-
Support and feedback
- FAQs
- Give feedback
- Sample apps
-
Releases
- Release notes
- Prior releases
- Migrate to Compose v2
- Testcontainers
- cagent
Experimental
- Building a coding agent
- Best practices
- Sharing agents
-
Reference
- Configuration file
- Toolsets
- CLI
- Examples
-
Integrations
- ACP
- MCP
- RAG
- AI
- MCP Catalog and Toolkit
Beta
- Get started
- MCP Catalog
- MCP Toolkit
- Dynamic MCP
New
- MCP Gateway
- Hub MCP server
- Security FAQs
- E2B sandboxes
- Docker Sandboxes
Experimental
- Get started
- Configure Claude Code
- Advanced
- Troubleshooting
- Model Runner
- Get started with DMR
- DMR REST API
- DMR examples
- Ask Gordon
Beta
- Model Context Protocol (MCP)
- Built-in tools in Gordon
- Configure MCP servers with YAML
-
AI and Docker Compose
- Use AI models in Compose
New
- Products
- Docker Desktop
-
Setup
-
Install
- Mac
- Mac permission requirements
- Windows
- Windows permission requirements
- Linux
- Ubuntu
- Debian
- Fedora
- Arch
- RHEL
- VM or VDI environments
- Sign in
- Allowlist
- Explore Docker Desktop
- Containers
- Images
- Volumes
- Builds
- Kubernetes
- Resource Saver mode
- Pause Docker Desktop
-
Features and capabilities
- Networking
- How-tos
- GPU support
- USB/IP support
- Synchronized file shares
- containerd image store
- Wasm workloads
Beta
- Docker Desktop CLI
- Virtual Machine Manager
- WSL
- Best practices
- Custom kernels on WSL
- Use WSL
-
Settings and maintenance
- Change settings
- Backup and restore data
-
Troubleshoot and support
- Troubleshoot and diagnose
- Common topics
- Known issues
- MacOS app damaged dialog
-
FAQs
- General
- Mac
- Windows
- Linux
- Releases
- Give feedback
- Uninstall
- Release notes
- Docker Hardened Images
New
- Quickstart
- About
- Hardened images
- Build process
- Image types
- Image testing
- Responsibility overview
- Feedback
- Features
- Continuous patching
- Enterprise support
- Flexibility
- Hardened, secure images
- Helm charts
- Seamless integration
- How-tos
- Explore images
- Mirror an image
- Customize an image
- Use an image
- Use an image in Kubernetes
- Use a Helm chart
Early Access
- Manage images
- Migrate an app
- Compare images
- Verify an image
- Scan an image
- Enforce image usage
- Debug a container
- Core concepts
- Attestations
- CIS Benchmark
- Code signing
- CVEs
- Distroless images
- FIPS
- glibc and musl
- Hardening
- Image digests
- Image provenance
- Immutability
- SBOMs
- SLSA
- Software Supply Chain Security
- SSDLC
- STIG
- VEX
- Troubleshoot
- Docker Offload
Early Access
- Quickstart
- About
- Configure
- Usage & billing
- Optimize usage
- Troubleshoot
- Give feedback
- Docker Build Cloud
- Setup
- Usage
- Continuous integration
- Optimization
- Builder settings
- Release notes
- Docker Hub
- Quickstart
- Library
- Search
- Trusted content
- Catalogs
- Mirror
- Repositories
- Create
-
Manage
- Repository information
- Access
- Images
- Tags
- Immutable tags
- Image Management
- Software artifacts
- Push images
- Move images
- Bulk migrate Docker images
- Image security insights
- Webhooks
- Automated builds
- Set up
- Link accounts
- Automated repository tests
- Advanced options
- Manage autobuilds
- Troubleshoot
- Trusted content
- Docker Official Images
- Docker Verified Publisher Program
- Docker-Sponsored Open Source Program
- Insights and analytics
- Export repositories
- Archive
- Delete
- Personal settings
- Usage and limits
- Pulls
- Optimize usage
- Service accounts
- Troubleshoot
- Release notes
- Docker Scout
- Install
- Quickstart
-
Explore
- Dashboard
- Docker Scout image analysis
- Docker Scout metrics exporter
- Image details view
- Manage vulnerability exceptions
-
How-tos
- Create an exception using the GUI
- Create an exception using the VEX
- Docker Scout environment variables
- Docker Scout SBOMs
- Use Scout with different artifact types
-
Deep dive
- Advisory database sources and matching service
- Data collection and storage in Docker Scout
- Policy Evaluation
- Configure policies
- Docker Scout health scores
- Evaluate policy compliance in CI
- Remediation with Docker Scout
- View Docker Scout policy status
- Integrations
-
Code quality
- SonarQube
-
Container registries
- Amazon ECR
- Artifactory Container Registry
- Azure Container Registry
- Continuous Integration
- Azure DevOps Pipelines
- Circle CI
- GitHub Actions
- GitLab CI/CD
- Jenkins
- Integrating Docker Scout with environments
- Generic (CLI)
- Sysdig
-
Source code management
- GitHub
-
Team collaboration
- Slack
-
Release notes
- CLI release notes
- Platform release notes
- Docker Extensions
- Marketplace extensions
- Non-marketplace extensions
- Configure a private marketplace
- Settings and feedback
- Extensions SDK
- The build and publish process
- Quickstart
-
Part one: Build
- Create a simple extension
- Create an advanced frontend extension
- Add a backend to your extension
- Part two: Publish
- Add labels
- Validate
- Package and release your extension
- Share your extension
- Publish in the Marketplace
- Build multi-arch extensions
- Architecture
- Metadata
- Security
- Design and UI styling
- Guidelines
- Docker design principles
- MUI best practices
-
Developer Guides
- Authentication
- Interacting with Kubernetes
- Invoke host binaries
- Use the Docker socket
-
Developer SDK tools
- Test and debug
- Continuous Integration (CI)
- CLI reference
-
Extension APIs
- Dashboard
- Docker
- Extension Backend
- Extension UI API
- Navigation
- Testcontainers Cloud
- Deprecated products and features
- Release lifecycle
- Platform
- Support
- Billing
- Add or update a payment method
- Manage your billing information
- 3D Secure authentication
- Invoices and billing history
- Change your billing cycle
- Submit a tax exemption certificate
- FAQs
- Docker accounts
- Accounts
- Create an account
- Manage an account
- Deactivate an account
- Security
- Personal access tokens
- Two-factor authentication
- Recover your Docker account
-
FAQs
- General
- Container
- Network and VM
- Security announcements
- Subscription
- Subscriptions and features
- Set up your subscription
- Scale your subscription
- Manage seats
- Change your subscription
- Docker Desktop license agreement
- FAQs
- Release notes
- Enterprise
- Administration
- Organization administration
- Create your organization
- Onboard your organization
- Manage organization members
- Convert an account into an organization
- Create and manage a team
- Deactivate an organization
- Manage Docker products
- Activity logs
- Organization information
- Insights
- Company administration overview
- Create a company
- Manage company members
- Manage company organizations
- Manage company owners
-
FAQ
- Organization
- Company
- Deploy Docker Desktop
- MSI installer
- PKG installer
- MS Store
- Deploy with Intune
- Deploy with Jamf Pro
- Microsoft Dev Box
- FAQs
- Security
- Single sign-on
- Configure
- Connect
-
FAQs
- General
- Domains
- Enforcement
- Identity providers
- User management
- Manage
- Provision
- Just-in-Time
- SCIM
- Group mapping
- Enforce sign-in
- Configure
- Roles and permissions
- Core roles
- Custom roles
- Manage domains
- Hardened Docker Desktop
- Enhanced Container Isolation
- Enable ECI
- Configure advanced settings
- Limitations
- FAQs
- Settings Management
- Use a JSON file
- Use the Admin Console
- Desktop settings reporting
- Settings reference
- Registry Access Management
- Image Access Management
- Air-gapped containers
- Organization access tokens
-
Troubleshoot
- Troubleshoot provisioning
- Troubleshoot SSO
Home/Manuals/Docker Engine/Networking/Packet filtering and firewallsPacket filtering and firewalls
Page optionsCopy page as Markdown for LLMs
View page as plain text
Ask questions with Docs AI
ClaudeOpen in Claude
function getCurrentPlaintextUrl(){const e=window.location.href.split("#")[0].replace(/\/$/,"");return`${e}/index.md`}function copyMarkdown(){fetch(getCurrentPlaintextUrl()).then(e=>e.text()).then(e=>{navigator.clipboard.writeText(e).then(()=>{const e=document.querySelector('[data-heap-id="copy-markdown-button"]');if(!e)return;const t=e.querySelectorAll(".icon-svg"),n=t[0],s=t[1];n.classList.add("hidden"),s.classList.remove("hidden"),setTimeout(()=>{n.classList.remove("hidden"),s.classList.add("hidden")},2e3)})}).catch(e=>{console.error("Error copying markdown:",e)})}function viewPlainText(){window.open(getCurrentPlaintextUrl(),"_blank")}function openInDocsAI(){const e=document.querySelector(".open-kapa-widget");e?e.click():alert("Couldn't find Docs AI.")}function openInClaude(){const e=getCurrentPlaintextUrl(),t=`Read ${e} so I can ask questions about it.`,n=encodeURIComponent(t),s=`https://claude.ai/new?q=${n}`;window.open(s,"_blank")}
Table of contents
- Firewall backend
- Docker on a router
- Prevent Docker from manipulating firewall rules
- Integration with firewalld
- Docker and ufw
On Linux, Docker creates firewall rules to implement network
isolation, port publishing and filtering.
Because these rules are required for the correct functioning of Docker bridge
networks, you should not modify the rules created by Docker.
This page describes options that control Docker's firewall rules to
implement functionality including port publishing, and NAT/masquerading.
Note
Docker creates firewall rules for bridge networks.
No rules are created for
```
ipvlan
```
,
```
macvlan
```
 or
```
host
```
 networking.
Firewall backend
By default, Docker Engine creates its firewall rules using iptables,
see Docker with iptables. It also has
support for nftables, see Docker with nftables.
For bridge networks, iptables and nftables have the same functionality.
Docker Engine option
```
firewall-backend
```
 can be used to select whether
iptables or nftables is used. See
daemon configuration.
Docker on a router
On Linux, Docker needs "IP Forwarding" enabled on the host. So, it enables
the
```
sysctl
```
 settings
```
net.ipv4.ip_forward
```
 and
```
net.ipv6.conf.all.forwarding
```
it they are not already enabled when it starts. When it does that, it also
configures the firewall to drop forwarded packets unless they are explicitly
accepted.
When Docker sets the default forwarding policy to "drop", it will prevent
your Docker host from acting as a router. This is the recommended setting when
IP Forwarding is enabled, unless router functionality is required.
To stop Docker from setting the forwarding policy to "drop", include
```
"ip-forward-no-drop": true
```
 in
```
/etc/docker/daemon.json
```
, or add option
```
--ip-forward-no-drop
```
 to the
```
dockerd
```
 command line.
Note
With the experimental nftables backend, Docker does not enable IP forwarding
itself, and it will not create a default "drop" nftables policy. See
Migrating from iptables to nftables.
Prevent Docker from manipulating firewall rules
Setting the
```
iptables
```
 or
```
ip6tables
```
 keys to
```
false
```
 in
daemon configuration, will
prevent Docker from creating most of its
```
iptables
```
 or
```
nftables
```
 rules. But,
this option is not appropriate for most users, it is likely to break
container networking for the Docker Engine.
For example, with Docker's firewalling disabled and no replacement
rules, containers in bridge networks will not be able to access
internet hosts by masquerading, but all of their ports will be accessible
to hosts on the local network.
It is not possible to completely prevent Docker from creating firewall
rules, and creating rules after-the-fact is extremely involved and beyond
the scope of these instructions.
Integration with firewalld
If you are running Docker with the
```
iptables
```
 or
```
ip6tables
```
 options set to
```
true
```
, and firewalld is enabled on your system, in
addition to its usual iptables or nftables rules, Docker creates a
```
firewalld
```
zone called
```
docker
```
, with target
```
ACCEPT
```
.
All bridge network interfaces created by Docker (for example,
```
docker0
```
) are
inserted into the
```
docker
```
 zone.
Docker also creates a forwarding policy called
```
docker-forwarding
```
 that allows
forwarding from
```
ANY
```
 zone to the
```
docker
```
 zone.
Docker and ufw
Uncomplicated Firewall
(ufw) is a frontend that ships with Debian and Ubuntu,
and it lets you manage firewall rules. Docker and ufw use firewall rules in
ways that make them incompatible with each other.
When you publish a container's ports using Docker, traffic to and from that
container gets diverted before it goes through the ufw firewall settings.
Docker routes container traffic in the
```
nat
```
 table, which means that packets
are diverted before it reaches the
```
INPUT
```
 and
```
OUTPUT
```
 chains that ufw uses.
Packets are routed before the firewall rules can be applied,
effectively ignoring your firewall configuration.
Edit this page
Request changes
Table of contents
- Firewall backend
- Docker on a router
- Prevent Docker from manipulating firewall rules
- Integration with firewalld
- Docker and ufw
Product offeringsPricingAbout usContributeRead llms.txt
Cookies Settings
Terms of ServiceStatusLegal
Copyright Â© 2013-2025 Docker Inc. All rights reserved.
