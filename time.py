from datetime import timedelta, datetime
import arrow


# Calculate time behind/ahead
def timeConversion(intseconds=None):
    """
    timeConversion - Displays a calculated time depending on
    the given value in seconds.
    """

    # Convert given parameter to a timedelta
    sec = timedelta(seconds=intseconds)

    unixTime = datetime.now() + sec

    # Return a human readable format
    return unixTime.strftime('%H:%M:%S %A %d %B %Y')


def getTime(weeks=0, days=0, hours=0, minutes=0, seconds=0):
    '''
    getTime - Displays the given time in seconds by the
    following arguments:
    - Weeks
    - Days
    - Hours
    - Minutes
    - Seconds
    '''
    print('Given time: {}'.format(timedelta(weeks=weeks, days=days,
                                            hours=hours, minutes=minutes,
                                            seconds=seconds)))

    seconds = timedelta(weeks=weeks, days=days, hours=hours,
                        minutes=minutes, seconds=seconds).total_seconds()
    print('That is {} seconds'.format(seconds))

    return seconds


def currentTime(zone=''):
    '''
    currentTime - Displays the time of a given timezone
    in a formatted way.
    '''
    try:
        # Get the current time in a specific timezone
        time = arrow.now(zone)

    # Display the local time formatted on Type/Key error
    except TypeError as error:
        return arrow.now().format()
    else:
        return time.format()


def convertTo(fromTz, toTz, *, laterDate=None):
    '''
    convertTo - Displays the given time/date in a specific
    timezone and returns the difference.
    '''
    # Check if laterDate has a value
    if laterDate:
        tzFrom = arrow.get(laterDate, fromTz)
        tzTo = tzFrom.to(toTz).datetime.replace(tzinfo=None)
    else:
        # Get that tzinfo shit out of here...
        tzFrom = arrow.now(fromTz)
        tzTo = arrow.now(toTz).datetime.replace(tzinfo=None)

    # Get a difference response
    diff = tzFrom.datetime.replace(tzinfo=None) - tzTo

    # Prevent displaying a large hour difference
    if diff.days < 0:
        diff = tzTo - tzFrom.datetime.replace(tzinfo=None)

    return diff
