---
                {
  "source": "web",
  "label": "man7-perf",
  "url": "https://man7.org/linux/man-pages/man1/perf.1.html",
  "description": "perf reference for performance profiling (used in KVM/XDP scenarios)",
  "license": null,
  "collected_at": "2025-12-15T17:15:20.712198+00:00"
}
                ---
                # perf(1) — Linux manual page

                perf(1) - Linux manual page
man7.org > Linux > man-pages
Linux/UNIX system programming training
perf(1) — Linux manual page
NAME | SYNOPSIS | OPTIONS | DESCRIPTION | SEE ALSO | COLOPHON
```
PERF(1)                        perf Manual                        PERF(1)
```
NAME          top
```
       perf - Performance analysis tools for Linux
```
SYNOPSIS          top
```
perf [--version] [--help] [OPTIONS] COMMAND [ARGS]
```
OPTIONS          top
```
       -h, --help
           Run perf help command.
       -v, --version
           Display perf version.
       -vv
           Print the compiled-in status of libraries.
       --exec-path
           Display or set exec path.
       --html-path
           Display html documentation path.
       -p, --paginate
           Set up pager.
       --no-pager
           Do not set pager.
       --buildid-dir
           Setup buildid cache directory. It has higher priority than
           buildid.dir config file option.
       --list-cmds
           List the most commonly used perf commands.
       --list-opts
           List available perf options.
       --debugfs-dir
           Set debugfs directory or set environment variable
           PERF_DEBUGFS_DIR.
       --debug
           Setup debug variable (see list below) in value range (0, 10).
           Use like: --debug verbose # sets verbose = 1 --debug verbose=2
           # sets verbose = 2
               List of debug variables allowed to set:
                 verbose          - general debug messages
                 ordered-events   - ordered events object debug messages
                 data-convert     - data convert command debug messages
                 stderr           - write debug output (option -v) to stderr
                                    in browser mode
                 perf-event-open  - Print perf_event_open() arguments and
                                    return value
                 kmaps            - Print kernel and module maps (perf script
                                    and perf report without browser)
       --debug-file
           Write debug output to a specified file.
```
DESCRIPTION          top
```
       Performance counters for Linux are a new kernel-based subsystem
       that provide a framework for all things performance analysis. It
       covers hardware level (CPU/PMU, Performance Monitoring Unit)
       features and software features (software counters, tracepoints) as
       well.
```
SEE ALSO          top
```
perf-stat(1), perf-top(1), perf-record(1), perf-report(1),
       perf-list(1)perf-amd-ibs(1), perf-annotate(1), perf-archive(1),
       perf-arm-spe(1), perf-bench(1), perf-buildid-cache(1),
       perf-buildid-list(1), perf-c2c(1), perf-config(1), perf-data(1),
       perf-diff(1), perf-evlist(1), perf-ftrace(1), perf-help(1),
       perf-inject(1), perf-intel-pt(1), perf-iostat(1),
       perf-kallsyms(1), perf-kmem(1), perf-kvm(1), perf-lock(1),
       perf-mem(1), perf-probe(1), perf-sched(1), perf-script(1),
       perf-test(1), perf-trace(1), perf-version(1)
```
COLOPHON          top
```
       This page is part of the perf (Performance analysis tools for
       Linux (in Linux source tree)) project.  Information about the
       project can be found at
       â¨https://perf.wiki.kernel.org/index.php/Main_Pageâ©.  If you have a
       bug report for this manual page, send it to
       linux-kernel@vger.kernel.org.  This page was obtained from the
       project's upstream Git repository
       â¨http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.gitâ©
       on 2025-08-11.  (At that time, the date of the most recent commit
       that was found in the repository was 2025-08-10.)  If you discover
       any rendering problems in this HTML version of the page, or you
       believe there is a better or more up-to-date source for the page,
       or you have corrections or improvements to the information in this
       COLOPHON (which is not part of the original manual page), send a
       mail to man-pages@man7.org
perf                            2024-06-20                        PERF(1)
```
Pages that refer to this page:
    perf-bench(1),
    perf-config(1),
    perf-data(1),
    perf-help(1),
    perf-lock(1),
    perf_event_open(2)
            HTML rendering created 2025-09-06
            by Michael Kerrisk,
            author of
            The Linux Programming Interface.
            For details of in-depth
            Linux/UNIX system programming training courses
            that I teach, look here.
            Hosting by jambit GmbH.
var sc_project=7422636;
var sc_invisible=1;
var sc_security="9b6714ff";
  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-9830363-8']);
  _gaq.push(['_trackPageview']);
  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();
