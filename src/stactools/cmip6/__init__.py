import stactools.core
from stactools.cli.registry import Registry
from stactools.cmip6.stac import create_collection, create_item

__all__ = ["create_collection", "create_item"]

stactools.core.use_fsspec()


def register_plugin(registry: Registry) -> None:
    from stactools.cmip6 import commands

    registry.register_subcommand(commands.create_cmip6_command)
