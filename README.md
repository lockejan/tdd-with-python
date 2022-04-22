# TDD Practice with Python and more

This projects' main purpose was to learn more about Django, Python, TDD and CI/CD.
The majority of this repository is based on Harry Percival's TDD book, which I've read.

The book is a bit dated now, but still contains a lot of relevant information in my opinion.
I changed and extended some parts of the project code where it made sense in my opinion.

A few of such occassions as well as things the author considered but didn't implement in the example code are:
- gitattributes to exclude versioned javascript libraries from languages calculation
- use nix to provide reproducible dev environments
- split up dev and live requirements in multiple files
- local provisioning of the project with vagrant and ansible
- using CDNs instead of relying on checked in source of used frontend libraries
- using yapf to achieve a consistent code style
- use type hints as proposed in [PEP 484](https://peps.python.org/pep-0484/)
- measuring code coverage with coverage.py
- update project to minimal active LTS (2.2)

<!-- https://github.com/hjwp/book-example.git -->
<!-- creative commons license??? -->

## Deployment

See [provisioning_notes.md](./deploy_tools/provisioning_notes.md) for more infos about deploying stuff.
