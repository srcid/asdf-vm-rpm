# ASDF-VM-RPM

This repo is used to packing [ASDF](https://github.com/asdf-vm/asdf) in RPM format and make it available for RHEL-like distros via COPR.

It does not compile ASDF from source, It just takes the pre-compiled binaries from ASDF repo and pack it in RPM format.

## Using COPR repo

```shell
dnf copr enable srcid/asdf
```

```shell
dnf install asdf
```
