#!/usr/bin/env python
"""Provides A GUI for specific Machine Learning Use-cases.

Aether Project.
"""
__author__ = "Eric Petersen @Ruckusist"
__copyright__ = "Copyright 2017, The Alpha Griffin Project"
__credits__ = ["Eric Petersen", "Shawn Wilson", "@alphagriffin"]
__license__ = "***"
__version__ = "0.0.1"
__maintainer__ = "Eric Petersen"
__email__ = "ruckusist@alphagriffin.com"
__status__ = "Prototype"

import os, sys, time
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '5'
from datetime import datetime
from time import sleep
from threading import Thread
import ag.logging as log
import ag.Aether.server.flask_server as flask_talker
import ag.Aether.database.database_interface as db
from ag.Aether.frontend.curses_frontend import Window as Curses
log.set(log.WARN)


class Options(object):
    """DEPRICATED."""

    def __init__(self):
        """Yeah, no."""
        self.host = "localhost"
        self.remote_host = 'agserver'
        self.remote_pass = 'dummypass'
        self.chat_port = 12345
        self.tf_port = 2222
        self.redis_port = 6379


class Aether(object):
    """AG Aether Project Runtime Class.

    This class should handle display and functionality
    of many different type of frontends to acomplish the
    same goal.
    """

    def __init__(self, options):
        """Define Menu stucture, for plugins in use."""
        self.running = True
        self.options = options
        self.errors = []
        self.working_panels = []
        self.cur = 0
        self.menu = ["Database",
                     "Web_Server",
                     "Error_Log"]

    @property
    def is_running(self):
        """Part of the polling mechinizm."""
        return self.running

    def start_frontend(self, frame='curses'):
        """This will allow a user to define their experience."""
        msg = "AlphaGriffin Aether Project | "
        msg += "Start Time: {} | ".format(datetime.now().isoformat(timespec='minutes'))
        msg += "PID: {}".format(os.getpid())
        if frame is 'curses':
            self.frontend = Curses()
            self.frontend.main_screen()
            msg_len = self.frontend.screen_w - 3
            if len(msg) > msg_len:
                msg = msg[:msg_len]
            self.frontend.header[0].addstr(1, 1, msg)

    def start_backend(self): pass

    def Web_Server(self):
        """A Flask webserver. For a better gui."""
        try:
            self.webserver = flask_talker.FlaskChat()
            Thread(target=self.webserver.run).start()
            self.working_panels[self.cur][0].addstr(5, 5, "Service Running: {}".format(self.menu[self.cur]))
        except:
            msg = "Service Failed: {}".format(self.menu[self.cur])
            self.working_panels[self.cur][0].addstr(5, 5, msg)
            # self.working_panels[self.cur][0].addstr(5, 5, sys.exc_info()[0])
        pass

    def Error_Log(self):
        """The program activity function log.

        This def is an example of the notion of 'services'
        operation within the enviroment. later will probably
        be called plugins. This will be permenent but stand
        as a plugin example.
        """
        msg = "Service: {} : Testing".format(self.menu[self.cur])
        msg += u"\u2588"
        self.working_panels[self.cur][0].addstr(1, 3, msg)
        y, x = self.working_panels[self.cur][0].getmaxyx()
        max_print = y-4
        index = 3
        # this is TOP DOWN
        #for count, j in enumerate(self.errors[-max_print:]):
        #    msg = "E:{0:3d} | {1}".format(len(self.errors) - count, j)
        #    self.working_panels[self.cur][0].addstr(index, 3, msg[:x-4])
        #    index += 1
        # this is Bottom UP
        for count, j in reversed(list(enumerate(self.errors[-max_print:]))):
            msg = "E:{0:3d} | {1}".format(len(self.errors) - count, j)
            self.working_panels[self.cur][0].addstr(index, 3, msg[:x-4])
            index += 1
        pass

    def Database(self):
        """Add redis support for long term memory storage."""
        msg = "Starting Service: {}".format(self.menu[self.cur])
        self.working_panels[self.cur][0].addstr(1, 3, msg)
        h = self.options.remote_host
        p = self.options.redis_port
        self.database = db.Database(h, p, db=0)
        self.working_panels[self.cur][0].addstr(5, 5, msg)
        msg = "Service Running: {}   ".format(self.menu[self.cur])
        self.working_panels[self.cur][0].addstr(1, 3, msg)
        return True

    def main_loop(self):
        """A polling mechinizm."""
        self.frontend.refresh()
        keypress = 0
        try:
            keypress = self.frontend.get_input()
        except:
            keypress = 0
            pass
        try:
            if keypress > 0:
                # self.errors.append(("keypress: ", keypress))
                self.decider(keypress)
        except:
            self.errors.append(("cmd", keypress))
            self.string_decider(keypress)
        ###
        # TODO: do other stuff
        ###

    def string_decider(self, string):
        """Not imelemented."""
        if 'stop' in string:
            self.working_panels[self.cur][0].addstr(5, 5, "Stoping Service: {}".format(self.menu[self.cur]))
        else:
            self.working_panels[self.cur][0].addstr(1, 1, string)
        self.selector()

    def decider(self, keypress):
        """Manage keypress and open type field input parsing."""
        # log.info("got this {} type {}".format(keypress, type(keypress)))
        # main decider functionality!
        try:
            if keypress is 113 or keypress is 1:
                command_text = """Exit"""
                self.errors.append(command_text)
                self.running = False
                pass
            elif keypress == 10:
                enter = self.menu[self.cur]
                command_text = """Enter"""
                self.errors.append(command_text)
                #self.working_panels[self.cur][0].addstr(4,5,"Attempting Service: {}".format(self.menu[self.cur]))
                # FIXME: DONT USE EVAL... WOW.!
                eval("self.{}()".format(enter))
                pass
            elif keypress == 9:
                command_text = """Tab"""
                if self.frontend.screen_mode:
                    self.frontend.screen_mode = False
                self.selector()
                pass
            elif keypress == 258:
                command_text = """scroll_up"""
                self.working_panels[self.cur][0].scroll(-1)
                self.frontend
                pass
            elif keypress == 259:
                command_text = """scroll_down"""
                self.errors.append(command_text)
                self.working_panels[self.cur][0].scroll(1)
                pass
            elif keypress == 338:
                command_text = """Page Down"""
                self.errors.append(command_text)
                if self.cur < len(self.menu) - 1:
                    self.cur += 1
                else:
                    self.cur = 0
                self.selector()
                pass
            elif keypress == 339:
                command_text = """Page Up"""
                self.errors.append(command_text)
                if self.cur > 0:
                    self.cur -= 1
                else:
                    self.cur = len(self.menu)-1
                self.selector()
                pass
            else:
                self.errors.append("""Unknown {}""".format(keypress))
                # log.error('Unknown Connand Function')
                pass
        finally:
            pass

    def selector(self):
        """Menu Selection functions."""
        self.frontend.redraw_window(self.frontend.winleft)
        for index, item in enumerate(self.menu):
            if self.cur == index:
                self.frontend.winleft[0].addstr(index+1, 1, item, self.frontend.color_rw)
            else:
                self.frontend.winleft[0].addstr(index+1, 1, item, self.frontend.color_cb)
        self.working_panels[self.cur][1].top()
        if self.frontend.screen_mode:
            options = ["|q| to quit   |Tab| switch Mode   |enter| to start service", "|pgUp| change menu |pgDn| change menu"]
            self.frontend.redraw_window(self.frontend.debug)
            self.frontend.debug[0].addstr(1, 1, options[0], self.frontend.color_gb)
            self.frontend.debug[0].addstr(2, 1, options[1], self.frontend.color_gb)
        else:
            options = ["|q| to quit   |Tab| switch Mode", "|enter| submit   |'stop'| to kill service"]
            self.frontend.redraw_window(self.frontend.debug)
            self.frontend.debug[0].addstr(1, 1, options[0], self.frontend.color_gb)
            self.frontend.debug[0].addstr(2, 1, options[1], self.frontend.color_gb)

    def working_panel(self):
        """Create a panel for all subsystems."""
        # this is only run 1 time during setup
        for item in self.menu:
            self.working_panels.append(
                self.frontend.make_panel(
                    self.frontend.winright_dims,
                    item,
                    True))

    def main(self):
        """System Operation Main Runtime."""
        self.start_frontend()
        self.start_backend()
        self.working_panel()
        self.selector()
        while self.is_running:
            time.sleep(.05)
            self.main_loop()
        self.exit_safely()

    def exit_safely(self, msg=None):
        """Return proper command control to the shell."""
        try:
            self.frontend.end_safely()
            sys.exit("{}\nSupported by Alphagriffin.com".format(
                msg))
        except Exception as e:
            sys.exit("Supported by Alphagriffin.com\n{}".format(e))


def main():
    """Method is only called when run via CLI."""
    options = Options()
    # TODO: this is still missing a command line arg parser!
    app = Aether(options)
    try:
        app.main()
        os.system('clear')
    except KeyboardInterrupt:
        app.exit_safely()
        os.system('clear')
        pass


if __name__ == '__main__':
    try:
        main()
    except:
        log.error("and thats okay too.")
