# Notes : Dataclass signature rendering issue

- https://github.com/sphinx-doc/sphinx/issues/14532 
- https://docs.python.org/3/library/stdtypes.html#types-genericalias


## Where does the warning comes from?

Based on the log messages the warning seems to appear after the `writing output`

```
...
copying static files: done
copying extra files... 
copying extra files: done
copying assets: done
writing output... [100%] index
<unknown>:1: WARNING: py:class reference target not found: dict[str [ref.class]
generating indices... genindex py-modindex done
writing additional pages... search done
dumping search index in English (code: en)... done
dumping object inventory... done
build succeeded, 2 warnings.

The HTML pages are in build/html.
```

The warning `py:class reference target not found: dict[str` is not generated while parsing. It is emitted during the reference resolution phase.

```
writing output
    ↓
ReferenceResolver._resolve_pending_xref()
    ↓
emit("missing-reference")
    ↓
Python domain's builtin_resolver
    ↓
warning
```

---

# Debugging strategies/tools

- `make html SPHINXOPTS="-W -T -vvv"`
    - -W : treat warnings as errors
    - T : show full Python traceback for exceptions
    - -vvv : maximum verbosity (shows events, extensions, builders, etc.)

- tried finding "missing-reference" in the output of the above command:

```
writing output... [ 75%] generated/dc_sphinx.dc
[app] emitting event: 'missing-reference'(<sphinx.environment.BuildEnvironment object at 0x10c5a2f90>, <pending_xref: <#text: 'dict[str'>>, <#text: 'dict[str'>)
[app] emitting event: 'warn-missing-reference'(<sphinx.domains.python.PythonDomain object at 0x10c69d2b0>, <pending_xref: <#text: 'dict[str'>>)
[app] emitting event: 'missing-reference'(<sphinx.environment.BuildEnvironment object at 0x10c5a2f90>, <pending_xref: <literal...>>, <literal: <#text: 'object'>>)
[app] emitting event: 'doctree-resolved'(<document: <section "dc_sphinx.dc"...>>, 'generated/dc_sphinx.dc')
[app] emitting event: 'html-page-context'('generated/dc_sphinx.dc', 'page.html', {'embedded': False, 'project': 'dc-sphinx', 'release': 'v0.1.0', 'version': '', 'last_updated': None, 'copyright': '2026, ...
...
```

- experimenting and adding `breakpoint()` at the start of different functions (_resolve_pending_xref(), restify(), stringify_annotation(), _parse_arglist(), _pseudo_parse_arglist(), _parse_annotation(), handle_signature(), etc.). Following are some insightful logs:

```
> /Desktop/sphinx/sphinx/transforms/post_transforms/__init__.py(127)_resolve_pending_xref()
-> breakpoint()
(Pdb) node["reftarget"]
'dict[str'
(Pdb) node.astext()
'dict[str'
(Pdb) type(node.parent)
<class 'sphinx.addnodes.desc_sig_name'>
(Pdb) node.parent
<desc_sig_name: <pending_xref...>>
(Pdb) node.parent.pformat()
'<desc_sig_name classes="n">\n    <pending_xref py:class="True" py:module="dc_sphinx.dc" refdoc="generated/dc_sphinx.dc" refdomain="py" refspecific="False" reftarget="dict[str" reftype="class">\n        dict[str\n'
(Pdb) 
```

from above, conclusion --> link is already broken by the time it reaches _resolve_pending_xref.

- backtracking and adding `breakpoint()` into various other functions in the pipeline, finally found where the origin of the issue was:

```
> /Desktop/sphinx/sphinx/domains/python/_annotations.py(556)_pseudo_parse_arglist()
-> breakpoint()
(Pdb) signode
<desc_signature: <desc_annotation...><desc_addname...><desc_name...>>
(Pdb) type(signode)
<class 'sphinx.addnodes.desc_signature'>
(Pdb) arglist
'my_dict: dict[str, str] = <factory>'
(Pdb) arglist.split(',')
['my_dict: dict[str', ' str] = <factory>']
(Pdb) n

...
...

(Pdb) n
> /Desktop/sphinx/sphinx/domains/python/_annotations.py(584)_pseudo_parse_arglist()
-> node = addnodes.desc_parameter()
(Pdb) argument
'my_dict: dict[str'
(Pdb) default_value
''
(Pdb) param_name
'my_dict'
(Pdb) annotation
' dict[str'
```

--- 

## pdb commands

- `n` -> Next line
- `s` -> Step into function
- `r` -> Return from current function
- `c` -> Continue
- `<variable>` -> Print variable's value
- `node["reftarget"]`: Pending xref
- `node.astext()`: render node as text
- `node.parent` : node's parent
- `node.parent.pformat()`: to get full tree

---

## Overall flow

```
field(default_factory=dict)
        ↓
inspect.signature()
        ↓
dict[str, str] = <factory>
        ↓
_parse_arglist()
        ↓
signature_from_str()
        ↓
SyntaxError
        ↓
fallback
        ↓
_pseudo_parse_arglist()
        ↓
split(',')
        ↓
dict[str
        ↓
_parse_annotation()
        ↓
pending_xref(reftarget="dict[str")
        ↓
ReferenceResolver
        ↓
WARNING
```

---

Also, I took inspiration from the `_parse_balanced_token_seq(self, end: list[str]) -> str` (issue: doesn't handle string literals and similar type hints) in sphinx/util/cfamily.py for creating the proposed balanced parser for this issue (see in issue comments for more).

---
