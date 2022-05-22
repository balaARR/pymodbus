#!/usr/bin/env python3
"""Test transport module"""
import pymodbus.transport as t_tcp


def test_transport():
    """Test transport."""

    my_obj = t_tcp.TCPtransport(False, None)
    my_obj.setup()
