print("blueMagic.py called")



print("start loading packages in magic.py")
import argparse
import logging
import os
import re
import json
from typing import Any, Optional, Union  # noqa
from openai_api import openAI as oA
import dotenv
from IPython.core.error import UsageError
from IPython.core.interactiveshell import InteractiveShell
from IPython.core.magic import (  # type: ignore
    Magics,
    line_cell_magic,
    line_magic,
    magics_class,
)
from IPython.core.magic_arguments import (  # type: ignore
    argument,
    magic_arguments,
    parse_argstring,
)
from traitlets import Bool, Dict, Instance, Unicode, default, observe  # noqa

print("end  loading packages in magic.py")


logger = logging.getLogger(__name__)

_DEFAULT_PROGRAM_NAME = "_default"
_DEFAULT_HISTORY_PROGRAM_NAME = "_default_history"
_DEFAULT_CHATONLY_PROGRAM_NAME = "_default_chatonly"


@magics_class
class blueMagic(Magics):
    def get_model():
        print("get model start")
        model = ""
        return model

    def execute_chat():
        print("get execute_chat start")
        model = get_model()
        res = ""
        return res
    def pp_res(self,ip):
        ip = str(ip)
       # ip_json = json.loads(ip)
        return ip

    @line_cell_magic
    def chat(self, line, cell=None):
        print(" def chat start")
        print("line is "+str(line))
        args = line
            #parse_argstring(self.chat, line)

        print("args is "+str(args))
        if cell is None:
            return
        current_message = cell

        try:
            print("current message is " + str(current_message))
        except:
            print("error in current_message")
        oA_obj = oA()
        program_out = oA_obj.get_res(current_message)
        program_out = self.pp_res(program_out)
            #self.execute_chat(current_message, args, self.shell)
        print("program_out is " + str(program_out))
        execution_id = self.shell.execution_count
        program_out = f"# Assistant Code for Cell [{execution_id}]:\n" + program_out
        self.shell.set_next_input(program_out)
        print("def chat end")

def load_ipython_extension(ipython):
    """
    Any module file that define a function named `load_ipython_extension`
    can be loaded via `%load_ext module.path` or be configured to be
    autoloaded by IPython at startup time.
    """
    ipython.register_magics(blueMagic)



























