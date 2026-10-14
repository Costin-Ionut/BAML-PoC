// Basic structured extraction of a support ticket.
// -> Priority: LOW / MEDIUM / HIGH.
// -> Ticket: title, priority, tags.
// -> ExtractTicket: LLM extracts a Ticket from free text (reused by most endpoints).
// -> SlowLogin: BAML test, asserts a blocking login issue is HIGH priority.

enum Priority {
  LOW
  MEDIUM
  HIGH
}

class Ticket {
  title string
  priority Priority
  tags string[]
}

function ExtractTicket(text: string) -> Ticket {
  client Local
  prompt #"
    Extract the support ticket from the text.

    {{ ctx.output_format }}

    {{ _.role("user") }}
    {{ text }}
  "#
}

test SlowLogin {
  functions [ExtractTicket]
  args {
    text "Login takes 30 seconds since yesterday and customers cannot work."
  }
  @@assert({{ this.priority == "HIGH" }})
}
