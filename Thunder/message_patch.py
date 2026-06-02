# Patch to fix is_outgoing=True messages being skipped by pytdbot
# This adds MessageText to allow_outgoing_message_types
import pytdbot.client as client_module
from pytdbot import types

# Store original __init__
_original_init = client_module.Client.__init__

def _patched_init(self, *args, **kwargs):
    _original_init(self, *args, **kwargs)
    # Add MessageText to allow_outgoing_message_types
    # This allows incoming command messages to be processed even when is_outgoing=True
    current = self.allow_outgoing_message_types
    if types.MessageText not in current:
        self.allow_outgoing_message_types = current + (types.MessageText,)

# Apply the patch
client_module.Client.__init__ = _patched_init

def apply_message_patch():
    """Entry point for importing this patch."""
    pass  # Patch is applied at module import time