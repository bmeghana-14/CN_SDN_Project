"""
Delay Monitor Controller using POX

This controller performs simple packet forwarding and enables
measurement of network delay using ping (RTT).
"""

from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()


class DelayMonitor(object):
    def __init__(self, connection):
        self.connection = connection
        connection.addListeners(self)
        log.info("Switch %s connected", connection)

    def _handle_PacketIn(self, event):
        packet = event.parsed

        if not packet.parsed:
            log.warning("Ignoring incomplete packet")
            return

        # Flood packets (basic forwarding logic)
        msg = of.ofp_packet_out()
        msg.data = event.ofp
        msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
        self.connection.send(msg)


def launch():
    def start_switch(event):
        log.info("Controlling %s" % (event.connection,))
        DelayMonitor(event.connection)

    core.openflow.addListenerByName("ConnectionUp", start_switch)
