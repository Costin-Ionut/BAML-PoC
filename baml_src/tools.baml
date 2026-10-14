// Tool-calling demo: LLM chooses which "tool" to call and fills its args.
// -> GetWeather: tool with a city.
// -> SendEmail: tool with recipient and body.
// -> PickTool: LLM returns one of the tools for the request.

class GetWeather {
  tool "get_weather"
  city string
}

class SendEmail {
  tool "send_email"
  to string
  body string
}

function PickTool(request: string) -> GetWeather | SendEmail {
  client Local
  prompt #"
    Choose the tool that fulfils the request.

    {{ ctx.output_format }}

    {{ _.role("user") }}
    {{ request }}
  "#
}
