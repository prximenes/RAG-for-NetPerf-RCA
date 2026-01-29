---
                {
  "source": "web",
  "label": "docker-bridge-driver",
  "url": "https://docs.docker.com/network/drivers/bridge/",
  "description": "Bridge driver behavior, options, MTU, ICC; supports docker bridge RTT/throughput scenarios",
  "license": "Docker docs (see site for license)",
  "collected_at": "2025-12-15T17:15:32.515936+00:00"
}
                ---
                # Docker bridge network driver

                Bridge network driver | Docker Docs
{"@context":"https://schema.org","@type":"WebPage","headline":"\"Bridge network driver\"","description":"\"All about using user-defined bridge networks and the default bridge\"","url":"https:\/\/docs.docker.com\/engine\/network\/drivers\/bridge\/"}function OptanonWrapper(){}(function(e,t,n,s,o){e[s]=e[s]||[],e[s].push({"gtm.start":(new Date).getTime(),event:"gtm.js"});var a=t.getElementsByTagName(n)[0],i=t.createElement(n),r=s!="dataLayer"?"&l="+s:"";i.async=!0,i.src="https://www.googletagmanager.com/gtm.js?id="+o+r,a.parentNode.insertBefore(i,a)})(window,document,"script","dataLayer","GTM-WL2QLG5")(function(e,t,n,s,o,i){e.hj=e.hj||function(){(e.hj.q=e.hj.q||[]).push(arguments)},e._hjSettings={hjid:3169877,hjsv:6},o=t.getElementsByTagName("head")[0],i=t.createElement("script"),i.async=1,i.src=n+e._hjSettings.hjid+s+e._hjSettings.hjsv,o.appendChild(i)})(window,document,"https://static.hotjar.com/c/hotjar-",".js?sv=")window.askAI=function(e="search-page-input"){const t=document.querySelector("#"+e),n=t?t.value.trim():"";n&&window.Kapa?window.Kapa.open({mode:"ai",query:n,submit:!1}):window.Kapa&&window.Kapa.open({mode:"ai"})},document.addEventListener("click",function(e){e.target.closest(".open-kapa-widget")&&(e.preventDefault(),window.askAI("search-page-input"))})(()=>{function t(){let e=localStorage.getItem("theme-preference");return e||(window.matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light")}var e=t();document.firstElementChild.className=e==="dark"?"dark":"light",localStorage.setItem("theme-preference",e)})()
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
Home/Manuals/Docker Engine/Networking/Network drivers/Bridge network driverBridge network driver
Page optionsCopy page as Markdown for LLMs
View page as plain text
Ask questions with Docs AI
ClaudeOpen in Claude
function getCurrentPlaintextUrl(){const e=window.location.href.split("#")[0].replace(/\/$/,"");return`${e}/index.md`}function copyMarkdown(){fetch(getCurrentPlaintextUrl()).then(e=>e.text()).then(e=>{navigator.clipboard.writeText(e).then(()=>{const e=document.querySelector('[data-heap-id="copy-markdown-button"]');if(!e)return;const t=e.querySelectorAll(".icon-svg"),n=t[0],s=t[1];n.classList.add("hidden"),s.classList.remove("hidden"),setTimeout(()=>{n.classList.remove("hidden"),s.classList.add("hidden")},2e3)})}).catch(e=>{console.error("Error copying markdown:",e)})}function viewPlainText(){window.open(getCurrentPlaintextUrl(),"_blank")}function openInDocsAI(){const e=document.querySelector(".open-kapa-widget");e?e.click():alert("Couldn't find Docs AI.")}function openInClaude(){const e=getCurrentPlaintextUrl(),t=`Read ${e} so I can ask questions about it.`,n=encodeURIComponent(t),s=`https://claude.ai/new?q=${n}`;window.open(s,"_blank")}
Table of contents
- Differences between user-defined bridges and the default bridge
- Options
- Default host binding address
- Manage a user-defined bridge
- Connect a container to a user-defined bridge
- Disconnect a container from a user-defined bridge
- Use IPv6 in a user-defined bridge network
- IPv6-only bridge networks
- Use the default bridge network
- Connect a container to the default bridge network
- Configure the default bridge network
- Use IPv6 with the default bridge network
- Connection limit for bridge networks
- Skip Bridge IP address configuration
- Usage examples
- Use the default bridge network
- Use user-defined bridge networks
- Next steps
A Docker bridge network has an IPv4 subnet and, optionally, an IPv6 subnet.
Each container connected to the bridge network has a network interface with
addresses in the network's subnets. By default, it:
- Allows unrestricted network access to containers in the network from
the host, and from other containers connected to the same bridge network.
- Blocks access from containers in other networks and from outside the
Docker host.
- Uses masquerading to give containers external network access. Devices on
the host's external networks only see the IP address of the Docker host.
- Supports port publishing, where network traffic is forwarded between
container ports and ports on host IP addresses. The published ports
can be accessed from outside the Docker host, on its IP addresses.
In terms of Docker, a bridge network uses a software bridge which lets
containers connected to the same bridge network communicate, while providing
isolation from containers that aren't connected to that bridge network. By
default, the Docker bridge driver automatically installs rules in the host
machine so that containers connected to different bridge networks can only
communicate with each other using published ports.
Bridge networks apply to containers running on the same Docker daemon host.
For communication among containers running on different Docker daemon hosts, you
can either manage routing at the OS level, or you can use an
overlay network.
When you start Docker, a default bridge network (also
called
```
bridge
```
) is created automatically, and newly-started containers connect
to it unless otherwise specified. You can also create user-defined custom bridge
networks. User-defined bridge networks are superior to the default
```
bridge
```
network.
Differences between user-defined bridges and the default bridge
- User-defined bridges provide automatic DNS resolution between containers.
Containers on the default bridge network can only access each other by IP
addresses, unless you use the
```
--link
```
 option, which is
considered legacy. On a user-defined bridge network, containers can resolve
each other by name or alias.
Imagine an application with a web front-end and a database back-end. If you call
your containers
```
web
```
 and
```
db
```
, the web container can connect to the db container
at
```
db
```
, no matter which Docker host the application stack is running on.
If you run the same application stack on the default bridge network, you need
to manually create links between the containers (using the legacy
```
--link
```
flag). These links need to be created in both directions, so you can see this
gets complex with more than two containers which need to communicate.
Alternatively, you can manipulate the
```
/etc/hosts
```
 files within the containers,
but this creates problems that are difficult to debug.
- User-defined bridges provide better isolation.
All containers without a
```
--network
```
 specified, are attached to the default bridge network. This can be a risk, as unrelated stacks/services/containers are then able to communicate.
Using a user-defined network provides a scoped network in which only containers attached to that network are able to communicate.
- Containers can be attached and detached from user-defined networks on the fly.
During a container's lifetime, you can connect or disconnect it from
user-defined networks on the fly. To remove a container from the default
bridge network, you need to stop the container and recreate it with different
network options.
- Each user-defined network creates a configurable bridge.
If your containers use the default bridge network, you can configure it, but
all the containers use the same settings, such as MTU and
```
iptables
```
 rules.
In addition, configuring the default bridge network happens outside of Docker
itself, and requires a restart of Docker.
User-defined bridge networks are created and configured using
```
docker network create
```
. If different groups of applications have different
network requirements, you can configure each user-defined bridge separately,
as you create it.
- Linked containers on the default bridge network share environment variables.
Originally, the only way to share environment variables between two containers
was to link them using the
```
--link
```
 flag. This type of
variable sharing isn't possible with user-defined networks. However, there
are superior ways to share environment variables. A few ideas:
- Multiple containers can mount a file or directory containing the shared
information, using a Docker volume.
- Multiple containers can be started together using
```
docker-compose
```
 and the
compose file can define the shared variables.
- You can use swarm services instead of standalone containers, and take
advantage of shared
secrets and
configs.
Containers connected to the same user-defined bridge network effectively expose all ports
to each other. For a port to be accessible to containers or non-Docker hosts on
different networks, that port must be published using the
```
-p
```
 or
```
--publish
```
flag.
Options
The following table describes the driver-specific options that you can pass to
```
--opt
```
 when creating a custom network using the
```
bridge
```
 driver.
OptionDefaultDescription
```
com.docker.network.bridge.name
```
Interface name to use when creating the Linux bridge.
```
com.docker.network.bridge.enable_ip_masquerade
```
```
true
```
Enable IP masquerading.
```
com.docker.network.host_ipv4
```
```
com.docker.network.host_ipv6
```
Address to use for source NAT. See Packet filtering and firewalls.
```
com.docker.network.bridge.gateway_mode_ipv4
```
```
com.docker.network.bridge.gateway_mode_ipv6
```
```
nat
```
Control external connectivity. See Packet filtering and firewalls.
```
com.docker.network.bridge.enable_icc
```
```
true
```
Enable or Disable inter-container connectivity.
```
com.docker.network.bridge.host_binding_ipv4
```
all IPv4 and IPv6 addressesDefault IP when binding container ports.
```
com.docker.network.driver.mtu
```
```
0
```
 (no limit)Set the containers network Maximum Transmission Unit (MTU).
```
com.docker.network.container_iface_prefix
```
```
eth
```
Set a custom prefix for container interfaces.
```
com.docker.network.bridge.inhibit_ipv4
```
```
false
```
Prevent Docker from assigning an IP address to the bridge.
Some of these options are also available as flags to the
```
dockerd
```
 CLI, and you
can use them to configure the default
```
docker0
```
 bridge when starting the Docker
daemon. The following table shows which options have equivalent flags in the
```
dockerd
```
 CLI.
OptionFlag
```
com.docker.network.bridge.name
```
-
```
com.docker.network.bridge.enable_ip_masquerade
```
```
--ip-masq
```
```
com.docker.network.bridge.enable_icc
```
```
--icc
```
```
com.docker.network.bridge.host_binding_ipv4
```
```
--ip
```
```
com.docker.network.driver.mtu
```
```
--mtu
```
```
com.docker.network.container_iface_prefix
```
-
The Docker daemon supports a
```
--bridge
```
 flag, which you can use to define
your own
```
docker0
```
 bridge. Use this option if you want to run multiple daemon
instances on the same host. For details, see
Run multiple daemons.
Default host binding address
When no host address is given in port publishing options like
```
-p 80
```
or
```
-p 8080:80
```
, the default is to make the container's port 80 available on all
host addresses, IPv4 and IPv6.
The bridge network driver option
```
com.docker.network.bridge.host_binding_ipv4
```
can be used to modify the default address for published ports.
Despite the option's name, it is possible to specify an IPv6 address.
When the default binding address is an address assigned to a specific interface,
the container's port will only be accessible via that address.
Setting the default binding address to
```
::
```
 means published ports will only be
available on the host's IPv6 addresses. However, setting it to
```
0.0.0.0
```
 means it
will be available on the host's IPv4 and IPv6 addresses.
To restrict a published port to IPv4 only, the address must be included in the
container's publishing options. For example,
```
-p 0.0.0.0:8080:80
```
.
Manage a user-defined bridge
Use the
```
docker network create
```
 command to create a user-defined bridge
network.
```
```
$ docker network create my-net
```
```
You can specify the subnet, the IP address range, the gateway, and other
options. See the
docker network create
reference or the output of
```
docker network create --help
```
 for details.
Use the
```
docker network rm
```
 command to remove a user-defined bridge
network. If containers are currently connected to the network,
disconnect them
first.
```
```
$ docker network rm my-net
```
```
What's really happening?
When you create or remove a user-defined bridge or connect or disconnect a
container from a user-defined bridge, Docker uses tools specific to the
operating system to manage the underlying network infrastructure (such as adding
or removing bridge devices or configuring
```
iptables
```
 rules on Linux). These
details should be considered implementation details. Let Docker manage your
user-defined networks for you.
Connect a container to a user-defined bridge
When you create a new container, you can specify one or more
```
--network
```
 flags.
This example connects an Nginx container to the
```
my-net
```
 network. It also
publishes port 80 in the container to port 8080 on the Docker host, so external
clients can access that port. Any other container connected to the
```
my-net
```
network has access to all ports on the
```
my-nginx
```
 container, and vice versa.
```
```
$ docker create --name my-nginx \
  --network my-net \
  --publish 8080:80 \
  nginx:latest
```
```
To connect a running container to an existing user-defined bridge, use the
```
docker network connect
```
 command. The following command connects an already-running
```
my-nginx
```
 container to an already-existing
```
my-net
```
 network:
```
```
$ docker network connect my-net my-nginx
```
```
Disconnect a container from a user-defined bridge
To disconnect a running container from a user-defined bridge, use the
```
docker network disconnect
```
 command. The following command disconnects
the
```
my-nginx
```
 container from the
```
my-net
```
 network.
```
```
$ docker network disconnect my-net my-nginx
```
```
Use IPv6 in a user-defined bridge network
When you create your network, you can specify the
```
--ipv6
```
 flag to enable IPv6.
```
```
$ docker network create --ipv6 --subnet 2001:db8:1234::/64 my-net
```
```
If you do not provide a
```
--subnet
```
 option, a Unique Local Address (ULA) prefix
will be chosen automatically.
IPv6-only bridge networks
To skip IPv4 address configuration on the bridge and in its containers, create
the network with option
```
--ipv4=false
```
, and enable IPv6 using
```
--ipv6
```
.
```
```
$ docker network create --ipv6 --ipv4=false v6net
```
```
IPv4 address configuration cannot be disabled in the default bridge network.
Use the default bridge network
The default
```
bridge
```
 network is considered a legacy detail of Docker and is not
recommended for production use. Configuring it is a manual operation, and it has
technical shortcomings.
Connect a container to the default bridge network
If you do not specify a network using the
```
--network
```
 flag, and you do specify a
network driver, your container is connected to the default
```
bridge
```
 network by
default. Containers connected to the default
```
bridge
```
 network can communicate,
but only by IP address, unless they're linked using the
legacy
```
--link
```
 flag.
Configure the default bridge network
To configure the default
```
bridge
```
 network, you specify options in
```
daemon.json
```
.
Here is an example
```
daemon.json
```
 with several options specified. Only specify
the settings you need to customize.
```
```
{"bip":"192.168.1.1/24","fixed-cidr":"192.168.1.0/25","mtu":1500,"default-gateway":"192.168.1.254","dns":["10.20.1.2","10.20.1.3"]}
```
```
In this example:
- The bridge's address is "192.168.1.1/24" (from
```
bip
```
).
- The bridge network's subnet is "192.168.1.0/24" (from
```
bip
```
).
- Container addresses will be allocated from "192.168.1.0/25" (from
```
fixed-cidr
```
).
Use IPv6 with the default bridge network
IPv6 can be enabled for the default bridge using the following options in
```
daemon.json
```
, or their command line equivalents.
These three options only affect the default bridge, they are not used by
user-defined networks. The addresses in below are examples from the
IPv6 documentation range.
- Option
```
ipv6
```
 is required.
- Option
```
bip6
```
 is optional, it specifies the address of the default bridge, which
will be used as the default gateway by containers. It also specifies the subnet
for the bridge network.
- Option
```
fixed-cidr-v6
```
 is optional, it specifies the address range Docker may
automatically allocate to containers.
- The prefix should normally be
```
/64
```
 or shorter.
- For experimentation on a local network, it is better to use a Unique Local
Address (ULA) prefix (matching
```
fd00::/8
```
) than a Link Local prefix (matching
```
fe80::/10
```
).
- Option
```
default-gateway-v6
```
 is optional. If unspecified, the default is the first
address in the
```
fixed-cidr-v6
```
 subnet.
```
```
{"ipv6":true,"bip6":"2001:db8::1111/64","fixed-cidr-v6":"2001:db8::/64","default-gateway-v6":"2001:db8:abcd::89"}
```
```
If no
```
bip6
```
 is specified,
```
fixed-cidr-v6
```
 defines the subnet for the bridge
network. If no
```
bip6
```
 or
```
fixed-cidr-v6
```
 is specified, a ULA prefix will be
chosen.
Restart Docker for changes to take effect.
Connection limit for bridge networks
Due to limitations set by the Linux kernel, bridge networks become unstable and
inter-container communications may break when 1000 containers or more connect
to a single network.
For more information about this limitation, see
moby/moby#44973.
Skip Bridge IP address configuration
The bridge is normally assigned the network's
```
--gateway
```
 address, which is
used as the default route from the bridge network to other networks.
The
```
com.docker.network.bridge.inhibit_ipv4
```
 option lets you create a network
without the IPv4 gateway address being assigned to the bridge. This is useful
if you want to configure the gateway IP address for the bridge manually. For
instance if you add a physical interface to your bridge, and need it to have
the gateway address.
With this configuration, north-south traffic (to and from the bridge network)
won't work unless you've manually configured the gateway address on the bridge,
or a device attached to it.
This option can only be used with user-defined bridge networks.
Usage examples
This section provides hands-on examples for working with bridge networks.
Use the default bridge network
This example shows how the default
```
bridge
```
 network works. You start two
```
alpine
```
 containers on the default bridge and test how they communicate.
Note
The default
```
bridge
```
 network is not recommended for production. Use
user-defined bridge networks instead.
- List current networks:
```
```
$ docker network ls
NETWORK ID          NAME                DRIVER              SCOPE
17e324f45964        bridge              bridge              local
6ed54d316334        host                host                local
7092879f2cc8        none                null                local
```
```
The default
```
bridge
```
 network is listed, along with
```
host
```
 and
```
none
```
.
- Start two
```
alpine
```
 containers running
```
ash
```
. The
```
-dit
```
 flags mean detached,
interactive, and with a TTY. Since you haven't specified a
```
--network
```
 flag,
the containers connect to the default
```
bridge
```
 network.
```
```
$ docker run -dit --name alpine1 alpine ash
$ docker run -dit --name alpine2 alpine ash
```
```
Verify both containers are running:
```
```
$ docker container ls
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
602dbf1edc81        alpine              "ash"               4 seconds ago       Up 3 seconds                            alpine2
da33b7aa74b0        alpine              "ash"               17 seconds ago      Up 16 seconds                           alpine1
```
```
- Inspect the
```
bridge
```
 network to see connected containers:
```
```
$ docker network inspect bridge
```
```
The output shows both containers connected, with their assigned IP addresses
(
```
172.17.0.2
```
 for
```
alpine1
```
 and
```
172.17.0.3
```
 for
```
alpine2
```
).
- Connect to
```
alpine1
```
:
```
```
$ docker attach alpine1
/ #
```
```
Show the network interfaces for
```
alpine1
```
 from within the container:
```
```
# ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
27: eth0@if28: <BROADCAST,MULTICAST,UP,LOWER_UP,M-DOWN> mtu 1500 qdisc noqueue state UP
    link/ether 02:42:ac:11:00:02 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.2/16 scope global eth0
       valid_lft forever preferred_lft forever
```
```
In this example, the
```
eth0
```
 interface has the IP address
```
172.17.0.2
```
.
- From within
```
alpine1
```
, verify you can connect to the internet:
```
```
# ping -c 2 google.com
PING google.com (172.217.3.174): 56 data bytes
64 bytes from 172.217.3.174: seq=0 ttl=41 time=9.841 ms
64 bytes from 172.217.3.174: seq=1 ttl=41 time=9.897 ms
--- google.com ping statistics ---
2 packets transmitted, 2 packets received, 0% packet loss
round-trip min/avg/max = 9.841/9.869/9.897 ms
```
```
- Ping the second container by its IP address:
```
```
# ping -c 2 172.17.0.3
PING 172.17.0.3 (172.17.0.3): 56 data bytes
64 bytes from 172.17.0.3: seq=0 ttl=64 time=0.086 ms
64 bytes from 172.17.0.3: seq=1 ttl=64 time=0.094 ms
--- 172.17.0.3 ping statistics ---
2 packets transmitted, 2 packets received, 0% packet loss
round-trip min/avg/max = 0.086/0.090/0.094 ms
```
```
This succeeds. Now try pinging by container name:
```
```
# ping -c 2 alpine2
ping: bad address 'alpine2'
```
```
On the default bridge network, containers can't resolve each other by name.
- Detach from
```
alpine1
```
 without stopping it using
```
CTRL+p CTRL+q
```
.
- Clean up: stop the containers and remove them.
```
```
$ docker container stop alpine1 alpine2
$ docker container rm alpine1 alpine2
```
```
Stopped containers lose their IP addresses.
Use user-defined bridge networks
This example shows how user-defined bridge networks provide better isolation
and automatic DNS resolution between containers.
- Create the
```
alpine-net
```
 network:
```
```
$ docker network create --driver bridge alpine-net
```
```
- List Docker's networks:
```
```
$ docker network ls
NETWORK ID          NAME                DRIVER              SCOPE
e9261a8c9a19        alpine-net          bridge              local
17e324f45964        bridge              bridge              local
6ed54d316334        host                host                local
7092879f2cc8        none                null                local
```
```
Inspect the
```
alpine-net
```
 network:
```
```
$ docker network inspect alpine-net
```
```
This shows the network's gateway (for example,
```
172.18.0.1
```
) and that no
containers are connected yet.
- Create four containers. Three connect to
```
alpine-net
```
, and one connects to
the default
```
bridge
```
. Then connect one container to both networks:
```
```
$ docker run -dit --name alpine1 --network alpine-net alpine ash
$ docker run -dit --name alpine2 --network alpine-net alpine ash
$ docker run -dit --name alpine3 alpine ash
$ docker run -dit --name alpine4 --network alpine-net alpine ash
$ docker network connect bridge alpine4
```
```
Verify all containers are running:
```
```
$ docker container ls
CONTAINER ID        IMAGE               COMMAND             CREATED              STATUS              PORTS               NAMES
156849ccd902        alpine              "ash"               41 seconds ago       Up 41 seconds                           alpine4
fa1340b8d83e        alpine              "ash"               51 seconds ago       Up 51 seconds                           alpine3
a535d969081e        alpine              "ash"               About a minute ago   Up About a minute                       alpine2
0a02c449a6e9        alpine              "ash"               About a minute ago   Up About a minute                       alpine1
```
```
- Inspect both networks again to see which containers are connected:
```
```
$ docker network inspect bridge
```
```
Containers
```
alpine3
```
 and
```
alpine4
```
 are connected to the
```
bridge
```
 network.
```
```
$ docker network inspect alpine-net
```
```
Containers
```
alpine1
```
,
```
alpine2
```
, and
```
alpine4
```
 are connected to
```
alpine-net
```
.
- On user-defined networks, containers can resolve each other by name. Connect
to
```
alpine1
```
 and test:
Note
Automatic service discovery only resolves custom container names, not
default automatically generated names.
```
```
$ docker container attach alpine1
# ping -c 2 alpine2
PING alpine2 (172.18.0.3): 56 data bytes
64 bytes from 172.18.0.3: seq=0 ttl=64 time=0.085 ms
64 bytes from 172.18.0.3: seq=1 ttl=64 time=0.090 ms
--- alpine2 ping statistics ---
2 packets transmitted, 2 packets received, 0% packet loss
round-trip min/avg/max = 0.085/0.087/0.090 ms
# ping -c 2 alpine4
PING alpine4 (172.18.0.4): 56 data bytes
64 bytes from 172.18.0.4: seq=0 ttl=64 time=0.076 ms
64 bytes from 172.18.0.4: seq=1 ttl=64 time=0.091 ms
--- alpine4 ping statistics ---
2 packets transmitted, 2 packets received, 0% packet loss
round-trip min/avg/max = 0.076/0.083/0.091 ms
```
```
- From
```
alpine1
```
, you can't connect to
```
alpine3
```
 because it's on a different
network:
```
```
# ping -c 2 alpine3
ping: bad address 'alpine3'
```
```
You also can't connect by IP address. If
```
alpine3
```
's IP is
```
172.17.0.2
```
:
```
```
# ping -c 2 172.17.0.2
PING 172.17.0.2 (172.17.0.2): 56 data bytes
--- 172.17.0.2 ping statistics ---
2 packets transmitted, 0 packets received, 100% packet loss
```
```
Detach from
```
alpine1
```
 using
```
CTRL+p CTRL+q
```
.
- Since
```
alpine4
```
 is connected to both networks, it can reach all containers.
However, you need to use
```
alpine3
```
's IP address:
```
```
$ docker container attach alpine4
# ping -c 2 alpine1
PING alpine1 (172.18.0.2): 56 data bytes
64 bytes from 172.18.0.2: seq=0 ttl=64 time=0.074 ms
64 bytes from 172.18.0.2: seq=1 ttl=64 time=0.082 ms
--- alpine1 ping statistics ---
2 packets transmitted, 2 packets received, 0% packet loss
round-trip min/avg/max = 0.074/0.078/0.082 ms
# ping -c 2 alpine2
PING alpine2 (172.18.0.3): 56 data bytes
64 bytes from 172.18.0.3: seq=0 ttl=64 time=0.075 ms
64 bytes from 172.18.0.3: seq=1 ttl=64 time=0.080 ms
--- alpine2 ping statistics ---
2 packets transmitted, 2 packets received, 0% packet loss
round-trip min/avg/max = 0.075/0.077/0.080 ms
# ping -c 2 alpine3
ping: bad address 'alpine3'
# ping -c 2 172.17.0.2
PING 172.17.0.2 (172.17.0.2): 56 data bytes
64 bytes from 172.17.0.2: seq=0 ttl=64 time=0.089 ms
64 bytes from 172.17.0.2: seq=1 ttl=64 time=0.075 ms
--- 172.17.0.2 ping statistics ---
2 packets transmitted, 2 packets received, 0% packet loss
round-trip min/avg/max = 0.075/0.082/0.089 ms
```
```
- Verify all containers can connect to the internet:
```
```
# ping -c 2 google.com
PING google.com (172.217.3.174): 56 data bytes
64 bytes from 172.217.3.174: seq=0 ttl=41 time=9.778 ms
64 bytes from 172.217.3.174: seq=1 ttl=41 time=9.634 ms
--- google.com ping statistics ---
2 packets transmitted, 2 packets received, 0% packet loss
round-trip min/avg/max = 9.634/9.706/9.778 ms
```
```
Detach with
```
CTRL+p CTRL+q
```
 and repeat for
```
alpine3
```
 and
```
alpine1
```
 if
desired.
- Clean up:
```
```
$ docker container stop alpine1 alpine2 alpine3 alpine4
$ docker container rm alpine1 alpine2 alpine3 alpine4
$ docker network rm alpine-net
```
```
Next steps
- Learn about networking from the container's point of view
- Learn about overlay networks
- Learn about Macvlan networks
Edit this page
Request changes
Table of contents
- Differences between user-defined bridges and the default bridge
- Options
- Default host binding address
- Manage a user-defined bridge
- Connect a container to a user-defined bridge
- Disconnect a container from a user-defined bridge
- Use IPv6 in a user-defined bridge network
- IPv6-only bridge networks
- Use the default bridge network
- Connect a container to the default bridge network
- Configure the default bridge network
- Use IPv6 with the default bridge network
- Connection limit for bridge networks
- Skip Bridge IP address configuration
- Usage examples
- Use the default bridge network
- Use user-defined bridge networks
- Next steps
Product offeringsPricingAbout usContributeRead llms.txt
Cookies Settings
Terms of ServiceStatusLegal
Copyright Â© 2013-2025 Docker Inc. All rights reserved.
