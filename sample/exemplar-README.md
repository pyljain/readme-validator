## Table of Contents

1. [Kubebuilder](#kubebuilder)
    - [Kubebuilder is also a framework](#kubebuilder-is-also-a-framework)
    - [Installation](#installation)
2. [Getting Started](#getting-started)
3. [Documentation](#documentation)
4. [Resources](#resources)
5. [Motivation](#motivation)
6. [Scope](#scope)
7. [Philosophy](#philosophy)
8. [Techniques](#techniques)
9. [Versioning and Releasing](#versioning-and-releasing)
10. [Troubleshooting](#troubleshooting)
11. [Contributing](#contributing)
12. [Supportability](#supportability)
    - [Apple Silicon](#apple-silicon)
13. [Community Meetings](#community-meetings)
14. [License](#license)

## Kubebuilder

Kubebuilder is a framework for building Kubernetes APIs using [custom resource definitions (CRDs)](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions).

Similar to web development frameworks such as *Ruby on Rails* and *SpringBoot*,
Kubebuilder increases velocity and reduces the complexity managed by
developers for rapidly building and publishing Kubernetes APIs in Go.

### Installation

It is strongly recommended that you use a released version. Release binaries are available on the [releases](https://github.com/kubernetes-sigs/kubebuilder/releases) page.
Follow the [instructions](https://book.kubebuilder.io/quick-start.html#installation) to install Kubebuilder.

## Getting Started

See the [Getting Started](https://book.kubebuilder.io/quick-start.html) documentation.

![Quick Start](docs/gif/kb-demo.v2.0.1.svg)

Also, ensure that you check out the [Deploy Image](https://book.kubebuilder.io/plugins/deploy-image-plugin-v1-alpha.html) 
Plugin. This plugin allows users to scaffold API/Controllers to deploy and manage an 
Operand (image) on the cluster following the guidelines and best practices. It abstracts the 
complexities of achieving this goal while allowing users to customize the generated code.

## Resources

- Kubebuilder Book: [book.kubebuilder.io](https://book.kubebuilder.io)
- GitHub Repo: [kubernetes-sigs/kubebuilder](https://github.com/kubernetes-sigs/kubebuilder)
- Slack channel: [#kubebuilder](https://slack.k8s.io/#kubebuilder)

## Motivation

Building Kubernetes tools and APIs involves making a lot of decisions and writing a lot of boilerplate.
Kubebuilder attempts to facilitate the following developer workflow for building APIs

1. Create a new project directory
2. Create one or more resource APIs as CRDs and then add fields to the resources
3. Implement reconcile loops in controllers and watch additional resources
4. Test by running against a cluster (self-installs CRDs and starts controllers automatically)
5. Update bootstrapped integration tests to test new fields and business logic
6. Build and publish a container from the provided Dockerfile

## Philosophy

See [DESIGN.md](DESIGN.md) for the guiding principles of the various Kubebuilder projects.

TL;DR:

Provide clean library abstractions with clear and well exampled godocs.

- Prefer using go *interfaces* and *libraries* over relying on *code generation*
- Prefer using *code generation* over *1 time init* of stubs
- Prefer *1 time init* of stubs over forked and modified boilerplate
- Never fork and modify boilerplate

## Versioning and Releasing

See [VERSIONING.md](VERSIONING.md).

## Troubleshooting

- ### Bugs and Feature Requests:
  If you have what looks like a bug, or you would like to make a feature request, please use the [Github issue tracking system.](https://github.com/kubernetes-sigs/kubebuilder/issues)

## Contributing

Contributions are greatly appreciated. The maintainers actively manage the issues list, and try to highlight issues suitable for newcomers.
The project follows the typical GitHub pull request model. See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.
Before starting any work, please either comment on an existing issue, or file a new one.

## License

[MIT License](https://github.com/temporalio/temporal/blob/master/LICENSE)

