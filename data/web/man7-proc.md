---
                {
  "source": "web",
  "label": "man7-proc",
  "url": "https://man7.org/linux/man-pages/man5/proc.5.html",
  "description": "Reference for /proc used in diagnostics (interrupts, softirqs, etc.)",
  "license": null,
  "collected_at": "2025-12-15T17:15:19.356697+00:00"
}
                ---
                # proc(5) — Linux manual page

                proc(5) - Linux manual page
man7.org > Linux > man-pages
Linux/UNIX system programming training
proc(5) — Linux manual page
NAME | DESCRIPTION | NOTES | SEE ALSO | COLOPHON
```
proc(5)                    File Formats Manual                    proc(5)
```
NAME          top
```
       proc - process information, system information, and sysctl pseudo-
       filesystem
```
DESCRIPTION          top
```
       The proc filesystem is a pseudo-filesystem which provides an
       interface to kernel data structures.  It is commonly mounted at
       /proc.  Typically, it is mounted automatically by the system, but
       it can also be mounted manually using a command such as:
           mount -t proc proc /proc
       Most of the files in the proc filesystem are read-only, but some
       files are writable, allowing kernel variables to be changed.
   Mount options
       The proc filesystem supports the following mount options:
       hidepid=n (since Linux 3.3)
              This option controls who can access the information in
              /proc/pid directories.  The argument, n, is one of the
              following values:
              0   Everybody may access all /proc/pid directories.  This
                  is the traditional behavior, and the default if this
                  mount option is not specified.
              1   Users may not access files and subdirectories inside
                  any /proc/pid directories but their own (the /proc/pid
                  directories themselves remain visible).  Sensitive
                  files such as /proc/pid/cmdline and /proc/pid/status
                  are now protected against other users.  This makes it
                  impossible to learn whether any user is running a
                  specific program (so long as the program doesn't
                  otherwise reveal itself by its behavior).
              2   As for mode 1, but in addition the /proc/pid
                  directories belonging to other users become invisible.
                  This means that /proc/pid entries can no longer be used
                  to discover the PIDs on the system.  This doesn't hide
                  the fact that a process with a specific PID value
                  exists (it can be learned by other means, for example,
                  by "kill -0 $PID"), but it hides a process's UID and
                  GID, which could otherwise be learned by employing
                  stat(2) on a /proc/pid directory.  This greatly
                  complicates an attacker's task of gathering information
                  about running processes (e.g., discovering whether some
                  daemon is running with elevated privileges, whether
                  another user is running some sensitive program, whether
                  other users are running any program at all, and so on).
              gid=gid (since Linux 3.3)
                  Specifies the ID of a group whose members are
                  authorized to learn process information otherwise
                  prohibited by hidepid (i.e., users in this group behave
                  as though /proc was mounted with hidepid=0).  This
                  group should be used instead of approaches such as
                  putting nonroot users into the sudoers(5) file.
       subset=pid (since Linux 5.8)
              Show only the specified subset of procfs, hiding all top
              level files and directories in the procfs that are not
              related to tasks.
   Overview
       Underneath /proc, there are the following general groups of files
       and subdirectories:
       /proc/pid subdirectories
              Each one of these subdirectories contains files and
              subdirectories exposing information about the process with
              the corresponding process ID.
              Underneath each of the /proc/pid directories, a task
              subdirectory contains subdirectories of the form task/tid,
              which contain corresponding information about each of the
              threads in the process, where tid is the kernel thread ID
              of the thread.
              The /proc/pid subdirectories are visible when iterating
              through /proc with getdents(2) (and thus are visible when
              one uses ls(1) to view the contents of /proc).
       /proc/tid subdirectories
              Each one of these subdirectories contains files and
              subdirectories exposing information about the thread with
              the corresponding thread ID.  The contents of these
              directories are the same as the corresponding
              /proc/pid/task/tid directories.
              The /proc/tid subdirectories are not visible when iterating
              through /proc with getdents(2) (and thus are not visible
              when one uses ls(1) to view the contents of /proc).
       /proc/self
              When a process accesses this magic symbolic link, it
              resolves to the process's own /proc/pid directory.
       /proc/thread-self
              When a thread accesses this magic symbolic link, it
              resolves to the process's own /proc/self/task/tid
              directory.
       /proc/[a-z]*
              Various other files and subdirectories under /proc expose
              system-wide information.
       All of the above are described in more detail in separate manpages
       whose names start with proc_.
```
NOTES          top
```
       Many files contain strings (e.g., the environment and command
       line) that are in the internal format, with subfields terminated
       by null bytes ('\0').  When inspecting such files, you may find
       that the results are more readable if you use a command of the
       following form to display them:
           $ cat file| tr '\000' '\n'
```
SEE ALSO          top
```
cat(1), dmesg(1), find(1), free(1), htop(1), init(1), ps(1),
       pstree(1), tr(1), uptime(1), chroot(2), mmap(2), readlink(2),
       syslog(2), slabinfo(5), sysfs(5), hier(7), namespaces(7), time(7),
       arp(8), hdparm(8), ifconfig(8), lsmod(8), lspci(8), mount(8),
       netstat(8), procinfo(8), route(8), sysctl(8)
       The Linux kernel source files: Documentation/filesystems/proc.rst,
       Documentation/admin-guide/sysctl/fs.rst,
       Documentation/admin-guide/sysctl/kernel.rst,
       Documentation/admin-guide/sysctl/net.rst, and
       Documentation/admin-guide/sysctl/vm.rst.
```
COLOPHON          top
```
       This page is part of the man-pages (Linux kernel and C library
       user-space interface documentation) project.  Information about
       the project can be found at
       â¨https://www.kernel.org/doc/man-pages/â©.  If you have a bug report
       for this manual page, see
       â¨https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/CONTRIBUTINGâ©.
       This page was obtained from the tarball man-pages-6.15.tar.gz
       fetched from
       â¨https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/â© on
       2025-08-11.  If you discover any rendering problems in this HTML
       version of the page, or you believe there is a better or more up-
       to-date source for the page, or you have corrections or
       improvements to the information in this COLOPHON (which is not
       part of the original manual page), send a mail to
       man-pages@man7.org
Linux man-pages 6.15            2025-05-17                        proc(5)
```
Pages that refer to this page:
    choom(1),
    htop(1),
    kill(1),
    lsfd(1),
    ps(1),
    pstree(1),
    strace(1),
    systemd-nspawn(1),
    unshare(1),
    chroot(2),
    close_range(2),
    delete_module(2),
    eventfd(2),
    execve(2),
    fork(2),
    getrlimit(2),
    init_module(2),
    ioctl_nsfs(2),
    io_setup(2),
    kcmp(2),
    mlock(2),
    mmap(2),
    mount(2),
    mount_setattr(2),
    msgctl(2),
    open(2),
    openat2(2),
    pidfd_open(2),
    posix_fadvise(2),
    seccomp(2),
    seccomp_unotify(2),
    semctl(2),
    shmctl(2),
    shmget(2),
    signalfd(2),
    statx(2),
    symlink(2),
    sysctl(2),
    sysfs(2),
    sysinfo(2),
    timer_create(2),
    vfork(2),
    errno(3),
    fexecve(3),
    getauxval(3),
    getloadavg(3),
    malloc(3),
    mallopt(3),
    procps(3),
    procps_misc(3),
    procps_pids(3),
    program_invocation_name(3),
    pthread_create(3),
    sd_bus_creds_get_pid(3),
    acct(5),
    core(5),
    filesystems(5),
    proc_apm(5),
    proc_buddyinfo(5),
    proc_bus(5),
    proc_cgroups(5),
    proc_cmdline(5),
    proc_config.gz(5),
    proc_cpuinfo(5),
    proc_crypto(5),
    proc_devices(5),
    proc_diskstats(5),
    proc_dma(5),
    proc_driver(5),
    proc_execdomains(5),
    proc_fb(5),
    proc_filesystems(5),
    proc_fs(5),
    proc_ide(5),
    proc_interrupts(5),
    proc_iomem(5),
    proc_ioports(5),
    proc_kallsyms(5),
    proc_kcore(5),
    proc_keys(5),
    proc_kmsg(5),
    proc_kpagecgroup(5),
    proc_kpagecount(5),
    proc_kpageflags(5),
    proc_loadavg(5),
    proc_locks(5),
    proc_malloc(5),
    proc_meminfo(5),
    proc_modules(5),
    proc_mtrr(5),
    proc_partitions(5),
    proc_pci(5),
    proc_pid(5),
    proc_pid_attr(5),
    proc_pid_autogroup(5),
    proc_pid_auxv(5),
    proc_pid_cgroup(5),
    proc_pid_clear_refs(5),
    proc_pid_cmdline(5),
    proc_pid_comm(5),
    proc_pid_coredump_filter(5),
    proc_pid_cpuset(5),
    proc_pid_cwd(5),
    proc_pid_environ(5),
    proc_pid_exe(5),
    proc_pid_fd(5),
    proc_pid_fdinfo(5),
    proc_pid_io(5),
    proc_pid_limits(5),
    proc_pid_map_files(5),
    proc_pid_maps(5),
    proc_pid_mem(5),
    proc_pid_mountinfo(5),
    proc_pid_mounts(5),
    proc_pid_mountstats(5),
    proc_pid_net(5),
    proc_pid_ns(5),
    proc_pid_numa_maps(5),
    proc_pid_oom_score(5),
    proc_pid_oom_score_adj(5),
    proc_pid_pagemap(5),
    proc_pid_personality(5),
    proc_pid_projid_map(5),
    proc_pid_root(5),
    proc_pid_seccomp(5),
    proc_pid_setgroups(5),
    proc_pid_smaps(5),
    proc_pid_stack(5),
    proc_pid_stat(5),
    proc_pid_statm(5),
    proc_pid_status(5),
    proc_pid_syscall(5),
    proc_pid_task(5),
    proc_pid_timers(5),
    proc_pid_timerslack_ns(5),
    proc_pid_uid_map(5),
    proc_pid_wchan(5),
    proc_profile(5),
    proc_scsi(5),
    proc_slabinfo(5),
    proc_stat(5),
    proc_swaps(5),
    proc_sys(5),
    proc_sys_abi(5),
    proc_sys_debug(5),
    proc_sys_dev(5),
    proc_sys_fs(5),
    proc_sys_kernel(5),
    proc_sys_net(5),
    proc_sys_proc(5),
    proc_sysrq-trigger(5),
    proc_sys_sunrpc(5),
    proc_sys_user(5),
    proc_sysvipc(5),
    proc_sys_vm(5),
    proc_tid_children(5),
    proc_timer_list(5),
    proc_timer_stats(5),
    proc_tty(5),
    proc_uptime(5),
    proc_version(5),
    proc_vmstat(5),
    proc_zoneinfo(5),
    sysfs(5),
    systemd.mount(5),
    capabilities(7),
    cgroup_namespaces(7),
    cpuset(7),
    credentials(7),
    epoll(7),
    fanotify(7),
    file-hierarchy(7),
    hier(7),
    inotify(7),
    libc(7),
    mount_namespaces(7),
    namespaces(7),
    netdevice(7),
    network_namespaces(7),
    pid_namespaces(7),
    pkeys(7),
    pthreads(7),
    pty(7),
    signal(7),
    symlink(7),
    user_namespaces(7),
    vdso(7),
    migratepages(8),
    netstat(8),
    numactl(8),
    sysctl(8),
    systemd-coredump(8)
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
