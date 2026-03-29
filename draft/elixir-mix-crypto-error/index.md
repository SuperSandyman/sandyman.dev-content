---
slug: elixir-mix-crypto-error
title: elixir mix エラー
tags: []
categories: []
date: '2026-04-11'
draft: true
---

░▒▓sandyman  ~/develop/codex_discord_bot    v1.19.5  ♥ 13:45  mix compile                            

13:45:20.019 [error] GenServer Mix.Sync.PubSub terminating
** (UndefinedFunctionError) function :crypto.strong_rand_bytes/1 is undefined (module :crypto is not available)
    :crypto.strong_rand_bytes(3)
    (mix 1.19.5) lib/mix/utils.ex:892: Mix.Utils.detect_user_id!/0
    (mix 1.19.5) lib/mix/sync/pubsub.ex:285: Mix.Sync.PubSub.base_path/0
    (mix 1.19.5) lib/mix/sync/pubsub.ex:280: Mix.Sync.PubSub.path/1
    (mix 1.19.5) lib/mix/sync/pubsub.ex:143: Mix.Sync.PubSub.handle_call/3
    (stdlib 7.3) gen_server.erl:2470: :gen_server.try_handle_call/4
    (stdlib 7.3) gen_server.erl:2499: :gen_server.handle_msg/3
    (stdlib 7.3) proc_lib.erl:333: :proc_lib.init_p_do_apply/3
Last message (from Mix.PubSub.Subscriber): {:subscribe, #PID<0.111.0>, "/home/sandyman/develop/codex_discord_bot/_build/dev"}
State: %{port: nil, hash_to_pids: %{}}
Client Mix.PubSub.Subscriber is alive

    (stdlib 7.3) gen.erl:243: :gen.do_call/4
    (elixir 1.19.5) lib/gen_server.ex:1139: GenServer.call/3
    (mix 1.19.5) lib/mix/sync/pubsub.ex:47: Mix.Sync.PubSub.subscribe/1
    (mix 1.19.5) lib/mix/pubsub/subscriber.ex:24: Mix.PubSub.Subscriber.init/1
    (stdlib 7.3) gen_server.erl:2276: :gen_server.init_it/2
    (stdlib 7.3) gen_server.erl:2236: :gen_server.init_it/6
    (stdlib 7.3) proc_lib.erl:333: :proc_lib.init_p_do_apply/3

13:45:20.033 [notice] Application mix exited: shutdown
** (ArgumentError) errors were found at the given arguments:

  * 1st argument: the table identifier does not refer to an existing ETS table

    (stdlib 7.3) :ets.lookup(Mix.State, :debug)
    (mix 1.19.5) lib/mix/state.ex:30: Mix.State.get/2
    (mix 1.19.5) lib/mix/cli.ex:134: Mix.CLI.run_task/2
    /home/sandyman/.local/share/mise/installs/elixir/1.19.5-otp-28/bin/mix:7: (file)

░▒▓sandyman  ~/develop/codex_discord_bot    v1.19.5  ♥ 13:45  mise uninstall erlang@latest elixir@latest

░▒▓sandyman  ~/develop/codex_discord_bot      ♥ 13:45  mise use -g erlang@latest elixir@latest   
mise erlang@28.4.1  install                                                                                                         ⠚  1s
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░mise 2026.1.6 by @jdx░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
mise erlang@28.4.1  install                                                                                                         ⠂  1s
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░mise 2026.1.6 by @jdx░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
mise erlang@28.4.1  install                                                                                                         ⠉  8s
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░mise 2026.1.6 by @jdx░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
mise erlang@28.4.1  install                                                                                                         ⠂  9s
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░mise 2026.1.6 by @jdx░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░Building (normal) Erlang/OTP 28.4.1 (28.4.1); please wait...
Initializing (build) log file at /home/sandyman/.cache/mise/erlang/kerl/builds/28.4.1/otp_build_28.4.1.log.
/home/sandyman/.cache/mise/erlang/kerl-4.4.0: 行 1006: -tumbleweed_probe: command not found
mise erlang@28.4.1  install                                                                                                         ⠖ 19s
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░mise 2026.1.6 by @jdx░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░APPLICATIONS DISABLED (See: /home/sandyman/.cache/mise/erlang/kerl/builds/28.4.1/otp_build_28.4.1.log)
 * jinterface     : No Java compiler found
 * odbc           : ODBC library - link check failed

APPLICATIONS INFORMATION (See: /home/sandyman/.cache/mise/erlang/kerl/builds/28.4.1/otp_build_28.4.1.log)
 * wx             : No GLU headers found, wx will NOT be usable
 * wxWidgets was not compiled with --enable-webview or wxWebView developer package is not installed, wxWebView will NOT be available
 *         wxWidgets must be installed on your system.
 *         Please check that wx-config is in path, the directory
 *         where wxWidgets libraries are installed (returned by
 *         'wx-config --libs' or 'wx-config --static --libs' command)
 *         is in LD_LIBRARY_PATH or equivalent variable and
 *         wxWidgets version is 3.0.2 or above.
mise erlang@28.4.1  install                                                                                                         ⠐ 63s
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░mise 2026.1.6 by @jdx░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░Erlang/OTP 28.4.1 (28.4.1) has been successfully built.
Installing Erlang/OTP 28.4.1 (28.4.1) in /home/sandyman/.local/share/mise/installs/erlang/28.4.1...
mise erlang@28.4.1  install                                                                                                         ⠖ 70s
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░mise 2026.1.6 by @jdx░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░You can activate this installation running the following command:
. /home/sandyman/.local/share/mise/installs/erlang/28.4.1/activate
Later on, you can leave the installation typing:
                                                                                                                                      71smise ~/.config/mise/config.toml tools: erlang@28.4.1, elixir@1.19.5-otp-28

░▒▓sandyman  ~/develop/codex_discord_bot    v1.19.5  ♥ 13:46  mix compile                               
Compiling 2 files (.ex)
Generated codex_discord_bot app
