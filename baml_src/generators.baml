// Codegen config: generates the async Pydantic client into ../baml_client.
// -> target: Python/Pydantic generator, pinned to the installed BAML version.

generator target {
  output_type "python/pydantic"
  output_dir "../"
  version "0.226.2"
  default_client_mode "async"
}
