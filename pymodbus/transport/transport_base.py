"""Transport level.

This async module is an abstraction of different transport types:
- TCP
- TCP/TLS
- UDP
- Serial
- Custom
And the protocol layer, for servers by calling startServer(),
and clients by calling accept()

The module transport bytes (the "how", where protocol does the "what").

Callbacks to handle the data exchange.

For future extensions it is possible to use a custom transport class.
"""
from __future__ import annotations
import abc


class TransportCallbacks(metaclass=abc.ABCMeta):
    """Base class for callbacks."""

    def cb_connection_made(self, transport: Transport) -> None:
        """Call when a new connection is establisehd."""

    def cb_data_received(self, data: bytes) -> None:
        """Call when data is received."""

    def cb_data_sent(self, exc: Exception = None) -> None:
        """Call when data have been sent."""

    def cb_connection_lost(self, exc: Exception = None) -> None:
        """Call when connection is lost (disconnect)."""


class Transport(metaclass=abc.ABCMeta):
    """Modbus transport layer interface class."""

    @abc.abstractmethod
    def __init__(self,
                 is_server: bool,
                 callbacks: TransportCallbacks) -> None:
        """Initialize interface."""
        self._is_server = is_server
        self._cbs = callbacks

    @abc.abstractmethod
    def setup(self) -> None:
        """Set parameters for implementation class."""

    @abc.abstractmethod
    async def async_server_start(self) -> None:
        """Start server and accept client connections."""

    @abc.abstractmethod
    async def async_client_connect(self) -> None:
        """Connect to server."""

    @abc.abstractmethod
    async def async_send(self, data: bytes) -> None:
        """Send data to client/server."""

    @abc.abstractmethod
    async def async_disconnect(self) -> None:
        """Disconnect from client/server."""


# --------------------------------------------------------------------------- #
# Exported symbols
# --------------------------------------------------------------------------- #

__all__ = ["Transport", "TransportCallbacks"]
