; === IMPORTS ===

; import foo
(import_statement
  name: (dotted_name) @import.module)

; import foo as bar
(import_statement
  name: (aliased_import
    name: (dotted_name) @import.module
    alias: (identifier) @import.alias))

; from foo import bar
(import_from_statement
  module_name: (dotted_name) @import.from
  name: (dotted_name) @import.name)

; from foo import bar as baz
(import_from_statement
  module_name: (dotted_name) @import.from
  name: (aliased_import
    name: (dotted_name) @import.name
    alias: (identifier) @import.alias))

; === FUNCTIONS ===

(function_definition
  name: (identifier) @func.name
  body: (block . (expression_statement (string) @func.doc)?)
) @func.def

; Direct function calls: func()
(call
  function: (identifier) @func.call)

; Method/attribute calls: obj.method() - capture full qualified name
(call
  function: (attribute) @func.call.qualified)