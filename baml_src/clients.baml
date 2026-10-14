// LLM client config shared by all BAML functions.
// -> Twice: retry policy, up to 2 retries with exponential backoff.
// -> Local: OpenAI-compatible client; HOST, API_KEY, MODEL come from env.

retry_policy Twice {
  max_retries 2
  strategy {
    type exponential_backoff
  }
}

client<llm> Local {
  provider "openai-generic"
  retry_policy Twice
  options {
    base_url env.HOST
    api_key env.API_KEY
    model env.MODEL
  }
}
