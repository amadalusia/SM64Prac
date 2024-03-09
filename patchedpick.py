from typing import Optional, Sequence
import pick
import curses
import os
import sys

def _wrapper(func):
    # Using workaround to address windows-curses bug on Python 3.12
    # More info: https://github.com/zephyrproject-rtos/windows-curses/issues/50
    if os.name == 'nt' and sys.version_info[0] == 3 and sys.version_info[1] >= 12:
        stdscr = None
        try:
            import _curses
            # This crashes on Python 3.12.
            # setupterm(term=_os.environ.get("TERM", "unknown"),
            #           fd=_sys.__stdout__.fileno())
            stdscr = _curses.initscr()
            for key, value in _curses.__dict__.items():
                if key[0:4] == 'ACS_' or key in ('LINES', 'COLS'):
                    setattr(curses, key, value)

            curses.noecho()
            curses.cbreak()

            if stdscr is not None:
                stdscr.keypad(True)
                return func(stdscr)
        finally:
            if stdscr is not None:
                stdscr.keypad(False)
            curses.nocbreak()
            curses.echo()
            curses.endwin()
    else:
        curses.wrapper(func)

class PatchedPicker(pick.Picker):
    def config_curses(self) -> None:
        try:
            # use the default colors of the terminal
            curses.use_default_colors()
            # hide the cursor
            curses.curs_set(0)
        except:
            # Curses failed to initialize color support, eg. when TERM=vt100
            if os.name == 'nt' and sys.version_info[0] == 3 and sys.version_info[1] >= 12:
                import _curses
                # This crashes on Python 3.12.
                    # setupterm(term=_os.environ.get("TERM", "unknown"),
                    #           fd=_sys.__stdout__.fileno())
                _curses.initscr()
                for key, value in _curses.__dict__.items():
                    if key[0:4] == 'ACS_' or key in ('LINES', 'COLS'):
                        setattr(curses, key, value)
            else:
                curses.initscr()
    def start(self):
        if self.screen:
            # Given an existing screen
            # don't make any lasting changes
            last_cur = curses.curs_set(0)
            ret = self.run_loop(self.screen)
            if last_cur:
                curses.curs_set(last_cur)
            return ret
        return _wrapper(self._start)


def pick(
    options: Sequence[pick.OPTION_T],
    title: Optional[str] = None,
    indicator: str = "*",
    default_index: int = 0,
    multiselect: bool = False,
    min_selection_count: int = 0,
    screen: Optional["curses._CursesWindow"] = None,
):
    picker: PatchedPicker = PatchedPicker(
        options,
        title,
        indicator,
        default_index,
        multiselect,
        min_selection_count,
        screen,
    )
    return picker.start()
