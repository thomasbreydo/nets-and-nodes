'''pynetworks
==========

A Python package that provides structure for networks of interconnected nodes
using the DOT language for representation.
'''

from .networks import Connection
from .networks import Network
from .networks import Node
from .networks import generate_network
from .dot import dotgraph
from .dot import escape_dot_id
from .pathfinding import Path
from .pathfinding import memoize
from .pathfinding import path_exists
from .pathfinding import shortest_path
from .pathfinding import shortest_path_through_network


__version__ = "0.5.1"

__all__ = ['Connection',
           'Network',
           'Node',
           'Path',
           'dotgraph',
           'escape_dot_id',
           'generate_network',
           'memoize',
           'path_exists',
           'shortest_path',
           'shortest_path_through_network',
           ]
