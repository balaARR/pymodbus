"""Transport implementation for TCP sync."""
from .transport_base import Transport, TransportCallbacks


class SERIALtransport(Transport):
    """Modbus tcp transport layer."""

    def __init__(self,
                 is_server: bool = False,
                 callbacks: TransportCallbacks = None) -> None:
        """Initialize interface."""
        super().__init__(is_server, callbacks)

    def setup(self) -> None:
        """Set parameters for implementation class."""

    async def async_server_start(self) -> None:
        """Start server and accept client connections."""
        await super().async_server_start()

    async def async_client_connect(self) -> None:
        """Connect to server."""
        await super().async_server_start()

    async def async_send(self, data: bytes) -> None:
        """Send data to client/server."""
        await super().async_send(data)

    async def async_disconnect(self) -> None:
        """Disconnect from client/server."""
        await super().async_disconnect()
