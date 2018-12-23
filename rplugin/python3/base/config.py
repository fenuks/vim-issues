from __future__ import annotations
import subprocess
from typing import Optional, List
from pathlib import Path
import json

from .constants import IssuesSoftware, ReviewSoftware, VcsSoftware


class Config:
    config_name = "project.json"
    apis: List[ApiConfig]
    projects: List[ProjectConfig]

    @staticmethod
    def create(cwd: str) -> Config:
        config_path = Config.get_config_path(cwd=Path(cwd))
        config_data = {}
        if config_path != None:
            with config_path.open('r') as fp:
                config_data = json.parse(fp)
        return Config()

    @staticmethod
    def get_config_path(cwd: Path = None) -> Optional[Path]:
        if cwd:
            config_path = cwd / Config.config_name
            if config_path.exists():
                return config_path

        commands = (['git', 'rev-parse', '--show-toplevel'], ['hg', 'root'])
        for vcs, resp in ((command[0], subprocess.run(command, stdout=subprocess.PIPE))
                        for command in commands):
            if resp.returncode == 0:
                return Path(resp.stdout.decode().strip())

        return None


class ApiConfig:
    url: str
    token: Optional[str]
    type_: str

class ProjectConfig:
    pass

class VcsConfig:
    type_: str
    url: str
