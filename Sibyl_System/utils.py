import re
from typing import Dict, Tuple


FLAG_REGEX = re.compile(r"-\w+")


def seprate_flags(message: str) -> Tuple[Dict[str, bool], str]:
    flags = FLAG_REGEX.findall(message)
    flags_dict = {flag[1:]: True for flag in flags}
    message = FLAG_REGEX.sub("", message)
    return (flags_dict, message)
