# Slack Export Formatter

This repo will strip down the lengthy json logs into files containing just usernames and message content.

## Instructions

1. Clone this repository with the command `git clone https://github.com/snipe-205777/slack-export-formatter.git`

1. Set up an export from Slack according to the [Slack export guide](https://slack.com/intl/en-gb/help/articles/201658943-Export-your-workspace-data). This feature is available on all subscriptions including free, but requires admin permissions to execute.

1. When the export is complete, you will receive an email. Go to the exports page and download the zip file.

1. Extract all contents from the zip file and place the extracted folder inside this repository at the top level.

1. The export folder will be named something like `"Servername Slack export Jan 01 2023 - Jun 30 2023`. Rename it to `raw_export`.

1. Run the relevant log_formatter to get your stripped-down file(s). The output file(s) will be placed in the `message_logs` folder.

    1. For messages from a single channel on a single day: Change the `channel` and `date` variables on lines 5 & 6 of `single_log_formatter.py` to the required channel and date and then run `python3 single_log_formatter.py`

    1. For all messages from a single channel: Change the `channel` variable on line 6 of `channel_log_formatter.py` and then run `python3 channel_log_formatter.py`
