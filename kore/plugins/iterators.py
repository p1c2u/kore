import logging
from pkg_resources import iter_entry_points

from kore.plugins.models import Plugin

log = logging.getLogger(__name__)


class PluginIterator(object):

    def __init__(self, group_name):
        self.group_name = group_name

    def __iter__(self):
        log.debug("Looking for `%s` plugins", self.group_name)
        entry_points = iter_entry_points(group=self.group_name, name=None)
        for entry_point in entry_points:
            yield Plugin(entry_point.name, entry_point.load())
