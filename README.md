# stactools-cmip6

<!-- [![PyPI](https://img.shields.io/pypi/v/stactools-cmip6?style=for-the-badge)](https://pypi.org/project/stactools-cmip6/) -->
![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/NASA-IMPACT/stactools-packages-cmip6/continuous-integration.yml?style=for-the-badge)

- Name: cmip6
- Package: `stactools.cmip6`
- Owner: @gadomski
- [Dataset homepage](https://esgf-node.llnl.gov/projects/cmip6/)
- STAC extensions used:
  - TBD
- Extra fields:
  - TBD

<!-- - [stactools-cmip6 on PyPI](https://pypi.org/project/stactools-cmip6/) -->
<!-- - [Browse the example in human-readable form](https://radiantearth.github.io/stac-browser/#/external/raw.githubusercontent.com/stactools-packages/cmip6/main/examples/collection.json) -->
<!-- - [Browse a notebook demonstrating the example item and collection](https://github.com/stactools-packages/cmip6/tree/main/docs/example.ipynb) -->

WIP

## STAC examples

TODO

## Installation

```shell
pip install stactools-cmip6
```

## Command-line usage

TODO

Use `stac cmip6 --help` to see all subcommands and options.

## Contributing

We use [pre-commit](https://pre-commit.com/) to check any changes.
To set up your development environment:

```shell
pip install -e '.[dev]'
pre-commit install
```

To check all files:

```shell
pre-commit run --all-files
```

To run the tests:

```shell
pytest -vv
```

If you've updated the STAC metadata output, update the examples:

```shell
scripts/update-examples
```
