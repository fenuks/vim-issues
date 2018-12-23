import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

import neovim

from base.config import Config
from providers.gitlab import GitlabProject


@neovim.plugin
class VimIssues:
    def __init__(self, nvim: neovim.Nvim) -> None:
        self.nvim = nvim
        self.config = Config.create(nvim.funcs.cwd())

    @neovim.function("ReloadConfig", sync=True)
    def reload(self, args):
        Config.create(self.nvim.funcs.cwd())
        return 'some string'

    # @neovim.command('Issues', range='', nargs='*')
    # def issues(self, args, range_):
    #     issues = self.project.get_issues(8, 2)
    #     formatted = self.project.format_issues(issues)
    #     self.nvim.current.buffer[:] = formatted
