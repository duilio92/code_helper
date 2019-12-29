
from IPython.core.magic import Magics, magics_class, line_magic
import os
@magics_class
class CodeHelperMagics(Magics):
    # dont need an init atm
    # def __init__(self, *a, **kw):
    #    super(CodeHelperMagics, self).__init__(*a, **kw)
    def _get_penultimate_session_id(self, ipython):
        """Get the penultimate session id using the history manager."""
        max1, max2 = 0, 0
        for x in ipython.history_manager.get_tail(n=100):
            if x[0] > max1:
                alt = max1
                max1 = x[0]
                max2 = alt
            elif x[0] > max2:
                max2 = x[0]
        #print("max1 is:{} and max2 is:{} ".format(max1, max2))
        return max2

    def _get_history_for_id(self, ipython, id):
        #import pdb; pdb.set_trace()
        """Get the history commands for the given id. """
        input_lines = []
        #print(id)
        for x in ipython.history_manager.get_tail(n=100):
            #print(x)
            if x[0] == id:
                input_lines.append(x[2])
        if input_lines:
            return input_lines

    @line_magic
    def last_history(self, parameter_s=''):
        # add functionality for -1 current behavior, -2 one before -3 another before.. up to 10?
        # create more commands after('line of code')
        # before('line of code')
        # no erros option(parameter)
        # current_history(with no errors option)
        ip = self.shell.get_ipython()
        penultimate_session_id = self._get_penultimate_session_id(ip)
        session_prefix = str(penultimate_session_id)+('/')
        hist = self._get_history_for_id(ip, penultimate_session_id)
        if hist:
            for x in hist:
                print(x)  # print(x[0])
        else:
            print("No last history was found for your session.")


def load_ipython_extension(ipython):
    # The `ipython` argument is the currently active `InteractiveShell`
    # instance, which can be used in any way. This allows you to register
    # new magics or aliases, for example.
    code_helper = CodeHelperMagics(ipython)
    ipython.register_magics(code_helper)
    print("Code Helper says: Hello")
    # this only says the datetime of last session
    # IPython.core.history.HistoryAccessor(profile='default') 
    # from IPython.core.history import HistoryAccessor
    # dir(HistoryAccessor)
    # HistoryAccesor(profile='default')
    # HistoryAccessor(profile='default')
    # ha = HistoryAccessor(profile='default')
    # history
    # hist
    # %history
    # ha
    # dir(ha)
    # ha.get_tail()
    # ha.get_session_info()
    # ha.get_session_info(100)
    # ha.get_session_info(1)
    # print(ha.get_session_info(1))
    # ha.get_last_session_id()
    # print(ha.get_session_info(151))


def unload_ipython_extension(ipython):
    # If you want your extension to be unloadable, put that logic here.
    print("Code Helper says: Goodbye")



#important read
# autoreload example:
# ipython/IPython/extensions/autoreload.py
# store magic example
#ipython/IPython/extensions/storemagic.py
# custom magic.rst
#ipython/docs/source/config/custommagics.rst

#ALSO READ THIS -->

#     . _events:
# .. _callbacks:

# ==============
# IPython Events
# ==============

# Extension code can register callbacks functions which will be called on specific
# events within the IPython code. You can see the current list of available
# callbacks, and the parameters that will be passed with each, in the callback
# prototype functions defined in :mod:`IPython.core.events`.

# To register callbacks, use :meth:`IPython.core.events.EventManager.register`.
# For example::

#     class VarWatcher(object):
#         def __init__(self, ip):
#             self.shell = ip
#             self.last_x = None
        
#         def pre_execute(self):
#             self.last_x = self.shell.user_ns.get('x', None)
        
#         def pre_run_cell(self, info):
#             print('Cell code: "%s"' % info.raw_cell)
        
#         def post_execute(self):
#             if self.shell.user_ns.get('x', None) != self.last_x:
#                 print("x changed!")
        
#         def post_run_cell(self, result):
#             print('Cell code: "%s"' % result.info.raw_cell)
#             if result.error_before_exec:
#                 print('Error before execution: %s' % result.error_before_exec)
        
#     def load_ipython_extension(ip):
#         vw = VarWatcher(ip)
#         ip.events.register('pre_execute', vw.pre_execute)
#         ip.events.register('pre_run_cell', vw.pre_run_cell)
#         ip.events.register('post_execute', vw.post_execute)
#         ip.events.register('post_run_cell', vw.post_run_cell)


# Events
# ======

# These are the events IPython will emit. Callbacks will be passed no arguments, unless otherwise specified.

# shell_initialized
# -----------------

# .. code-block:: python

#     def shell_initialized(ipython):
#         ...

# This event is triggered only once, at the end of setting up IPython.
# Extensions registered to load by default as part of configuration can use this to execute code to finalize setup.
# Callbacks will be passed the InteractiveShell instance.

# pre_run_cell
# ------------

# ``pre_run_cell`` fires prior to interactive execution (e.g. a cell in a notebook).
# It can be used to note the state prior to execution, and keep track of changes.
# An object containing information used for the code execution is provided as an argument.

# pre_execute
# -----------

# ``pre_execute`` is like ``pre_run_cell``, but is triggered prior to *any* execution.
# Sometimes code can be executed by libraries, etc. which
# skipping the history/display mechanisms, in which cases ``pre_run_cell`` will not fire.

# post_run_cell
# -------------

# ``post_run_cell`` runs after interactive execution (e.g. a cell in a notebook).
# It can be used to cleanup or notify or perform operations on any side effects produced during execution.
# For instance, the inline matplotlib backend uses this event to display any figures created but not explicitly displayed during the course of the cell.
# The object which will be returned as the execution result is provided as an
# argument.

# post_execute
# ------------

# The same as ``pre_execute``, ``post_execute`` is like ``post_run_cell``,
# but fires for *all* executions, not just interactive ones.


# .. seealso::

#    Module :mod:`IPython.core.hooks`
#      The older 'hooks' system allows end users to customise some parts of
#      IPython's behaviour.
   
#    :doc:`inputtransforms`
#      By registering input transformers that don't change code, you can monitor
#      what is being executed.

