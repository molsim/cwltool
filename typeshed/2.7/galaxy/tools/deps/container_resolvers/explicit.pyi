# Stubs for galaxy.tools.deps.container_resolvers.explicit (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ..container_resolvers import ContainerResolver

class ExplicitContainerResolver(ContainerResolver):
    resolver_type = ...  # type: str
    def resolve(self, enabled_container_types, tool_info): ...
