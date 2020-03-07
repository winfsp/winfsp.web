#!/usr/bin/python

import json, re, sys

pygcss = [
    '',     None,                       # Token:
    '',     None,                       # Text:
    'w',    None,                       # Whitespace:
    'esc',  None,                       # Escape:
    'err',  None,                       # Error:
    'x',    None,                       # Other:
    'k',    "keyword",                  # Keyword:
    'kc',   "keyword",                  # Keyword.Constant:
    'kd',   "keyword",                  # Keyword.Declaration:
    'kn',   "keyword",                  # Keyword.Namespace:
    'kp',   "keyword",                  # Keyword.Pseudo:
    'kr',   "keyword",                  # Keyword.Reserved:
    'kt',   "keyword",                  # Keyword.Type:
    'n',    None,                       # Name:
    'na',   None,                       # Name.Attribute:
    'nb',   "variable.language",        # Name.Builtin:
    'bp',   "variable.language",        # Name.Builtin.Pseudo:
    'nc',   "entity",                   # Name.Class:
    'no',   None,                       # Name.Constant:
    'nd',   None,                       # Name.Decorator:
    'ni',   None,                       # Name.Entity:
    'ne',   None,                       # Name.Exception:
    'nf',   "entity",                   # Name.Function:
    'fm',   None,                       # Name.Function.Magic:
    'py',   None,                       # Name.Property:
    'nl',   "constant",                 # Name.Label:
    'nn',   None,                       # Name.Namespace:
    'nx',   None,                       # Name.Other:
    'nt',   None,                       # Name.Tag:
    'nv',   None,                       # Name.Variable:
    'vc',   None,                       # Name.Variable.Class:
    'vg',   None,                       # Name.Variable.Global:
    'vi',   None,                       # Name.Variable.Instance:
    'vm',   None,                       # Name.Variable.Magic:
    'l',    None,                       # Literal:
    'ld',   None,                       # Literal.Date:
    's',    "string",                   # String:
    'sa',   "string",                   # String.Affix:
    'sb',   "string",                   # String.Backtick:
    'sc',   "string",                   # String.Char:
    'dl',   "string",                   # String.Delimiter:
    'sd',   "string",                   # String.Doc:
    's2',   "string",                   # String.Double:
    'se',   "string",                   # String.Escape:
    'sh',   "string",                   # String.Heredoc:
    'si',   "string",                   # String.Interpol:
    'sx',   "string",                   # String.Other:
    'sr',   "string",                   # String.Regex:
    's1',   "string",                   # String.Single:
    'ss',   "string",                   # String.Symbol:
    'm',    "constant",                 # Number:
    'mb',   "constant",                 # Number.Bin:
    'mf',   "constant",                 # Number.Float:
    'mh',   "constant",                 # Number.Hex:
    'mi',   "constant",                 # Number.Integer:
    'il',   "constant",                 # Number.Integer.Long:
    'mo',   "constant",                 # Number.Oct:
    'o',    None,                       # Operator:
    'ow',   None,                       # Operator.Word:
    'p',    None,                       # Punctuation:
    'c',    "comment",                  # Comment:
    'ch',   "comment",                  # Comment.Hashbang:
    'cm',   "comment",                  # Comment.Multiline:
    'cp',   "support",                  # Comment.Preproc:
    'cpf',  "string",                   # Comment.PreprocFile:
    'c1',   "comment",                  # Comment.Single:
    'cs',   "comment",                  # Comment.Special:
    'g',    None,                       # Generic:
    'gd',   None,                       # Generic.Deleted:
    'ge',   None,                       # Generic.Emph:
    'gr',   None,                       # Generic.Error:
    'gh',   None,                       # Generic.Heading:
    'gi',   None,                       # Generic.Inserted:
    'go',   None,                       # Generic.Output:
    'gp',   None,                       # Generic.Prompt:
    'gs',   None,                       # Generic.Strong:
    'gu',   None,                       # Generic.Subheading:
    'gt',   None,                       # Generic.Traceback:
]

def convert_to_css(css, k, v):
    if "fontStyle" == k:
        for p in v.split():
            if "bold" == p:
                css["font-weight"] = p
            elif "italic" == p:
                css["font-style"] = p
            elif "underline" == p:
                css["text-decoration"] = p
    elif "foreground" == k:
        css["color"] = v
    elif "background" == k:
        css["background-color"] = v
    elif "content" == k:
        css[k] = v

theme = {}
for s in json.load(sys.stdin)["settings"]:
    scope = re.split(",\\s*", s["scope"]) if "scope" in s else None
    if scope is None:
        continue
    css = {}
    for k in s["settings"]:
        convert_to_css(css, k, s["settings"][k])
    for c in scope:
        theme[c] = css

for i in range(0, len(pygcss), 2):
    s, c = pygcss[i], pygcss[i + 1]
    if c is None:
        continue
    t = theme[c]
    p = []
    p.append(".highlight .%s,.tok-%s {" % (s, s))
    for k in sorted(t.keys()):
        p.append("%s: %s;" % (k, t[k]))
    p.append("}")
    print " ".join(p)
