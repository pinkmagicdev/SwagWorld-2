import twitter
from evennia import Command

# here you insert your unique App tokens
# from the Twitter dev site
TWITTER_API = twitter.Api(consumer_key='api_key',
                          consumer_secret='api_secret',
                          access_token_key='access_token_key',
                          access_token_secret='access_token_secret')

class CmdTweet(Command):
    """
    Tweet a message

    Usage:
      tweet <message>

    This will send a Twitter tweet to a pre-configured Twitter account.
    A tweet has a maximum length of 140 characters.
    """

    key = "tweet"
    locks = "cmd:pperm(tweet) or pperm(Developers)"
    help_category = "Comms"

    def func(self):
        "This performs the tweet"

        caller = self.caller
        tweet = self.args

        if not tweet:
            caller.msg("Usage: tweet <message>")
            return

        tlen = len(tweet)
        if tlen > 140:
            caller.msg("Your tweet was %i chars long (max 140)." % tlen)
            return

        # post the tweet
        TWITTER_API.PostUpdate(tweet)

        caller.msg("You tweeted:\n%s" % tweet)
