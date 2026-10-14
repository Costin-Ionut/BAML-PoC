// Dynamic enum demo: categories are added at runtime via TypeBuilder.
// -> Category: enum with a single OTHER placeholder, marked @@dynamic.
// -> Classify: LLM picks one Category for the text.

enum Category {
  OTHER
  @@dynamic
}

function Classify(text: string) -> Category {
  client Local
  prompt #"
    Classify the text.

    {{ ctx.output_format }}

    {{ _.role("user") }}
    {{ text }}
  "#
}
