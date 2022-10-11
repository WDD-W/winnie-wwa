import requests
import json
addr = ["8KjSqLVgWgSyjV3qntMjtRtMCcmQWbMYwU",
 "8XpzQTfEgHwRJzffb6FQh9QnCEGFCF3stV",
 "8VzjC3wyqswwvfPUAYzxciUaBin2H4T3Hi", 
 "8Sca59VgqEqg2AJK5PfrGg6TpYRwd5RGMo",
 "8GqWvQTyUBWXTP38y5peFse3eBcbMKkQiM",
 "8a5gjXTZCZzUFD8PwZNTA6FeRZuuDLju2J", 
 "8SZs5fKC3tDxNQYmnP4fRzDCEkQmG3BmFg", 
 "8VYGn7GQjWPpSPu91yEEr2m6tnPLwT6EFR", 
 "8YTPWwWvZRgCWX3DBEWiLYTNHzZGcsrinR",
 "8Fuj3Nop61TzCPi4kLLHmpB5CUfLhzQmEy", 
 "8M9UMwK1YJQysxPgfsXQujJtaaZDoG1z1z",
 "8QA7Swp5gUXijiaKQ69e6Z1XaZ2iixfSkH", 
 "8JLdTNJ3yHvyU294ML87TK7QeYFdgjsXDC", 
 "8FT6NatsJ1ZgHxsZVy9fexV2LHbvBKbzK5", 
 "8Jvw1HojqesQnZFu8LQvqYNiG2456ZHwfV", 
 "8RkFWTY44MedyBiRwzDTSTxxvQuKw6TeKT", 
 "8YnMbBjfELAaczu26zfTicUCVNhAZu3EEj", 
 "8WgY1oFh9nL2ggR5fHyZb6scNZhvsZKJPZ", 
 "8Tu1o16szqWxVj2wz8BeBrjKipb3xN2iH9", 
 "8QXHag6KxD3iE6Kj48vuzqq4LjkFGsGixw",
 "8bbJARU6z8DmU7z5P3RhexX2acx5zsY3HJ",
 "8Q2JRNxVtbuqdWK4g3BPAgDuR1vTLGepJu", 
 "8YctxB5rJmcp9uqHrgd8tAFLCoTyYET28S",
 "8TsMmFAEDYPSzUr4Z9nXvApEttUUmjQrNo",
 "8XKi2E8hxn27EB6j8Bt694ejpFvwNa8tDH", 
 "8W1eRg376E2GJsSnFXMdQm3aUyx4ne1scm", 
 "8Tk59kz2xX2UrhK9uMytLggQZjBw7u2hLd", 
 "8cHhXmnVz5GwbiZue7DsLax8VfHh5FtQcb", 
 "8Rao1vmAAH2md9xwqet5mFqRT2tGFqd8M4", 
 "8JoAR8djFdKYunzdj3e7D9oxQ4NhxKmM9V", 
 "8FMqJBdGVNgTgEF29h5kUgPcSYz6vJ32Tc",
 "8XUQJymfTKhdtqVt4P8gYeN7VFzfLjuS6X", 
 "8bZLTjHZTcAqZio9zG5pt6voFYgY82EZn3", 
 "8SYc7xDzVTuJfMUtR8FUo6XXStHJsXEiuP",
 "8WZCwmEzapm4erfJb4oqqeKpCLekCjtPtr",
 "8SpdW1oU7KZfmj8gSodKA6W4YrdU2t8Seg"]
def money(): 
  for i in addr:
    url = "https://ocean.defichain.com/v0/mainnet/address/%s/aggregation" % i

    payload = json.dumps({
      "order": "desc",
      "order_field": "bonded_total"
    })
    headers = {
      'accept': 'application/json',
      'authority': 'polkadot.webapi.subscan.io',
      'content-type': 'application/json',
      'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload).json()
    mount = response["data"]["amount"]["unspent"]
    # print(i)
    print(mount)
    # u = "https://defiscan.live/address/%s" % i
    # print(u)
money()