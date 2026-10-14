// Validation demo: @assert fails the call, @check only reports the result.
// -> Order: extracted order; quantity must be > 0 (assert), email should contain "@" (check).
// -> ExtractOrder: LLM extracts an Order from free text.

class Order {
  quantity int @assert(positive, {{ this > 0 }})
  email string @check(has_at, {{ "@" in this }})
}

function ExtractOrder(text: string) -> Order {
  client Local
  prompt #"
    Extract the order from the text.

    {{ ctx.output_format }}

    {{ _.role("user") }}
    {{ text }}
  "#
}
