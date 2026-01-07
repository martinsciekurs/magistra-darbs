(method
  name: (identifier) @func.name
  parameters: (method_parameters)? @func.args
) @func.def

(call
  method: (identifier) @func.call
)

(call
  method: (call
    method: (identifier) @func.call
  )
)