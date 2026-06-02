import os

from pytdbot import Client

from Thunder.vars import Var

# Import message patch to fix outgoing message filtering
from Thunder.message_patch import apply_message_patch
apply_message_patch()

_ENCRYPTION_KEY = b"thunder_tdlib_encryption_key_32b"

StreamBot = Client(
    token=Var.BOT_TOKEN,
    api_id=Var.API_ID,
    api_hash=Var.API_HASH,
    files_directory=os.path.join("tdlib_data", "primary"),
    database_encryption_key=_ENCRYPTION_KEY,
    workers=Var.WORKERS,
    td_verbosity=0,
    default_parse_mode="markdown",  # Enable Markdown parsing by default
)

multi_clients = {}
work_loads = {}
